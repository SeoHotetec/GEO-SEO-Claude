"""
Genera el informe ejecutivo (1-2 págs) en .docx para el Account de Miramar
Collection — caso re-rename Apartamentos Can Denga.
"""
from pathlib import Path
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


PRIMARY = RGBColor(0x0F, 0x3D, 0x5C)
ACCENT_OK = RGBColor(0x1B, 0x7A, 0x3E)
ACCENT_WARN = RGBColor(0xC2, 0x6A, 0x05)
ACCENT_BAD = RGBColor(0xB3, 0x1B, 0x1B)
MUTED = RGBColor(0x55, 0x55, 0x55)


def set_cell_shading(cell, hex_color):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), hex_color)
    tc_pr.append(shd)


def add_heading(doc, text, size=13, color=PRIMARY, space_before=8, space_after=2):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(size)
    run.font.color.rgb = color
    return p


def add_para(doc, runs, size=9.5, space_after=3, align=None):
    """runs: list of (text, bold, color or None)"""
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(0)
    if align is not None:
        p.alignment = align
    for text, bold, color in runs:
        r = p.add_run(text)
        r.bold = bold
        r.font.size = Pt(size)
        if color is not None:
            r.font.color.rgb = color
    return p


def add_bullet(doc, runs, size=9.5):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.left_indent = Cm(0.5)
    for text, bold, color in runs:
        r = p.add_run(text)
        r.bold = bold
        r.font.size = Pt(size)
        if color is not None:
            r.font.color.rgb = color
    return p


def build():
    doc = Document()

    # Márgenes ajustados para 1-2 páginas
    for section in doc.sections:
        section.top_margin = Cm(1.4)
        section.bottom_margin = Cm(1.4)
        section.left_margin = Cm(1.6)
        section.right_margin = Cm(1.6)

    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(9.5)

    # ---- CABECERA ----
    title = doc.add_paragraph()
    title.paragraph_format.space_after = Pt(0)
    r = title.add_run("INFORME EJECUTIVO SEO")
    r.bold = True
    r.font.size = Pt(15)
    r.font.color.rgb = PRIMARY

    sub = doc.add_paragraph()
    sub.paragraph_format.space_after = Pt(2)
    r = sub.add_run("Propuesta de re-rename — Apartamentos Can Denga (ex “Aptos Miramar 2”)")
    r.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = PRIMARY

    meta = doc.add_paragraph()
    meta.paragraph_format.space_after = Pt(4)
    r = meta.add_run(
        "Cliente: Miramar Mallorca Collection · Web: miramarcollection.com · "
        "Establecimiento: Apartamentos Can Denga (Port de Pollença) · "
        "Para: Account · Autor: SEO Manager — Hotetec · Fecha: 14 mayo 2026"
    )
    r.font.size = Pt(8.5)
    r.font.color.rgb = MUTED
    r.italic = True

    # Línea separadora visual
    line = doc.add_paragraph()
    line.paragraph_format.space_after = Pt(4)
    rline = line.add_run("─" * 95)
    rline.font.color.rgb = PRIMARY
    rline.font.size = Pt(7)

    # ---- 1. RECOMENDACIÓN ----
    add_heading(doc, "1 · Recomendación al cliente", size=11)
    add_para(doc, [
        ("NO revertir", True, ACCENT_BAD),
        (" el naming a “Aptos Miramar 2” y ", False, None),
        ("NO ejecutar ningún cambio de marca en plena temporada", True, ACCENT_BAD),
        (" (mayo–octubre 2026). El cambio de 2023 fue una decisión SEO correcta y los datos lo respaldan: ", False, None),
        ("la caída de conversión percibida no se explica de forma concluyente por el rename", True, None),
        (". Sí existen oportunidades reales de mejora en la ficha y en el ecosistema de marca que deben ser el foco de acción.", False, None),
    ], space_after=4)

    # ---- 2. ARGUMENTARIO PARA EL CLIENTE ----
    add_heading(doc, "2 · Argumentos para defender la decisión de 2023", size=11)
    add_bullet(doc, [
        ("Naming anterior débil y canibalizador. ", True, None),
        ("“Aptos Miramar 2” era genérico, con sufijo numérico, sin entidad propia y colisionaba con Hotel Miramar Mallorca y Apartamentos Miramar dentro del mismo grupo. Provocaba canibalización SERP, confusión de usuario y ambigüedad para Google.", False, None),
    ])
    add_bullet(doc, [
        ("“Can Denga” es toponímico, único y arraigado. ", True, None),
        ("Identifica un POI físico diferenciado, rankeable como entidad propia (Knowledge Graph), sin colisión con el resto de la cadena.", False, None),
    ])
    add_bullet(doc, [
        ("La keyword “aptos miramar 2” no tenía demanda real. ", True, None),
        ("Volumen ≈ 0 en Ahrefs y GSC: era una zombie keyword sin búsquedas branded medibles. Volver no recupera tráfico, porque nunca lo hubo bajo ese nombre.", False, None),
    ])
    add_bullet(doc, [
        ("Tendencia del dominio post-rename es positiva. ", True, None),
        ("Posición media en GSC mejora de 46 (oct 2024) → 10,8 (abr 2026); impresiones y clicks crecen en temporada (pico 1.116 clicks en jul 2025). El dominio NO se ha deteriorado tras el cambio.", False, None),
    ])
    add_bullet(doc, [
        ("Revertir ahora sería el peor escenario posible. ", True, None),
        ("Implica reindexación, pérdida temporal de branded, fluctuaciones SEO, desalineación OTA, problemas de tracking, confusión del usuario en plena temporada y pérdida del trabajo de notoriedad de los últimos 24 meses.", False, None),
    ])

    # ---- 3. LECCIÓN APRENDIDA SOBRE LA MIGRACIÓN ----
    add_heading(doc, "3 · Lección aprendida: la migración de 2023 necesitaba orquestación", size=11)
    add_para(doc, [
        ("Un cambio de nombre solo funciona si se ejecuta como ", False, None),
        ("una operación coordinada en bloque, simultánea y rápida en todos los canales", True, None),
        (". En 2023 desde SEO se acompañó la migración con redirecciones 301, actualización de la ficha y metadatos. ", False, None),
        ("Sin embargo, ", False, None),
        ("si el cambio no se trasladó de forma sincronizada al resto de canales", True, None),
        (" — Booking, Expedia, Tripadvisor, metabuscadores, directorios locales, GBP, Apple Maps, campañas de email a clientes y prospects, RRSS, materiales offline, comunicación pre-stay y post-stay — el ecosistema de marca queda fragmentado durante meses, las entidades no se fusionan correctamente en Google, los reviews históricos no se traspasan al nuevo perfil, y la nueva marca tarda mucho más en consolidarse.", False, None),
    ], space_after=3)
    add_para(doc, [
        ("Es razonable que parte de la caída de conversión que percibe el cliente provenga de ese gap de coordinación, no del nombre en sí mismo. ", False, None),
        ("La lectura correcta no es revertir, sino completar y reforzar ahora lo que entonces no se cerró:", True, None),
        (" auditar y unificar la presencia en todas las OTAs/directorios, ejecutar una campaña activa de comunicación de marca (email a base de clientes, post-stay con CTA a reseña, social, prensa local de Pollença, materiales del propio establecimiento), y aplicar endorsing visual “Ca’n Denga — Miramar Mallorca Collection” en todos los puntos de contacto.", False, None),
    ], space_after=4)

    # ---- 4. HALLAZGOS CLAVE (TABLA) ----
    add_heading(doc, "4 · Hallazgos clave (Ahrefs · GSC · revisión SEO)", size=11)
    table = doc.add_table(rows=1, cols=3)
    table.autofit = True
    hdr = table.rows[0].cells
    hdr[0].text = "Bloque"
    hdr[1].text = "Diagnóstico"
    hdr[2].text = "Estado"
    for c in hdr:
        set_cell_shading(c, "0F3D5C")
        for p in c.paragraphs:
            for run in p.runs:
                run.bold = True
                run.font.size = Pt(9)
                run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    rows = [
        ("Decisión rename 2023", "Acertada. Era nombre débil y canibalizador dentro del grupo.", "✅ Defendible"),
        ("Volumen branded “Can Denga”", "Sin volumen medible en Ahrefs tras 24 meses: marca aún en fase de construcción de notoriedad (proceso 5–7 años en este nicho).", "🟠 Esperado"),
        ("Volumen “Aptos Miramar 2”", "Volumen ≈ 0. El nombre anterior tampoco generaba demanda branded.", "✅ Confirma rename"),
        ("URL de ficha en Ahrefs", "0 keywords / 0 tráfico orgánico (mayo 2026). Caída anómala del URL Rating jun–sep 2025 (5,0 → 0,6) — incidencia técnica a investigar.", "🔴 Crítico"),
        ("Tendencia GSC dominio", "Posición media 46 → 10,8 en 18 meses. Clicks pico 1.116 en jul 2025. Tendencia positiva sostenida.", "✅ Positivo"),
        ("Ficha técnica SEO", "Schema VacationRental incompleto (sin AggregateRating, sin Offer, numberOfRooms null), og:url incorrecto, endorsing “by Miramar” no visible junto al H1.", "🔴 Crítico"),
        ("Web bloquea crawlers", "Acceso devuelve HTTP 403 incluso a User-Agent de navegador. Puede afectar a bots SEO y matching engines de OTAs.", "🟠 Revisar"),
        ("Google Business Profile", "NAP correcto y verificado, pero solo 6 reseñas / 4,7★. Knowledge Panel no se dispara para búsqueda branded pura, sí con destino añadido.", "🟠 Mejorable"),
        ("Teléfono GBP", "Compartido con Hotel Miramar (+34 971 866 400). Riesgo de que Google fusione entidades.", "🟠 Mejorable"),
        ("Cambio en plena temporada", "Riesgo SEO/local muy alto: reindexación, desalineación OTA, confusión usuario, pérdida temporal de branded.", "🛑 No hacer"),
    ]
    for bloque, diag, estado in rows:
        row = table.add_row().cells
        row[0].text = bloque
        row[1].text = diag
        row[2].text = estado
        for c in row:
            for p in c.paragraphs:
                p.paragraph_format.space_after = Pt(0)
                for run in p.runs:
                    run.font.size = Pt(8.5)

    # Anchos de columna
    widths = [Cm(4.2), Cm(11.0), Cm(2.5)]
    for row in table.rows:
        for idx, cell in enumerate(row.cells):
            cell.width = widths[idx]

    # ---- 5. FACTORES NO-SEO ----
    add_heading(doc, "5 · Factores ajenos al SEO a considerar en la caída de conversión", size=11)
    add_para(doc, [
        ("La caída de conversión que percibe el cliente puede estar influida por variables que escapan del ámbito SEO y que conviene contrastar con datos antes de imputarlas al rename: ", False, None),
        ("estacionalidad y cambios de mercado en Pollensa, política de precios y ADR vs competencia directa, pérdida de reviews históricas asociadas al perfil antiguo, cambios en motor de reservas o UX de la ficha, visibilidad y ranking en OTAs (Booking score, Genius, Preferred), inversión paid y media mix, y ", False, None),
        ("la falta de una campaña de comunicación de marca acompañando el rename en 2023.", True, None),
        (" Se solicita al cliente compartir datos de GA4, motor de reservas y OTAs (ADR, ocupación, revenue directo, CVR, canales) en ventana abr 2022–abr 2026 para completar el análisis de conversión que el SEO puro no cubre.", False, None),
    ], space_after=4)

    # ---- 6. PLAN DE ACCIÓN ----
    add_heading(doc, "6 · Plan de acción propuesto (sin tocar el naming)", size=11)
    add_bullet(doc, [
        ("Refuerzo de endorsing de marca (no es rename). ", True, None),
        ("Reposicionar la ficha como ", False, None),
        ("“Apartamentos Ca’n Denga — Miramar Mallorca Collection”", True, PRIMARY),
        (" en title, H1, meta description, Open Graph, schema, GBP, OTAs y materiales. Mantiene la diferenciación SEO y recupera el vínculo de cadena.", False, None),
    ])
    add_bullet(doc, [
        ("Optimización técnica de la ficha. ", True, None),
        ("Completar schema VacationRental (AggregateRating, Offer, numberOfRooms, brand), corregir og:url, jerarquía H1/H2, alts de imagen, hreflang, render JS, y resolver el bloqueo 403 a crawlers SEO.", False, None),
    ])
    add_bullet(doc, [
        ("Auditoría NAP y limpieza en bloque. ", True, None),
        ("Revisar Booking, Expedia, Tripadvisor, Trivago, Kayak, HolidayCheck, Apple Maps, Yelp, Foursquare, Bing Places y registros turísticos CAIB. Eliminar listings residuales como “Aptos Miramar 2”, consolidar reviews y unificar denominación.", False, None),
    ])
    add_bullet(doc, [
        ("SEO Local intensivo. ", True, None),
        ("Alta y curación en Wikidata, OpenStreetMap, Mapbox, Geonames, Foursquare, Visit Mallorca, Illesbalears.travel. Diferenciar teléfono respecto al Hotel Miramar.", False, None),
    ])
    add_bullet(doc, [
        ("Estrategia activa de reseñas. ", True, None),
        ("Objetivo +30 reseñas en GBP en 6 meses vía email post-stay automatizado, QR en check-in/llaves, formación de recepción y respuesta sistemática.", False, None),
    ])
    add_bullet(doc, [
        ("Campaña de comunicación de marca (la que faltó en 2023). ", True, None),
        ("Email a base histórica y prospects anunciando la consolidación de marca, social ads geolocalizadas, nota a prensa local, materiales del establecimiento con el endorsing nuevo.", False, None),
    ])
    add_bullet(doc, [
        ("Aplazar cualquier movimiento disruptivo a noviembre 2026 (post-temporada). ", True, None),
        ("Ventana segura para cambios estructurales si tras 6 meses los KPIs siguen por debajo de objetivo.", False, None),
    ])

    # ---- CIERRE ----
    closing = doc.add_paragraph()
    closing.paragraph_format.space_before = Pt(4)
    closing.paragraph_format.space_after = Pt(0)
    r = closing.add_run(
        "Resumen para el cliente: el cambio de 2023 fue correcto y los datos lo respaldan; "
        "lo que faltó fue una campaña coordinada que acompañara la migración en todos los canales. "
        "Esa es la palanca a activar ahora — no revertir."
    )
    r.italic = True
    r.font.size = Pt(9)
    r.font.color.rgb = PRIMARY

    out_path = Path(__file__).resolve().parents[1] / (
        "informe-ejecutivo-apartamentos-can-denga-2026-05-14.docx"
    )
    doc.save(out_path)
    print(f"OK: {out_path}")
    return out_path


if __name__ == "__main__":
    build()
