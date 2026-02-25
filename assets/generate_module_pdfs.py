#!/usr/bin/env python3
"""
Generador de PDFs individuales por módulo
Curso: Estrategia Tecnológica + Mindset Digital
Un PDF por módulo, listo para distribuir a participantes.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT

# ============================================================
# DESIGN SYSTEM
# ============================================================
DARK_NAVY   = HexColor('#0f172a')
CYAN        = HexColor('#0891b2')
PURPLE      = HexColor('#7c3aed')
MAGENTA     = HexColor('#be185d')
AMBER       = HexColor('#d97706')
EMERALD     = HexColor('#059669')
LIGHT_BG    = HexColor('#f8fafc')
CARD_BG     = HexColor('#f1f5f9')
BORDER      = HexColor('#e2e8f0')
TEXT_DARK   = HexColor('#0f172a')
TEXT_BODY   = HexColor('#334155')
TEXT_MUTED  = HexColor('#94a3b8')
WHITE       = white

PAGE_W, PAGE_H = A4
MARGIN = 0.85 * inch

# Accent color per module
MODULE_COLORS = {
    1: CYAN,
    2: PURPLE,
    3: AMBER,
    4: MAGENTA,
    5: EMERALD,
    6: CYAN,
}

MODULE_LABELS = {
    1: "MÓDULO 01",
    2: "MÓDULO 02",
    3: "MÓDULO 03",
    4: "MÓDULO 04",
    5: "MÓDULO 05",
    6: "BONUS",
}

# ============================================================
# STYLES
# ============================================================
def make_styles(accent):
    S = getSampleStyleSheet()

    S.add(ParagraphStyle('M_ModuleTag',
        fontSize=10, leading=14, textColor=accent,
        fontName='Helvetica-Bold', spaceAfter=4, spaceBefore=0))

    S.add(ParagraphStyle('M_CoverTitle',
        fontSize=30, leading=36, textColor=TEXT_DARK,
        fontName='Helvetica-Bold', spaceAfter=8, alignment=TA_LEFT))

    S.add(ParagraphStyle('M_CoverSubtitle',
        fontSize=15, leading=20, textColor=accent,
        fontName='Helvetica', spaceAfter=6, alignment=TA_LEFT))

    S.add(ParagraphStyle('M_CoverMeta',
        fontSize=10, leading=15, textColor=TEXT_MUTED,
        fontName='Helvetica', alignment=TA_LEFT))

    S.add(ParagraphStyle('M_SectionH1',
        fontSize=16, leading=22, textColor=TEXT_DARK,
        fontName='Helvetica-Bold', spaceBefore=22, spaceAfter=8))

    S.add(ParagraphStyle('M_SectionH2',
        fontSize=13, leading=18, textColor=accent,
        fontName='Helvetica-Bold', spaceBefore=16, spaceAfter=6))

    S.add(ParagraphStyle('M_SectionH3',
        fontSize=11, leading=16, textColor=TEXT_DARK,
        fontName='Helvetica-Bold', spaceBefore=12, spaceAfter=4))

    S.add(ParagraphStyle('M_Body',
        fontSize=10.5, leading=16, textColor=TEXT_BODY,
        fontName='Helvetica', spaceAfter=8, alignment=TA_JUSTIFY))

    S.add(ParagraphStyle('M_BodyLeft',
        fontSize=10.5, leading=16, textColor=TEXT_BODY,
        fontName='Helvetica', spaceAfter=6, alignment=TA_LEFT))

    S.add(ParagraphStyle('M_Quote',
        fontSize=12, leading=19, textColor=accent,
        fontName='Helvetica-Oblique', spaceBefore=12, spaceAfter=12,
        leftIndent=24, rightIndent=24, alignment=TA_LEFT))

    S.add(ParagraphStyle('M_Bullet',
        fontSize=10.5, leading=15, textColor=TEXT_BODY,
        fontName='Helvetica', spaceAfter=5, leftIndent=18,
        firstLineIndent=-14))

    S.add(ParagraphStyle('M_TH',
        fontSize=9.5, leading=13, textColor=WHITE,
        fontName='Helvetica-Bold', alignment=TA_LEFT))

    S.add(ParagraphStyle('M_TD',
        fontSize=9, leading=13, textColor=TEXT_BODY,
        fontName='Helvetica', alignment=TA_LEFT))

    S.add(ParagraphStyle('M_TDCenter',
        fontSize=9, leading=13, textColor=TEXT_BODY,
        fontName='Helvetica', alignment=TA_CENTER))

    S.add(ParagraphStyle('M_TDBold',
        fontSize=9, leading=13, textColor=TEXT_BODY,
        fontName='Helvetica-Bold', alignment=TA_LEFT))

    S.add(ParagraphStyle('M_Outcome',
        fontSize=10, leading=15, textColor=TEXT_BODY,
        fontName='Helvetica', spaceAfter=4, leftIndent=16, firstLineIndent=-12))

    S.add(ParagraphStyle('M_Footer',
        fontSize=8, leading=11, textColor=TEXT_MUTED,
        fontName='Helvetica', alignment=TA_CENTER))

    return S


# ============================================================
# HELPERS
# ============================================================
def hr(accent, thickness=0.8, space_before=6, space_after=6):
    return HRFlowable(width='100%', thickness=thickness,
                      color=accent, spaceAfter=space_after, spaceBefore=space_before)


def bullet(text, S):
    return Paragraph(f'<font color="#0891b2">▸</font>  {text}', S['M_Bullet'])


def make_table(data, col_widths, S, accent, zebra=True):
    table = Table(data, colWidths=col_widths, repeatRows=1)
    styles = [
        ('BACKGROUND', (0, 0), (-1, 0), accent),
        ('TEXTCOLOR',  (0, 0), (-1, 0), WHITE),
        ('FONTNAME',   (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE',   (0, 0), (-1, 0), 9.5),
        ('ALIGN',      (0, 0), (-1, 0), 'LEFT'),
        ('LEFTPADDING',  (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING',   (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING',(0, 0), (-1, -1), 6),
        ('VALIGN',       (0, 0), (-1, -1), 'TOP'),
        ('GRID',         (0, 0), (-1, -1), 0.4, BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1),
         [LIGHT_BG, CARD_BG] if zebra else [LIGHT_BG]),
    ]
    table.setStyle(TableStyle(styles))
    return table


def page_header_footer(canvas_obj, doc, module_num, module_title, accent):
    canvas_obj.saveState()
    w, h = A4

    # Header bar
    canvas_obj.setFillColor(accent)
    canvas_obj.rect(MARGIN, h - 0.55*inch, w - 2*MARGIN, 2.5, fill=1, stroke=0)

    # Header text
    canvas_obj.setFont('Helvetica-Bold', 8)
    canvas_obj.setFillColor(accent)
    canvas_obj.drawString(MARGIN, h - 0.45*inch,
                          f"{MODULE_LABELS[module_num]}  ·  {module_title}")

    # Footer
    page_num = canvas_obj.getPageNumber()
    canvas_obj.setFont('Helvetica', 8)
    canvas_obj.setFillColor(TEXT_MUTED)
    canvas_obj.drawCentredString(w / 2, 0.45*inch,
                                 f"Estrategia Tecnológica + Mindset Digital  ·  Página {page_num}")

    # Footer line
    canvas_obj.setStrokeColor(BORDER)
    canvas_obj.setLineWidth(0.4)
    canvas_obj.line(MARGIN, 0.6*inch, w - MARGIN, 0.6*inch)

    canvas_obj.restoreState()


# ============================================================
# COVER PAGE (first page — no header/footer)
# ============================================================
def build_cover(canvas_obj, doc, module_num, title, subtitle, objective, guiding_q, accent):
    canvas_obj.saveState()
    w, h = A4

    # Full-page left color band
    canvas_obj.setFillColor(accent)
    canvas_obj.rect(0, 0, 0.35*inch, h, fill=1, stroke=0)

    # Top accent strip
    canvas_obj.setFillColor(accent)
    canvas_obj.rect(0, h - 0.12*inch, w, 0.12*inch, fill=1, stroke=0)

    # Module tag
    canvas_obj.setFont('Helvetica-Bold', 9)
    canvas_obj.setFillColor(accent)
    tag = MODULE_LABELS[module_num]
    canvas_obj.drawString(MARGIN, h - 1.1*inch, tag.upper())

    # Module number large watermark
    canvas_obj.setFont('Helvetica-Bold', 120)
    canvas_obj.setFillColor(HexColor('#f1f5f9'))
    num_str = str(module_num).zfill(2)
    canvas_obj.drawRightString(w - MARGIN + 0.2*inch, h - 3.8*inch, num_str)

    # Title
    canvas_obj.setFont('Helvetica-Bold', 28)
    canvas_obj.setFillColor(TEXT_DARK)
    # Word-wrap title manually (simple approach)
    title_lines = _wrap_text(title, 28, w - 2*MARGIN - 0.2*inch)
    y = h - 1.6*inch
    for line in title_lines:
        canvas_obj.drawString(MARGIN, y, line)
        y -= 34

    # Subtitle
    canvas_obj.setFont('Helvetica', 15)
    canvas_obj.setFillColor(accent)
    canvas_obj.drawString(MARGIN, y - 4, subtitle)
    y -= 26

    # Divider
    canvas_obj.setStrokeColor(accent)
    canvas_obj.setLineWidth(1.5)
    canvas_obj.line(MARGIN, y - 14, w - MARGIN, y - 14)
    y -= 40

    # Guiding question
    canvas_obj.setFont('Helvetica-Oblique', 11)
    canvas_obj.setFillColor(TEXT_BODY)
    q_lines = _wrap_text(f'"{guiding_q}"', 11, w - 2*MARGIN)
    for line in q_lines:
        canvas_obj.drawString(MARGIN, y, line)
        y -= 17

    # Objective box
    y -= 20
    box_h = _estimate_text_height(objective, 10, w - 2*MARGIN - 40) + 30
    canvas_obj.setFillColor(CARD_BG)
    canvas_obj.roundRect(MARGIN, y - box_h, w - 2*MARGIN, box_h, 6, fill=1, stroke=0)
    canvas_obj.setFillColor(accent)
    canvas_obj.setFont('Helvetica-Bold', 8.5)
    canvas_obj.drawString(MARGIN + 14, y - 16, 'OBJETIVO DEL MÓDULO')
    canvas_obj.setFillColor(TEXT_BODY)
    canvas_obj.setFont('Helvetica', 10)
    obj_lines = _wrap_text(objective, 10, w - 2*MARGIN - 30)
    oy = y - 32
    for line in obj_lines:
        canvas_obj.drawString(MARGIN + 14, oy, line)
        oy -= 14

    # Bottom bar
    canvas_obj.setFillColor(DARK_NAVY)
    canvas_obj.rect(0, 0, w, 0.85*inch, fill=1, stroke=0)
    canvas_obj.setFont('Helvetica', 8.5)
    canvas_obj.setFillColor(TEXT_MUTED)
    canvas_obj.drawString(MARGIN, 0.32*inch,
                          'Programa Ejecutivo · Educación Superior mediada por Tecnología · LATAM · 2026')

    canvas_obj.restoreState()


def _wrap_text(text, font_size, max_width):
    """Very simple word-wrap for canvas drawString."""
    words = text.split()
    lines = []
    current = ''
    char_w = font_size * 0.52  # rough estimate
    max_chars = int(max_width / char_w)
    for word in words:
        if len(current) + len(word) + 1 <= max_chars:
            current = (current + ' ' + word).strip()
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def _estimate_text_height(text, font_size, max_width):
    lines = _wrap_text(text, font_size, max_width)
    return len(lines) * (font_size + 4) + 6


# ============================================================
# DOCUMENT BUILDER
# ============================================================
def build_pdf(output_path, module_num, title, subtitle, guiding_q, objective, build_content_fn):
    accent = MODULE_COLORS[module_num]
    S = make_styles(accent)

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=MARGIN,
        leftMargin=MARGIN,
        topMargin=0.85*inch,
        bottomMargin=0.85*inch,
    )

    story = []

    # ---- Cover (built via canvas, page break opens content) ----
    # We use a dummy first page with onFirstPage callback
    story.append(Spacer(1, 0.1))  # placeholder so cover canvas fires
    story.append(PageBreak())

    # ---- Content pages ----
    build_content_fn(story, S, accent)

    def on_first_page(c, d):
        build_cover(c, d, module_num, title, subtitle, objective, guiding_q, accent)

    def on_later_pages(c, d):
        page_header_footer(c, d, module_num, title, accent)

    doc.build(story, onFirstPage=on_first_page, onLaterPages=on_later_pages)
    print(f"  ✓  {os.path.basename(output_path)}")


# ============================================================
# MODULE 1 CONTENT
# ============================================================
def content_m1(story, S, accent):
    # --- Three levels ---
    story.append(Paragraph("Los Tres Niveles de Relación con la Tecnología", S['M_SectionH1']))
    story.append(hr(accent))
    story.append(Paragraph(
        "No todas las organizaciones se relacionan con la tecnología de la misma manera. La diferencia entre niveles define la capacidad competitiva — y el techo de crecimiento.",
        S['M_Body']))

    data = [
        [Paragraph('<b>Nivel</b>', S['M_TH']),
         Paragraph('<b>Descripción</b>', S['M_TH']),
         Paragraph('<b>Ejemplo educativo</b>', S['M_TH']),
         Paragraph('<b>Diferenciación</b>', S['M_TH'])],
        [Paragraph('<b>1 · Usar</b>', S['M_TDBold']),
         Paragraph('Comprar herramientas y usarlas tal como vienen. Alta dependencia del proveedor.', S['M_TD']),
         Paragraph('Adoptar Zoom para dar clases virtuales.', S['M_TD']),
         Paragraph('Nula', S['M_TDCenter'])],
        [Paragraph('<b>2 · Operar</b>', S['M_TDBold']),
         Paragraph('Integrar herramientas, personalizar flujos, conectar datos. Genera eficiencia e inteligencia operativa.', S['M_TD']),
         Paragraph('LMS + CRM para detectar riesgo de deserción.', S['M_TD']),
         Paragraph('Parcial', S['M_TDCenter'])],
        [Paragraph('<b>3 · Diseñar</b>', S['M_TDBold']),
         Paragraph('El modelo de negocio NACE de las capacidades tecnológicas. Diferenciación real y escalabilidad estructural.', S['M_TD']),
         Paragraph('Platzi: modelo de suscripción y plataforma como sistema integrado desde el día uno.', S['M_TD']),
         Paragraph('Alta', S['M_TDCenter'])],
    ]
    story.append(make_table(data, [1.05*inch, 2.15*inch, 1.85*inch, 0.9*inch], S, accent))
    story.append(Spacer(1, 10))

    story.append(Paragraph(
        '«  El nivel en el que estás define el techo de tu crecimiento.  »', S['M_Quote']))

    # --- Impacto económico ---
    story.append(Paragraph("Impacto Económico por Nivel", S['M_SectionH1']))
    story.append(hr(accent))

    data2 = [
        [Paragraph('<b>Dimensión</b>', S['M_TH']),
         Paragraph('<b>Nivel 1 — Usar</b>', S['M_TH']),
         Paragraph('<b>Nivel 2 — Operar</b>', S['M_TH']),
         Paragraph('<b>Nivel 3 — Diseñar</b>', S['M_TH'])],
        [Paragraph('Margen', S['M_TDBold']),
         Paragraph('Crece lineal con estructura', S['M_TD']),
         Paragraph('Mejora por eficiencia', S['M_TD']),
         Paragraph('Escalable, costo marginal decreciente', S['M_TD'])],
        [Paragraph('CAC', S['M_TDBold']),
         Paragraph('Alto, poco optimizado', S['M_TD']),
         Paragraph('Optimizable con datos', S['M_TD']),
         Paragraph('Optimizado por analítica', S['M_TD'])],
        [Paragraph('Retención / LTV', S['M_TDBold']),
         Paragraph('Dependiente del docente', S['M_TD']),
         Paragraph('Mejorada por datos', S['M_TD']),
         Paragraph('Diseñada como sistema', S['M_TD'])],
        [Paragraph('Velocidad de lanzamiento', S['M_TDBold']),
         Paragraph('Lenta', S['M_TD']),
         Paragraph('Media', S['M_TD']),
         Paragraph('Alta', S['M_TD'])],
    ]
    story.append(make_table(data2, [1.3*inch, 1.57*inch, 1.57*inch, 1.57*inch], S, accent))

    # --- Software eating the world ---
    story.append(Paragraph("Software Is Eating The World", S['M_SectionH1']))
    story.append(hr(accent))
    story.append(Paragraph(
        "Marc Andreessen (2011): las empresas más valiosas del mundo no <i>usan</i> tecnología — <b>son</b> empresas de tecnología que operan en una industria específica. En educación, esto cambia todo.",
        S['M_Body']))

    data3 = [
        [Paragraph('<b>Lo que creías</b>', S['M_TH']),
         Paragraph('<b>Lo que está pasando</b>', S['M_TH'])],
        [Paragraph('"Tenemos Moodle, estamos digitalizados"', S['M_TD']),
         Paragraph('Duolingo tiene 47M de usuarios diarios con IA adaptativa.', S['M_TD'])],
        [Paragraph('"Competimos con universidades vecinas"', S['M_TD']),
         Paragraph('Tu estudiante elige entre vos, Coursera, Platzi y un bootcamp en Berlín.', S['M_TD'])],
        [Paragraph('"IT es un área de soporte"', S['M_TD']),
         Paragraph('2U compró contenido de Harvard y MIT por USD 800M. Sin tech sostenible, está al borde de la quiebra.', S['M_TD'])],
        [Paragraph('"Invertir en tech es un gasto"', S['M_TD']),
         Paragraph('No invertir es una decisión de cierre en cámara lenta.', S['M_TD'])],
    ]
    story.append(make_table(data3, [2.5*inch, 3.5*inch], S, accent))

    # --- El mapa EdTech ---
    story.append(Paragraph("El Ecosistema EdTech Global", S['M_SectionH1']))
    story.append(hr(accent))
    story.append(Paragraph(
        "El ecosistema EdTech supera los <b>USD 400 mil millones</b> y se proyecta hacia el trillón en 2030. "
        "Conocer el mapa permite entender dónde competís realmente, dónde hay oportunidades y dónde están las amenazas invisibles.",
        S['M_Body']))

    cats = [
        ("Plataformas de aprendizaje", "LMS, MOOCs, plataformas adaptativas"),
        ("Sistemas de gestión institucional", "SIS, ERP educativo"),
        ("Herramientas de engagement", "CRM, comunicaciones, comunidades"),
        ("Inteligencia artificial aplicada", "Tutores, asistentes, analítica predictiva"),
        ("Credenciales y certificación", "Badges, micro-credenciales, blockchain"),
    ]
    for cat, desc in cats:
        story.append(bullet(f'<b>{cat}</b> — {desc}', S))

    # --- Tres fuerzas ---
    story.append(Paragraph("Las Tres Fuerzas que Reconfiguran la Educación Superior", S['M_SectionH1']))
    story.append(hr(accent))

    forces = [
        ("1. Presión financiera y sostenibilidad",
         "Más de 20 universidades cerraron en EE.UU. en 2024. La Reserva Federal proyecta hasta 80 cierres por año. "
         "2U pagó USD 800M por edX y hoy enfrenta USD 900M en deuda. Tener el mejor contenido no alcanza sin modelo sostenible."),
        ("2. Cambio en la demanda laboral",
         "Google, Apple, IBM y 150+ empresas eliminaron el requisito de título universitario. "
         "El 81% de los empleadores ya contrata por skills, no por diplomas."),
        ("3. Competencia nativa digital",
         "Duolingo tiene 47 millones de usuarios diarios y proyecta USD 1B en revenue para 2025. "
         "Un estudiante en Buenos Aires compite entre universidades locales y plataformas globales."),
    ]
    for title_f, desc_f in forces:
        story.append(Paragraph(title_f, S['M_SectionH2']))
        story.append(Paragraph(desc_f, S['M_Body']))

    # --- Decisiones directivas ---
    story.append(Paragraph("El Rol del Equipo Directivo en Decisiones Tecnológicas", S['M_SectionH1']))
    story.append(hr(accent))
    story.append(Paragraph(
        "Hay decisiones tecnológicas que no son operativas. Son estratégicas. Un directivo no necesita saber programar, pero sí necesita <b>criterio tecnológico</b>.",
        S['M_Body']))

    data4 = [
        [Paragraph('<b>Decisión</b>', S['M_TH']),
         Paragraph('<b>Por qué es del equipo directivo</b>', S['M_TH'])],
        [Paragraph('¿Construimos o compramos nuestra plataforma core?', S['M_TD']),
         Paragraph('Define dependencia estructural y costos a largo plazo.', S['M_TD'])],
        [Paragraph('¿Qué datos son estratégicos y quién los gobierna?', S['M_TD']),
         Paragraph('Define capacidad de decisión basada en evidencia.', S['M_TD'])],
        [Paragraph('¿Cuánto invertimos en tecnología vs. otras áreas?', S['M_TD']),
         Paragraph('Define prioridades y visión de futuro.', S['M_TD'])],
        [Paragraph('¿Cómo integramos IA en nuestra operación?', S['M_TD']),
         Paragraph('Define posición competitiva a 3-5 años.', S['M_TD'])],
    ]
    story.append(make_table(data4, [2.9*inch, 3.1*inch], S, accent))

    # --- Resultado esperado ---
    story.append(Paragraph("Al terminar este módulo, cada participante:", S['M_SectionH1']))
    story.append(hr(accent))
    outcomes = [
        "Entiende que la tecnología es arquitectura competitiva, no soporte.",
        "Puede identificar su nivel de madurez tecnológica.",
        "Comprende el impacto económico de cada nivel.",
        "Reconoce qué decisiones tecnológicas no puede delegar.",
        "Entiende que la competencia ya es global y tecnológica.",
    ]
    for o in outcomes:
        story.append(bullet(o, S))

    story.append(Spacer(1, 20))
    story.append(Paragraph(
        '«  Si la tecnología define el techo de crecimiento de tu institución, ¿estás diseñando ese techo?  »',
        S['M_Quote']))


# ============================================================
# MODULE 2 CONTENT
# ============================================================
def content_m2(story, S, accent):
    story.append(Paragraph("El Costo de las Decisiones Tecnológicas Equivocadas", S['M_SectionH1']))
    story.append(hr(accent))
    story.append(Paragraph(
        "La deuda técnica consume el <b>40% del presupuesto de IT</b> en la empresa promedio (McKinsey, 2024). "
        "Cada peso que va a mantener sistemas viejos es un peso que no va a innovación.",
        S['M_Body']))

    cases = [
        ("2U / edX", "Invirtió USD 800M en adquirir edX (Harvard + MIT). Hoy tiene USD 900M en deuda. "
                     "La decisión Build vs Buy más cara de la historia de EdTech. El problema no fue la tecnología. Fue la estrategia."),
        ("Universidad Siglo 21", "Tomó la decisión opuesta: construyó su propio SIS (Proyecto Algarrobo). "
                                  "Resultado: de 30.000 a 60.000+ estudiantes con NPS de +31. Control total del dato, flexibilidad para crecer."),
    ]
    for name, desc in cases:
        story.append(Paragraph(name, S['M_SectionH2']))
        story.append(Paragraph(desc, S['M_Body']))

    # Build vs Buy
    story.append(Paragraph("Decisión 1 — Build vs. Buy", S['M_SectionH1']))
    story.append(hr(accent))
    story.append(Paragraph(
        '<b>La regla de oro:</b> Comprá lo que es commodity. Construí lo que es tu ventaja competitiva.',
        S['M_Body']))

    data = [
        [Paragraph('', S['M_TH']),
         Paragraph('<b>Build (Construir)</b>', S['M_TH']),
         Paragraph('<b>Buy (Comprar)</b>', S['M_TH'])],
        [Paragraph('<b>Ventaja</b>', S['M_TDBold']),
         Paragraph('Control total, diferenciación, propiedad de los datos', S['M_TD']),
         Paragraph('Velocidad de implementación, menor riesgo inicial', S['M_TD'])],
        [Paragraph('<b>Riesgo</b>', S['M_TDBold']),
         Paragraph('Costos altos, requiere equipo técnico, tiempo', S['M_TD']),
         Paragraph('Dependencia del proveedor, limitaciones de personalización', S['M_TD'])],
        [Paragraph('<b>Cuándo conviene</b>', S['M_TDBold']),
         Paragraph('Cuando el proceso es parte de tu ventaja competitiva', S['M_TD']),
         Paragraph('Cuando el proceso es estándar en la industria', S['M_TD'])],
        [Paragraph('<b>Impacto financiero</b>', S['M_TDBold']),
         Paragraph('CAPEX + equipo permanente', S['M_TD']),
         Paragraph('OPEX predecible (gasto mensual)', S['M_TD'])],
    ]
    story.append(make_table(data, [1.1*inch, 2.4*inch, 2.5*inch], S, accent))

    # Cloud vs On-premise
    story.append(Paragraph("Decisión 2 — Cloud vs. On-premise", S['M_SectionH1']))
    story.append(hr(accent))

    data2 = [
        [Paragraph('', S['M_TH']),
         Paragraph('<b>Cloud</b>', S['M_TH']),
         Paragraph('<b>On-premise</b>', S['M_TH'])],
        [Paragraph('<b>Analogía</b>', S['M_TDBold']),
         Paragraph('Alquilar un departamento: flexible, mantenimiento incluido', S['M_TD']),
         Paragraph('Comprar una casa: control total, vos te ocupás de todo', S['M_TD'])],
        [Paragraph('<b>Ventaja</b>', S['M_TDBold']),
         Paragraph('Escalabilidad, sin inversión inicial grande, actualizaciones automáticas', S['M_TD']),
         Paragraph('Control total, costos predecibles a largo plazo', S['M_TD'])],
        [Paragraph('<b>Riesgo</b>', S['M_TDBold']),
         Paragraph('Costos que pueden crecer, dependencia del proveedor', S['M_TD']),
         Paragraph('Obsolescencia, necesidad de equipo de infraestructura', S['M_TD'])],
        [Paragraph('<b>Impacto financiero</b>', S['M_TDBold']),
         Paragraph('Convierte CAPEX en OPEX. Sin inversión inicial grande.', S['M_TD']),
         Paragraph('CAPEX alto. Planificación presupuestaria predecible.', S['M_TD'])],
    ]
    story.append(make_table(data2, [1.1*inch, 2.4*inch, 2.5*inch], S, accent))

    # Core vs Commodity
    story.append(Paragraph("Decisión 3 — Core vs. Commodity", S['M_SectionH1']))
    story.append(hr(accent))
    story.append(Paragraph(
        "No todos los sistemas tienen el mismo valor estratégico. La trampa común: invertir tiempo en personalizar commodities e ignorar lo que es core.",
        S['M_Body']))

    data3 = [
        [Paragraph('<b>Tipo</b>', S['M_TH']),
         Paragraph('<b>Qué es</b>', S['M_TH']),
         Paragraph('<b>Ejemplo educativo</b>', S['M_TH'])],
        [Paragraph('<b>Core</b>', S['M_TDBold']),
         Paragraph('Define tu ventaja competitiva. Si lo perdés, perdés diferenciación.', S['M_TD']),
         Paragraph('Plataforma de aprendizaje personalizado, motor de analítica de retención.', S['M_TD'])],
        [Paragraph('<b>Commodity</b>', S['M_TDBold']),
         Paragraph('Necesitás pero no te diferencia. Cualquier proveedor lo resuelve.', S['M_TD']),
         Paragraph('Email corporativo, herramienta de videoconferencia, sistema contable.', S['M_TD'])],
    ]
    story.append(make_table(data3, [1.1*inch, 2.3*inch, 2.6*inch], S, accent))

    # 6 dimensiones
    story.append(Paragraph("Las 6 Dimensiones de una Estrategia Tecnológica", S['M_SectionH1']))
    story.append(hr(accent))

    dims = [
        ("Infraestructura", "¿Dónde viven tus sistemas? ¿Cloud, on-premise o híbrido? ¿Puede escalar en picos?"),
        ("Arquitectura", "¿Cómo están organizados tus sistemas? ¿Se hablan entre sí o son islas?"),
        ("Datos", "¿Qué datos tenemos? ¿Son confiables? ¿Quién los gobierna? ¿Tomamos decisiones basadas en datos?"),
        ("Seguridad", "¿Tenemos políticas definidas? ¿Preparados para un incidente (ransomware, fuga de datos)?"),
        ("Talento", "¿Equipo de IT que 'apaga incendios' o que construye estratégicamente?"),
        ("Innovación", "¿Cómo incorporamos nuevas tecnologías? ¿Hay proceso o es ad hoc?"),
    ]
    for dim, q in dims:
        story.append(bullet(f'<b>{dim}:</b> {q}', S))

    # Framework de alineación
    story.append(Paragraph("Framework de Alineación Negocio–Tecnología", S['M_SectionH1']))
    story.append(hr(accent))

    fw_data = [
        [Paragraph('<b>Paso</b>', S['M_TH']),
         Paragraph('<b>Pregunta</b>', S['M_TH']),
         Paragraph('<b>Ejemplo</b>', S['M_TH'])],
        [Paragraph('1. Objetivos de negocio', S['M_TDBold']),
         Paragraph('¿Qué queremos lograr en 3 años?', S['M_TD']),
         Paragraph('Reducir deserción del 42% al 25%', S['M_TD'])],
        [Paragraph('2. Capacidades necesarias', S['M_TDBold']),
         Paragraph('¿Qué debemos ser capaces de hacer?', S['M_TD']),
         Paragraph('Detectar estudiantes en riesgo a tiempo', S['M_TD'])],
        [Paragraph('3. Habilitadores tecnológicos', S['M_TDBold']),
         Paragraph('¿Qué tecnología lo hace posible?', S['M_TD']),
         Paragraph('Analítica predictiva + LMS + SIS integrados', S['M_TD'])],
        [Paragraph('4. Inversión y priorización', S['M_TDBold']),
         Paragraph('¿Qué construimos primero y cuánto cuesta?', S['M_TD']),
         Paragraph('Integración de datos + modelo de alertas + equipo', S['M_TD'])],
    ]
    story.append(make_table(fw_data, [1.4*inch, 2.0*inch, 2.6*inch], S, accent))

    # Resultado
    story.append(Paragraph("Al terminar este módulo, cada participante:", S['M_SectionH1']))
    story.append(hr(accent))
    outcomes = [
        "Maneja el vocabulario de decisiones tecnológicas estratégicas (Build vs. Buy, Cloud vs. On-premise, Core vs. Commodity).",
        "Puede distinguir entre decisiones tácticas y estructurales.",
        "Entiende las 6 dimensiones de una estrategia tecnológica.",
        "Comprende el impacto financiero (CAPEX vs. OPEX, deuda técnica).",
        "Puede participar activamente en conversaciones sobre estrategia tecnológica.",
    ]
    for o in outcomes:
        story.append(bullet(o, S))

    story.append(Spacer(1, 20))
    story.append(Paragraph(
        '«  Cada decisión tecnológica define la estructura de costos, la velocidad y la dependencia de tu organización por los próximos 3-5 años. ¿Estás eligiendo... o estás heredando?  »',
        S['M_Quote']))


# ============================================================
# MODULE 3 CONTENT
# ============================================================
def content_m3(story, S, accent):
    # Analogía de la ciudad
    story.append(Paragraph("¿Qué es una Arquitectura IT?", S['M_SectionH1']))
    story.append(hr(accent))
    story.append(Paragraph(
        "Una arquitectura IT es el <b>mapa</b> de todos los sistemas tecnológicos de una organización: qué sistemas existen, qué hace cada uno, cómo se conectan y cómo fluye la información.",
        S['M_Body']))
    story.append(Paragraph(
        "<b>Analogía:</b> pensá en tu organización como una ciudad. "
        "Los sistemas son los edificios (cada uno cumple una función). "
        "Las integraciones son las calles (conectan los edificios). "
        "Los datos son las personas que circulan. "
        "La arquitectura IT es el plano completo.",
        S['M_Body']))
    story.append(Paragraph(
        "Un directivo no necesita saber construir edificios. Pero sí necesita poder leer el plano para decidir dónde construir el próximo, cuál demoler y cuál renovar.",
        S['M_Body']))

    # Sistemas clave
    story.append(Paragraph("Los Sistemas Clave de una Institución Educativa", S['M_SectionH1']))
    story.append(hr(accent))

    systems = [
        ('CMS', 'Content Management System', 'Presenta la institución en la web, publica oferta académica, puede incluir e-commerce.', 'El "sitio" de la institución'),
        ('SIS', 'Student Information System', 'Gestiona toda la vida académica: inscripción, cursada, notas, título. Sistema CORE.', 'El "DNI" del estudiante'),
        ('LMS', 'Learning Management System', 'Plataforma de aprendizaje: contenidos, actividades, foros, evaluación formativa.', 'El "aula" virtual'),
        ('EXAM', 'Exam & Proctoring', 'Plataforma de examinación segura, con auditorías de fraude y supervisión online.', 'La validación del aprendizaje'),
        ('CRM', 'Customer Relationship Mgmt', 'Relación con prospectos y estudiantes: campañas, seguimiento, comunicación.', 'La "memoria" de interacciones'),
        ('ERP', 'Enterprise Resource Planning', 'Administración y finanzas: facturación, pagos, contabilidad, RRHH.', 'La "administración" del negocio'),
        ('BI', 'Business Intelligence', 'Analítica y reportes: dashboards, indicadores, tendencias.', 'Los "ojos" de la organización'),
        ('IA', 'Inteligencia Artificial', 'Capa transversal: chatbots, analítica predictiva, personalización, automatización.', 'El "asistente inteligente"'),
    ]

    data = [[Paragraph('<b>Sistema</b>', S['M_TH']),
             Paragraph('<b>Nombre completo</b>', S['M_TH']),
             Paragraph('<b>Qué hace</b>', S['M_TH']),
             Paragraph('<b>Analogía</b>', S['M_TH'])]]
    for sig, name, desc, analogy in systems:
        data.append([Paragraph(f'<b>{sig}</b>', S['M_TDBold']),
                     Paragraph(name, S['M_TD']),
                     Paragraph(desc, S['M_TD']),
                     Paragraph(analogy, S['M_TD'])])

    story.append(make_table(data, [0.6*inch, 1.25*inch, 2.4*inch, 1.75*inch], S, accent))

    # Ciclo de vida
    story.append(Paragraph("El Ciclo de Vida del Estudiante Visto desde los Sistemas", S['M_SectionH1']))
    story.append(hr(accent))
    story.append(Paragraph(
        "La experiencia del estudiante es un viaje que atraviesa múltiples sistemas. Cada etapa depende de que los sistemas correctos funcionen y estén conectados.",
        S['M_Body']))

    lifecycle = [
        ('Captación', 'CRM / Marketing', 'El prospecto llega por publicidad, referidos o búsqueda orgánica. El CRM registra el primer contacto.'),
        ('Evaluación', 'CMS / Web', 'El prospecto navega la oferta académica, compara, solicita información.'),
        ('Admisión', 'SIS', 'El prospecto se convierte en estudiante. El SIS registra su perfil académico.'),
        ('Onboarding', 'SIS + LMS', 'El estudiante activa su cuenta, accede a la plataforma y al aula virtual.'),
        ('Cursada', 'LMS', 'El estudiante consume contenidos, participa en actividades, interactúa con docentes.'),
        ('Examinación', 'EXAM', 'El estudiante rinde evaluaciones. El sistema garantiza integridad y registra resultados.'),
        ('Graduación', 'SIS', 'El SIS emite el título, valida créditos y cierra el expediente académico.'),
        ('Alumni', 'CRM', 'El graduado pasa al CRM como contacto estratégico para comunidad y futuros servicios.'),
    ]

    data2 = [[Paragraph('<b>Etapa</b>', S['M_TH']),
              Paragraph('<b>Sistema principal</b>', S['M_TH']),
              Paragraph('<b>Qué sucede</b>', S['M_TH'])]]
    for stage, system, desc in lifecycle:
        data2.append([Paragraph(stage, S['M_TDBold']),
                      Paragraph(system, S['M_TD']),
                      Paragraph(desc, S['M_TD'])])
    story.append(make_table(data2, [1.05*inch, 1.2*inch, 3.75*inch], S, accent))

    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "<b>Los problemas reales surgen en las transiciones:</b> el prospecto que se inscribe en el CRM pero sus datos no llegan al SIS → recarga todo manualmente. El estudiante que aprueba en el LMS pero la nota no se refleja en el SIS → necesita un trámite. Cada quiebre es una mala experiencia y un costo operativo.",
        S['M_Body']))

    # Integraciones
    story.append(Paragraph("Niveles de Integración entre Sistemas", S['M_SectionH1']))
    story.append(hr(accent))
    story.append(Paragraph(
        "Lo que define la madurez de una arquitectura no son los sistemas individuales, sino <b>cómo se conectan entre sí</b>. Cada integración manual es un riesgo y un costo.",
        S['M_Body']))

    data3 = [
        [Paragraph('<b>Nivel</b>', S['M_TH']),
         Paragraph('<b>Cómo funciona</b>', S['M_TH']),
         Paragraph('<b>Velocidad</b>', S['M_TH']),
         Paragraph('<b>Ejemplo</b>', S['M_TH'])],
        [Paragraph('Manual', S['M_TDBold']),
         Paragraph('Alguien exporta un Excel y lo importa en otro sistema', S['M_TD']),
         Paragraph('Días', S['M_TDCenter']),
         Paragraph('Pasar notas del LMS al SIS a mano', S['M_TD'])],
        [Paragraph('Archivos', S['M_TDBold']),
         Paragraph('Un sistema genera un archivo que otro consume automáticamente', S['M_TD']),
         Paragraph('Horas', S['M_TDCenter']),
         Paragraph('CSV de inscriptos que se importa cada noche', S['M_TD'])],
        [Paragraph('APIs', S['M_TDBold']),
         Paragraph('Los sistemas se hablan en tiempo real vía interfaces programáticas', S['M_TD']),
         Paragraph('Segundos', S['M_TDCenter']),
         Paragraph('Inscripción en SIS crea automáticamente cuenta en LMS', S['M_TD'])],
        [Paragraph('Eventos', S['M_TDBold']),
         Paragraph('Los sistemas reaccionan a lo que pasa en otros sin intervención humana', S['M_TD']),
         Paragraph('Tiempo real', S['M_TDCenter']),
         Paragraph('Sin ingreso al LMS por 7 días → alerta automática en CRM', S['M_TD'])],
    ]
    story.append(make_table(data3, [0.75*inch, 2.1*inch, 0.85*inch, 2.3*inch], S, accent))

    # Arquitectura como herramienta de decisión
    story.append(Paragraph("La Arquitectura como Herramienta de Decisión Ejecutiva", S['M_SectionH1']))
    story.append(hr(accent))

    decisiones = [
        ("Escalabilidad", "¿Puede mi infraestructura soportar el doble de estudiantes? ¿O necesito cambiar sistemas antes de crecer?"),
        ("Gobierno de datos", "¿Quién es el 'dueño' de cada dato? ¿Hay una visión unificada o cada área compra lo que necesita?"),
        ("Costos ocultos", "¿Cuánto cuesta mantener sistemas que no se integran? ¿Cuántas horas-persona se pierden en procesos manuales?"),
        ("Gestión del riesgo", "¿Qué pasa si cae el sistema central? ¿Hay plan B? ¿Los datos están respaldados?"),
    ]
    for dim, q in decisiones:
        story.append(bullet(f'<b>{dim}:</b> {q}', S))

    # Resultado
    story.append(Paragraph("Al terminar este módulo, cada participante:", S['M_SectionH1']))
    story.append(hr(accent))
    outcomes = [
        "Puede nombrar y describir los sistemas principales de una institución educativa.",
        "Entiende el ciclo de vida del estudiante como un flujo que depende de la integración entre sistemas.",
        "Puede leer un mapa de arquitectura IT y hacer preguntas relevantes.",
        "Comprende que la arquitectura no es un tema de IT — es un tema de gobierno y competitividad.",
    ]
    for o in outcomes:
        story.append(bullet(o, S))


# ============================================================
# MODULE 4 CONTENT
# ============================================================
def content_m4(story, S, accent):
    # Triángulo
    story.append(Paragraph("El Triángulo de la Transformación Digital", S['M_SectionH1']))
    story.append(hr(accent))
    story.append(Paragraph(
        "McKinsey define la transformación digital como un <b>cambio fundamental en cómo una organización crea y entrega valor</b>, habilitado por tecnología pero no determinado por ella. "
        "Las organizaciones que la tratan como un proyecto de IT fracasan. Las que la tratan como un cambio de modelo de negocio tienen 2,5 veces más probabilidad de éxito.",
        S['M_Body']))

    data = [
        [Paragraph('<b>Dimensión</b>', S['M_TH']),
         Paragraph('<b>Qué implica</b>', S['M_TH']),
         Paragraph('<b>Sin ella...</b>', S['M_TH'])],
        [Paragraph('<b>Cultura</b>', S['M_TDBold']),
         Paragraph('Liderazgo visible, apertura al cambio, mentalidad de aprendizaje', S['M_TD']),
         Paragraph('La tecnología se compra pero nadie la usa', S['M_TD'])],
        [Paragraph('<b>Procesos</b>', S['M_TDBold']),
         Paragraph('Rediseño real de cómo se hacen las cosas, no digitalización de lo ineficiente', S['M_TD']),
         Paragraph('Se automatizan procesos que no deberían existir', S['M_TD'])],
        [Paragraph('<b>Tecnología</b>', S['M_TDBold']),
         Paragraph('Arquitectura moderna, datos integrados, capacidad de iterar', S['M_TD']),
         Paragraph('La estrategia no se puede ejecutar', S['M_TD'])],
    ]
    story.append(make_table(data, [1.1*inch, 2.7*inch, 2.2*inch], S, accent))

    # Anti-patrones
    story.append(Paragraph("¿Por Qué Fallan las Transformaciones?", S['M_SectionH1']))
    story.append(hr(accent))
    story.append(Paragraph(
        "McKinsey reporta que el <b>70% de las transformaciones digitales no alcanzan sus objetivos</b>. Las causas son sistemáticas:",
        S['M_Body']))

    anti = [
        ("Ferrari en el barro", "Tecnología potente, baja adopción", "Cultura débil"),
        ("Maquillaje digital", "Automatización de procesos rotos", "Procesos sin rediseñar"),
        ("Visionario sin herramientas", "Intención sin infraestructura", "Tecnología insuficiente"),
        ("Piloto eterno", "Pruebas sin escalamiento ni gobernanza", "Gobernanza ausente"),
    ]

    data2 = [
        [Paragraph('<b>Anti-patrón</b>', S['M_TH']),
         Paragraph('<b>Qué ocurre</b>', S['M_TH']),
         Paragraph('<b>Dimensión débil</b>', S['M_TH'])]]
    for ap, what, dim in anti:
        data2.append([Paragraph(f'<b>{ap}</b>', S['M_TDBold']),
                      Paragraph(what, S['M_TD']),
                      Paragraph(dim, S['M_TD'])])
    story.append(make_table(data2, [1.5*inch, 2.5*inch, 2.0*inch], S, accent))

    # Framework IA
    story.append(Paragraph("Framework Estratégico de Implementación de IA", S['M_SectionH1']))
    story.append(hr(accent))
    story.append(Paragraph(
        "En lugar de pensar la IA como experimentación aislada, el framework R'Evolution 2026 define un <b>modelo operativo real</b> con gobernanza formal, ejes estratégicos obligatorios, presupuesto explícito y revisión periódica.",
        S['M_Body']))

    # Principios
    story.append(Paragraph("Principios Rectores", S['M_SectionH2']))
    principles = [
        ("Centralización estratégica", "Ejes definidos por una Célula Estratégica IA. Validación técnica. KPIs y ROI obligatorios. Presupuesto revisado en MBR."),
        ("Ejecución descentralizada", "Cada institución implementa en su contexto. Autonomía dentro de lineamientos comunes."),
        ("Iteración ágil", "Pilotos acotados. Escalar lo que funciona. Descartar lo que no. Sin 'pilotos eternos'."),
        ("Ética y responsabilidad", "Transparencia, equidad, protección de datos y explicabilidad no son opcionales."),
    ]
    for p, d in principles:
        story.append(bullet(f'<b>{p}:</b> {d}', S))

    # Gobernanza
    story.append(Paragraph("Estructura de Gobernanza", S['M_SectionH2']))

    gov = [
        [Paragraph('<b>Rol</b>', S['M_TH']),
         Paragraph('<b>Responsabilidades</b>', S['M_TH'])],
        [Paragraph('<b>Célula Estratégica IA</b>', S['M_TDBold']),
         Paragraph('Define lineamientos y ejes estratégicos. Aprueba presupuesto. Valida KPIs y ROI.', S['M_TD'])],
        [Paragraph('<b>Equipo Experto IA</b>', S['M_TDBold']),
         Paragraph('Valida arquitecturas y selecciona herramientas. Documenta aprendizajes. Apoya equipos reducidos.', S['M_TD'])],
        [Paragraph('<b>Instituciones / EdTech</b>', S['M_TDBold']),
         Paragraph('Ejecutan ejes estratégicos. Proponen iniciativas propias. Reportan en MBR mensual y QBR trimestral.', S['M_TD'])],
    ]
    story.append(make_table(gov, [1.6*inch, 4.4*inch], S, accent))

    story.append(Spacer(1, 8))
    story.append(Paragraph(
        '«  En una organización, lo que no tiene presupuesto propio no tiene prioridad real.  »',
        S['M_Quote']))

    # IA como capa transversal
    story.append(Paragraph("IA como Capa Transversal", S['M_SectionH1']))
    story.append(hr(accent))
    story.append(Paragraph(
        "La IA no es un producto que se compra y se instala en un rincón. Es una <b>capacidad que se integra en cada proceso existente</b>. "
        "Un chatbot desconectado del SIS no sabe cuándo vence la cuota. Desconectado del CRM, no detecta que el estudiante lleva 3 semanas inactivo. "
        "El chatbot responde — pero no transforma nada.",
        S['M_Body']))

    cross = [
        ("CRM", "Segmentación inteligente, alertas de riesgo, personalización de comunicaciones"),
        ("SIS", "Predicción de deserción, recomendaciones académicas, análisis de cohortes"),
        ("LMS", "Contenido adaptativo, evaluación automatizada, análisis de engagement"),
        ("ERP", "Detección de anomalías financieras, optimización de cobros, automatización contable"),
        ("BI", "Dashboards predictivos, anomaly detection, natural language queries"),
    ]
    for sys, app in cross:
        story.append(bullet(f'<b>{sys}:</b> {app}', S))

    # Ética y riesgos
    story.append(Paragraph("Riesgos y Marco Ético", S['M_SectionH1']))
    story.append(hr(accent))
    story.append(Paragraph(
        "Cuando un algoritmo decide qué estudiante recibe una beca o quién es marcado 'en riesgo', esas decisiones tienen consecuencias reales. Si el modelo fue entrenado con datos sesgados, reproduce y amplifica ese sesgo — sin que nadie lo note, porque 'lo dijo el sistema'.",
        S['M_Body']))

    risks = [
        "Supervisión humana significativa en toda decisión que afecte a personas.",
        "Robustez técnica: el modelo debe funcionar bien en todos los contextos, no solo en el promedio.",
        "Gobernanza de datos: ¿qué datos usamos? ¿con qué consentimiento?",
        "Transparencia y explicabilidad: ¿podemos explicar por qué el sistema tomó esa decisión?",
        "No discriminación: auditar regularmente los modelos para detectar sesgos.",
        "Rendición de cuentas: alguien en la organización es responsable de las decisiones de los sistemas.",
    ]
    for r in risks:
        story.append(bullet(r, S))

    # Resultado
    story.append(Paragraph("Al terminar este módulo, cada participante:", S['M_SectionH1']))
    story.append(hr(accent))
    outcomes = [
        "Entiende la transformación digital como sistema (cultura + procesos + tecnología).",
        "Conoce un framework operativo real de implementación de IA.",
        "Puede diseñar gobernanza básica para IA en su organización.",
        "Identifica un eje estratégico prioritario y define un primer paso estructurado.",
    ]
    for o in outcomes:
        story.append(bullet(o, S))


# ============================================================
# MODULE 5 CONTENT
# ============================================================
def content_m5(story, S, accent):
    # Qué es
    story.append(Paragraph("¿Qué es el Mindset Digital?", S['M_SectionH1']))
    story.append(hr(accent))

    data = [
        [Paragraph('<b>NO es...</b>', S['M_TH']),
         Paragraph('<b>SÍ es...</b>', S['M_TH'])],
        [Paragraph('Ser joven o "millennial"', S['M_TD']),
         Paragraph('Una forma de tomar decisiones basada en datos, experimentación y velocidad', S['M_TD'])],
        [Paragraph('Saber usar herramientas digitales', S['M_TD']),
         Paragraph('La capacidad de liderar en contextos de incertidumbre tecnológica', S['M_TD'])],
        [Paragraph('Hablar de innovación en conferencias', S['M_TD']),
         Paragraph('Un conjunto de prácticas concretas que se pueden instalar en una organización', S['M_TD'])],
        [Paragraph('Tener cuentas en redes sociales', S['M_TD']),
         Paragraph('La capa humana que hace posible la estrategia tecnológica', S['M_TD'])],
    ]
    story.append(make_table(data, [2.9*inch, 3.1*inch], S, accent))

    # Los 7 pilares
    story.append(Paragraph("Los 7 Pilares del Mindset Digital", S['M_SectionH1']))
    story.append(hr(accent))

    pillars = [
        ("1 · Orientación a Producto",
         "El campus virtual no es un proyecto que termina — es un producto que se itera y mejora. "
         "La pregunta no es '¿cuándo terminamos?' sino '¿cuánto valor estamos entregando hoy vs. hace 3 meses?'",
         '"Implementamos el LMS hace 2 años y desde entonces no lo tocamos porque ya funciona."'),
        ("2 · Aprendizaje Continuo",
         "La tecnología cambia más rápido que los organigramas. Un líder que dejó de aprender hace 3 años toma decisiones con información desactualizada. "
         "2-3 horas semanales de lectura sobre tendencias. Probar personalmente las herramientas que usa la organización.",
         '"Yo no necesito entender de tecnología, para eso tengo un equipo de IT."'),
        ("3 · Experimentación",
         "Hipótesis → Prototipo → Prueba controlada → Medir → Decidir (escalar o descartar). "
         "Experimentar no es improvisar: es testear con métricas definidas, en alcance controlado.",
         '"Necesitamos un business case de 50 páginas y aprobación de 5 comités antes de probar algo."'),
        ("4 · Colaboración Multidisciplinaria",
         "Negocio + Tecnología + Datos + Diseño = Decisiones integrales. "
         "El área académica no elige el LMS sola — lo elige con IT y experiencia del estudiante.",
         '"Eso es tema de sistemas, no mío."'),
        ("5 · Cultura de Datos",
         "No opinar, medir. No asumir, probar. '¿Las discusiones en el comité directivo se basan en datos o en yo creo que?' "
         "No se trata de tener data science — se trata de que las decisiones ejecutivas se basen en evidencia.",
         '"Yo creo que la deserción bajó" (sin datos).'),
        ("6 · Agencia Digital",
         "La tecnología no es responsabilidad exclusiva de IT. Cada persona debería poder entender, usar y proponer mejoras. "
         "Niveles: Pasivo → Usuario → Participante → Protagonista.",
         '"Solo IT propone soluciones tecnológicas."'),
        ("7 · Seguridad y Ética como Base",
         "¿Qué datos personales almacenamos? ¿Quién tiene acceso? ¿Cumplimos regulación de protección de datos? "
         "En 2024, una filtración de datos es una crisis reputacional que llega a dirección general, no solo al CTO.",
         '"La seguridad es tema del equipo de IT."'),
    ]

    for pname, pdesc, panti in pillars:
        story.append(KeepTogether([
            Paragraph(pname, S['M_SectionH2']),
            Paragraph(pdesc, S['M_Body']),
            Paragraph(f'<font color="#94a3b8"><i>Anti-patrón:</i> {panti}</font>',
                      ParagraphStyle('AntiPat', parent=S['M_BodyLeft'],
                                     fontSize=9.5, textColor=TEXT_MUTED,
                                     leftIndent=12, spaceBefore=0, spaceAfter=10)),
        ]))

    # Platzi como caso integrador
    story.append(Paragraph("Caso Integrador: Platzi y los 7 Pilares", S['M_SectionH1']))
    story.append(hr(accent))

    platzi = [
        [Paragraph('<b>Pilar</b>', S['M_TH']),
         Paragraph('<b>Platzi</b>', S['M_TH']),
         Paragraph('<b>Universidad tradicional</b>', S['M_TH'])],
        [Paragraph('Producto', S['M_TDBold']),
         Paragraph('Actualización semanal de la plataforma, sin "versiones"', S['M_TD']),
         Paragraph('Reforma curricular cada 3-5 años', S['M_TD'])],
        [Paragraph('Aprendizaje', S['M_TDBold']),
         Paragraph('Los fundadores siguen creando cursos y aprendiendo', S['M_TD']),
         Paragraph('Formación continua no es sistemática', S['M_TD'])],
        [Paragraph('Experimentación', S['M_TDBold']),
         Paragraph('Nuevos formatos de contenido se prueban continuamente', S['M_TD']),
         Paragraph('Cambios requieren aprobaciones largas', S['M_TD'])],
        [Paragraph('Datos', S['M_TDBold']),
         Paragraph('Tasas de finalización, engagement y NPS como indicadores centrales', S['M_TD']),
         Paragraph('Matrícula + egresados como métricas principales', S['M_TD'])],
        [Paragraph('Agencia', S['M_TDBold']),
         Paragraph('Toda la organización propone mejoras al producto', S['M_TD']),
         Paragraph('IT decide sobre tecnología de forma aislada', S['M_TD'])],
    ]
    story.append(make_table(platzi, [0.9*inch, 2.5*inch, 2.6*inch], S, accent))

    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "La pregunta no es 'cómo ser como Platzi' — es <b>qué prácticas de este mindset puedo incorporar en mi contexto</b>.",
        S['M_Body']))

    # Resultado
    story.append(Paragraph("Al terminar este módulo, cada participante:", S['M_SectionH1']))
    story.append(hr(accent))
    outcomes = [
        "Entiende el mindset digital como un sistema de decisión concreto, no como una actitud aspiracional.",
        "Puede diagnosticar el nivel de madurez de los 7 pilares en su organización.",
        "Identifica anti-patrones en su propia gestión y en la de su organización.",
        "Tiene acciones concretas para mejorar al menos 2 pilares en el corto plazo.",
        "Puede modelar y comunicar este mindset a su equipo directivo.",
    ]
    for o in outcomes:
        story.append(bullet(o, S))

    story.append(Spacer(1, 20))
    story.append(Paragraph(
        '«  La estrategia tecnológica sin mindset digital es un plan. El mindset digital sin estrategia tecnológica es improvisación. Juntos, son transformación.  »',
        S['M_Quote']))


# ============================================================
# MODULE 6 CONTENT (Bonus — Panel IA y Educación)
# ============================================================
def content_m6(story, S, accent):
    story.append(Paragraph("Propósito del Panel", S['M_SectionH1']))
    story.append(hr(accent))
    story.append(Paragraph(
        "Este módulo abre un espacio de reflexión profunda — sin respuestas predefinidas — sobre cómo la inteligencia artificial va a transformar la educación en los próximos 5-10 años. "
        "<b>No es una clase. Es una conversación entre líderes que toman decisiones hoy sobre un futuro incierto.</b>",
        S['M_Body']))

    fmt_data = [
        [Paragraph('<b>Elemento</b>', S['M_TH']),
         Paragraph('<b>Detalle</b>', S['M_TH'])],
        [Paragraph('Duración', S['M_TDBold']), Paragraph('60 minutos', S['M_TD'])],
        [Paragraph('Formato', S['M_TDBold']), Paragraph('Panel de discusión moderado', S['M_TD'])],
        [Paragraph('Dinámica', S['M_TDBold']),
         Paragraph('Preguntas provocadoras → debate abierto → votación de posiciones', S['M_TD'])],
        [Paragraph('Selección', S['M_TDBold']),
         Paragraph('Se eligen 3 de 5 preguntas según la energía del grupo (sugeridas: 1, 4 y 5)', S['M_TD'])],
    ]
    story.append(make_table(fmt_data, [1.5*inch, 4.5*inch], S, accent))

    # 5 preguntas
    story.append(Paragraph("Las 5 Preguntas Provocadoras", S['M_SectionH1']))
    story.append(hr(accent))

    questions = [
        (
            "1. ¿La IA va a reemplazar docentes o va a potenciarlos?",
            [
                "Sal Khan (Khan Academy): un tutor de IA personalizado es el mayor avance educativo desde la imprenta.",
                "UNESCO advierte que la adopción sin regulación puede ampliar la brecha educativa.",
                "Tec de Monterrey: no reemplazó docentes, les dio herramientas de IA para amplificar su impacto.",
            ],
            [
                "A: La IA va a reemplazar al docente en tareas repetitivas, liberándolo para mentoría y pensamiento crítico.",
                "B: Va a crear el 'docente aumentado' que usa IA como co-piloto.",
                "C: Riesgo real de que instituciones reemplacen docentes por IA para reducir costos.",
            ],
            "Si un estudiante puede aprender más con un tutor de IA que con una clase magistral de 200 personas, ¿cuál es el rol de la institución educativa?"
        ),
        (
            "2. ¿Los títulos universitarios van a perder valor?",
            [
                "Google, Apple, IBM y otras Big Tech eliminaron el requisito de título para muchos puestos.",
                "Las micro-credenciales (badges, certificados) crecen exponencialmente.",
                "En LATAM, el título sigue siendo un diferenciador social y económico fuerte.",
            ],
            [
                "A: El título va a perder valor como credencial laboral, pero mantendrá valor como experiencia formativa.",
                "B: Va a ser reemplazado por portafolios de habilidades verificables.",
                "C: Va a evolucionar, no desaparecer. Se complementará con certificaciones y evidencia de competencias.",
            ],
            "Si un estudiante demuestra competencia con un portafolio verificado por IA, ¿necesita pasar por 4-5 años de formación formal?"
        ),
        (
            "3. ¿Quién debe regular la IA en educación?",
            [
                "La UE avanza con el AI Act, que clasifica la IA en educación como 'alto riesgo'.",
                "LATAM tiene regulación desigual: algunos países avanzan, otros no tienen marco legal.",
                "Las propias instituciones están definiendo sus políticas caso a caso.",
            ],
            [
                "A: Gobiernos nacionales deben establecer marcos regulatorios claros.",
                "B: Las instituciones deben autorregularse con estándares éticos propios.",
                "C: La regulación va a llegar siempre tarde. Lo importante es tener principios claros hoy.",
            ],
            "¿Estás dispuesto a que un algoritmo decida si un estudiante está en riesgo de deserción? ¿Y si el algoritmo tiene sesgos que no podemos detectar?"
        ),
        (
            "4. ¿La IA va a democratizar o concentrar la educación?",
            [
                "Un estudiante en zona rural de Perú puede acceder a un tutor de IA de nivel mundial con un celular.",
                "Las universidades con más recursos desarrollarán ecosistemas de IA mucho más sofisticados.",
                "La brecha puede redefinirse, no eliminarse.",
            ],
            [
                "A: Democratización — la IA reduce barreras de acceso y personaliza a escala.",
                "B: Concentración — solo instituciones con presupuesto implementarán IA de calidad.",
                "C: Ambas cosas al mismo tiempo. La brecha se va a redefinir, no a eliminar.",
            ],
            "Si ChatGPT puede dar una clase mejor que el 80% de los docentes del mundo, ¿qué hacemos con esa realidad?"
        ),
        (
            "5. ¿Qué debería saber hacer un profesional de 2030?",
            [
                "Si la IA puede escribir código, traducir idiomas y analizar datos, ¿cuáles son las habilidades humanas irremplazables?",
                "El WEF proyecta que el 65% de los niños que hoy entran a primaria trabajarán en profesiones que aún no existen.",
            ],
            [
                "A: Pensamiento crítico, creatividad, colaboración y adaptabilidad. Las soft skills pasan a ser las core skills.",
                "B: Alfabetización en IA como competencia fundamental para todos.",
                "C: Aprender a aprender. La capacidad de adaptación es la única skill a prueba de futuro.",
            ],
            "¿Tu plan de estudios actual prepara estudiantes para 2030 o para 2010?"
        ),
    ]

    for q_title, context, positions, filosa in questions:
        story.append(KeepTogether([
            Paragraph(q_title, S['M_SectionH2']),
            Paragraph('<b>Contexto:</b>', S['M_BodyLeft']),
        ]))
        for c in context:
            story.append(bullet(c, S))
        story.append(Paragraph('<b>Posiciones posibles:</b>', S['M_BodyLeft']))
        for p in positions:
            story.append(bullet(p, S))
        story.append(Paragraph(
            f'<font color="#94a3b8"><i>Pregunta filosa: {filosa}</i></font>',
            ParagraphStyle('Filosa', parent=S['M_BodyLeft'],
                           fontSize=9.5, textColor=TEXT_MUTED,
                           leftIndent=12, spaceAfter=16)))

    # Cierre
    story.append(Paragraph("Dinámica de Cierre: Votación de Posiciones", S['M_SectionH1']))
    story.append(hr(accent))
    story.append(Paragraph(
        "Cada participante vota la afirmación que más le resuena. El objetivo no es consenso — es hacer visible la diversidad de perspectivas en la sala.",
        S['M_Body']))

    posiciones = [
        '"La IA es la mayor oportunidad para la educación en 100 años."',
        '"La IA es un riesgo que necesitamos gestionar con cuidado."',
        '"La IA no va a cambiar tanto como creemos — es otra ola tecnológica más."',
        '"No tengo una posición clara y eso está bien."',
    ]
    for p in posiciones:
        story.append(bullet(p, S))

    # Lecturas
    story.append(Paragraph("Lecturas Sugeridas para Profundizar", S['M_SectionH1']))
    story.append(hr(accent))

    reads = [
        ("Sal Khan", "Brave New Words: How AI Will Revolutionize Education (and Why That's a Good Thing)", "2024"),
        ("Ethan Mollick", "Co-Intelligence: Living and Working with AI", "2024"),
        ("UNESCO", "Guidance for Generative AI in Education and Research", "2023"),
        ("World Economic Forum", "Future of Jobs Report", "Edición más reciente"),
        ("Audrey Watters", "Teaching Machines: The History of Personalized Learning", "2021 — perspectiva crítica"),
    ]

    read_data = [
        [Paragraph('<b>Autor</b>', S['M_TH']),
         Paragraph('<b>Título</b>', S['M_TH']),
         Paragraph('<b>Año</b>', S['M_TH'])]]
    for author, title, year in reads:
        read_data.append([Paragraph(author, S['M_TDBold']),
                          Paragraph(title, S['M_TD']),
                          Paragraph(year, S['M_TDCenter'])])
    story.append(make_table(read_data, [1.3*inch, 3.8*inch, 0.9*inch], S, accent))

    story.append(Spacer(1, 20))
    story.append(Paragraph(
        '«  No vinimos a resolver estas preguntas. Vinimos a hacérnoslas con mejor criterio.  »',
        S['M_Quote']))


# ============================================================
# MAIN
# ============================================================
def main():
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'docs', 'pdfs')
    os.makedirs(output_dir, exist_ok=True)

    modules = [
        (1,
         "Hello World",
         "Tecnología como ventaja competitiva",
         "¿Por qué la tecnología dejó de ser un área de soporte y pasó a ser parte de la estrategia del negocio?",
         "Comprender por qué la tecnología dejó de ser soporte y se convirtió en una pieza central del negocio educativo. Al terminar, cada líder identifica en qué nivel está su organización y qué implica esa posición para competir.",
         content_m1),
        (2,
         "Estrategia Tecnológica",
         "Decisiones que definen el futuro",
         "¿Qué decisiones tecnológicas son estratégicas y cuáles son tácticas?",
         "Adquirir el vocabulario, los criterios y los frameworks para participar activamente en la definición de la estrategia tecnológica. No se trata de aprender tecnología, sino de aprender a decidir sobre tecnología.",
         content_m2),
        (3,
         "Arquitectura IT Educativa",
         "El mapa de tus sistemas",
         "¿Cómo funciona realmente una institución educativa moderna por dentro?",
         "Poder leer, cuestionar y discutir la arquitectura tecnológica de una institución, aunque no se sea técnico. Entender cómo funcionan los sistemas para tomar mejores decisiones y hacer mejores preguntas.",
         content_m3),
        (4,
         "Transformación Digital e IA",
         "De la intención a la gobernanza",
         "¿Cómo transformar sin romper la organización?",
         "Comprender que la transformación digital requiere cultura + procesos + tecnología. Entender que la adopción de IA no es un proyecto aislado, sino una decisión estratégica con gobernanza.",
         content_m4),
        (5,
         "Mindset Digital",
         "El sistema operativo del liderazgo",
         "¿Qué tipo de líder necesita ser tu organización para que la estrategia tecnológica funcione?",
         "Internalizar el mindset digital no como una actitud motivacional, sino como un sistema concreto de toma de decisiones que se puede modelar y escalar en la organización.",
         content_m5),
        (6,
         "IA y el Futuro de la Educación",
         "Panel de discusión — Bonus",
         "¿Cómo va a transformar la IA la educación en los próximos 5-10 años?",
         "Abrir un espacio de reflexión profunda entre líderes sobre el futuro de la educación mediada por IA. Sin respuestas predefinidas — con mejor criterio para abordar las preguntas que definen el sector.",
         content_m6),
    ]

    print("\nGenerando PDFs por módulo...\n")
    for num, title, subtitle, guiding_q, objective, content_fn in modules:
        filename = f"modulo-{num:02d}-{title.lower().replace(' ', '-').replace('/', '-')}.pdf"
        out = os.path.join(output_dir, filename)
        build_pdf(out, num, title, subtitle, guiding_q, objective, content_fn)

    print(f"\n✅  6 PDFs generados en: docs/pdfs/\n")


if __name__ == "__main__":
    main()
