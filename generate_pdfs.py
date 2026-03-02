#!/usr/bin/env python3
"""
Generador de PDFs por módulo desde Markdown
Curso: Estrategia Tecnológica + Mindset Digital
Lee los archivos .md de contenido/ y genera un PDF por módulo en docs/pdfs/
"""

import os
import re
from dataclasses import dataclass, field
from typing import List, Optional

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, HRFlowable, KeepTogether, Preformatted
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

# ============================================================
# DESIGN SYSTEM
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
WHITE = white

PAGE_W, PAGE_H = A4
MARGIN = 0.85 * inch

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# MODULE REGISTRY
# ============================================================
MODULES = [
    {
        "number": 0,
        "label": "MÓDULO 00",
        "accent": DARK_NAVY,
        "file": "contenido/modulo-00/modulo-00-intro.md",
        "title": "Introducción",
        "subtitle": "Estrategia Tecnológica + Mindset Digital",
        "output": "docs/pdfs/modulo-00-introduccion.pdf",
    },
    {
        "number": 1,
        "label": "MÓDULO 01",
        "accent": CYAN,
        "file": "contenido/modulo-01/modulo-01-hello-world.md",
        "title": "Hello World: Tecnología como ventaja competitiva",
        "subtitle": "El negocio educativo es digital-first",
        "output": "docs/pdfs/modulo-01-hello-world.pdf",
    },
    {
        "number": 2,
        "label": "MÓDULO 02",
        "accent": PURPLE,
        "file": "contenido/modulo-02/modulo-02-estrategia-tecnologica.md",
        "title": "Estrategia Tecnológica del negocio",
        "subtitle": "Decidir sobre tecnología con criterio ejecutivo",
        "output": "docs/pdfs/modulo-02-estrategia-tecnologica.pdf",
    },
    {
        "number": 3,
        "label": "MÓDULO 03",
        "accent": AMBER,
        "file": "contenido/modulo-03/modulo-03-arquitectura-it.md",
        "title": "Arquitectura IT Educativa",
        "subtitle": "Cómo funciona una institución moderna por dentro",
        "output": "docs/pdfs/modulo-03-arquitectura-it.pdf",
    },
    {
        "number": 4,
        "label": "MÓDULO 04",
        "accent": MAGENTA,
        "file": "contenido/modulo-04/modulo-04-transformacion-digital-ia.md",
        "title": "Transformación Digital e IA",
        "subtitle": "Cómo transformar sin romper la organización",
        "output": "docs/pdfs/modulo-04-transformacion-digital-ia.pdf",
    },
    {
        "number": 5,
        "label": "MÓDULO 05",
        "accent": EMERALD,
        "file": "contenido/modulo-05/modulo-05-mindset-digital.md",
        "title": "Mindset Digital",
        "subtitle": "El sistema operativo del liderazgo",
        "output": "docs/pdfs/modulo-05-mindset-digital.pdf",
    },
    {
        "number": 6,
        "label": "MÓDULO 06",
        "accent": CYAN,
        "file": "contenido/modulo-06/modulo-06-ia-educacion.md",
        "title": "IA y el Futuro de la Educación",
        "subtitle": "La IA no es un proyecto. Es una decisión estratégica.",
        "output": "docs/pdfs/modulo-06-ia-educacion.pdf",
    },
    {
        "number": 7,
        "label": "MÓDULO 07",
        "accent": DARK_NAVY,
        "file": "contenido/modulo-07/modulo-07-cierre-challenge.md",
        "title": "Cierre y Lanzamiento del Challenge",
        "subtitle": "Arquitectos del Futuro",
        "output": "docs/pdfs/modulo-07-cierre-challenge.pdf",
    },
]


# ============================================================
# STYLES
# ============================================================
def make_styles(accent):
    S = getSampleStyleSheet()

    S.add(ParagraphStyle('M_ModuleTag',
        fontSize=10, leading=14, textColor=accent,
        fontName='Helvetica-Bold', spaceAfter=4, spaceBefore=0))

    S.add(ParagraphStyle('M_CoverTitle',
        fontSize=28, leading=34, textColor=TEXT_DARK,
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

    S.add(ParagraphStyle('M_Quote',
        fontSize=12, leading=19, textColor=accent,
        fontName='Helvetica-Oblique', spaceBefore=12, spaceAfter=12,
        leftIndent=24, rightIndent=24, alignment=TA_LEFT))

    S.add(ParagraphStyle('M_Bullet',
        fontSize=10.5, leading=15, textColor=TEXT_BODY,
        fontName='Helvetica', spaceAfter=5, leftIndent=18,
        firstLineIndent=-14))

    S.add(ParagraphStyle('M_NumberedItem',
        fontSize=10.5, leading=15, textColor=TEXT_BODY,
        fontName='Helvetica', spaceAfter=5, leftIndent=22,
        firstLineIndent=-18))

    S.add(ParagraphStyle('M_TH',
        fontSize=9.5, leading=13, textColor=WHITE,
        fontName='Helvetica-Bold', alignment=TA_LEFT))

    S.add(ParagraphStyle('M_TD',
        fontSize=9, leading=13, textColor=TEXT_BODY,
        fontName='Helvetica', alignment=TA_LEFT))

    S.add(ParagraphStyle('M_Code',
        fontSize=8.5, leading=12, textColor=TEXT_DARK,
        fontName='Courier', spaceAfter=8, spaceBefore=8,
        leftIndent=12, rightIndent=12, backColor=CARD_BG))

    S.add(ParagraphStyle('M_Footer',
        fontSize=8, leading=11, textColor=TEXT_MUTED,
        fontName='Helvetica', alignment=TA_CENTER))

    return S


# ============================================================
# MARKDOWN PARSER
# ============================================================
@dataclass
class Block:
    type: str  # h1, h2, h3, h4, paragraph, table, blockquote,
               # bullet_list, numbered_list, code_block, hr
    content: str = ""
    children: List[str] = field(default_factory=list)
    rows: List[List[str]] = field(default_factory=list)


def tokenize(filepath: str) -> List[Block]:
    """Parse a markdown file into a list of Block tokens."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    blocks: List[Block] = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # Skip empty lines
        if not stripped:
            i += 1
            continue

        # HTML comments — skip
        if stripped.startswith('<!--'):
            while i < n and '-->' not in lines[i]:
                i += 1
            i += 1
            continue

        # HTML img tags — skip
        if stripped.startswith('<img'):
            i += 1
            continue

        # Markdown images — skip
        if re.match(r'^!\[', stripped):
            i += 1
            continue

        # Navigation links at end of file
        if stripped.startswith('*Siguiente:') or stripped.startswith('*Anterior:'):
            i += 1
            continue

        # Raw URLs — skip
        if re.match(r'^https?://', stripped):
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^-{3,}\s*$', stripped) or re.match(r'^\*{3,}\s*$', stripped):
            blocks.append(Block(type='hr'))
            i += 1
            continue

        # Headings
        m = re.match(r'^(#{1,4})\s+(.*)', stripped)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            # Remove leading emoji characters
            text = re.sub(r'^[💡🔥⏳☕🍽️]+\s*', '', text)
            # Remove bold markers wrapping the whole heading
            text = re.sub(r'^\*\*(.*)\*\*$', r'\1', text)
            blocks.append(Block(type=f'h{level}', content=text))
            i += 1
            continue

        # Code block
        if stripped.startswith('```'):
            code_lines = []
            i += 1
            while i < n and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i].rstrip())
                i += 1
            i += 1  # skip closing ```
            blocks.append(Block(type='code_block', content='\n'.join(code_lines)))
            continue

        # Blockquote
        if stripped.startswith('>'):
            quote_lines = []
            while i < n and lines[i].strip().startswith('>'):
                text = re.sub(r'^>\s*', '', lines[i].strip())
                # Remove leading emoji
                text = re.sub(r'^[💡🔥]+\s*', '', text)
                if text:
                    quote_lines.append(text)
                i += 1
            blocks.append(Block(type='blockquote', content=' '.join(quote_lines)))
            continue

        # Table
        if stripped.startswith('|'):
            table_rows = []
            while i < n and lines[i].strip().startswith('|'):
                row_text = lines[i].strip()
                # Skip separator rows
                if re.match(r'^\|[\s\-:|]+\|$', row_text):
                    i += 1
                    continue
                cells = [c.strip() for c in row_text.split('|')[1:-1]]
                table_rows.append(cells)
                i += 1
            if table_rows:
                blocks.append(Block(type='table', rows=table_rows))
            continue

        # Bullet list
        if re.match(r'^[-*•]\s+', stripped):
            items = []
            while i < n and re.match(r'^\s*[-*•]\s+', lines[i]):
                text = re.sub(r'^\s*[-*•]\s+', '', lines[i].strip())
                items.append(text)
                i += 1
            blocks.append(Block(type='bullet_list', children=items))
            continue

        # Numbered list
        if re.match(r'^\d+[\.\)]\s+', stripped):
            items = []
            while i < n and re.match(r'^\s*\d+[\.\)]\s+', lines[i].strip()):
                text = re.sub(r'^\s*\d+[\.\)]\s+', '', lines[i].strip())
                items.append(text)
                i += 1
            blocks.append(Block(type='numbered_list', children=items))
            continue

        # Unordered list with * at start (like "* item")
        if re.match(r'^\*\s+[^*]', stripped):
            items = []
            while i < n and re.match(r'^\*\s+', lines[i].strip()):
                text = re.sub(r'^\*\s+', '', lines[i].strip())
                items.append(text)
                i += 1
            blocks.append(Block(type='bullet_list', children=items))
            continue

        # Paragraph — accumulate lines
        para_lines = []
        while i < n:
            s = lines[i].strip()
            if not s:
                break
            if s.startswith('#') or s.startswith('>') or s.startswith('|'):
                break
            if s.startswith('```') or s.startswith('<!--') or s.startswith('<img'):
                break
            if re.match(r'^-{3,}\s*$', s) or re.match(r'^\*{3,}\s*$', s):
                break
            if re.match(r'^[-*•]\s+', s) and not re.match(r'^\*\*', s):
                break
            if re.match(r'^\d+[\.\)]\s+', s):
                break
            if s.startswith('*Siguiente:') or s.startswith('*Anterior:'):
                break
            if re.match(r'^https?://', s):
                break
            if s.startswith('!['):
                break
            para_lines.append(s)
            i += 1

        if para_lines:
            text = ' '.join(para_lines)
            # Skip lines that are just "Para profundizar:" links
            blocks.append(Block(type='paragraph', content=text))

    return blocks


def format_inline(text: str) -> str:
    """Convert markdown inline formatting to ReportLab XML tags."""
    # Escape XML entities first (but preserve existing tags)
    text = text.replace('&', '&amp;')
    # Don't escape < and > that are part of markdown
    # Handle bold: **text**
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Handle italic: *text* (but not bullet points)
    text = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<i>\1</i>', text)
    # Handle links: [text](url) → underlined text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'<u>\1</u>', text)
    # Handle inline code: `text`
    text = re.sub(r'`([^`]+)`', r'<font name="Courier" size="9">\1</font>', text)
    # Handle em dash
    text = text.replace(' — ', ' \u2014 ')
    text = text.replace('—', '\u2014')
    return text


# ============================================================
# FLOWABLE BUILDERS
# ============================================================
def block_to_flowables(block: Block, S, accent) -> List:
    """Convert a Block into ReportLab flowables."""
    elements = []
    accent_hex = accent.hexval() if hasattr(accent, 'hexval') else '#0891b2'

    if block.type == 'h1':
        # H1 is used for cover page title — skip in body
        return []

    elif block.type == 'h2':
        # Major section — page break before
        elements.append(PageBreak())
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(format_inline(block.content), S['M_SectionH1']))
        elements.append(HRFlowable(width='100%', thickness=1.2,
                                   color=accent, spaceAfter=10, spaceBefore=4))

    elif block.type == 'h3':
        elements.append(Spacer(1, 6))
        elements.append(Paragraph(format_inline(block.content), S['M_SectionH2']))

    elif block.type == 'h4':
        elements.append(Spacer(1, 4))
        elements.append(Paragraph(format_inline(block.content), S['M_SectionH3']))

    elif block.type == 'paragraph':
        elements.append(Paragraph(format_inline(block.content), S['M_Body']))

    elif block.type == 'blockquote':
        elements.append(Spacer(1, 4))
        elements.append(Paragraph(format_inline(block.content), S['M_Quote']))
        elements.append(Spacer(1, 4))

    elif block.type == 'bullet_list':
        for item in block.children:
            text = f'<font color="{accent_hex}">\u25b8</font>  {format_inline(item)}'
            elements.append(Paragraph(text, S['M_Bullet']))

    elif block.type == 'numbered_list':
        for idx, item in enumerate(block.children, 1):
            text = f'<b>{idx}.</b>  {format_inline(item)}'
            elements.append(Paragraph(text, S['M_NumberedItem']))

    elif block.type == 'table':
        elements.extend(build_table(block.rows, S, accent))

    elif block.type == 'code_block':
        elements.append(Spacer(1, 6))
        elements.append(Preformatted(block.content,
                                     S['M_Code'],
                                     maxLineLength=80))
        elements.append(Spacer(1, 6))

    elif block.type == 'hr':
        elements.append(HRFlowable(width='100%', thickness=0.8,
                                   color=accent, spaceAfter=8, spaceBefore=8))

    return elements


def build_table(rows: List[List[str]], S, accent) -> List:
    """Build a ReportLab Table from parsed rows."""
    if not rows:
        return []

    # Convert cells to Paragraphs
    header = rows[0]
    data_rows = rows[1:] if len(rows) > 1 else []

    # Calculate column widths
    num_cols = len(header)
    available_width = PAGE_W - 2 * MARGIN - 4
    col_width = available_width / num_cols

    # Build table data
    table_data = []
    # Header
    header_cells = [Paragraph(format_inline(c), S['M_TH']) for c in header]
    table_data.append(header_cells)

    # Data rows
    for row in data_rows:
        # Pad row if needed
        while len(row) < num_cols:
            row.append('')
        cells = [Paragraph(format_inline(c), S['M_TD']) for c in row[:num_cols]]
        table_data.append(cells)

    col_widths = [col_width] * num_cols
    table = Table(table_data, colWidths=col_widths, repeatRows=1)

    styles = [
        ('BACKGROUND', (0, 0), (-1, 0), accent),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9.5),
        ('ALIGN', (0, 0), (-1, 0), 'LEFT'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [LIGHT_BG, CARD_BG]),
    ]
    table.setStyle(TableStyle(styles))

    return [Spacer(1, 8), KeepTogether([table]), Spacer(1, 8)]


# ============================================================
# COVER PAGE
# ============================================================
def _wrap_text(text, font_size, max_width):
    """Simple word-wrap for canvas drawing."""
    from reportlab.pdfbase.pdfmetrics import stringWidth
    words = text.split()
    lines = []
    current = ""
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


def build_cover(canvas_obj, doc, mod, accent):
    """Draw cover page."""
    canvas_obj.saveState()
    w, h = A4

    # Left accent band
    canvas_obj.setFillColor(accent)
    canvas_obj.rect(0, 0, 0.35 * inch, h, fill=1, stroke=0)

    # Top accent strip
    canvas_obj.setFillColor(accent)
    canvas_obj.rect(0, h - 0.12 * inch, w, 0.12 * inch, fill=1, stroke=0)

    # Module label
    canvas_obj.setFont('Helvetica-Bold', 9)
    canvas_obj.setFillColor(accent)
    canvas_obj.drawString(MARGIN, h - 1.1 * inch, mod['label'])

    # Large watermark number
    canvas_obj.setFont('Helvetica-Bold', 120)
    canvas_obj.setFillColor(HexColor('#f1f5f9'))
    num_str = str(mod['number']).zfill(2)
    canvas_obj.drawRightString(w - MARGIN + 0.2 * inch, h - 3.8 * inch, num_str)

    # Title
    canvas_obj.setFont('Helvetica-Bold', 28)
    canvas_obj.setFillColor(TEXT_DARK)
    title_lines = _wrap_text(mod['title'], 28, w - 2 * MARGIN - 0.2 * inch)
    y = h - 1.6 * inch
    for line in title_lines:
        canvas_obj.drawString(MARGIN, y, line)
        y -= 34

    # Subtitle
    canvas_obj.setFont('Helvetica', 15)
    canvas_obj.setFillColor(accent)
    sub_lines = _wrap_text(mod['subtitle'], 15, w - 2 * MARGIN - 0.2 * inch)
    y -= 10
    for line in sub_lines:
        canvas_obj.drawString(MARGIN, y, line)
        y -= 22

    # Divider line
    y -= 16
    canvas_obj.setStrokeColor(BORDER)
    canvas_obj.setLineWidth(0.6)
    canvas_obj.line(MARGIN, y, w - MARGIN, y)

    # Course info at bottom
    canvas_obj.setFillColor(DARK_NAVY)
    canvas_obj.rect(0, 0, w, 0.7 * inch, fill=1, stroke=0)

    canvas_obj.setFont('Helvetica', 9)
    canvas_obj.setFillColor(HexColor('#94a3b8'))
    canvas_obj.drawString(MARGIN, 0.35 * inch,
                          "Estrategia Tecnológica + Mindset Digital")
    canvas_obj.drawRightString(w - MARGIN, 0.35 * inch,
                               "Programa Ejecutivo")

    canvas_obj.restoreState()


def page_header_footer(canvas_obj, doc, mod, accent):
    """Draw header and footer on content pages."""
    canvas_obj.saveState()
    w, h = A4

    # Header bar
    canvas_obj.setFillColor(accent)
    canvas_obj.rect(MARGIN, h - 0.55 * inch, w - 2 * MARGIN, 2.5, fill=1, stroke=0)

    # Header text
    canvas_obj.setFont('Helvetica-Bold', 8)
    canvas_obj.setFillColor(accent)
    canvas_obj.drawString(MARGIN, h - 0.45 * inch,
                          f"{mod['label']}  ·  {mod['title']}")

    # Footer
    page_num = canvas_obj.getPageNumber()
    canvas_obj.setFont('Helvetica', 8)
    canvas_obj.setFillColor(TEXT_MUTED)
    canvas_obj.drawCentredString(w / 2, 0.45 * inch,
                                 f"Estrategia Tecnológica + Mindset Digital  ·  Página {page_num}")

    # Footer line
    canvas_obj.setStrokeColor(BORDER)
    canvas_obj.setLineWidth(0.4)
    canvas_obj.line(MARGIN, 0.6 * inch, w - MARGIN, 0.6 * inch)

    canvas_obj.restoreState()


# ============================================================
# PDF GENERATION
# ============================================================
def generate_module_pdf(mod):
    """Generate a single module PDF."""
    accent = mod['accent']
    S = make_styles(accent)

    filepath = os.path.join(BASE_DIR, mod['file'])
    output_path = os.path.join(BASE_DIR, mod['output'])

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Parse markdown
    blocks = tokenize(filepath)

    # Build flowables
    elements = []

    # Cover page: tiny spacer triggers onFirstPage, then page break
    elements.append(Spacer(1, 0.1))
    elements.append(PageBreak())

    # Track if we've seen the first H2 (to avoid extra page break)
    first_h2 = True

    for block in blocks:
        if block.type == 'h2' and first_h2:
            # First section — already on a new page from cover break
            first_h2 = False
            elements.append(Spacer(1, 12))
            elements.append(Paragraph(format_inline(block.content), S['M_SectionH1']))
            elements.append(HRFlowable(width='100%', thickness=1.2,
                                       color=accent, spaceAfter=10, spaceBefore=4))
            continue

        flowables = block_to_flowables(block, S, accent)
        elements.extend(flowables)

    # Build PDF
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=0.75 * inch,
        bottomMargin=0.85 * inch,
    )

    def on_first_page(canvas_obj, doc_obj):
        build_cover(canvas_obj, doc_obj, mod, accent)

    def on_later_pages(canvas_obj, doc_obj):
        page_header_footer(canvas_obj, doc_obj, mod, accent)

    doc.build(elements, onFirstPage=on_first_page, onLaterPages=on_later_pages)
    return output_path


# ============================================================
# MAIN
# ============================================================
def main():
    print(f"Generando PDFs para {len(MODULES)} módulos...\n")

    for mod in MODULES:
        filepath = os.path.join(BASE_DIR, mod['file'])
        if not os.path.exists(filepath):
            print(f"  SKIP  {mod['file']} (no encontrado)")
            continue
        try:
            out = generate_module_pdf(mod)
            print(f"  ✓  {mod['output']}")
        except Exception as e:
            print(f"  ✗  {mod['output']} — Error: {e}")

    print(f"\nListo. PDFs generados en docs/pdfs/")


if __name__ == '__main__':
    main()
