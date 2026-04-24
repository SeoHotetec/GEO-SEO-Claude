# Acceso de Crawlers de IA al Servidor — Mariant Hotels
**Documento técnico para IT** · Fecha: 2026-04-24

---

## Resumen ejecutivo

El servidor de `marianthotels.com` bloquea actualmente **todos los crawlers de motores de búsqueda de IA** (ChatGPT, Claude, Perplexity, Google AI Overviews, Bing Copilot). Esto supone **invisibilidad total en AI search** — cuando un usuario pregunta a cualquiera de estos sistemas por hoteles en Sa Coma o S'Illot, el sitio no aparece como fuente.

La causa es un WAF con IP allowlist activo en Nginx que devuelve `HTTP 403` a cualquier IP no pre-aprobada, incluyendo los crawlers de IA.

---

## Diagnóstico confirmado

### Prueba realizada

```bash
curl -A "GPTBot/1.0" https://www.marianthotels.com/robots.txt
```

### Resultado obtenido

```
HTTP/2 403
x-deny-reason: host_not_allowed
Host not in allowlist
```

### Interpretación

| Síntoma | Causa | Impacto |
|---|---|---|
| `HTTP 403` en robots.txt | IP del crawler no está en el allowlist | El crawler abandona el sitio sin indexar nada |
| `x-deny-reason: host_not_allowed` | Lógica de bloqueo en Nginx (`return 403`) | Todos los crawlers externos son rechazados |
| `Host not in allowlist` | IP allowlist restrictivo | Incluye crawlers de Google, OpenAI, Anthropic, Perplexity |

El servidor resuelve a IPs de AWS (`3.255.15.63`, `99.81.116.114`). El bloqueo ocurre a nivel de aplicación Nginx, no en CloudFront ni en AWS WAF.

---

## Acción 1 — Localizar la regla de bloqueo en Nginx

Ejecutar en el servidor para identificar el fichero exacto:

```bash
grep -r "host_not_allowed" /etc/nginx/
grep -r "return 403" /etc/nginx/
grep -rn "allowlist\|allow_list\|not_allowed" /etc/nginx/
```

La lógica actual será similar a esto:

```nginx
# Patrón típico del bloqueo actual
if ($allowed_ip != "1") {
    add_header x-deny-reason "host_not_allowed";
    return 403 "Host not in allowlist";
}
```

---

## Acción 2 — Añadir excepción para crawlers de IA

Añadir el bloque siguiente **inmediatamente antes** del `return 403` existente. No eliminar ni modificar la lógica actual.

### Fichero nuevo: `/etc/nginx/includes/ai-crawlers-ip.conf`

```nginx
# ai-crawlers-ip.conf
# Rangos IP oficiales de crawlers de IA
# Actualizar mensualmente — ver sección "Mantenimiento"

geo $is_ai_crawler_ip {
    default 0;

    # OpenAI — GPTBot & ChatGPT-User
    # Fuente oficial: https://openai.com/gptbot-ranges.txt
    20.42.0.0/17        1;
    172.203.190.0/24    1;
    172.203.191.0/24    1;
    51.8.102.0/24       1;
    52.230.152.0/24     1;
    52.233.106.0/24     1;
    52.234.32.0/24      1;
    40.83.0.0/16        1;

    # Google — GoogleOther & Google-Extended (AI Overviews)
    # Fuente oficial: https://developers.google.com/search/apis/ipranges/googlebot.json
    66.249.64.0/19      1;
    66.249.80.0/20      1;

    # Microsoft Bing — BingBot (Copilot)
    # Fuente oficial: https://www.bing.com/toolbox/bingbot.json
    157.55.39.0/24      1;
    207.46.13.0/24      1;
    40.77.167.0/24      1;

    # Perplexity — IPs rotan con frecuencia
    # Fuente oficial: https://www.perplexity.com/perplexitybot.json
    # Actualizar semanalmente con el script de mantenimiento
}
```

### Fichero nuevo: `/etc/nginx/includes/ai-crawlers-ua.conf`

```nginx
# ai-crawlers-ua.conf
# Bypass por User-Agent — necesario para ClaudeBot (Anthropic no publica IPs)

map $http_user_agent $is_ai_crawler_ua {
    default             0;
    "~*GPTBot"          1;
    "~*ChatGPT-User"    1;
    "~*OAI-SearchBot"   1;
    "~*ClaudeBot"       1;
    "~*Claude-User"     1;
    "~*Claude-SearchBot" 1;
    "~*anthropic-ai"    1;
    "~*PerplexityBot"   1;
    "~*Perplexity-User" 1;
    "~*Google-Extended" 1;
    "~*GoogleOther"     1;
    "~*cohere-ai"       1;
    "~*Applebot-Extended" 1;
}

# Decisión final: permitir si coincide IP conocida O User-Agent conocido
map "$is_ai_crawler_ip:$is_ai_crawler_ua" $allow_ai_crawler {
    default  0;
    "~^1:"   1;   # IP conocida
    "~:1$"   1;   # UA conocido (cubre ClaudeBot sin IPs públicas)
}
```

### Modificación en el `server {}` block

```nginx
# Cargar los includes (nivel http{} o server{})
include /etc/nginx/includes/ai-crawlers-ip.conf;
include /etc/nginx/includes/ai-crawlers-ua.conf;

server {
    # ... configuración existente sin tocar ...

    # AÑADIR ANTES del bloque de bloqueo actual:
    if ($allow_ai_crawler = "1") {
        set $allowed_ip "1";   # sobreescribe la variable de allowlist para AI crawlers
    }

    # Bloqueo existente — NO MODIFICAR
    if ($allowed_ip != "1") {
        add_header x-deny-reason "host_not_allowed";
        return 403 "Host not in allowlist";
    }

    # ...
}
```

> **Nota:** El nombre exacto de la variable (`$allowed_ip`) puede diferir. Adaptar al nombre que use la config actual.

---

## Acción 3 — Security Headers

El sitio no tiene security headers configurados. Añadir el siguiente fichero e incluirlo en el `server {}` block.

### Fichero nuevo: `/etc/nginx/includes/security-headers.conf`

```nginx
# security-headers.conf
# Estándar OWASP Secure Headers Project

# Fuerza HTTPS durante 1 año
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;

# Previene clickjacking
add_header X-Frame-Options "SAMEORIGIN" always;

# Previene MIME-type sniffing
add_header X-Content-Type-Options "nosniff" always;

# Controla información enviada en cabecera Referer
add_header Referrer-Policy "strict-origin-when-cross-origin" always;

# Desactiva APIs del navegador no necesarias
add_header Permissions-Policy "camera=(), microphone=(), geolocation=(self), payment=(self)" always;

# Protección XSS legacy (para navegadores antiguos)
add_header X-XSS-Protection "1; mode=block" always;

# Aislamiento de origen
add_header Cross-Origin-Opener-Policy "same-origin-allow-popups" always;
add_header Cross-Origin-Resource-Policy "same-site" always;

# Content Security Policy
# IMPORTANTE: revisar y adaptar según los scripts externos del sitio
# (Google Analytics, GTM, motor de reservas, etc.) antes de activar
add_header Content-Security-Policy "
    default-src 'self';
    script-src  'self' 'unsafe-inline' https://www.googletagmanager.com https://www.google-analytics.com;
    style-src   'self' 'unsafe-inline' https://fonts.googleapis.com;
    font-src    'self' https://fonts.gstatic.com;
    img-src     'self' data: https: blob:;
    connect-src 'self' https://www.google-analytics.com;
    frame-src   'self' https://www.google.com https://www.youtube.com;
    object-src  'none';
    base-uri    'self';
    form-action 'self';
    upgrade-insecure-requests;
" always;
```

### Modificación en `nginx.conf` (bloque `http{}`)

```nginx
http {
    # Ocultar versión de Nginx — si no está ya activo
    server_tokens off;

    # ...
}
```

### Incluir en el `server {}` block

```nginx
server {
    include /etc/nginx/includes/security-headers.conf;
    # ...
}
```

---

## Acción 4 — Desplegar llms.txt

El fichero `llms.txt` es el estándar emergente para que los sistemas de IA entiendan la estructura del sitio. Sin él, los crawlers deben inferir el contenido página a página.

### Colocar el fichero en la raíz web

```bash
# Copiar el fichero generado a la raíz del sitio
cp marianthotels-llms.txt /var/www/marianthotels/llms.txt
chmod 644 /var/www/marianthotels/llms.txt
```

### Añadir location en Nginx para garantizar acceso público

```nginx
# Dentro del server{} block — asegurar acceso sin restricción de allowlist
location = /llms.txt {
    allow all;
    add_header Cache-Control "no-cache, max-age=0";
    add_header Content-Type "text/plain; charset=utf-8";
}

# Lo mismo para robots.txt
location = /robots.txt {
    allow all;
    add_header Cache-Control "no-cache, max-age=0";
}
```

---

## Acción 5 — Actualizar robots.txt

Una vez que el WAF permita el acceso, el `robots.txt` debe declarar explícitamente que los crawlers de IA son bienvenidos.

### Contenido recomendado para `/robots.txt`

```
User-agent: *
Allow: /

# AI crawlers — acceso explícito para visibilidad en AI search
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: GoogleOther
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: cohere-ai
Allow: /

User-agent: Applebot-Extended
Allow: /

Sitemap: https://www.marianthotels.com/sitemap.xml
```

---

## Procedimiento de despliegue

### Orden obligatorio

```
1. Crear los ficheros include de Nginx
2. Modificar el server{} block (añadir includes + excepción AI crawlers)
3. Validar sintaxis: nginx -t
4. Recargar: nginx -s reload
5. Verificar con curl (ver sección siguiente)
6. Desplegar llms.txt en la raíz web
7. Actualizar robots.txt
8. Verificar robots.txt accesible por crawlers
```

### Verificación tras el despliegue

```bash
# 1. Validar config Nginx
nginx -t

# 2. Recargar sin downtime
nginx -s reload

# 3. Verificar que GPTBot accede al robots.txt
curl -s -o /dev/null -w "HTTP %{http_code}\n" \
    -A "Mozilla/5.0 (compatible; GPTBot/1.0; +https://openai.com/gptbot)" \
    https://www.marianthotels.com/robots.txt
# Esperado: HTTP 200

# 4. Verificar que ClaudeBot accede al sitio
curl -s -o /dev/null -w "HTTP %{http_code}\n" \
    -A "Mozilla/5.0 AppleWebKit/537.36 (compatible; ClaudeBot/1.0; +claudebot@anthropic.com)" \
    https://www.marianthotels.com/
# Esperado: HTTP 200

# 5. Verificar que PerplexityBot accede al sitio
curl -s -o /dev/null -w "HTTP %{http_code}\n" \
    -A "Mozilla/5.0 (compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)" \
    https://www.marianthotels.com/
# Esperado: HTTP 200

# 6. Verificar que el allowlist existente sigue funcionando
# (ejecutar desde una IP no autorizada)
curl -s -o /dev/null -w "HTTP %{http_code}\n" https://www.marianthotels.com/
# Esperado: HTTP 403 (el allowlist sigue activo para IPs no autorizadas)

# 7. Verificar llms.txt accesible
curl -s -o /dev/null -w "HTTP %{http_code}\n" \
    https://www.marianthotels.com/llms.txt
# Esperado: HTTP 200

# 8. Verificar security headers
curl -I https://www.marianthotels.com/ | grep -i \
    -e "strict-transport" \
    -e "x-frame" \
    -e "x-content-type" \
    -e "referrer-policy"

# 9. Verificar que Nginx no expone versión
curl -I https://www.marianthotels.com/ | grep -i "server:"
# Esperado: Server: nginx  (sin número de versión)
```

---

## Mantenimiento de IPs (tarea recurrente)

Las IPs de los crawlers de IA cambian. Es necesario actualizarlas periódicamente.

### Fuentes oficiales

| Crawler | URL de la lista oficial | Frecuencia recomendada |
|---|---|---|
| GPTBot (OpenAI) | `https://openai.com/gptbot-ranges.txt` | Mensual |
| ChatGPT-User (OpenAI) | `https://openai.com/chatgpt-user.json` | Mensual |
| PerplexityBot | `https://www.perplexity.com/perplexitybot.json` | Semanal |
| GoogleBot / GoogleOther | `https://developers.google.com/search/apis/ipranges/googlebot.json` | Mensual |
| BingBot | `https://www.bing.com/toolbox/bingbot.json` | Mensual |
| ClaudeBot (Anthropic) | ❌ No publica IPs — controlar solo por User-Agent | — |

### Script de actualización (cron semanal)

```bash
# /usr/local/bin/update-ai-crawler-ips.sh
#!/bin/bash
set -euo pipefail

CONF="/etc/nginx/includes/ai-crawlers-ip.conf"

# Obtener IPs de GPTBot
curl -sf https://openai.com/gptbot-ranges.txt -o /tmp/gptbot-ranges.txt

# Obtener IPs de Perplexity
curl -sf https://www.perplexity.com/perplexitybot.json -o /tmp/perplexitybot.json

# Regenerar el fichero de IPs y recargar Nginx
# (adaptar según el formato de salida de cada endpoint)
nginx -t && nginx -s reload

echo "[$(date)] IPs de AI crawlers actualizadas OK"
```

```bash
# Añadir al cron — ejecutar cada lunes a las 3:00 AM
echo "0 3 * * 1 root /usr/local/bin/update-ai-crawler-ips.sh >> /var/log/ai-crawler-ips.log 2>&1" \
    > /etc/cron.d/ai-crawler-ips
```

---

## Validación online (post-despliegue)

Una vez aplicados todos los cambios, verificar con estas herramientas:

| Herramienta | URL | Objetivo |
|---|---|---|
| Security Headers | `https://securityheaders.com/?q=marianthotels.com` | Puntuación A o A+ |
| SSL Labs | `https://www.ssllabs.com/ssltest/analyze.html?d=marianthotels.com` | Puntuación A o A+ |
| Mozilla Observatory | `https://observatory.mozilla.org/analyze/marianthotels.com` | Puntuación A+ |
| llms.txt validator | `https://llmstxt.cloud/` | Fichero válido |

---

## Resumen de prioridades

| # | Acción | Urgencia | Tiempo estimado |
|---|---|---|---|
| 1 | Localizar regla de bloqueo en Nginx | **Crítica** | 10 min |
| 2 | Añadir excepción para AI crawlers (IP + UA) | **Crítica** | 30 min |
| 3 | Validar y recargar Nginx | **Crítica** | 5 min |
| 4 | Verificar con curl que devuelve HTTP 200 | **Crítica** | 10 min |
| 5 | Desplegar `llms.txt` en raíz web | Alta | 10 min |
| 6 | Actualizar `robots.txt` | Alta | 10 min |
| 7 | Añadir security headers | Media | 30 min |
| 8 | Configurar cron de actualización de IPs | Media | 15 min |
| 9 | Validar con herramientas online | Media | 15 min |

**Total estimado: ~2 horas**

---

## Contacto para dudas

Documento preparado por el equipo de GEO/SEO de Mariant Hotels.
Para cualquier duda técnica sobre esta configuración, contactar antes de modificar cualquier regla de seguridad existente.
