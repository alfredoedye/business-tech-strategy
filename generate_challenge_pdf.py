#!/usr/bin/env python3
"""
Genera el PDF del Template de Trabajo del Challenge "Arquitecto del Futuro"
con comentarios-guía para que los estudiantes hagan un buen trabajo.
Reutiliza el design system de generate_pdfs.py.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

# ============================================================
# DESIGN SYSTEM (same as module PDFs)
# ============================================================
DARK_NAVY = HexColor('#0f172a')
CYAN = HexColor('#0891b2')
PURPLE = HexColor('#7c3aed')
MAGENTA = HexColor('#be185d')
AMBER = HexColor('#d97706')
EMERALD = HexColor('#059669')
LIGHT_BG = HexColor('#f8fafc')
CARD_BG = HexColor('#f1f5f9')
BORDER = HexColor('#e2e8f0')
TEXT_DARK = HexColor('#0f172a')
TEXT_BODY = HexColor('#334155')
TEXT_MUTED = HexColor('#94a3b8')
ACCENT_LIGHT = HexColor('#e0f2fe')  # light cyan for hint boxes
WHITE = white

PAGE_W, PAGE_H = A4
MARGIN = 0.85 * inch
ACCENT = CYAN  # challenge accent color

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(BASE_DIR, 'docs/pdfs/template-challenge-arquitecto-del-futuro.pdf')


# ============================================================
# STYLES
# ============================================================
def make_styles():
    S = getSampleStyleSheet()

    S.add(ParagraphStyle('M_ModuleTag',
        fontSize=10, leading=14, textColor=ACCENT,
        fontName='Helvetica-Bold', spaceAfter=4))

    S.add(ParagraphStyle('M_CoverTitle',
        fontSize=28, leading=34, textColor=TEXT_DARK,
        fontName='Helvetica-Bold', spaceAfter=8, alignment=TA_LEFT))

    S.add(ParagraphStyle('M_CoverSubtitle',
        fontSize=15, leading=20, textColor=ACCENT,
        fontName='Helvetica', spaceAfter=6, alignment=TA_LEFT))

    S.add(ParagraphStyle('M_SlideTitle',
        fontSize=16, leading=22, textColor=TEXT_DARK,
        fontName='Helvetica-Bold', spaceBefore=4, spaceAfter=4))

    S.add(ParagraphStyle('M_SlideNum',
        fontSize=10, leading=14, textColor=ACCENT,
        fontName='Helvetica-Bold', spaceBefore=0, spaceAfter=2))

    S.add(ParagraphStyle('M_Body',
        fontSize=10.5, leading=16, textColor=TEXT_BODY,
        fontName='Helvetica', spaceAfter=8, alignment=TA_JUSTIFY))

    S.add(ParagraphStyle('M_Hint',
        fontSize=9.5, leading=14.5, textColor=HexColor('#1e40af'),
        fontName='Helvetica-Oblique', spaceAfter=6,
        leftIndent=12, rightIndent=12, spaceBefore=4,
        backColor=ACCENT_LIGHT, borderPadding=8))

    S.add(ParagraphStyle('M_FieldLabel',
        fontSize=10.5, leading=16, textColor=TEXT_DARK,
        fontName='Helvetica-Bold', spaceAfter=2, spaceBefore=8))

    S.add(ParagraphStyle('M_FieldSpace',
        fontSize=10, leading=32, textColor=TEXT_MUTED,
        fontName='Helvetica', spaceAfter=4,
        borderWidth=0, borderColor=BORDER))

    S.add(ParagraphStyle('M_Quote',
        fontSize=12, leading=19, textColor=ACCENT,
        fontName='Helvetica-Oblique', spaceBefore=10, spaceAfter=10,
        leftIndent=24, rightIndent=24, alignment=TA_LEFT))

    S.add(ParagraphStyle('M_Bullet',
        fontSize=10.5, leading=15, textColor=TEXT_BODY,
        fontName='Helvetica', spaceAfter=4, leftIndent=18,
        firstLineIndent=-14))

    S.add(ParagraphStyle('M_Warning',
        fontSize=9.5, leading=14, textColor=HexColor('#9a3412'),
        fontName='Helvetica-Oblique', spaceAfter=6,
        leftIndent=12, rightIndent=12, spaceBefore=4,
        backColor=HexColor('#fff7ed'), borderPadding=8))

    S.add(ParagraphStyle('M_TH',
        fontSize=9.5, leading=13, textColor=WHITE,
        fontName='Helvetica-Bold', alignment=TA_LEFT))

    S.add(ParagraphStyle('M_TD',
        fontSize=9, leading=13, textColor=TEXT_BODY,
        fontName='Helvetica', alignment=TA_LEFT))

    S.add(ParagraphStyle('M_SectionH2',
        fontSize=13, leading=18, textColor=ACCENT,
        fontName='Helvetica-Bold', spaceBefore=14, spaceAfter=6))

    S.add(ParagraphStyle('M_Footer',
        fontSize=8, leading=11, textColor=TEXT_MUTED,
        fontName='Helvetica', alignment=TA_CENTER))

    return S


# ============================================================
# HELPERS
# ============================================================
def hr(thickness=0.8, space_before=6, space_after=6):
    return HRFlowable(width='100%', thickness=thickness,
                      color=ACCENT, spaceAfter=space_after, spaceBefore=space_before)


def bullet(text, S):
    return Paragraph(f'<font color="#0891b2">\u25b8</font>  {text}', S['M_Bullet'])


def field_block(label, S, lines=3):
    """A labeled field with blank writing space."""
    elements = [Paragraph(label, S['M_FieldLabel'])]
    for _ in range(lines):
        elements.append(Paragraph(
            '_______________________________________________________________________________',
            S['M_FieldSpace']))
    return elements


def hint(text, S):
    """A coach hint box in light blue."""
    return Paragraph(f'<b>Tip:</b> {text}', S['M_Hint'])


def warning(text, S):
    """A warning/prohibition box in light orange."""
    return Paragraph(f'<b>Cuidado:</b> {text}', S['M_Warning'])


def make_table(data, col_widths, S, zebra=True):
    table = Table(data, colWidths=col_widths, repeatRows=1)
    styles = [
        ('BACKGROUND', (0, 0), (-1, 0), ACCENT),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1),
         [LIGHT_BG, CARD_BG] if zebra else [LIGHT_BG]),
    ]
    table.setStyle(TableStyle(styles))
    return table


def _wrap_text(text, font_size, max_width):
    from reportlab.pdfbase.pdfmetrics import stringWidth
    words = text.split()
    lines, current = [], ""
    for word in words:
        test = f"{current} {word}".strip()
        if stringWidth(test, 'Helvetica-Bold', font_size) <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


# ============================================================
# COVER PAGE
# ============================================================
def build_cover(c, doc):
    c.saveState()
    w, h = A4

    # Left accent band
    c.setFillColor(ACCENT)
    c.rect(0, 0, 0.35 * inch, h, fill=1, stroke=0)

    # Top accent strip
    c.setFillColor(ACCENT)
    c.rect(0, h - 0.12 * inch, w, 0.12 * inch, fill=1, stroke=0)

    # Label
    c.setFont('Helvetica-Bold', 9)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN, h - 1.1 * inch, "CHALLENGE")

    # Watermark
    c.setFont('Helvetica-Bold', 100)
    c.setFillColor(HexColor('#f1f5f9'))
    c.drawRightString(w - MARGIN + 0.2 * inch, h - 3.6 * inch, "AF")

    # Title
    c.setFont('Helvetica-Bold', 28)
    c.setFillColor(TEXT_DARK)
    title_lines = _wrap_text("Arquitecto del Futuro", 28, w - 2 * MARGIN - 0.2 * inch)
    y = h - 1.6 * inch
    for line in title_lines:
        c.drawString(MARGIN, y, line)
        y -= 34

    # Subtitle
    c.setFont('Helvetica', 15)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN, y - 10, "Template de Trabajo")
    y -= 32
    c.setFont('Helvetica', 12)
    c.setFillColor(TEXT_MUTED)
    c.drawString(MARGIN, y, "Completar como borrador antes de armar las slides finales.")

    # Divider
    y -= 30
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.6)
    c.line(MARGIN, y, w - MARGIN, y)

    # Instructions box
    y -= 30
    c.setFont('Helvetica', 10)
    c.setFillColor(TEXT_BODY)
    instructions = [
        "Trabajo individual  \u2014  10\u201315 slides  \u2014  Defensa oral de 10 min",
        "No se eval\u00faa si la idea es interesante.",
        "Se eval\u00faa si es ejecutable, priorizable y defendible.",
    ]
    for line in instructions:
        c.drawString(MARGIN, y, line)
        y -= 18

    # Bottom bar
    c.setFillColor(DARK_NAVY)
    c.rect(0, 0, w, 0.7 * inch, fill=1, stroke=0)
    c.setFont('Helvetica', 9)
    c.setFillColor(HexColor('#94a3b8'))
    c.drawString(MARGIN, 0.35 * inch, "Estrategia Tecnol\u00f3gica + Mindset Digital")
    c.drawRightString(w - MARGIN, 0.35 * inch, "Programa Ejecutivo")

    c.restoreState()


def page_header_footer(c, doc):
    c.saveState()
    w, h = A4

    c.setFillColor(ACCENT)
    c.rect(MARGIN, h - 0.55 * inch, w - 2 * MARGIN, 2.5, fill=1, stroke=0)
    c.setFont('Helvetica-Bold', 8)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN, h - 0.45 * inch, "CHALLENGE  \u00b7  Arquitecto del Futuro")

    page_num = c.getPageNumber()
    c.setFont('Helvetica', 8)
    c.setFillColor(TEXT_MUTED)
    c.drawCentredString(w / 2, 0.45 * inch,
                        f"Estrategia Tecnol\u00f3gica + Mindset Digital  \u00b7  P\u00e1gina {page_num}")
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.4)
    c.line(MARGIN, 0.6 * inch, w - MARGIN, 0.6 * inch)

    c.restoreState()


# ============================================================
# CONTENT
# ============================================================
def build_content(story, S):
    avail = PAGE_W - 2 * MARGIN - 4

    # ----------------------------------------------------------
    # Slide 1 — Contexto Estratégico
    # ----------------------------------------------------------
    story.append(Paragraph("SLIDE 1", S['M_SlideNum']))
    story.append(Paragraph("Contexto Estrat\u00e9gico", S['M_SlideTitle']))
    story.append(hr(1.2))

    story.append(hint(
        "Esta slide es tu <b>pitch ejecutivo</b>. En menos de 30 segundos, "
        "el comit\u00e9 directivo debe entender qu\u00e9 duele, cu\u00e1nto cuesta "
        "y por qu\u00e9 deber\u00eda importarles. No es un resumen \u2014 es un llamado a la acci\u00f3n. "
        "Pens\u00e1 como si estuvieras pidiendo presupuesto en una reuni\u00f3n de directorio.", S))

    story.extend(field_block("Organizaci\u00f3n / \u00c1rea / Proceso elegido:", S))
    story.extend(field_block("Qu\u00e9 duele hoy (problema espec\u00edfico, no general):", S))
    story.extend(field_block("KPI cr\u00edtico afectado (con n\u00famero si es posible):", S))
    story.extend(field_block("Por qu\u00e9 es estrat\u00e9gico (consecuencia de no actuar):", S))

    story.append(warning(
        "Evit\u00e1 frases como \u201cfalta innovaci\u00f3n\u201d o \u201cnecesitamos digitalizarnos\u201d. "
        "El evaluador busca <b>evidencia concreta</b>, no generalidades.", S))

    # ----------------------------------------------------------
    # Slide 2 — Diagnóstico
    # ----------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("SLIDE 2", S['M_SlideNum']))
    story.append(Paragraph("Diagn\u00f3stico", S['M_SlideTitle']))
    story.append(hr(1.2))

    story.append(hint(
        "Aplic\u00e1 el framework de <b>Good Strategy / Bad Strategy</b>: el poder de un buen "
        "diagn\u00f3stico est\u00e1 en identificar la <b>causa ra\u00edz</b>, no los s\u00edntomas. "
        "Si tu diagn\u00f3stico podr\u00eda aplicarse a cualquier organizaci\u00f3n, es demasiado gen\u00e9rico. "
        "Preguntate: \u00bfqu\u00e9 creencia o pr\u00e1ctica espec\u00edfica sostiene el problema hoy?", S))

    story.extend(field_block("Problema real (espec\u00edfico, observable):", S))
    story.extend(field_block("Evidencia observable (datos, hechos, m\u00e9tricas):", S))
    story.extend(field_block("Causa ra\u00edz (por qu\u00e9 existe el problema):", S))
    story.extend(field_block("Falsa explicaci\u00f3n dominante (qu\u00e9 ilusi\u00f3n existe hoy):", S))

    story.append(hint(
        "La <b>falsa explicaci\u00f3n</b> es clave. Es la narrativa c\u00f3moda que evita el cambio. "
        "Ejemplo: \u201cEl problema es que el CRM no sirve\u201d cuando en realidad nadie lo alimenta con datos.", S))

    # ----------------------------------------------------------
    # Slide 3 — Decisión Estratégica
    # ----------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("SLIDE 3", S['M_SlideNum']))
    story.append(Paragraph("La Decisi\u00f3n Estrat\u00e9gica", S['M_SlideTitle']))
    story.append(hr(1.2))

    story.append(hint(
        "Aqu\u00ed se eval\u00faa tu <b>pensamiento estrat\u00e9gico real</b>. Estrategia no es elegir qu\u00e9 hacer "
        "\u2014 es elegir qu\u00e9 <b>NO</b> hacer. Una buena decisi\u00f3n estrat\u00e9gica duele un poco, "
        "porque implica renunciar a algo que parece importante.", S))

    story.append(Spacer(1, 12))
    story.append(Paragraph(
        '<b>Complet\u00e1 la f\u00f3rmula:</b>', S['M_Body']))
    story.append(Paragraph(
        '\u201cElijo NO ______________________________\npara concentrarme en ______________________________\u201d',
        S['M_Quote']))

    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Ejemplos para inspirarte:</b>", S['M_Body']))
    story.append(bullet("NO escalar features \u2192 S\u00cd redise\u00f1ar onboarding", S))
    story.append(bullet("NO cambiar de LMS \u2192 S\u00cd construir capa de experiencia/datos encima", S))
    story.append(bullet("NO digitalizar todo a la vez \u2192 S\u00cd resolver el cuello de botella de admisi\u00f3n", S))

    story.extend(field_block("Tu decisi\u00f3n estrat\u00e9gica:", S, 4))

    # ----------------------------------------------------------
    # Slide 4 — Principio Rector
    # ----------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("SLIDE 4", S['M_SlideNum']))
    story.append(Paragraph("Principio Rector", S['M_SlideTitle']))
    story.append(hr(1.2))

    story.append(hint(
        "Tu principio rector es la <b>br\u00fajula</b> de toda la propuesta. Debe ser una frase corta "
        "que permita validar cada acci\u00f3n que propongas despu\u00e9s. Si una acci\u00f3n no pasa el filtro "
        "de tu principio rector, no deber\u00eda estar en tu propuesta.", S))

    story.append(Paragraph("<b>Ejemplo:</b>", S['M_Body']))
    story.append(Paragraph(
        '\u201cReducir fricci\u00f3n operativa antes de incorporar IA.\u201d', S['M_Quote']))

    story.extend(field_block("Tu principio rector:", S, 3))

    story.append(hint(
        "Test r\u00e1pido: \u00bfpodr\u00edas usar esta frase para decirle \u201cno\u201d a una propuesta "
        "que suena bien pero no es prioritaria? Si s\u00ed, tu principio rector funciona.", S))

    # ----------------------------------------------------------
    # Slide 5 — Acciones Coherentes
    # ----------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("SLIDE 5", S['M_SlideNum']))
    story.append(Paragraph("Conjunto Coherente de Acciones", S['M_SlideTitle']))
    story.append(hr(1.2))

    story.append(hint(
        "Las acciones deben leerse como un <b>sistema</b>, no como un backlog de tareas. "
        "Cada acci\u00f3n debe conectarse causalmente con las dem\u00e1s: la acci\u00f3n 1 habilita "
        "la 2, que amplifica la 3. Si pudieras eliminar una acci\u00f3n sin afectar a las otras, "
        "probablemente no es parte del sistema.", S))

    # Editable table with empty rows
    data = [
        [Paragraph('<b>Acci\u00f3n</b>', S['M_TH']),
         Paragraph('<b>Qu\u00e9 cambia</b>', S['M_TH']),
         Paragraph('<b>Por qu\u00e9 importa</b>', S['M_TH'])],
    ]
    for i in range(5):
        data.append([
            Paragraph(f'{i+1}.', S['M_TD']),
            Paragraph('', S['M_TD']),
            Paragraph('', S['M_TD']),
        ])
    w3 = avail / 3
    table = make_table(data, [w3, w3, w3], S)
    story.append(Spacer(1, 8))
    story.append(table)

    story.append(Spacer(1, 10))
    story.append(warning(
        "No listes m\u00e1s de 5 acciones. Si ten\u00e9s 8, no ten\u00e9s estrategia \u2014 "
        "ten\u00e9s una lista de deseos. Prioriz\u00e1.", S))

    # ----------------------------------------------------------
    # Slide 6 — AS IS
    # ----------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("SLIDE 6", S['M_SlideNum']))
    story.append(Paragraph("AS IS \u2014 Proceso Actual", S['M_SlideTitle']))
    story.append(hr(1.2))

    story.append(hint(
        "Mapeá el flujo real como <b>es hoy</b>, no como dice el manual. "
        "Habl\u00e1 con las personas que ejecutan el proceso \u2014 siempre hay pasos manuales, "
        "workarounds y \u201cExcels secretos\u201d que ning\u00fan diagrama oficial captura. "
        "Cuantific\u00e1 al menos UNA fricci\u00f3n (tiempo perdido, tasa de error, costo).", S))

    story.extend(field_block("Flujo actual (pasos principales):", S, 4))
    story.extend(field_block("Fricciones cr\u00edticas:", S, 2))
    story.extend(field_block("Cuellos de botella:", S, 2))
    story.extend(field_block("Manualidad (procesos que dependen de personas espec\u00edficas):", S, 2))
    story.extend(field_block("Puntos sin datos (decisiones a ciegas):", S, 2))
    story.extend(field_block("Costos invisibles (cuantific\u00e1 al menos uno):", S, 2))

    # ----------------------------------------------------------
    # Slide 7 — TO BE
    # ----------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("SLIDE 7", S['M_SlideNum']))
    story.append(Paragraph("TO BE \u2014 Proceso Redise\u00f1ado", S['M_SlideTitle']))
    story.append(hr(1.2))

    story.append(hint(
        "No basta decir \u201cimplementamos una herramienta\u201d. "
        "El evaluador quiere ver <b>qu\u00e9 cambia concretamente</b> en la experiencia del estudiante "
        "o en la eficiencia operativa. Contrastá cada punto con el AS IS: "
        "si antes tomaba 48 horas, ahora toma 4. Si antes era manual, ahora es autom\u00e1tico.", S))

    story.extend(field_block("Qu\u00e9 desaparece del proceso:", S, 2))
    story.extend(field_block("Qu\u00e9 se automatiza:", S, 2))
    story.extend(field_block("Qu\u00e9 se simplifica:", S, 2))
    story.extend(field_block("Qu\u00e9 decisi\u00f3n mejora (y con qu\u00e9 datos):", S, 2))
    story.extend(field_block("Qu\u00e9 KPI cambia (y en qu\u00e9 direcci\u00f3n):", S, 2))

    story.append(warning(
        "Si tu TO BE no resuelve las fricciones que identificaste en el AS IS, hay una desconexión. "
        "Rele\u00e9 ambas slides juntas antes de pasar a la siguiente.", S))

    # ----------------------------------------------------------
    # Slide 8 — Arquitectura Objetivo
    # ----------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("SLIDE 8", S['M_SlideNum']))
    story.append(Paragraph("Arquitectura Objetivo (visi\u00f3n ejecutiva)", S['M_SlideTitle']))
    story.append(hr(1.2))

    story.append(hint(
        "No necesit\u00e1s un diagrama t\u00e9cnico complejo. Necesit\u00e1s mostrar con claridad "
        "<b>qu\u00e9 sistemas interact\u00faan, c\u00f3mo fluyen los datos y d\u00f3nde est\u00e1 el cambio estructural</b>. "
        "Record\u00e1 los 4 niveles de integraci\u00f3n del M\u00f3dulo 3: Manual \u2192 Archivos \u2192 APIs \u2192 Eventos. "
        "\u00bfEn qu\u00e9 nivel est\u00e1s hoy y a cu\u00e1l quer\u00e9s llegar?", S))

    story.append(Paragraph("<b>Capas sugeridas:</b>", S['M_Body']))

    layers_data = [
        [Paragraph('<b>Capa</b>', S['M_TH']),
         Paragraph('<b>Qu\u00e9 incluye</b>', S['M_TH']),
         Paragraph('<b>Tu propuesta</b>', S['M_TH'])],
        [Paragraph('<b>Systems</b>', S['M_TD']),
         Paragraph('SIS, LMS, CRM, ERP, etc.', S['M_TD']),
         Paragraph('', S['M_TD'])],
        [Paragraph('<b>Data</b>', S['M_TD']),
         Paragraph('Integraciones, fuente de verdad, gobernanza', S['M_TD']),
         Paragraph('', S['M_TD'])],
        [Paragraph('<b>IA</b>', S['M_TD']),
         Paragraph('Automatizaci\u00f3n, predicci\u00f3n, asistencia', S['M_TD']),
         Paragraph('', S['M_TD'])],
        [Paragraph('<b>Experience</b>', S['M_TD']),
         Paragraph('Lo que ve el estudiante/usuario', S['M_TD']),
         Paragraph('', S['M_TD'])],
    ]
    story.append(Spacer(1, 6))
    story.append(make_table(layers_data, [avail * 0.2, avail * 0.35, avail * 0.45], S))
    story.append(Spacer(1, 10))

    story.extend(field_block("Qu\u00e9 permanece (y por qu\u00e9):", S, 2))
    story.extend(field_block("Qu\u00e9 se integra (y c\u00f3mo):", S, 2))
    story.extend(field_block("Qu\u00e9 se elimina (y por qu\u00e9):", S, 2))

    story.append(hint(
        "Evaluamos <b>coherencia</b>, no complejidad t\u00e9cnica. "
        "Un diagrama simple que conecta 4 sistemas con flechas claras es mejor que un blueprint "
        "de 20 componentes que nadie entiende en 30 segundos.", S))

    # ----------------------------------------------------------
    # Slide 9 — Rol de la IA
    # ----------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("SLIDE 9", S['M_SlideNum']))
    story.append(Paragraph("Rol de la IA", S['M_SlideTitle']))
    story.append(hr(1.2))

    story.append(hint(
        "La IA debe resolver un <b>problema concreto y medible</b>, no ser un adorno. "
        "Record\u00e1 el caso Georgia State (M\u00f3dulo 4): la IA funcion\u00f3 porque estaba conectada "
        "a datos reales del estudiante. Un chatbot gen\u00e9rico no habr\u00eda logrado lo mismo. "
        "\u00bfQu\u00e9 datos de TU organizaci\u00f3n alimentar\u00edan el modelo?", S))

    story.extend(field_block("Problema concreto que resuelve la IA:", S, 3))
    story.extend(field_block("Tipo de intervenci\u00f3n (automatiza / predice / asiste):", S, 2))
    story.extend(field_block("Riesgo si la IA falla o tiene sesgo:", S, 2))
    story.extend(field_block("KPI impactado directamente:", S, 2))

    story.append(warning(
        "Prohibido: \u201cusar IA para mejorar la experiencia\u201d. "
        "Eso no dice nada. S\u00e9 espec\u00edfico: \u00bfqu\u00e9 hace, con qu\u00e9 datos, y c\u00f3mo sab\u00e9s que funcion\u00f3?", S))

    # ----------------------------------------------------------
    # Slide 10 — Impacto en Negocio
    # ----------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("SLIDE 10", S['M_SlideNum']))
    story.append(Paragraph("Impacto en Negocio", S['M_SlideTitle']))
    story.append(hr(1.2))

    story.append(hint(
        "Evaluamos <b>criterio econ\u00f3mico</b>, no exactitud contable. "
        "No necesit\u00e1s n\u00fameros exactos \u2014 necesit\u00e1s \u00f3rdenes de magnitud cre\u00edbles. "
        "Record\u00e1 la distinci\u00f3n del M\u00f3dulo 2: \u00bfes CAPEX o OPEX? \u00bfEs inversi\u00f3n o gasto recurrente? "
        "El CFO necesita entender el modelo econ\u00f3mico, no solo el beneficio.", S))

    story.extend(field_block("KPI impactado:", S, 2))
    story.extend(field_block("Orden de magnitud (\u2191 revenue / \u2193 costo / \u2191 conversi\u00f3n / \u2193 deserci\u00f3n):", S, 2))
    story.extend(field_block("Inversi\u00f3n relativa (qu\u00e9 requiere implementar esto):", S, 2))
    story.extend(field_block("Horizonte de retorno (cu\u00e1ndo se ve el impacto):", S, 2))

    # ----------------------------------------------------------
    # Slide 11 — Trade-offs
    # ----------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("SLIDE 11", S['M_SlideNum']))
    story.append(Paragraph("Trade-offs", S['M_SlideTitle']))
    story.append(hr(1.2))

    story.append(hint(
        "<b>Sin trade-offs, no hay estrategia.</b> Una propuesta donde todo es beneficio y nada "
        "se sacrifica no es cre\u00edble. Mostr\u00e1 qu\u00e9 elegiste postergar, qu\u00e9 aceptaste perder "
        "a corto plazo, y por qu\u00e9 esa renuncia vale la pena. Esto demuestra madurez ejecutiva.", S))

    story.append(Paragraph("<b>Decisiones dif\u00edciles tomadas:</b>", S['M_Body']))
    story.append(Spacer(1, 4))

    for i in range(4):
        story.extend(field_block(f"Trade-off {i+1}:", S, 2))

    story.append(Paragraph("<b>Ejemplos de trade-offs reales:</b>", S['M_Body']))
    story.append(bullet("Precisi\u00f3n vs. velocidad de implementaci\u00f3n", S))
    story.append(bullet("Personalizaci\u00f3n vs. simplicidad de mantenimiento", S))
    story.append(bullet("Innovaci\u00f3n radical vs. estabilizaci\u00f3n primero", S))
    story.append(bullet("Build interno vs. dependencia de proveedor", S))

    # ----------------------------------------------------------
    # Slide 12 — Roadmap 18 meses
    # ----------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("SLIDE 12", S['M_SlideNum']))
    story.append(Paragraph("Roadmap 18 meses", S['M_SlideTitle']))
    story.append(hr(1.2))

    story.append(hint(
        "El roadmap debe mostrar <b>l\u00f3gica de negocio</b>, no fases tecnol\u00f3gicas. "
        "H1 desbloquea, H2 redise\u00f1a, H3 escala. Cada horizonte debe tener un resultado concreto, "
        "no solo una actividad. \u201cIntegrar CRM\u201d es una actividad. "
        "\u201cReducir summer melt un 15%\u201d es un resultado.", S))

    story.append(Spacer(1, 8))
    story.append(Paragraph('<font color="#0891b2"><b>H1 (0\u20136 meses)</b></font> \u2014 '
                           'Desbloqueos / Quick Wins', S['M_SectionH2']))
    story.append(hint("Qu\u00e9 puedo hacer YA con lo que tengo. Demostr\u00e1 impacto r\u00e1pido para ganar credibilidad.", S))
    story.extend(field_block("Acci\u00f3n 1:", S, 2))
    story.extend(field_block("Acci\u00f3n 2:", S, 2))

    story.append(Spacer(1, 6))
    story.append(Paragraph('<font color="#0891b2"><b>H2 (6\u201312 meses)</b></font> \u2014 '
                           'Redise\u00f1o Estructural', S['M_SectionH2']))
    story.append(hint("Cambios que requieren inversi\u00f3n y esfuerzo sostenido. Aqu\u00ed va la transformaci\u00f3n real.", S))
    story.extend(field_block("Acci\u00f3n 1:", S, 2))
    story.extend(field_block("Acci\u00f3n 2:", S, 2))

    story.append(Spacer(1, 6))
    story.append(Paragraph('<font color="#0891b2"><b>H3 (12\u201318 meses)</b></font> \u2014 '
                           'Evoluci\u00f3n / Escala', S['M_SectionH2']))
    story.append(hint("Escalar lo que funcion\u00f3. Expandir a otras \u00e1reas. Medir ROI completo.", S))
    story.extend(field_block("Acci\u00f3n 1:", S, 2))
    story.extend(field_block("Acci\u00f3n 2:", S, 2))

    # ----------------------------------------------------------
    # Slide 13 — Riesgos Estratégicos
    # ----------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("SLIDE 13", S['M_SlideNum']))
    story.append(Paragraph("Riesgos Estrat\u00e9gicos", S['M_SlideTitle']))
    story.append(hr(1.2))

    story.append(hint(
        "Identific\u00e1 riesgos en las <b>4 dimensiones</b>: cultural, operativo, tecnol\u00f3gico y financiero. "
        "Record\u00e1 el Tri\u00e1ngulo de Transformaci\u00f3n (M\u00f3dulo 4): si ignor\u00e1s una dimensi\u00f3n, "
        "el sistema colapsa. La mitigaci\u00f3n debe ser <b>realista</b>, no \u201ccapacitar al equipo\u201d "
        "como respuesta gen\u00e9rica a todo.", S))

    risk_data = [
        [Paragraph('<b>Riesgo</b>', S['M_TH']),
         Paragraph('<b>Tipo</b>', S['M_TH']),
         Paragraph('<b>Mitigaci\u00f3n</b>', S['M_TH'])],
    ]
    for _ in range(4):
        risk_data.append([
            Paragraph('', S['M_TD']),
            Paragraph('', S['M_TD']),
            Paragraph('', S['M_TD']),
        ])
    story.append(Spacer(1, 8))
    story.append(make_table(risk_data, [avail * 0.35, avail * 0.25, avail * 0.40], S))

    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>Tipos de riesgo:</b>", S['M_Body']))
    story.append(bullet("<b>Cultural:</b> resistencia al cambio, falta de sponsor ejecutivo", S))
    story.append(bullet("<b>Operativo:</b> procesos que dependen de personas espec\u00edficas", S))
    story.append(bullet("<b>Tecnol\u00f3gico:</b> deuda t\u00e9cnica, dependencia de proveedor, integraciones fr\u00e1giles", S))
    story.append(bullet("<b>Financiero:</b> costos ocultos, ROI incierto, competencia por presupuesto", S))

    # ----------------------------------------------------------
    # Slide 14 — Qué NO voy a hacer
    # ----------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("SLIDE 14 (Opcional pero poderoso)", S['M_SlideNum']))
    story.append(Paragraph("Qu\u00e9 NO voy a hacer", S['M_SlideTitle']))
    story.append(hr(1.2))

    story.append(hint(
        "Esta slide <b>demuestra madurez ejecutiva</b>. Decir qu\u00e9 NO vas a hacer "
        "es tan estrat\u00e9gico como decir qu\u00e9 s\u00ed. Muestra que entend\u00e9s las limitaciones "
        "de recursos, tiempo y capacidad organizacional. El evaluador valorar\u00e1 que hayas "
        "descartado expl\u00edcitamente opciones tentadoras.", S))

    for i in range(4):
        story.extend(field_block(f"NO voy a:", S, 2))

    # ----------------------------------------------------------
    # Criterios de Evaluación (página de referencia)
    # ----------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("Referencia", S['M_SlideNum']))
    story.append(Paragraph("Criterios de Evaluaci\u00f3n", S['M_SlideTitle']))
    story.append(hr(1.2))

    story.append(Paragraph(
        "Us\u00e1 esta tabla como checklist antes de entregar. "
        "Cada criterio tiene un peso expl\u00edcito \u2014 asegur\u00e1 que tu propuesta "
        "sea fuerte en los que m\u00e1s pesan.", S['M_Body']))

    eval_data = [
        [Paragraph('<b>Criterio</b>', S['M_TH']),
         Paragraph('<b>Peso</b>', S['M_TH']),
         Paragraph('<b>Qu\u00e9 busca el evaluador</b>', S['M_TH'])],
        [Paragraph('Claridad del diagn\u00f3stico', S['M_TD']),
         Paragraph('<b>20%</b>', S['M_TD']),
         Paragraph('Problema espec\u00edfico con evidencia, causa ra\u00edz identificada', S['M_TD'])],
        [Paragraph('Decisi\u00f3n estrat\u00e9gica', S['M_TD']),
         Paragraph('<b>15%</b>', S['M_TD']),
         Paragraph('Renuncia expl\u00edcita, foco claro, l\u00f3gica defendible', S['M_TD'])],
        [Paragraph('Coherencia estrat\u00e9gica', S['M_TD']),
         Paragraph('<b>15%</b>', S['M_TD']),
         Paragraph('Acciones conectadas causalmente, principio rector aplicado', S['M_TD'])],
        [Paragraph('Redise\u00f1o real de proceso', S['M_TD']),
         Paragraph('<b>15%</b>', S['M_TD']),
         Paragraph('AS IS honesto, TO BE con cambios concretos y medibles', S['M_TD'])],
        [Paragraph('Comprensi\u00f3n arquitect\u00f3nica', S['M_TD']),
         Paragraph('<b>10%</b>', S['M_TD']),
         Paragraph('Sistemas, datos e integraciones coherentes', S['M_TD'])],
        [Paragraph('Uso inteligente de IA', S['M_TD']),
         Paragraph('<b>10%</b>', S['M_TD']),
         Paragraph('Problema concreto, tipo de intervenci\u00f3n, riesgo considerado', S['M_TD'])],
        [Paragraph('Impacto econ\u00f3mico cre\u00edble', S['M_TD']),
         Paragraph('<b>10%</b>', S['M_TD']),
         Paragraph('\u00d3rdenes de magnitud realistas, horizonte de retorno', S['M_TD'])],
        [Paragraph('Integraci\u00f3n Cultura\u2013Proceso\u2013Tech', S['M_TD']),
         Paragraph('<b>5%</b>', S['M_TD']),
         Paragraph('Tri\u00e1ngulo equilibrado, no solo tecnolog\u00eda', S['M_TD'])],
    ]
    story.append(Spacer(1, 8))
    story.append(make_table(eval_data, [avail * 0.25, avail * 0.1, avail * 0.65], S))

    # ----------------------------------------------------------
    # Preguntas de la defensa oral
    # ----------------------------------------------------------
    story.append(Spacer(1, 20))
    story.append(Paragraph("Prepar\u00e1 tu Defensa Oral", S['M_SectionH2']))
    story.append(hr(0.8))

    story.append(Paragraph(
        "El comit\u00e9 directivo har\u00e1 preguntas dif\u00edciles en 3 minutos. "
        "Prepar\u00e1 respuestas cortas y directas para estas:", S['M_Body']))

    questions = [
        "\u00bfPor qu\u00e9 esto y no otra cosa?",
        "\u00bfD\u00f3nde est\u00e1 el impacto econ\u00f3mico?",
        "\u00bfQu\u00e9 pasa si la cultura no cambia?",
        "\u00bfCu\u00e1l es el mayor riesgo real?",
        "\u00bfQu\u00e9 sacrificaste?",
        "\u00bfQu\u00e9 har\u00eda fracasar esta estrategia?",
    ]
    for q in questions:
        story.append(bullet(f"<b>{q}</b>", S))

    story.append(Spacer(1, 14))
    story.append(warning(
        "<b>Errores t\u00edpicos a evitar:</b> Lista de iniciativas sin estrategia \u00b7 "
        "Diagn\u00f3stico gen\u00e9rico \u00b7 IA como adorno \u00b7 Arquitectura sobre-ingenierizada \u00b7 "
        "Roadmap tecnol\u00f3gico sin l\u00f3gica de negocio \u00b7 Impacto econ\u00f3mico m\u00e1gico", S))


# ============================================================
# MAIN
# ============================================================
def main():
    S = make_styles()

    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)

    story = []
    story.append(Spacer(1, 0.1))  # trigger cover
    story.append(PageBreak())

    build_content(story, S)

    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=0.75 * inch,
        bottomMargin=0.85 * inch,
    )

    doc.build(story,
              onFirstPage=build_cover,
              onLaterPages=page_header_footer)

    print(f"  \u2713  {os.path.relpath(OUTPUT, BASE_DIR)}")


if __name__ == '__main__':
    main()
