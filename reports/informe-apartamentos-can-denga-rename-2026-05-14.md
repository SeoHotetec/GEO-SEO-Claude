# Informe SEO — Propuesta de Re-Rename de "Apartamentos Can Denga" (ex "Aptos Miramar 2")

**Cliente:** Miramar Mallorca Collection
**Web:** https://www.miramarcollection.com
**Establecimiento:** Apartamentos Can Denga — Port de Pollença, Mallorca
**URL ficha:** https://www.miramarcollection.com/alojamiento/apartamentos-can-denga
**Fecha del informe:** 14 de mayo de 2026
**Autor:** SEO Manager — Hotetec
**Solicitud:** Evaluación del cambio de nombre realizado en mayo 2023 (de *"Aptos Miramar 2"* → *"Apartamentos Can Denga"*) ante la propuesta de revertir el naming.

---

## 0. Resumen ejecutivo (TL;DR para el Account)

**Recomendación:** **NO revertir** el naming a "Aptos Miramar 2", y **NO ejecutar ningún cambio de naming en plena temporada (mayo–octubre 2026)**. La caída de conversión que percibe el cliente **no se explica de forma concluyente por el cambio de nombre**: el cambio fue acertado desde el punto de vista SEO/local y la marca "Can Denga" se ha consolidado mínimamente. Sin embargo, **sí existen problemas SEO técnicos y de visibilidad orgánica significativos en la ficha actual** que sí pueden estar afectando la conversión y que son **el verdadero foco de acción**.

| Bloque | Diagnóstico | Conclusión |
|---|---|---|
| Decisión rename 2023 | Acertada: "Aptos Miramar 2" era débil, genérica y canibalizaba a Hotel Miramar y Apartamentos Miramar | ✅ Defendible |
| Estado SEO ficha actual | URL `apartamentos-can-denga` con **0 keywords y 0 tráfico orgánico** en Ahrefs (mayo 2026) | 🔴 Crítico |
| Marca "Can Denga" en la web | "Can Denga" aparece 10 veces en el HTML, pero **sin endorsing visible "by Miramar"** junto al H1 | 🟠 Mejorable |
| Schema VacationRental | Implementado pero **incompleto**: sin `AggregateRating`, sin `Offer`, `numberOfRooms: null`, `og:url` apunta a home | 🔴 Crítico |
| Organic dominio (2y) | Tráfico orgánico estimado **+200–300%** desde el rename (de 5/mes en may 2023 → 21/mes en may 2026; pico 58 en ago 2025) | ✅ Tendencia positiva |
| Posición media GSC | **Mejorando**: de 46 (oct 2024) → 10.8 (abr 2026) | ✅ Positivo |
| Páginas con tráfico | **Caída fuerte**: de 75 páginas (abr 2024) → 4 páginas (may 2026). Long-tail desaparecido | 🔴 Crítico |
| GBP Apartamentos Can Denga | Solo 6 reseñas / 4.7★ / KP no se dispara para búsqueda branded pura | 🟠 Mejorable |
| Cambio en temporada | Riesgo SEO/local muy alto: reindexación, fluctuaciones, desalineación OTA, confusión usuario | 🛑 No hacer |

**Plan propuesto (resumido):**
1. **Mantener naming** "Apartamentos Can Denga" pero **reforzar endorsing**: rebrand a *"Apartamentos Ca'n Denga — Miramar Mallorca Collection"* en title, H1, OG, schema, GBP y OTAs. **Esto NO es un rename, es un refuerzo de marca**.
2. **Optimización técnica completa** de la ficha (ver §4): schema, OG, H1, AggregateRating, hreflang, render JS, etc.
3. **Estrategia SEO Local intensiva**: revisar inconsistencias NAP en OTAs/directorios, captar reseñas (objetivo 30+ en 6 meses), alta en Wikidata/OSM/Foursquare/Mapbox/Geonames.
4. **Aplazar cualquier intervención de marca disruptiva a noviembre 2026** (post-temporada).
5. Solicitar **datos de GA4 y motor de reservas pre/post rename** para cerrar el bloque de conversión que hoy no se puede medir desde SEO puro.

---

## 1. Contexto del cambio y por qué fue correcto

### 1.1. Histórico
- Hasta **mayo 2023**: el establecimiento se comercializaba como **"Aptos Miramar 2"** (URL `/alojamiento/apartamentos-miramar-2/`).
- **Mayo 2023**: por recomendación de Hotetec se renombró a **"Apartamentos Can Denga"** y se migró a la URL `/alojamiento/apartamentos-can-denga`.
- **Mayo 2026**: el cliente percibe una caída de conversión y propone revertir.

### 1.2. Argumentos a favor del rename (recordatorio del racional de 2023)
1. **Diferenciación intra-marca**: el grupo Miramar Mallorca Collection ya operaba *Hotel Miramar Mallorca* y *Apartamentos Miramar*. Un tercer producto llamado *"Aptos Miramar 2"* implicaba:
   - **Canibalización SERP** entre las tres fichas para *"miramar"*, *"hotel miramar pollensa"*, *"apartamentos miramar"*.
   - **Confusión de usuario** (¿"Miramar 2" es una versión inferior? ¿una segunda torre?).
   - **Ambigüedad para Google** sobre qué establecimiento mostrar en el knowledge panel y resultados locales.
2. **Naming débil y genérico**: "Aptos Miramar 2" es un sufijo numérico que no construye marca. No genera búsquedas branded distintas, no se puede vincular a un POI físico diferenciado y no aporta valor diferencial.
3. **"Can Denga"** (Ca'n Denga en mallorquín) es **toponímico, único y arraigado**: identifica una casa señorial concreta, conecta con la cultura local, permite ranking sin colisión y es indexable como entidad propia por Google (KGE).
4. **Tendencia del mercado**: Booking, Tripadvisor y OTAs penalizan duplicidades nominales dentro del mismo grupo (impacto en la matching engine y en la dispersión de reviews).

### 1.3. Verificación post-hoc en datos (mayo 2026)
- La keyword **"aptos miramar 2"** no genera ni un solo resultado en SERP overview Ahrefs ni en GSC (volumen ≈ 0). Era una *zombie keyword* sin demanda real.
- En contraste, **"miramar"** + Pollensa concentra todo el tráfico branded del grupo (ver §5). El cambio liberó esa "ranking equity" hacia el verdadero Hotel Miramar y Apartamentos Miramar, que hoy son los que más tráfico capturan.

> **Conclusión §1**: el rename fue una decisión SEO **correcta y respaldada por datos**. Mantenerlo es la base del informe.

---

## 2. Análisis de marca online — "Apartamentos Can Denga" en la SERP, OTAs y directorios

### 2.1. Visibilidad SERP (Ahrefs SERP Overview, mercado ES)

| Keyword | Volumen ES | Resultados Ahrefs | Hallazgo |
|---|---|---|---|
| "apartamentos can denga" | n.d. (<10) | **0 resultados trackeados** | Volumen tan bajo que Ahrefs no indexa la SERP. La marca pura no genera demanda medible. |
| "can denga puerto pollensa" | n.d. | 0 resultados trackeados | Igual: demanda mínima. |
| "apartamentos can denga puerto pollensa" | n.d. | 0 resultados trackeados | Igual. |
| "aptos miramar 2" | 0 | 0 resultados trackeados | El naming anterior tampoco tenía demanda. |
| "apartamentos miramar puerto pollensa" | n.d. | 0 resultados trackeados | — |

**Lectura SEO:** la marca "Can Denga" todavía está en fase de **construcción de notoriedad** (3 años escasos). No hay un body of search significativo. **Esto es esperable y no implica fracaso del rename**: la búsqueda branded de un apartamento independiente con volumen estimado <50 al mes tarda 5–7 años en consolidarse, sobre todo en un mercado tan saturado como Pollensa.

> **Acción correctiva:** la baja visibilidad SERP no se debe revertir cambiando otra vez de nombre — se debe atacar con (a) endorsing de marca paraguas Miramar, (b) optimización técnica de la ficha, (c) SEO local, (d) building de reseñas y citaciones.

### 2.2. OTAs, metabuscadores y directorios — Inconsistencias a verificar

> ⚠️ **Verificación manual pendiente.** El cliente debe completar el checklist siguiente porque las OTAs bloquean crawlers automáticos. Lo que conocemos con certeza:

**Datos de referencia (GBP, captura del cliente):**
- Nombre: **Apartamentos Can Denga** ✅ Verified
- Categoría: **Apartamento turístico**
- Place ID: `ChIJoX4KoiTVlxIRdCLwj-YUSnI`
- CID: `8235417849090286196`
- Business Profile ID: `14708320502346111732`
- KG ID: `/g/11b8t7hgg4`
- Dirección: `Carrer de l'Almirall Cervera, 11, 07470 Port de Pollença, Illes Balears`
- Teléfono: `+34 971 866 400` (idéntico al Hotel Miramar — ver §2.3)
- Web (con UTM): `https://www.miramarcollection.com/alojamiento/apartamentos-can-denga/?utm_source=google&utm_medium=organic&utm_campaign=GMB&utm_content=ApartamentosCanDenga` ✅ correcto
- 6 reviews · 4.7★ · 35 fotos
- 3 servicios / 0 atributos

**Checklist NAP — verificación manual urgente (próximos 15 días):**

| Plataforma | Verificar | Estado |
|---|---|---|
| Booking.com | Nombre exacto, dirección, teléfono propio (no compartido), web con UTM, sin "Aptos Miramar 2" residual | ⬜ |
| Expedia / Hotels.com | Idem | ⬜ |
| Tripadvisor | Nombre, dirección, fotos, web | ⬜ |
| Hotels.com / Vrbo / Airbnb (si listado) | Idem | ⬜ |
| Trivago / Kayak / Skyscanner (meta) | Idem | ⬜ |
| HolidayCheck | Idem | ⬜ |
| Google Hotel Ads / Google Travel | Knowledge panel, info, fotos, precio link | ⬜ |
| Bing Places | Existencia + datos | ⬜ |
| Apple Business Connect (Apple Maps) | Existencia, NAP, fotos | ⬜ |
| Yelp | Existencia, NAP | ⬜ |
| Foursquare | Existencia, NAP | ⬜ |
| OpenStreetMap | Existencia del POI, etiqueta `tourism=apartment`, nombre actualizado | ⬜ |
| Wikidata | Item creado para Can Denga | ⬜ |
| Mapbox | Verificar POI | ⬜ |
| Geonames | Verificar entrada | ⬜ |
| Visit Mallorca / Illesbalears.travel | Ficha turística oficial | ⬜ |
| Cámara de Comercio / Registro turístico CAIB | Nombre comercial registrado | ⬜ |

**Banderas rojas habituales a buscar específicamente:**
1. Listings antiguos con **"Aptos Miramar 2"** sin redirección/actualización (revisar Booking history y Tripadvisor especialmente).
2. Listings duplicados (un perfil "Aptos Miramar 2" + un perfil "Can Denga" en la misma plataforma).
3. **Teléfono compartido con Hotel Miramar** (`+34 971 866 400`): conviene tener un número o extensión propia para Can Denga para evitar que Google fusione entidades.
4. Email del schema: `reservas@hotel-miramar.net` → señal débil para una entidad llamada "Can Denga". Considerar `reservas@candenga.com` o `candenga@miramarcollection.com`.
5. Coordenadas GPS: el schema marca `39.9083, 3.08307` (idénticas al edificio principal de Miramar). Si Can Denga está físicamente en un edificio distinto, **ajustar coordenadas** para diferenciar el POI.

### 2.3. Riesgo de "merging de entidad" con Hotel Miramar

Google puede estar **fusionando la entidad Can Denga con Hotel Miramar** debido a:
- Mismo teléfono.
- Mismas coordenadas en schema (a confirmar).
- Misma dirección postal (¿está el establecimiento en el mismo número 11 o en otro?).
- Email corporativo `@hotel-miramar.net`.
- Endorsing "Miramar Collection" en logo + nombres de archivo de imágenes.

→ Si Google considera que Can Denga es un departamento del Hotel Miramar, el knowledge panel branded para "apartamentos can denga" simplemente no se mostrará como entidad independiente (que es exactamente lo que reporta el cliente). **Esto se ataca con datos estructurados distintivos, NO con un rebrand al naming anterior**.

---

## 3. Análisis evolutivo orgánico — 24 meses pre/post rename

### 3.1. Tráfico orgánico estimado del dominio (Ahrefs, mercado ES)

| Periodo | Tráfico orgánico mensual medio | Pico |
|---|---|---|
| **Pre-rename** may 2022 – abr 2023 (12 meses) | **9** | 17 (dic 2022) |
| **Post-rename Y1** may 2023 – abr 2024 (12 meses) | **20** | 28 (sep 2023) |
| **Post-rename Y2** may 2024 – abr 2025 (12 meses) | **35** | 57 (abr 2025) |
| **Post-rename Y3** may 2025 – may 2026 (12 meses) | **40** | 58 (ago 2025) |

**Conclusión:** el dominio en su conjunto ha **multiplicado x4 su tráfico orgánico estimado** desde el rename. No estamos ante una crisis de tráfico orgánico global. *Sin embargo, esta métrica es del dominio, no del establecimiento Can Denga aislado — ver §3.4.*

### 3.2. Keywords rankeadas (Ahrefs, todas las posiciones)

| Mes | Top 3 | Top 4-10 | Top 11-20 | Top 21-50 | Top 51+ | **Total** |
|---|---|---|---|---|---|---|
| abr 2023 (pre) | 0 | 2 | 12 | 39 | 78 | **131** |
| oct 2023 | 1 | 10 | 16 | 81 | 237 | **345** (pico) |
| abr 2024 | 1 | 8 | 33 | 105 | 223 | **370** (pico absoluto) |
| oct 2024 | 0 | 11 | 9 | 65 | 99 | 184 |
| abr 2025 | 0 | 14 | 19 | 47 | 32 | 112 |
| oct 2025 | 0 | 14 | 5 | 10 | 2 | 31 |
| **may 2026** | **0** | **5** | **1** | **1** | **0** | **7** |

**Hallazgo crítico:** entre abril 2024 y mayo 2026 el dominio ha perdido **el 98% de las keywords del long-tail (top 51+)** y el 96% de las del medio (top 21–50). Esto NO es atribuible al rename de mayo 2023 (que ocurrió mucho antes). **Algo ocurrió en H2 2024 que afectó masivamente la indexación / ranking del long-tail**, y se mantiene la sangría hasta hoy. Hipótesis a investigar:

- Cambio de plantilla / re-lanzamiento web (verificar con cliente: ¿hubo migración o cambio importante de la web en 2024?).
- Cambio de motor de reservas o de gestor de contenidos.
- Bloqueo de bots o robots.txt accidental.
- Eliminación masiva de páginas (blog, actividades) — ver §3.3.
- Algún update de Google (Helpful Content / Reviews / Spam) que penalizó el contenido fino del long-tail.

### 3.3. Páginas con tráfico orgánico (Ahrefs)

| Mes | Pages con tráfico |
|---|---|
| may 2022 | 2 |
| abr 2023 (pre-rename) | 36 |
| oct 2023 | 58 |
| **abr 2024 (pico)** | **75** |
| oct 2024 | 29 |
| abr 2025 | 14 |
| oct 2025 | 11 |
| **may 2026** | **4** |

**El dominio sólo tiene HOY 4 páginas que reciben algo de tráfico orgánico**:
1. `/` (home) – 14 visits, top KW "hotel miramar puerto pollensa" pos 7
2. `/alojamiento/apartamentos-miramar` – 9 visits, top KW "miramar apartamentos" pos 6
3. `/puerto-de-pollensa` – 1 visit
4. `/en/alojamiento/apartamentos-miramar` – 0 visits

**La ficha `/alojamiento/apartamentos-can-denga` NO está entre ellas.** Esto es lo verdaderamente preocupante para el cliente, y es un problema técnico-SEO de la ficha (ver §4), no del naming.

### 3.4. Datos GSC (mercado global, oct 2024 – abr 2026; integración Ahrefs)

> Limitación: la conexión GSC del proyecto solo cubre desde oct 2024. Datos pre-rename no disponibles vía Ahrefs/GSC. Si el cliente tiene GSC en cuenta propia, se puede recuperar 16 meses adicionales — **acción: solicitar export CSV de GSC sin filtro desde 2022 si está disponible**.

| Mes | Clicks | Impresiones | CTR | Posición media |
|---|---|---|---|---|
| oct 2024 | 581 | 20.727 | 2.80% | 46.2 |
| abr 2025 | 573 | 21.988 | 2.61% | 31.9 |
| jul 2025 (pico) | **1.116** | **29.532** | 3.78% | 25.4 |
| ago 2025 | 961 | 31.849 | 3.02% | 24.1 |
| oct 2025 | 583 | 15.124 | 3.85% | 14.3 |
| ene 2026 | 760 | 20.871 | 3.64% | 16.3 |
| **abr 2026** | **530** | **16.950** | **3.13%** | **10.8** |

**Tendencias claras de los últimos 18 meses:**
- Posición media **se ha cuatruplicado en calidad** (46 → 10.8). El SEO básico del dominio está mejor que nunca.
- CTR mejorando ligeramente (de 2.8% → 3.1%).
- Estacionalidad muy marcada: pico jun-sep, valle dic-feb. Normal en hotel vacacional.
- **Clicks de temporada alta 2025 (jul-ago: 2.077 acumulados)** es el mejor verano histórico medido en GSC.

### 3.5. Keywords branded post-rename (GSC anonymous queries, 12m)

Las **12 únicas keywords** que generan algo de tráfico orgánico al dominio en los últimos 12 meses son:

| Keyword | Pos | Vol | Tráfico | URL destino |
|---|---|---|---|---|
| hotel miramar puerto pollensa | 7 | 150 | 8 | / |
| mallorca collection | 7 | 150 | 6 | / |
| miramar apartamentos | 6 | 150 | 5 | /alojamiento/apartamentos-miramar |
| hotel miramar pollensa | 7 | 150 | 4 | /alojamiento/apartamentos-miramar |
| miramar hotel puerto pollensa | 7 | 60 | 3 | / |
| apartamentos en puerto pollensa | 6 | 20 | 1 | / |
| apartamentos miramar | 7 | 250 | 1 | /alojamiento/apartamentos-miramar |
| pollensa puerto | 11 | 200 | 1 | /puerto-de-pollensa |
| pueblo pollensa | 12 | 10 | 0 | /puerto-de-pollensa |
| portomar apartments | 39 | 500 | 0 | /en/alojamiento/apartamentos-miramar |
| puerto de pollensa | 22 | 1.300 | 0 | /puerto-de-pollensa |
| pollensa | 41 | 4.400 | 0 | /puerto-de-pollensa |

**Observaciones:**
- **Cero keywords contienen "can denga"** — la marca aún no aparece como query orgánica con clicks reales.
- **Cero keywords contienen "miramar 2"** — confirma que el nombre antiguo tampoco generaba search demand.
- Toda la tracción branded la captura el lockup **"miramar"** (que beneficia a Hotel y Apartamentos Miramar, no a Can Denga).
- El cliente puede percibir "caída de conversión Can Denga" porque la ficha Can Denga **literalmente no recibe búsquedas branded**: nadie busca "can denga" todavía, y como la ficha no rankea por keywords genéricas de Pollensa, no entra tráfico.

### 3.6. URL Rating de la ficha (Ahrefs)

| Mes | UR | Comentario |
|---|---|---|
| abr 2024 | 5.0 | Estable |
| may 2025 | 4.5 | Inicio caída |
| **jul 2025** | **0.6** | **Colapso (¿desindexación? ¿pérdida masiva enlaces?)** |
| sep 2025 | 1.7 | Recuperación parcial |
| oct 2025 | 6.0 | Recuperado a niveles mejores que antes |
| abr 2026 | 6.0 | Estable |

→ Algo grave ocurrió en jun-sep 2025 con la URL (¿noindex temporal? ¿404? ¿migración?). Verificar con cliente. **Si esto se produjo justo antes de la última temporada alta, podría explicar parte de la caída de conversión que se reporta**.

---

## 4. Auditoría técnica SEO de la ficha (crawl Ahrefs Site Audit, 11-may-2026)

URL auditada: `https://www.miramarcollection.com/alojamiento/apartamentos-can-denga`
Raw HTML 75 KB · Rendered HTML no devuelto por Ahrefs (alta dependencia de JS).

### 4.1. HEAD

| Elemento | Valor | Diagnóstico |
|---|---|---|
| `<html lang>` | `es` | ✅ OK (debería complementarse con hreflang) |
| `<title>` | `Apartamentos Can Denga • Apartamentos en Puerto de Pollensa` (59c) | 🟠 Falta endorsing "Miramar Mallorca Collection" |
| `<meta description>` | `Apartamentos de 3 llaves cerca del mar...` (156c) | 🟠 Genérica, no menciona Can Denga ni la marca paraguas |
| Canonical | URL self ✅ | ✅ |
| Robots | `all` | 🟠 Redundante, usar `index,follow` o nada |

### 4.2. Hreflang

- es / de / en / fr → ✅
- **`x-default`** → 🟠 AUSENTE. Añadir apuntando a la versión es.

### 4.3. Open Graph (CRÍTICO)

| Tag | Valor actual | Problema |
|---|---|---|
| `og:title` | "Miramar Collection • Apartamentos Puerto de Pollensa, Mallorca" | 🔴 Genérico, no menciona Can Denga |
| `og:description` | Descripción de grupo, no de la ficha | 🔴 Genérico |
| `og:url` | `https://miramarcollection.com/` | 🔴 **Apunta a la home — incoherente con canonical** |
| `og:image` | `galeria9-apartamentos-can-denga-miramar-mallorca-collection.jpg` | 🟠 Usar el hero, no foto secundaria |
| `og:type` | `website` | 🟠 Debería ser `product` o `article` |
| `og:site_name` | AUSENTE | 🟠 Añadir "Miramar Mallorca Collection" |
| `og:locale` | AUSENTE | 🟠 Añadir `es_ES` |

→ **Cualquier compartición en WhatsApp/Facebook/LinkedIn/Slack lleva al usuario a la home**, no a la ficha. Pérdida directa de conversión social.

### 4.4. Twitter Card

- `twitter:card` `summary_large_image` ✅
- `twitter:image` ✅
- `twitter:title`, `twitter:description`, `twitter:site` → AUSENTES 🟠

### 4.5. Headings

- **H1 contaminado:** `"APARTAMENTOS CAN DENGA Desayuno disponible en el Hotel Miramar. Consulte en recepción."` — el `<span class="tooltiptext">` está dentro del `<h1>`. Google indexa todo el H1, ensuciando la relevancia semántica.
- Falta endorsing visible: no aparece "by Miramar" o "Miramar Mallorca Collection" junto al H1.
- H2 / H3 razonables pero genéricos (`APARTAMENTOS`, `SERVICIOS`, `TAMBIÉN TE RECOMENDAMOS`).

### 4.6. Schema VacationRental (CRÍTICO)

Implementado (✅) pero **muy incompleto**:

```json
"@type":"VacationRental","name":"Apartamentos Can Denga",
"address":{"streetAddress":"Carrer de l'Almirall Cervera, 11",
"postalCode":"07470","addressLocality":"Port de Pollença",
"addressRegion":"Illes Balears","addressCountry":"España"},
"telephone":"(+34) 971 86 64 00",
"geo":{"latitude":39.9083,"longitude":3.08307},
"starRating":"***","numberOfRooms":null,
"email":"reservas@hotel-miramar.net"
```

**Campos AUSENTES o vacíos** (cada uno es una pérdida de visibilidad en rich results):

| Campo | Estado | Impacto |
|---|---|---|
| `aggregateRating` | AUSENTE | 🔴 Sin estrellas en SERP. Mata el CTR. |
| `review` / `Review` items | AUSENTE | 🔴 |
| `numberOfRooms` | `null` | 🟠 |
| `numberOfBedrooms` | AUSENTE | 🟠 |
| `floorSize` | AUSENTE | 🟠 |
| `occupancy` | AUSENTE | 🟠 |
| `checkinTime` / `checkoutTime` | AUSENTE | 🟠 |
| `priceRange` / `Offer` | AUSENTE | 🔴 Sin precio en knowledge panel |
| `amenityFeature` granular | Parcial (string) | 🟠 |
| `image` (multiple) | Solo 1 imagen | 🟠 Debería listar 6-8 |
| `addressCountry` | `"España"` | 🟠 Usar ISO `"ES"` |
| `telephone` E.164 | `(+34) 971 86 64 00` | 🟠 Usar `+34971866400` |
| Tipo principal | `VacationRental` | ✅ OK. Alternativa: `LodgingBusiness` o `Apartment` |
| `BreadcrumbList` JSON-LD | AUSENTE (solo microdata) | 🟠 Duplicar como JSON-LD |
| `Organization` (marca paraguas) | AUSENTE | 🟠 Añadir org Miramar Collection con `sameAs` redes |

### 4.7. Imágenes

- 28 `<img>` en la página.
- ✅ Todas con `alt` no vacío.
- 🔴 Todas con `src="data:image/png;base64,..."` (pixel transparente) + `data-src` real → **dependencia total de JS para que se carguen**. Bots sin JS no ven imágenes reales.
- Hero con `loading="lazy"` Y `fetchpriority="high"` simultáneamente: **contradictorio**. Para LCP usar `loading="eager" fetchpriority="high"`.

### 4.8. Render JS

- Ahrefs no consiguió obtener el `rendered_html` (devuelve `null`). Indica que la página tiene dependencia muy alta de JS o algún error en el render.
- Acción: comprobar con Google Search Console URL Inspection si Googlebot está renderizando correctamente la ficha.

### 4.9. Site Audit — Issues activos del proyecto (paraguas)

17 issues con URLs afectadas. Los más relevantes:

| Issue | Importancia | URLs afectadas | Categoría |
|---|---|---|---|
| Page in multiple sitemaps | Notice | 148 | Sitemaps (limpiar duplicidades) |
| X-default hreflang annotation missing | Notice | 156 | Localization |
| Open Graph URL not matching canonical | Warning | 156 | Social tags |
| Structured data schema.org validation error | Notice | 48 | Schema |
| Meta description too long | Warning | 38 | Content |
| 302 redirect | Warning | 29 | Redirects (revisar si deberían ser 301) |
| 3XX redirect | Warning | 30 | Redirects |
| Title too long | Warning | 12 | Content |
| Meta description missing or empty | Warning | 8 | Content |
| CSS file size too large | Warning | 4 | Performance |
| Slow page | Warning | 2 | Performance |
| **Organic traffic dropped** | Notice | 1 | **Other** |
| **Pages dropped from Top 10** | Notice | 1 | **Other** |

→ Site Audit confirma que Ahrefs ha detectado pérdida de tráfico orgánico y caídas de keywords del top 10. Mapear concretamente qué URLs son.

---

## 5. Análisis del perfil GBP y Google Maps

Datos extraídos de la captura proporcionada:

| Campo | Valor | Diagnóstico |
|---|---|---|
| Nombre | Apartamentos Can Denga | ✅ |
| Verificación | ✅ Verified | ✅ |
| Categoría | Apartamento turístico (solo 1) | 🟠 Añadir categorías secundarias: "Servicio de alquiler vacacional", "Hospedaje turístico" |
| Place ID | ChIJoX4KoiTVlxIRdCLwj-YUSnI | ✅ |
| CID | 8235417849090286196 | ✅ |
| KG ID | /g/11b8t7hgg4 | ✅ La entidad existe en Knowledge Graph |
| Dirección | Carrer de l'Almirall Cervera, 11, 07470 Port de Pollença | ✅ Coherente con schema |
| Teléfono | +34 971 866 400 | 🔴 **Compartido con Hotel Miramar — riesgo merging de entidad** |
| Web | URL ficha + UTM ✅ | ✅ Correcto |
| Reseñas | **6** | 🔴 Muy bajo (vs Hotel Miramar y Apartamentos Miramar, comprobar) |
| Rating | 4.7★ | ✅ Excelente media (pero base pequeña) |
| Fotos | 35 | 🟠 Aceptable pero ampliable a 60-100 |
| Atributos | 0 | 🔴 Crítico: 0 atributos completados |
| Servicios | 3 | 🟠 Ampliable |
| KP en search "apartamentos can denga" (puro) | NO se dispara | 🔴 Falta autoridad de entidad |
| KP en search "apartamentos can denga puerto pollensa" | SÍ se dispara | ✅ Funciona con modificador geo |

### 5.1. Diagnóstico GBP

1. El perfil **existe, está verificado y referencia correctamente la web** con UTM.
2. El knowledge panel **no se dispara para búsqueda branded pura** porque la entidad Can Denga aún no tiene suficiente "evidence" en la red (citaciones, reseñas, menciones, schema). Google la trata como un POI poco prominente.
3. **6 reseñas son muy pocas** para una marca que lleva 3 años. Como referencia, hoteles similares en Pollensa rondan 200–1.500 reseñas. Esto es lo que más urge atacar.
4. **Teléfono compartido con Hotel Miramar** y **email corporativo `@hotel-miramar.net`**: refuerzan la ambigüedad de entidad. Si Google fusiona Can Denga con Hotel Miramar, el KP propio de Can Denga es difícil que se separe.
5. **0 atributos cumplimentados** → desperdicia coincidencias para filtros de búsqueda (WiFi gratis, piscina, admite mascotas — actualmente "No"—, etc.).

### 5.2. Acciones GBP — prioridad ALTA (semanas 1-4)

| Acción | Detalle |
|---|---|
| **Catalogar 30+ atributos** | Servicios, accesibilidad, opciones de pago, mascotas, idiomas, sostenibilidad, accommodations features |
| **Aumentar a 80+ fotos** | Por categoría: exterior, interior por habitación, baño, cocina, piscina, vistas, alrededores, equipo |
| **Estrategia de reseñas** | (a) QR física check-in/check-out · (b) Email post-stay automatizado a las 24-48 h del checkout · (c) Tablet en recepción · (d) Tarjeta de agradecimiento con link corto · (e) Incentivar reseñas en idiomas variados (EN/DE/FR) |
| **Posts de Google** | 1 post/semana mínimo: ofertas, eventos Pollensa, novedades |
| **Q&A propio** | Sembrar 10-15 preguntas frecuentes con respuestas propias |
| **Productos / habitaciones** | Listar las distintas tipologías de apartamento con foto, precio rango, descripción |
| **Mensajes activos** | Mensajería de GBP activada con respuesta < 1 h |
| **NAP independiente** | Si físicamente es viable, asignar teléfono propio o extensión visible diferenciada |
| **Email no-paraguas** | `candenga@miramarcollection.com` o similar |

---

## 6. Riesgo de cambiar el naming AHORA — argumentario para el Account

Cambiar el nombre EN PLENA TEMPORADA (mayo–octubre) tendría consecuencias técnicas y comerciales graves:

### 6.1. Riesgos SEO

| Riesgo | Probabilidad | Impacto |
|---|---|---|
| Reindexación lenta del nuevo URL (cambio de slug) | Alta | Pérdida 4-12 semanas de visibilidad orgánica residual |
| Pérdida del Place ID actual y necesidad de migración GBP (con cambio de nombre Google requiere revalidación, fotos pueden caerse, link a reviews puede romperse) | Media-Alta | Pérdida temporal de KP, reviews "reset" perceptual |
| Cancelación/duplicación de listings OTA (Booking pide alta nueva si renombras) | Alta | Caída inmediata de visibilidad en metas / OTAs |
| Pérdida histórica de reviews en plataformas que no permitan rename del listing (Tripadvisor especialmente conservador) | Media | Las 6 reviews actuales podrían "resetearse" en algunos canales |
| Desalineación entre los datos en wholesalers, channel manager, PMS y motor de reservas | Alta | Disponibilidad/precios desincronizados; cancelaciones forzadas |
| Schema.org y citaciones (Yelp, OSM, Wikidata) requieren actualización manual una a una | Alta | Inconsistencia NAP penaliza SEO local 6-12 meses |
| Confusión de huéspedes con reservas pendientes ("¿es el sitio donde reservé?") | Alta | Reclamaciones, cancelaciones, mala reputación |
| Pérdida temporal de búsquedas branded | Cierta | Pérdida directa de conversión |
| Inestabilidad tracking GA4 / Tag Manager (cambiar nombre rompe segmentos, audiencias, dashboards) | Media | Falta de visibilidad para decisiones |

### 6.2. Coste-beneficio de revertir a "Aptos Miramar 2"

| Aspecto | Volver a "Aptos Miramar 2" | Mantener "Can Denga" + reforzar |
|---|---|---|
| Demanda search documentada | 0 búsquedas/mes | Demanda incipiente pero diferenciable |
| Diferenciación intra-marca | -- canibaliza Hotel y Apartamentos Miramar | ++ identidad propia |
| Reutilizar reviews históricas Booking pre-2023 | Posible (depende de cómo se hizo la migración 2023) | Acumular reviews bajo marca actual |
| Coste de reversión | Muy alto (ver §6.1) | 0 |
| Resultados visibles | 3-9 meses + temporada perdida | 1-3 meses (optimizaciones técnicas) |
| Riesgo regulatorio (registro turístico CAIB) | Trámites administrativos | 0 |

→ **Volver atrás cuesta caro y resuelve un problema que no es el verdadero**.

### 6.3. Si hubiera que rebrand alguna vez: ventana correcta

- **Nunca** entre 1 mayo y 31 octubre.
- Ventana ideal: **1 noviembre – 15 enero**.
- Pre-trabajo de 30-45 días antes (alineación OTA, PMS, channel manager, redirects, comunicación a clientes con reservas).

---

## 7. Propuesta de naming reforzado (mantener Can Denga + endorsing)

En lugar de un rename completo, **refuerzo de marca paraguas** sin perder la diferenciación SEO:

| Opción | Pros | Contras | Recomendación |
|---|---|---|---|
| **"Ca'n Denga by Miramar Mallorca"** | Endorsing claro, identidad propia, vinculación grupal, longitud razonable | Cambio mínimo en GBP/OTA | ⭐ **PRIMERA OPCIÓN** |
| "Ca'n Denga – Miramar Collection" | Estilo collection, premium | Menos directo el lockup geográfico | Segunda opción |
| "Apartamentos Ca'n Denga – Miramar Mallorca" | Mantiene "apartamentos" para SEO genérico | Largo | Alternativa |
| "Apartamentos Can Denga" (actual) | Cambio cero | Cero endorsing visible | Status quo, no recomendado |

### 7.1. Implementación del endorsing (sin rename pleno)

Se trata de un cambio **de copy y schema, no de slug URL ni de razón social registrada**. No requiere migración OTA ni cambio de Place ID. Pasos:

1. **Title** → `Ca'n Denga by Miramar Mallorca · Apartamentos en Port de Pollença`
2. **H1** → `Apartamentos Ca'n Denga` + subtítulo H2 / kicker `by Miramar Mallorca Collection`
3. **og:title** y **twitter:title** alineados.
4. **Schema VacationRental**: `"name": "Ca'n Denga by Miramar Mallorca"`, añadir `"brand": {"@type":"Organization","name":"Miramar Mallorca Collection"}`, `"parentOrganization": {...}`.
5. **GBP** → renombrar a "Ca'n Denga by Miramar Mallorca" (cambio de display name, no de Place ID si Google lo permite — alternativamente solicitar el cambio gestionado vía soporte GBP).
6. **OTAs** → cambio de display name coordinado con Booking/Expedia/Tripadvisor (no cambia el property ID, sólo el nombre mostrado).
7. **Comunicación** a clientes con reservas: email informativo de "evolución de marca" con foto y dirección iguales.
8. Plazo: implementación de copy/schema en 1 sprint (1 semana); OTAs/GBP en 4-6 semanas.

> ⚠️ Aunque sea un cambio "menor", **NO ejecutarlo en plena temporada**. Lanzar en **noviembre 2026** salvo que SEM/PR/marca tengan urgencia mayor demostrada.

---

## 8. Plan de acción SEO recomendado (sin tocar el naming en temporada)

### 8.1. Sprint 1 — semanas 1-2 (URGENTE, sin riesgo de temporada)

| # | Acción | Owner | Impacto esperado |
|---|---|---|---|
| 1 | Arreglar `og:url` (debe apuntar a la URL canónica, no a home) | Web Dev | Recuperación de tráfico social-share |
| 2 | Personalizar `og:title`, `og:description`, `og:image` para la ficha | Web Dev + SEO | CTR social |
| 3 | Limpiar `<h1>` (sacar tooltip fuera) | Web Dev | Relevancia semántica |
| 4 | Añadir `og:type=product`, `og:site_name`, `og:locale=es_ES` | Web Dev | Cobertura Open Graph |
| 5 | Añadir `twitter:title`, `twitter:description`, `twitter:site` | Web Dev | Cobertura social |
| 6 | Schema: añadir `aggregateRating`, `review`, `priceRange`, `Offer`, `numberOfRooms`, `numberOfBedrooms`, `floorSize`, `occupancy`, `checkinTime/checkoutTime`, `image` array | SEO + Web Dev | **Recuperación rich results / estrellas en SERP** |
| 7 | Schema: corregir `addressCountry` a `ES`, teléfono a E.164, parent `Organization`, breadcrumbs en JSON-LD | SEO + Web Dev | Schema cleanliness |
| 8 | Hreflang: añadir `x-default` | Web Dev | Cobertura internacional |
| 9 | Hero image: `loading="eager"` + `fetchpriority="high"` (eliminar lazy) | Web Dev | LCP, Core Web Vitals |
| 10 | Auditar render JS con Search Console URL Inspection | SEO | Identificar bloqueos de indexación |

### 8.2. Sprint 2 — semanas 3-6

| # | Acción |
|---|---|
| 11 | Auditoría exhaustiva de la caída de páginas indexadas H2 2024 (75 → 4): identificar URLs caídas, motivo, plan recuperación |
| 12 | Investigar el colapso UR jun-sep 2025 (¿noindex? ¿4xx? ¿migración?) — eventualmente recuperar enlaces internos / backlinks perdidos |
| 13 | Optimización GBP (atributos, fotos, productos, posts, Q&A) — ver §5.2 |
| 14 | Plan de captación de reseñas (email post-stay, QR check-in/out, tablet recepción) |
| 15 | Auditoría NAP en todas las OTAs y directorios (checklist §2.2) — corregir inconsistencias |
| 16 | Limpiar duplicidades en sitemaps (148 URLs afectadas) |
| 17 | Convertir 302 a 301 donde proceda (29 + 30 URLs afectadas) |
| 18 | Acortar metas description largas (38 URLs) |
| 19 | Optimizar CSS pesados / slow pages (Core Web Vitals) |
| 20 | Crear contenido SEO local Pollensa: guía detallada, mejor época, transporte, calas cercanas, mercado, eventos → atraer long-tail informacional |

### 8.3. Sprint 3 — meses 2-4 (durante temporada, sin riesgos)

| # | Acción |
|---|---|
| 21 | Estrategia de link-building local: prensa balear, guías turísticas, blogs viaje, partnerships con calas, restaurantes vecinos |
| 22 | Alta y/o optimización en fuentes de valor: **Wikidata** (crear Q-item Can Denga), **OpenStreetMap** (POI `tourism=apartment`), **Foursquare**, **Mapbox**, **Geonames**, **Apple Business Connect**, **Bing Places**, **Yandex**, **Cámara Comercio Mallorca**, **CAIB Turisme** |
| 23 | Schema Organization padre `Miramar Mallorca Collection` con `subOrganization` para cada propiedad (Hotel, Apartamentos Miramar, Can Denga, Casa Peña, Brisas, Maricel...) → ayuda Knowledge Graph a vincular entidades |
| 24 | Embeber mapa propio con Place ID + reviews snippet |
| 25 | Solicitar a clientes con buenas estancias review en Booking + Google + Tripadvisor (cadencia: 30 reseñas Q3, 60 acumuladas Q4) |
| 26 | Crear página `/sobre-can-denga` (historia del topónimo, casa, vínculo cultural) — refuerzo de entidad |

### 8.4. Sprint 4 — meses 5-6 (post-temporada, noviembre 2026)

| # | Acción |
|---|---|
| 27 | (Si aprobado) Implementar **rebrand suave** a *"Ca'n Denga by Miramar Mallorca"* — alineado en web, schema, GBP, OTAs, PMS, motor de reservas. NO cambio de URL ni Place ID si evitable. |
| 28 | Hacer schema testing y validación post-cambio |
| 29 | Comunicación coordinada a clientes (newsletter), redes sociales, prensa local |
| 30 | Medir 90 días post-cambio: GSC impresiones/clicks branded, CTR, conversiones GA4, revenue motor |

---

## 9. Factores AJENOS al SEO que pueden estar afectando la conversión

Es legítimo plantear al Account que la conversión es **multifactorial** y el SEO es solo una palanca. Hay que pedir al cliente datos para descartar:

| Factor | Cómo medirlo | Quién aporta |
|---|---|---|
| **Cambios de mercado y demanda Pollensa 2024-2026** | INE, Frontur, Ibestat Baleares, AENA llegadas PMI | SEO/Insight |
| **Precios ADR** (subida tras pandemia) | Comparar ADR 2022 vs 2025 vs competencia local | Revenue Manager |
| **Pérdida de reviews históricas** | ¿Se migraron las reviews de Booking de "Aptos Miramar 2" cuando se renombró en 2023? | Ecommerce/OTA |
| **Estacionalidad** | Comparar mismas semanas YoY | Revenue Manager |
| **Cambio de motor de reservas o web (¿2024?)** | Verificar timeline | Cliente |
| **UX del booking engine** | Heatmaps Hotjar/Clarity, tests usabilidad | UX/CRO |
| **Visibilidad OTA / contratos Booking 2024-2026** | Genius level, position bonus, % comisión, programas de visibilidad | Channel Manager |
| **Política de cancelación, depósitos, condiciones** | Auditoría del flow checkout | Revenue Manager |
| **Inversión SEM/Meta/PR vs años anteriores** | Comparar inversión total marketing | Marketing |
| **Eventos locales y comparables (Tour Mallorca, Pep Lluís Pollensa Music Festival, etc.)** | Calendar de Pollensa | Marketing |
| **Estado del producto físico** | Reformas pendientes, reseñas con críticas concretas | Operaciones |

### 9.1. Datos solicitados al cliente para cerrar el análisis

1. **GSC export 2022-2026** del dominio (CSV) si tienen GSC nativo conectado.
2. **GA4**: tráfico orgánico, conversiones, revenue directo, channel mix mensual, % nuevo vs recurrente, dispositivo, países top, de **may 2022 a hoy** filtrando por landing `/alojamiento/apartamentos-can-denga` y `/alojamiento/apartamentos-miramar-2`.
3. **Motor de reservas**: reservas, room nights, ADR, RevPAR mensual de Can Denga desde may 2022.
4. **Booking extranet**: visualizaciones, clicks, conversiones, position score, % genius, comisión efectiva.
5. **Histórico de reviews** plataforma a plataforma (cuántas tenía "Aptos Miramar 2" antes del rename, cuántas se migraron, cuántas se han añadido).
6. **Timeline de cambios web 2023-2026**: cualquier rediseño, migración, cambio de CMS o de booking engine.
7. **Inversión marketing total** (SEM, social, PR, OTAs) por año.

---

## 10. KPIs y cuadro de seguimiento propuesto

| KPI | Métrica | Baseline (may 2026) | Objetivo 3m | Objetivo 6m | Objetivo 12m |
|---|---|---|---|---|---|
| Tráfico orgánico ficha Can Denga | sesiones/mes GA4 | a recibir | +30% | +80% | +200% |
| Keywords rankeadas dominio | Ahrefs top-50 | 7 | 30 | 80 | 150 |
| Impresiones GSC ficha Can Denga | mes | a recibir | +40% | +100% | +250% |
| Reseñas Google | total | 6 | 25 | 60 | 150 |
| Rating Google | media | 4.7 | ≥4.7 | ≥4.7 | ≥4.8 |
| Fotos GBP | total | 35 | 80 | 120 | 200 |
| Atributos GBP | completados | 0 | 30 | 50 | 60 |
| Citaciones / directorios | NAP consistentes | a auditar | 20 | 35 | 60 |
| Wikidata Q-item | existencia | no | sí | enriquecido | enriquecido |
| OSM POI | etiquetado | a auditar | sí | sí | sí |
| Schema rich results | estrellas + precio en SERP | no | parcial | completo | completo |
| Conversiones directas motor | bookings/mes | a recibir | TBD | +20% | +50% |

---

## 11. Conclusiones y mensaje para el Account

1. **El rename de mayo 2023 fue una decisión SEO acertada** y está respaldada por datos: la demanda search del antiguo "Aptos Miramar 2" era inexistente, canibalizaba el lockup Miramar, y "Can Denga" permite construir una entidad propia diferenciable.
2. **La caída de conversión que percibe el cliente no se explica de forma concluyente por el rename**. El propio dominio ha multiplicado x4 su tráfico orgánico y su posición media global ha mejorado de 46 a 11 desde octubre 2024.
3. **Sin embargo, la ficha Can Denga tiene problemas técnicos SEO graves y problemas de visibilidad** que sí pueden estar dañando la conversión: 0 keywords orgánicas rankeadas, schema VacationRental incompleto, og:url apuntando a la home, dependencia total de JS para imágenes, posible fusión de entidad con Hotel Miramar, GBP sin atributos y con solo 6 reseñas.
4. **Cambiar el naming en plena temporada es una mala decisión**: alto coste, alto riesgo, beneficio nulo dado que la demanda "aptos miramar 2" es inexistente.
5. **Propuesta**: mantener "Can Denga", optimizar técnicamente la ficha en sprints inmediatos, ejecutar estrategia de SEO local, captar reseñas. En noviembre 2026 (post-temporada) valorar un **rebrand suave a "Ca'n Denga by Miramar Mallorca"** que sume endorsing sin perder identidad propia.
6. **Faltan datos del cliente** (GA4, motor, OTAs, timeline cambios web) para cerrar el análisis de conversión y descartar factores ajenos al SEO. Estos datos son el siguiente bloque a recopilar.

---

## Anexo A — Inventario de datos extraídos

- **Site Explorer metrics**: actual (may 2026) + comparativa (abr 2023)
- **Metrics history 48 meses** (may 2022 – may 2026): tráfico, costo, paid
- **Keywords history 48 meses**: distribución por posiciones
- **Pages history 48 meses**: número de páginas con tráfico
- **Top pages**: actual vs abril 2023
- **Organic keywords**: 100 KW abril 2023 vs 7 KW mayo 2026
- **URL Rating history 24 meses**
- **GSC performance history**: oct 2024 – abr 2026
- **GSC anonymous queries 12m**: 12 KW
- **Site Audit issues**: 17 issues activos
- **Site Audit page content**: HTML completo de la ficha (auditoría técnica completa §4)
- **SERP overview** branded: 4 keywords (todas con 0 resultados — confirmación de baja demanda)
- **GBP** datos capturados de la pantalla del cliente

## Anexo B — Datos pendientes de recopilar (cliente)

- GSC export CSV nativo 2022-2026
- GA4 tráfico orgánico + conversiones filtrado por landing Can Denga (may 2022 – hoy)
- Motor de reservas: bookings/ADR/revenue Can Denga
- Booking extranet métricas
- Histórico de reviews por plataforma (Booking, Tripadvisor)
- Timeline de cambios web/booking engine 2023-2026
- Inversión marketing total por año

## Anexo C — Referencias técnicas

- Proyecto Ahrefs Site Explorer/Audit: `Miramarcollection` (ID 9482880)
- Proyecto Site Explorer relacionado: `Miramarsoller` (ID 9482885)
- Ahrefs Site Audit crawl: 2026-05-11 — Health score 100, 612 URLs crawled, 0 errores, 190 warnings, 157 notices
- Subscripción Ahrefs Advanced (anual)
- API units consumidos en este informe: ≈5.700 / 1.000.000 disponibles

---

*Informe redactado por el SEO Manager. Para dudas o ampliaciones, escalar antes de presentar al cliente.*
