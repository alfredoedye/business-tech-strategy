#!/usr/bin/env python3
"""
Generador de PDF profesional para el curso de Estrategia Tecnológica + Mindset Digital
Diseño: Tema Neon Cyber con fondo oscuro y acentos cyan/magenta
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, ListFlowable, ListItem
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# ============================================
# THEME COLORS
# ============================================
BG_DARK = HexColor('#0d0d12')
BG_SURFACE = HexColor('#16161d')
BG_CARD = HexColor('#1c1c26')
TEXT_PRIMARY = HexColor('#e8e6e3')
TEXT_SECONDARY = HexColor('#9090a0')
MUTED = HexColor('#6b6b78')
CYAN = HexColor('#00e5ff')
MAGENTA = HexColor('#ff0080')
PURPLE = HexColor('#8b5cf6')

# For PDF (dark backgrounds don't work well), we'll use a light theme with dark accents
BG_LIGHT = HexColor('#ffffff')
TEXT_DARK = HexColor('#1a1a2e')
TEXT_BODY = HexColor('#2d2d44')
ACCENT_CYAN = HexColor('#0891b2')
ACCENT_MAGENTA = HexColor('#be185d')
ACCENT_PURPLE = HexColor('#7c3aed')
BORDER_LIGHT = HexColor('#e5e7eb')

# ============================================
# CUSTOM STYLES
# ============================================
def get_custom_styles():
    styles = getSampleStyleSheet()

    # Title style
    styles.add(ParagraphStyle(
        name='CoverTitle',
        fontSize=32,
        leading=38,
        textColor=TEXT_DARK,
        alignment=TA_CENTER,
        spaceAfter=20,
        fontName='Helvetica-Bold'
    ))

    styles.add(ParagraphStyle(
        name='CoverSubtitle',
        fontSize=16,
        leading=20,
        textColor=ACCENT_CYAN,
        alignment=TA_CENTER,
        spaceAfter=10,
        fontName='Helvetica'
    ))

    styles.add(ParagraphStyle(
        name='ModuleTitle',
        fontSize=24,
        leading=30,
        textColor=TEXT_DARK,
        alignment=TA_LEFT,
        spaceBefore=30,
        spaceAfter=20,
        fontName='Helvetica-Bold'
    ))

    styles.add(ParagraphStyle(
        name='SectionHeader',
        fontSize=14,
        leading=18,
        textColor=ACCENT_CYAN,
        alignment=TA_LEFT,
        spaceBefore=20,
        spaceAfter=10,
        fontName='Helvetica-Bold'
    ))

    styles.add(ParagraphStyle(
        name='CustomBody',
        fontSize=11,
        leading=16,
        textColor=TEXT_BODY,
        alignment=TA_JUSTIFY,
        spaceAfter=10,
        fontName='Helvetica'
    ))

    styles.add(ParagraphStyle(
        name='QuoteText',
        fontSize=12,
        leading=18,
        textColor=ACCENT_PURPLE,
        alignment=TA_CENTER,
        spaceBefore=15,
        spaceAfter=15,
        fontName='Helvetica-Oblique',
        leftIndent=30,
        rightIndent=30
    ))

    styles.add(ParagraphStyle(
        name='BulletText',
        fontSize=11,
        leading=15,
        textColor=TEXT_BODY,
        alignment=TA_LEFT,
        spaceAfter=6,
        fontName='Helvetica',
        leftIndent=20,
        bulletIndent=10
    ))

    styles.add(ParagraphStyle(
        name='TableHeader',
        fontSize=10,
        leading=14,
        textColor=white,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    ))

    styles.add(ParagraphStyle(
        name='TableCell',
        fontSize=9,
        leading=12,
        textColor=TEXT_BODY,
        alignment=TA_LEFT,
        fontName='Helvetica'
    ))

    styles.add(ParagraphStyle(
        name='TOCEntry',
        fontSize=12,
        leading=20,
        textColor=TEXT_BODY,
        alignment=TA_LEFT,
        fontName='Helvetica',
        leftIndent=20
    ))

    styles.add(ParagraphStyle(
        name='PageNumber',
        fontSize=9,
        textColor=MUTED,
        alignment=TA_CENTER,
        fontName='Helvetica'
    ))

    return styles


def create_cover_page(story, styles):
    """Create the cover page"""
    story.append(Spacer(1, 2*inch))

    # Decorative line
    story.append(Paragraph("━" * 40, ParagraphStyle(
        name='DecorLine',
        fontSize=12,
        textColor=ACCENT_CYAN,
        alignment=TA_CENTER
    )))
    story.append(Spacer(1, 0.5*inch))

    # Main title
    story.append(Paragraph("Estrategia Tecnológica", styles['CoverTitle']))
    story.append(Paragraph("+ Mindset Digital", styles['CoverTitle']))

    story.append(Spacer(1, 0.3*inch))

    # Subtitle
    story.append(Paragraph("Módulo V — Manual del Participante", styles['CoverSubtitle']))

    story.append(Spacer(1, 0.5*inch))

    # Decorative line
    story.append(Paragraph("━" * 40, ParagraphStyle(
        name='DecorLine2',
        fontSize=12,
        textColor=ACCENT_MAGENTA,
        alignment=TA_CENTER
    )))

    story.append(Spacer(1, 2*inch))

    # Program info
    story.append(Paragraph(
        "Programa Ejecutivo de Estrategia Digital<br/>para Líderes del Sector Educativo",
        ParagraphStyle(
            name='ProgramInfo',
            fontSize=12,
            leading=18,
            textColor=TEXT_BODY,
            alignment=TA_CENTER,
            fontName='Helvetica'
        )
    ))

    story.append(PageBreak())


def create_toc(story, styles):
    """Create table of contents"""
    story.append(Paragraph("Contenido", styles['ModuleTitle']))
    story.append(Spacer(1, 0.3*inch))

    toc_items = [
        ("01", "Hello World: Tecnología como ventaja competitiva", "3"),
        ("02", "Estrategia Tecnológica del negocio", "6"),
        ("03", "Arquitectura IT Educativa", "10"),
        ("04", "Transformación Digital e IA", "14"),
        ("05", "Mindset Digital: El sistema operativo del liderazgo", "18"),
    ]

    for num, title, page in toc_items:
        toc_text = f'<font color="{ACCENT_CYAN.hexval()}">{num}</font>&nbsp;&nbsp;&nbsp;{title}'
        story.append(Paragraph(toc_text, styles['TOCEntry']))
        story.append(Spacer(1, 0.1*inch))

    story.append(PageBreak())


def create_module_1(story, styles):
    """Module 1: Hello World"""
    # Module header
    story.append(Paragraph(
        '<font color="#0891b2">MÓDULO 01</font>',
        ParagraphStyle(name='ModNum', fontSize=12, textColor=ACCENT_CYAN, spaceAfter=5)
    ))
    story.append(Paragraph("Hello World", styles['ModuleTitle']))
    story.append(Paragraph("Tecnología como ventaja competitiva", styles['CoverSubtitle']))

    # Guiding question
    story.append(Paragraph(
        "« ¿Por qué la tecnología dejó de ser un área de soporte y pasó a ser parte del core del negocio? »",
        styles['QuoteText']
    ))

    # Objective
    story.append(Paragraph("Objetivo del módulo", styles['SectionHeader']))
    story.append(Paragraph(
        "Comprender por qué la tecnología dejó de ser un área de soporte y se convirtió en una pieza central del negocio educativo. Al terminar, cada líder debe poder identificar en qué nivel se encuentra su organización y qué implica esa posición para competir.",
        styles['CustomBody']
    ))

    # Key concept 1
    story.append(Paragraph("Software Is Eating The World", styles['SectionHeader']))
    story.append(Paragraph(
        "Las empresas más valiosas del mundo no 'usan' tecnología — son empresas de tecnología que operan en una industria específica. En educación: la tecnología ES la experiencia del estudiante.",
        styles['CustomBody']
    ))

    # Comparison table
    table_data = [
        [Paragraph('<b>Ayer</b>', styles['TableCell']),
         Paragraph('<b>Hoy</b>', styles['TableCell'])],
        [Paragraph('La tecnología era el campus virtual', styles['TableCell']),
         Paragraph('La tecnología ES la experiencia del estudiante', styles['TableCell'])],
        [Paragraph('IT era un área de soporte', styles['TableCell']),
         Paragraph('IT habilita (o limita) el crecimiento', styles['TableCell'])],
        [Paragraph('Invertir en tech era un gasto', styles['TableCell']),
         Paragraph('No invertir en tech es un riesgo estratégico', styles['TableCell'])],
    ]

    table = Table(table_data, colWidths=[2.5*inch, 3*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), ACCENT_CYAN),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), HexColor('#f8fafc')),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_LIGHT),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(table)
    story.append(Spacer(1, 0.2*inch))

    # Three levels
    story.append(Paragraph("Los tres niveles de relación con la tecnología", styles['SectionHeader']))

    levels_data = [
        [Paragraph('<b>Nivel</b>', styles['TableCell']),
         Paragraph('<b>Descripción</b>', styles['TableCell']),
         Paragraph('<b>Ejemplo</b>', styles['TableCell'])],
        [Paragraph('<font color="#0891b2"><b>1. Usar</b></font>', styles['TableCell']),
         Paragraph('Comprar herramientas y usarlas tal como vienen', styles['TableCell']),
         Paragraph('Adoptar Zoom para clases virtuales', styles['TableCell'])],
        [Paragraph('<font color="#7c3aed"><b>2. Operar</b></font>', styles['TableCell']),
         Paragraph('Integrar herramientas, personalizar flujos, conectar datos', styles['TableCell']),
         Paragraph('Conectar LMS con CRM para detectar deserción', styles['TableCell'])],
        [Paragraph('<font color="#be185d"><b>3. Diseñar</b></font>', styles['TableCell']),
         Paragraph('El modelo de negocio nace de las capacidades tecnológicas', styles['TableCell']),
         Paragraph('Platzi: modelo nativo digital desde el día uno', styles['TableCell'])],
    ]

    table2 = Table(levels_data, colWidths=[1.2*inch, 2.3*inch, 2*inch])
    table2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), TEXT_DARK),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 1), (-1, -1), HexColor('#f8fafc')),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_LIGHT),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(table2)

    # CEO decisions
    story.append(Paragraph("El rol del CEO en las decisiones tecnológicas", styles['SectionHeader']))
    story.append(Paragraph(
        "Hay decisiones tecnológicas que un CEO no puede delegar porque SON decisiones de negocio:",
        styles['CustomBody']
    ))

    bullets = [
        "¿Construimos o compramos nuestra plataforma core?",
        "¿Qué datos son estratégicos y quién los gobierna?",
        "¿Cuánto invertimos en tecnología vs. otras áreas?",
        "¿Cómo integramos IA en nuestra operación?"
    ]

    for bullet in bullets:
        story.append(Paragraph(f"• {bullet}", styles['BulletText']))

    story.append(PageBreak())


def create_module_2(story, styles):
    """Module 2: Estrategia Tecnológica"""
    story.append(Paragraph(
        '<font color="#0891b2">MÓDULO 02</font>',
        ParagraphStyle(name='ModNum2', fontSize=12, textColor=ACCENT_CYAN, spaceAfter=5)
    ))
    story.append(Paragraph("Estrategia Tecnológica", styles['ModuleTitle']))
    story.append(Paragraph("Decisiones que definen el futuro", styles['CoverSubtitle']))

    story.append(Paragraph(
        "« ¿Qué decisiones tecnológicas son estratégicas y cuáles son tácticas? »",
        styles['QuoteText']
    ))

    story.append(Paragraph("Objetivo del módulo", styles['SectionHeader']))
    story.append(Paragraph(
        "Adquirir el vocabulario, los criterios y los frameworks necesarios para participar activamente en la definición de la estrategia tecnológica. No se trata de aprender tecnología, sino de aprender a DECIDIR sobre tecnología.",
        styles['CustomBody']
    ))

    # Decision 1: Build vs Buy
    story.append(Paragraph("Decisión 1: Build vs Buy", styles['SectionHeader']))

    bb_data = [
        [Paragraph('<b></b>', styles['TableCell']),
         Paragraph('<b>Build (Construir)</b>', styles['TableCell']),
         Paragraph('<b>Buy (Comprar)</b>', styles['TableCell'])],
        [Paragraph('<b>Ventaja</b>', styles['TableCell']),
         Paragraph('Control total, diferenciación, propiedad de datos', styles['TableCell']),
         Paragraph('Velocidad de implementación, menor riesgo inicial', styles['TableCell'])],
        [Paragraph('<b>Riesgo</b>', styles['TableCell']),
         Paragraph('Costos altos, requiere equipo técnico', styles['TableCell']),
         Paragraph('Dependencia del proveedor, limitaciones', styles['TableCell'])],
        [Paragraph('<b>Cuándo</b>', styles['TableCell']),
         Paragraph('El proceso es tu ventaja competitiva', styles['TableCell']),
         Paragraph('El proceso es estándar en la industria', styles['TableCell'])],
    ]

    table = Table(bb_data, colWidths=[1*inch, 2.25*inch, 2.25*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), ACCENT_CYAN),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('BACKGROUND', (0, 1), (0, -1), HexColor('#f1f5f9')),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_LIGHT),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(table)
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph(
        '<b>La regla de oro:</b> Comprá lo que es commodity. Construí lo que es tu ventaja competitiva.',
        styles['CustomBody']
    ))

    # Decision 2: Cloud vs On-premise
    story.append(Paragraph("Decisión 2: Cloud vs On-premise", styles['SectionHeader']))

    cloud_data = [
        [Paragraph('<b></b>', styles['TableCell']),
         Paragraph('<b>Cloud</b>', styles['TableCell']),
         Paragraph('<b>On-premise</b>', styles['TableCell'])],
        [Paragraph('<b>Analogía</b>', styles['TableCell']),
         Paragraph('Alquilar departamento: flexible, mantenimiento incluido', styles['TableCell']),
         Paragraph('Comprar casa: control total, vos te ocupás de todo', styles['TableCell'])],
        [Paragraph('<b>Ventaja</b>', styles['TableCell']),
         Paragraph('Escalabilidad, sin inversión inicial grande', styles['TableCell']),
         Paragraph('Control total, costos predecibles a largo plazo', styles['TableCell'])],
        [Paragraph('<b>Tendencia</b>', styles['TableCell']),
         Paragraph('Mayoría de organizaciones migrando', styles['TableCell']),
         Paragraph('Se mantiene para regulaciones específicas', styles['TableCell'])],
    ]

    table2 = Table(cloud_data, colWidths=[1*inch, 2.25*inch, 2.25*inch])
    table2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), ACCENT_PURPLE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('BACKGROUND', (0, 1), (0, -1), HexColor('#f1f5f9')),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_LIGHT),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(table2)
    story.append(Spacer(1, 0.15*inch))

    # 5 Components
    story.append(Paragraph("Los 5 componentes de una estrategia tecnológica", styles['SectionHeader']))

    components = [
        ("Plataforma", "¿Cuál es la plataforma central? ¿Propia o de terceros? ¿Puede escalar?"),
        ("Datos", "¿Son confiables? ¿Quién los gobierna? ¿Decisiones basadas en datos?"),
        ("Integraciones", "¿Los sistemas se hablan? ¿Fluye la información automáticamente?"),
        ("Seguridad", "¿Hay políticas definidas? ¿Preparados para incidentes?"),
        ("Talento", "¿Equipo de 'apaga incendios' o de construcción estratégica?"),
    ]

    for comp, desc in components:
        story.append(Paragraph(
            f'<font color="#0891b2"><b>{comp}:</b></font> {desc}',
            styles['BulletText']
        ))

    # Framework
    story.append(Paragraph("Framework de Alineación", styles['SectionHeader']))
    story.append(Paragraph(
        '<font color="#7c3aed"><b>Objetivos de Negocio → Capacidades Necesarias → Habilitadores Tecnológicos → Inversión y Priorización</b></font>',
        ParagraphStyle(name='Framework', fontSize=11, alignment=TA_CENTER, spaceAfter=15, spaceBefore=10)
    ))

    story.append(Paragraph(
        '<b>Ejemplo:</b> Objetivo: reducir deserción del 42% al 25% → Capacidad: detectar estudiantes en riesgo → Habilitador: analítica predictiva → Inversión: integración de datos + modelo de alertas',
        styles['CustomBody']
    ))

    story.append(PageBreak())


def create_module_3(story, styles):
    """Module 3: Arquitectura IT"""
    story.append(Paragraph(
        '<font color="#0891b2">MÓDULO 03</font>',
        ParagraphStyle(name='ModNum3', fontSize=12, textColor=ACCENT_CYAN, spaceAfter=5)
    ))
    story.append(Paragraph("Arquitectura IT Educativa", styles['ModuleTitle']))
    story.append(Paragraph("El mapa de tus sistemas", styles['CoverSubtitle']))

    story.append(Paragraph(
        "« ¿Cómo funciona realmente una institución educativa moderna por dentro? »",
        styles['QuoteText']
    ))

    story.append(Paragraph("Objetivo del módulo", styles['SectionHeader']))
    story.append(Paragraph(
        "Poder LEER, CUESTIONAR y DISCUTIR la arquitectura tecnológica de una institución educativa, aunque no sean técnicos. Entender cómo funcionan los sistemas para tomar mejores decisiones.",
        styles['CustomBody']
    ))

    # Systems table
    story.append(Paragraph("Sistemas clave de una institución educativa", styles['SectionHeader']))

    systems_data = [
        [Paragraph('<b>Sistema</b>', styles['TableCell']),
         Paragraph('<b>Qué hace</b>', styles['TableCell']),
         Paragraph('<b>Analogía</b>', styles['TableCell'])],
        [Paragraph('<b>SIS</b>', styles['TableCell']),
         Paragraph('Gestiona vida académica: inscripción, cursada, notas, título', styles['TableCell']),
         Paragraph('El "DNI" del estudiante', styles['TableCell'])],
        [Paragraph('<b>LMS</b>', styles['TableCell']),
         Paragraph('Plataforma de aprendizaje: contenidos, actividades, foros', styles['TableCell']),
         Paragraph('El "aula" virtual', styles['TableCell'])],
        [Paragraph('<b>CRM</b>', styles['TableCell']),
         Paragraph('Relación con prospectos y estudiantes: campañas, seguimiento', styles['TableCell']),
         Paragraph('La "memoria" de interacciones', styles['TableCell'])],
        [Paragraph('<b>ERP</b>', styles['TableCell']),
         Paragraph('Administración y finanzas: facturación, pagos, RRHH', styles['TableCell']),
         Paragraph('La "administración" del negocio', styles['TableCell'])],
        [Paragraph('<b>BI</b>', styles['TableCell']),
         Paragraph('Analítica y reportes: dashboards, indicadores', styles['TableCell']),
         Paragraph('Los "ojos" de la organización', styles['TableCell'])],
        [Paragraph('<b>IAM</b>', styles['TableCell']),
         Paragraph('Identidades y permisos: quién accede a qué', styles['TableCell']),
         Paragraph('La "seguridad" del edificio', styles['TableCell'])],
    ]

    table = Table(systems_data, colWidths=[0.8*inch, 2.7*inch, 2*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), TEXT_DARK),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('BACKGROUND', (0, 1), (0, -1), HexColor('#f1f5f9')),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_LIGHT),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(table)
    story.append(Spacer(1, 0.2*inch))

    # Student lifecycle
    story.append(Paragraph("Ciclo de vida del estudiante", styles['SectionHeader']))
    story.append(Paragraph(
        '<font color="#0891b2"><b>Descubrimiento → Evaluación → Admisión → Onboarding → Cursada → Evaluación → Graduación → Alumni</b></font>',
        ParagraphStyle(name='Lifecycle', fontSize=10, alignment=TA_CENTER, spaceAfter=10, spaceBefore=10)
    ))
    story.append(Paragraph(
        '<b>Los problemas surgen en las transiciones:</b> El prospecto que se inscribe en el CRM pero sus datos no llegan al SIS. El estudiante que aprueba en el LMS pero la nota no se refleja. Cada quiebre es una mala experiencia y un costo operativo.',
        styles['CustomBody']
    ))

    # Integration levels
    story.append(Paragraph("Niveles de integración", styles['SectionHeader']))

    int_data = [
        [Paragraph('<b>Nivel</b>', styles['TableCell']),
         Paragraph('<b>Cómo funciona</b>', styles['TableCell']),
         Paragraph('<b>Ejemplo</b>', styles['TableCell'])],
        [Paragraph('Manual', styles['TableCell']),
         Paragraph('Alguien exporta Excel y lo importa en otro sistema', styles['TableCell']),
         Paragraph('Pasar notas del LMS al SIS a mano', styles['TableCell'])],
        [Paragraph('Archivos', styles['TableCell']),
         Paragraph('Un sistema genera archivo que otro consume automáticamente', styles['TableCell']),
         Paragraph('CSV de inscriptos que se importa cada noche', styles['TableCell'])],
        [Paragraph('APIs', styles['TableCell']),
         Paragraph('Los sistemas se hablan en tiempo real', styles['TableCell']),
         Paragraph('Inscripción en SIS crea cuenta en LMS', styles['TableCell'])],
        [Paragraph('Eventos', styles['TableCell']),
         Paragraph('Los sistemas reaccionan a lo que pasa en otros', styles['TableCell']),
         Paragraph('Si no ingresa al LMS en 7 días, alerta automática', styles['TableCell'])],
    ]

    table2 = Table(int_data, colWidths=[0.9*inch, 2.3*inch, 2.3*inch])
    table2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), ACCENT_PURPLE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_LIGHT),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(table2)

    story.append(PageBreak())


def create_module_4(story, styles):
    """Module 4: Transformación Digital e IA"""
    story.append(Paragraph(
        '<font color="#0891b2">MÓDULO 04</font>',
        ParagraphStyle(name='ModNum4', fontSize=12, textColor=ACCENT_CYAN, spaceAfter=5)
    ))
    story.append(Paragraph("Transformación Digital e IA", styles['ModuleTitle']))
    story.append(Paragraph("Cómo transformar sin romper la organización", styles['CoverSubtitle']))

    story.append(Paragraph(
        "« ¿Cómo transformar sin romper la organización? »",
        styles['QuoteText']
    ))

    story.append(Paragraph("El Triángulo de la Transformación Digital", styles['SectionHeader']))
    story.append(Paragraph(
        "La transformación digital NO es un proyecto de tecnología. Es la intersección de tres fuerzas que deben avanzar juntas:",
        styles['CustomBody']
    ))

    tri_data = [
        [Paragraph('<b>Dimensión</b>', styles['TableCell']),
         Paragraph('<b>Qué implica</b>', styles['TableCell']),
         Paragraph('<b>Sin ella...</b>', styles['TableCell'])],
        [Paragraph('<font color="#0891b2"><b>Cultura</b></font>', styles['TableCell']),
         Paragraph('Mentalidad de cambio, apertura a experimentar', styles['TableCell']),
         Paragraph('Se compra tecnología que nadie usa', styles['TableCell'])],
        [Paragraph('<font color="#7c3aed"><b>Procesos</b></font>', styles['TableCell']),
         Paragraph('Rediseño de cómo se hacen las cosas', styles['TableCell']),
         Paragraph('Se automatizan procesos ineficientes', styles['TableCell'])],
        [Paragraph('<font color="#be185d"><b>Tecnología</b></font>', styles['TableCell']),
         Paragraph('Herramientas, plataformas, infraestructura', styles['TableCell']),
         Paragraph('Se quiere cambiar pero no se puede ejecutar', styles['TableCell'])],
    ]

    table = Table(tri_data, colWidths=[1.2*inch, 2.3*inch, 2*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), TEXT_DARK),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_LIGHT),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(table)
    story.append(Spacer(1, 0.15*inch))

    # Three horizons
    story.append(Paragraph("Los tres horizontes de transformación", styles['SectionHeader']))

    hor_data = [
        [Paragraph('<b>Horizonte</b>', styles['TableCell']),
         Paragraph('<b>Plazo</b>', styles['TableCell']),
         Paragraph('<b>Foco</b>', styles['TableCell']),
         Paragraph('<b>Ejemplo</b>', styles['TableCell'])],
        [Paragraph('<font color="#0891b2"><b>H1: Optimizar</b></font>', styles['TableCell']),
         Paragraph('0-6 meses', styles['TableCell']),
         Paragraph('Mejorar lo que existe', styles['TableCell']),
         Paragraph('Integrar SIS con LMS', styles['TableCell'])],
        [Paragraph('<font color="#7c3aed"><b>H2: Evolucionar</b></font>', styles['TableCell']),
         Paragraph('6-18 meses', styles['TableCell']),
         Paragraph('Rediseñar procesos clave', styles['TableCell']),
         Paragraph('Implementar CRM completo', styles['TableCell'])],
        [Paragraph('<font color="#be185d"><b>H3: Reinventar</b></font>', styles['TableCell']),
         Paragraph('18+ meses', styles['TableCell']),
         Paragraph('Cuestionar el modelo', styles['TableCell']),
         Paragraph('IA como tutor personalizado', styles['TableCell'])],
    ]

    table2 = Table(hor_data, colWidths=[1.2*inch, 1*inch, 1.5*inch, 1.8*inch])
    table2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), ACCENT_CYAN),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_LIGHT),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(table2)
    story.append(Spacer(1, 0.15*inch))

    # AI Framework
    story.append(Paragraph("Framework de adopción de IA", styles['SectionHeader']))

    ai_levels = [
        ("Nivel 0 — Ignorar", "\"La IA no aplica a nosotros\"", "Riesgo: quedarse atrás"),
        ("Nivel 1 — Explorar", "Herramientas aisladas (ChatGPT)", "Uso individual, sin política"),
        ("Nivel 2 — Experimentar", "Pilotos controlados con objetivos", "Se empieza a medir impacto"),
        ("Nivel 3 — Integrar", "IA en procesos clave", "Hay políticas y gobernanza"),
        ("Nivel 4 — Redefinir", "Modelo de negocio aprovecha IA", "IA como capa transversal"),
    ]

    for level, desc, result in ai_levels:
        story.append(Paragraph(
            f'<font color="#0891b2"><b>{level}:</b></font> {desc} — <i>{result}</i>',
            styles['BulletText']
        ))

    # Risks
    story.append(Paragraph("Riesgos y consideraciones éticas", styles['SectionHeader']))
    risks = [
        "Sesgo algorítmico: modelos que discriminan sin que lo sepamos",
        "Privacidad de datos: ¿qué datos usamos? ¿hay consentimiento?",
        "Dependencia de proveedores: ¿qué pasa si cambian términos?",
        "Desplazamiento sin plan: automatizar sin reskilling genera resistencia",
    ]
    for risk in risks:
        story.append(Paragraph(f"• {risk}", styles['BulletText']))

    story.append(PageBreak())


def create_module_5(story, styles):
    """Module 5: Mindset Digital"""
    story.append(Paragraph(
        '<font color="#0891b2">MÓDULO 05</font>',
        ParagraphStyle(name='ModNum5', fontSize=12, textColor=ACCENT_CYAN, spaceAfter=5)
    ))
    story.append(Paragraph("Mindset Digital", styles['ModuleTitle']))
    story.append(Paragraph("El sistema operativo del liderazgo", styles['CoverSubtitle']))

    story.append(Paragraph(
        "« ¿Qué tipo de líder necesita ser tu organización para que la estrategia tecnológica funcione? »",
        styles['QuoteText']
    ))

    story.append(Paragraph("¿Qué es el Mindset Digital?", styles['SectionHeader']))
    story.append(Paragraph(
        "<b>NO es:</b> ser joven, saber usar herramientas, hablar de innovación, tener redes sociales.",
        styles['CustomBody']
    ))
    story.append(Paragraph(
        "<b>SÍ es:</b> una forma de tomar decisiones basada en datos, experimentación y velocidad. La capa humana que hace posible la estrategia tecnológica.",
        styles['CustomBody']
    ))

    story.append(Paragraph("Los 7 Pilares del Mindset Digital", styles['SectionHeader']))

    pillars = [
        ("1. Orientación a Producto", "El campus virtual no es un proyecto que termina. Es un producto que se itera y mejora continuamente. La pregunta no es '¿cuándo terminamos?' sino '¿cuánto valor entregamos hoy vs hace 3 meses?'"),
        ("2. Aprendizaje Continuo", "Un líder que dejó de aprender hace 3 años toma decisiones con información desactualizada. 2-3 horas semanales leyendo tendencias, probar las herramientas que usa la organización."),
        ("3. Experimentación", "Hipótesis → Prototipo → Prueba controlada → Medir → Decidir. Experimentar no es improvisar: es testear con métricas definidas, en alcance controlado."),
        ("4. Colaboración Multidisciplinaria", "Negocio + Tecnología + Datos + Diseño = Decisiones integrales. El área académica no elige el LMS sola — lo elige con IT y experiencia del estudiante."),
        ("5. Cultura de Datos", "No opinar, medir. No asumir, probar. ¿Las discusiones en el comité directivo se basan en datos o en 'yo creo que'?"),
        ("6. Agencia Digital", "La tecnología no es responsabilidad exclusiva de IT. Cada persona debería poder entender, usar y proponer mejoras tecnológicas."),
        ("7. Seguridad y Ética", "¿Qué datos personales almacenamos? ¿Qué pasaría si sufrimos un ataque? ¿Cumplimos regulación de protección de datos?"),
    ]

    for title, desc in pillars:
        story.append(Paragraph(
            f'<font color="#0891b2"><b>{title}</b></font>',
            ParagraphStyle(name='PillarTitle', fontSize=11, spaceAfter=3, spaceBefore=10, fontName='Helvetica-Bold')
        ))
        story.append(Paragraph(desc, styles['CustomBody']))

    story.append(PageBreak())

    # Closing page
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph("━" * 40, ParagraphStyle(
        name='DecorLineEnd',
        fontSize=12,
        textColor=ACCENT_CYAN,
        alignment=TA_CENTER
    )))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(
        "La estrategia tecnológica sin mindset digital es un plan.<br/>El mindset digital sin estrategia tecnológica es improvisación.<br/><b>Juntos, son transformación.</b>",
        ParagraphStyle(
            name='ClosingQuote',
            fontSize=14,
            leading=22,
            textColor=TEXT_DARK,
            alignment=TA_CENTER,
            fontName='Helvetica-Oblique'
        )
    ))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("━" * 40, ParagraphStyle(
        name='DecorLineEnd2',
        fontSize=12,
        textColor=ACCENT_MAGENTA,
        alignment=TA_CENTER
    )))


def add_page_number(canvas, doc):
    """Add page numbers to each page"""
    page_num = canvas.getPageNumber()
    if page_num > 1:  # Skip cover page
        text = f"— {page_num} —"
        canvas.saveState()
        canvas.setFont('Helvetica', 9)
        canvas.setFillColor(MUTED)
        canvas.drawCentredString(letter[0]/2, 0.5*inch, text)
        canvas.restoreState()


def main():
    """Generate the PDF"""
    output_path = "curso-estrategia-tecnologica.pdf"

    # Create document
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )

    # Get styles
    styles = get_custom_styles()

    # Build content
    story = []

    create_cover_page(story, styles)
    create_toc(story, styles)
    create_module_1(story, styles)
    create_module_2(story, styles)
    create_module_3(story, styles)
    create_module_4(story, styles)
    create_module_5(story, styles)

    # Build PDF
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)

    print(f"✓ PDF generado exitosamente: {output_path}")
    return output_path


if __name__ == "__main__":
    main()
