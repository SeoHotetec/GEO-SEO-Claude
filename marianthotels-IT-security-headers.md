# Encabezados de Seguridad HTTP — Mariant Hotels
**Documento técnico para IT** · Fecha: 2026-04-24

---

## Resumen ejecutivo

El servidor de `marianthotels.com` no devuelve ningún encabezado de seguridad HTTP en sus respuestas. Esto expone el sitio a vectores de ataque comunes (XSS, clickjacking, MIME sniffing, inyección de contenido) y genera puntuaciones bajas en auditorías de seguridad estándar.

La corrección completa se estima en **menos de 1 hora** y no requiere reinicio del servidor, solo recarga de Nginx.

---

## Diagnóstico confirmado

### Estado actual

```bash
curl -I https://www.marianthotels.com/
```

**Cabeceras de seguridad presentes:** ninguna  
**Versión de Nginx expuesta en header `Server`:** pendiente de verificar

### Cabeceras ausentes y su riesgo

| Cabecera | Riesgo sin ella | Severidad |
|---|---|---|
| `Strict-Transport-Security` | Posible downgrade HTTP, ataques man-in-the-middle | Crítica |
| `Content-Security-Policy` | XSS, inyección de scripts maliciosos | Crítica |
| `X-Frame-Options` | Clickjacking — el sitio puede cargarse en iframes de terceros | Alta |
| `X-Content-Type-Options` | MIME sniffing — el navegador interpreta ficheros como ejecutables | Alta |
| `Referrer-Policy` | Fuga de URLs internas a dominios de terceros | Media |
| `Permissions-Policy` | Acceso no controlado a cámara, micrófono, geolocalización | Media |
| `X-XSS-Protection` | Ausencia de protección en navegadores legacy | Baja |
| `server_tokens` activos | Fingerprinting del servidor — expone versión de Nginx a atacantes | Alta |

---

## Dónde van los headers — servidor vs. CMS

**Respuesta directa: siempre en el servidor Nginx.** Los meta tags HTML son un sustituto parcial e incompleto.

| Header | En Nginx | En meta tag HTML |
|---|---|---|
| `Strict-Transport-Security` | Funciona al 100% | No existe equivalente en HTML |
| `Content-Security-Policy` | Funciona al 100% | Funciona parcialmente (no cubre todos los recursos) |
| `X-Frame-Options` | Funciona al 100% | Ignorado por navegadores modernos |
| `X-Content-Type-Options` | Funciona al 100% | No existe equivalente en HTML |
| `Referrer-Policy` | Funciona al 100% | Funciona solo para navegación, no para recursos |
| `Permissions-Policy` | Funciona al 100% | No existe equivalente en HTML |
| `server_tokens off` | Funciona al 100% | No aplica |

El navegador lee los HTTP headers **antes** de parsear el HTML. Si el header viene en la respuesta del servidor, cualquier meta tag equivalente es redundante o conflictivo. **El CMS no debe gestionar seguridad de headers.**

---

## Implementación en Nginx

### Estructura de ficheros recomendada

```
/etc/nginx/
├── nginx.conf
├── conf.d/
│   └── marianthotels.conf
└── includes/
    └── security-headers.conf     ← todos los headers en un fichero separado
```

Separar los headers en un `include` permite reutilizarlos en todos los `server {}` blocks sin duplicar código y facilita el mantenimiento.

---

### Paso 1 — Crear `/etc/nginx/includes/security-headers.conf`

```bash
mkdir -p /etc/nginx/includes
nano /etc/nginx/includes/security-headers.conf
```

Contenido del fichero:

```nginx
# =============================================================
# SECURITY HEADERS — marianthotels.com
# Estándar: OWASP Secure Headers Project
# Fecha: 2026-04-24
# =============================================================

# -------------------------------------------------------
# 1. HTTP Strict Transport Security (HSTS)
# Fuerza HTTPS durante 1 año en todos los subdominios.
# ATENCIÓN: activar preload solo tras verificar que TODO
# el dominio y subdominios funcionan en HTTPS sin excepciones.
# -------------------------------------------------------
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;

# -------------------------------------------------------
# 2. X-Frame-Options
# Previene que el sitio se cargue en iframes de terceros.
# SAMEORIGIN permite iframes del propio dominio.
# -------------------------------------------------------
add_header X-Frame-Options "SAMEORIGIN" always;

# -------------------------------------------------------
# 3. X-Content-Type-Options
# Previene MIME-type sniffing.
# El navegador respeta siempre el Content-Type declarado.
# -------------------------------------------------------
add_header X-Content-Type-Options "nosniff" always;

# -------------------------------------------------------
# 4. Referrer-Policy
# Envía el origen completo en peticiones same-origin.
# Solo envía el origen (sin path) en peticiones cross-origin HTTPS.
# No envía nada en peticiones cross-origin HTTP.
# -------------------------------------------------------
add_header Referrer-Policy "strict-origin-when-cross-origin" always;

# -------------------------------------------------------
# 5. Permissions-Policy (antes Feature-Policy)
# Desactiva APIs del navegador no necesarias para el sitio.
# Ajustar si el motor de reservas usa geolocalización o pagos.
# -------------------------------------------------------
add_header Permissions-Policy "
    accelerometer=(),
    ambient-light-sensor=(),
    autoplay=(self),
    camera=(),
    display-capture=(),
    encrypted-media=(self),
    fullscreen=(self),
    geolocation=(self),
    gyroscope=(),
    interest-cohort=(),
    magnetometer=(),
    microphone=(),
    midi=(),
    payment=(self),
    picture-in-picture=(self),
    publickey-credentials-get=(),
    screen-wake-lock=(),
    serial=(),
    usb=(),
    web-share=(self),
    xr-spatial-tracking=()
" always;

# -------------------------------------------------------
# 6. X-XSS-Protection
# Obsoleto en navegadores modernos (CSP lo reemplaza),
# pero requerido por escáneres de seguridad y navegadores legacy.
# -------------------------------------------------------
add_header X-XSS-Protection "1; mode=block" always;

# -------------------------------------------------------
# 7. Cross-Origin Headers (COOP / CORP)
# Aislamiento de origen — recomendado para aplicaciones modernas.
# same-origin-allow-popups permite ventanas emergentes del motor de reservas.
# -------------------------------------------------------
add_header Cross-Origin-Opener-Policy "same-origin-allow-popups" always;
add_header Cross-Origin-Resource-Policy "same-site" always;

# -------------------------------------------------------
# 8. Content Security Policy (CSP)
# IMPORTANTE: Esta directiva DEBE adaptarse antes de activarse.
# Ver sección "Configuración del CSP" más abajo.
# Activar primero en modo Report-Only durante 1-2 semanas.
# -------------------------------------------------------
# add_header Content-Security-Policy "..." always;   ← descomentarla tras pruebas
```

---

### Paso 2 — Configuración del CSP (hacerlo en dos fases)

El CSP es el header más potente pero también el más delicado. Activarlo directamente puede romper funcionalidades del sitio (scripts de analytics, motor de reservas, widgets externos).

#### Fase A — Modo reporte (activar 1-2 semanas, no bloquea nada)

```nginx
# Añadir en el server{} block durante la fase de pruebas
add_header Content-Security-Policy-Report-Only "
    default-src 'self';
    script-src  'self' 'unsafe-inline' https:;
    style-src   'self' 'unsafe-inline' https:;
    img-src     'self' data: https: blob:;
    connect-src 'self' https:;
    font-src    'self' https:;
    frame-src   'self' https:;
    object-src  'none';
" always;
```

Monitorizar las violaciones en los logs de Nginx o en la consola del navegador (DevTools → Console → violaciones CSP).

#### Fase B — CSP definitivo para Mariant Hotels

Basado en los recursos externos habituales de un sitio hotelero con Google Analytics y motor de reservas:

```nginx
add_header Content-Security-Policy "
    default-src 'self';
    script-src  'self' 'unsafe-inline'
                https://www.googletagmanager.com
                https://www.google-analytics.com
                https://connect.facebook.net
                https://widget.trustpilot.com
                https://secure.reservations.com;
    style-src   'self' 'unsafe-inline'
                https://fonts.googleapis.com;
    font-src    'self'
                https://fonts.gstatic.com;
    img-src     'self' data: https: blob:;
    connect-src 'self'
                https://www.google-analytics.com
                https://analytics.google.com;
    frame-src   'self'
                https://www.google.com
                https://www.youtube.com
                https://secure.reservations.com;
    object-src  'none';
    base-uri    'self';
    form-action 'self' https://secure.reservations.com;
    upgrade-insecure-requests;
" always;
```

> **Nota:** Los dominios del motor de reservas (`secure.reservations.com` en el ejemplo) deben sustituirse por los dominios reales del sistema de reservas utilizado.

---

### Paso 3 — Ocultar versión de Nginx

En el fichero `/etc/nginx/nginx.conf`, dentro del bloque `http {}`:

```nginx
http {
    server_tokens off;   # Oculta versión de Nginx en header Server y páginas de error
    # ...
}
```

**Antes:** `Server: nginx/1.24.0`  
**Después:** `Server: nginx`

---

### Paso 4 — Incluir los headers en el `server {}` block

En el fichero de configuración del sitio `/etc/nginx/conf.d/marianthotels.conf`:

```nginx
server {
    listen 443 ssl http2;
    server_name www.marianthotels.com marianthotels.com;

    # ← Cargar security headers
    include /etc/nginx/includes/security-headers.conf;

    # Cache-Control por tipo de recurso
    location ~* \.(css|js|woff2?|ttf|otf|ico|png|jpg|jpeg|webp|gif|svg|avif)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
        access_log off;
    }

    location ~* \.(html|htm)$ {
        add_header Cache-Control "no-cache, no-store, must-revalidate";
        add_header Pragma "no-cache";
    }

    # Área de administración — cache estricto
    location /admin {
        add_header Cache-Control "no-store, no-cache, must-revalidate, private";
    }

    # ... resto de la configuración ...
}
```

---

### Paso 5 — Aplicar cambios

```bash
# 1. Validar sintaxis — ejecutar siempre antes de recargar
nginx -t

# 2. Recargar sin downtime (no reiniciar)
nginx -s reload
```

---

## Verificación post-despliegue

### Comandos de verificación

```bash
# Verificar que los headers están presentes
curl -I https://www.marianthotels.com/ | grep -i \
    -e "strict-transport" \
    -e "x-frame-options" \
    -e "x-content-type" \
    -e "referrer-policy" \
    -e "permissions-policy" \
    -e "x-xss-protection" \
    -e "content-security-policy"

# Resultado esperado (un header por línea):
# strict-transport-security: max-age=31536000; includeSubDomains; preload
# x-frame-options: SAMEORIGIN
# x-content-type-options: nosniff
# referrer-policy: strict-origin-when-cross-origin
# permissions-policy: accelerometer=(), ...
# x-xss-protection: 1; mode=block

# Verificar que Nginx no expone versión
curl -I https://www.marianthotels.com/ | grep -i "^server:"
# Esperado: Server: nginx
# Incorrecto: Server: nginx/1.24.0

# Verificar SSL y TLS
openssl s_client -connect www.marianthotels.com:443 -brief 2>/dev/null | head -3
# Esperado: TLSv1.3
```

### Herramientas de validación online

Ejecutar tras el despliegue para obtener puntuación oficial:

| Herramienta | URL | Puntuación objetivo |
|---|---|---|
| **Security Headers** | `https://securityheaders.com/?q=marianthotels.com` | **A+** |
| **SSL Labs** | `https://www.ssllabs.com/ssltest/analyze.html?d=marianthotels.com` | **A o A+** |
| **Mozilla Observatory** | `https://observatory.mozilla.org/analyze/marianthotels.com` | **A+** |
| **CSP Evaluator** | `https://csp-evaluator.withgoogle.com/` | Sin errores críticos |

---

## Guía rápida por CMS (referencia para otros proyectos)

Este mismo patrón se aplica a cualquier proyecto web en el servidor.

### WordPress

No configurar headers en WordPress (wp-config.php, plugins). Gestionar exclusivamente en Nginx con el `include` descrito. Los plugins de seguridad de WordPress (Wordfence, iThemes) que añaden headers lo hacen vía PHP — menos eficiente y con menor cobertura que Nginx.

### Otro CMS / aplicación PHP

Mismo criterio. Si el CMS añade headers por su cuenta y Nginx también los añade, pueden duplicarse o entrar en conflicto. Centralizar siempre en Nginx.

### Múltiples sitios en el mismo servidor

Reutilizar el mismo `include` en todos los `server {}` blocks:

```nginx
# En cada server{} block de cada sitio
include /etc/nginx/includes/security-headers.conf;
```

Si algún sitio necesita una configuración distinta (por ejemplo, un CSP diferente), crear un fichero específico:

```
/etc/nginx/includes/
├── security-headers.conf            ← base común para todos los sitios
├── security-headers-mariant.conf    ← overrides específicos de Mariant
└── security-headers-otrosite.conf   ← overrides específicos de otro sitio
```

---

## Resumen de prioridades

| # | Acción | Urgencia | Tiempo estimado |
|---|---|---|---|
| 1 | Crear `/etc/nginx/includes/security-headers.conf` | **Crítica** | 10 min |
| 2 | Añadir `server_tokens off` en `nginx.conf` | **Crítica** | 2 min |
| 3 | Incluir el fichero en el `server {}` block | **Crítica** | 5 min |
| 4 | Validar con `nginx -t` y recargar con `nginx -s reload` | **Crítica** | 2 min |
| 5 | Verificar headers con curl | Alta | 5 min |
| 6 | Activar CSP en modo Report-Only | Alta | 10 min |
| 7 | Analizar violaciones CSP durante 1-2 semanas | Alta | Pasivo |
| 8 | Activar CSP definitivo con dominios reales del motor de reservas | Alta | 15 min |
| 9 | Validar con Security Headers y Mozilla Observatory | Media | 10 min |

**Total para headers básicos (pasos 1-5): ~25 minutos**  
**Total para CSP completo (pasos 1-9): ~2 semanas + 45 minutos activos**

---

## Referencia de headers — tabla completa

| Header | Valor recomendado | Protege contra |
|---|---|---|
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains; preload` | Downgrade HTTP, MITM |
| `X-Frame-Options` | `SAMEORIGIN` | Clickjacking |
| `X-Content-Type-Options` | `nosniff` | MIME sniffing |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | Fuga de URLs internas |
| `Permissions-Policy` | `camera=(), microphone=(), ...` | Abuso de APIs del navegador |
| `X-XSS-Protection` | `1; mode=block` | XSS en navegadores legacy |
| `Cross-Origin-Opener-Policy` | `same-origin-allow-popups` | Cross-origin attacks |
| `Cross-Origin-Resource-Policy` | `same-site` | Cross-origin data leaks |
| `Content-Security-Policy` | Ver sección CSP | XSS, inyección de scripts |
| `server_tokens off` | — | Fingerprinting del servidor |

---

## Contacto para dudas

Documento preparado por el equipo de GEO/SEO de Mariant Hotels.  
Para cualquier duda técnica sobre esta configuración, contactar antes de activar el CSP en producción.
