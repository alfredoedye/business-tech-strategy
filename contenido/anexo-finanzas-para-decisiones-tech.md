# Anexo — Finanzas para Decisiones Tecnológicas

> Este anexo proporciona el vocabulario y las herramientas financieras necesarias para que un líder pueda evaluar, justificar y presentar inversiones tecnológicas ante el CFO, el board o comités de inversión.

---

## Por qué un CEO necesita hablar de finanzas tech

La tecnología ya no es un "gasto de IT" — es una inversión estratégica que compite por capital con marketing, expansión, talento y otras prioridades. Para defender una inversión tecnológica, necesitás hablar el idioma de finanzas.

> "Si no podés cuantificarlo, no podés defenderlo ante el board."

---

## 1. TCO — Total Cost of Ownership

### ¿Qué es?

El TCO es el costo TOTAL de una solución tecnológica a lo largo de su vida útil, no solo el precio de compra o la licencia.

### Componentes del TCO

```
┌─────────────────────────────────────────────────────────────────┐
│                    TCO = TOTAL COST OF OWNERSHIP                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────┐  ┌──────────────────┐  ┌────────────────┐ │
│  │   ADQUISICIÓN    │  │  IMPLEMENTACIÓN  │  │   OPERACIÓN    │ │
│  │                  │  │                  │  │                │ │
│  │ • Licencias      │  │ • Consultoría    │  │ • Hosting      │ │
│  │ • Hardware       │  │ • Integración    │  │ • Soporte      │ │
│  │ • Setup inicial  │  │ • Migración      │  │ • Mantenimiento│ │
│  │                  │  │ • Capacitación   │  │ • Actualizac.  │ │
│  │                  │  │ • Change mgmt    │  │ • Personal IT  │ │
│  └──────────────────┘  └──────────────────┘  └────────────────┘ │
│                                                                  │
│  ┌──────────────────┐  ┌──────────────────┐                     │
│  │    COSTOS        │  │     SALIDA       │                     │
│  │    OCULTOS       │  │                  │                     │
│  │                  │  │ • Migración out  │                     │
│  │ • Downtime       │  │ • Penalidades    │                     │
│  │ • Productividad  │  │ • Extracción     │                     │
│  │ • Oportunidad    │  │   de datos       │                     │
│  │ • Deuda técnica  │  │                  │                     │
│  └──────────────────┘  └──────────────────┘                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Ejemplo: LMS - SaaS vs On-premise (5 años, 10,000 estudiantes)

| Componente | SaaS (Canvas) | On-premise (Moodle) |
|------------|--------------|---------------------|
| **Adquisición** | | |
| Licencias/año | $50,000 x 5 = $250,000 | $0 (open source) |
| Hardware | $0 | $80,000 |
| **Implementación** | | |
| Consultoría | $30,000 | $60,000 |
| Integración | $20,000 | $40,000 |
| Capacitación | $10,000 | $15,000 |
| **Operación (5 años)** | | |
| Hosting | Incluido | $60,000 |
| Soporte interno | $25,000 | $150,000 |
| Actualizaciones | Incluido | $50,000 |
| **Costos ocultos** | | |
| Downtime estimado | $5,000 | $30,000 |
| **TCO 5 años** | **$340,000** | **$485,000** |
| **TCO/estudiante/año** | **$6.80** | **$9.70** |

### El error común

> "Moodle es gratis" — Solo la licencia. El TCO real suele ser mayor que SaaS porque incluye hosting, soporte, actualizaciones y talento interno.

---

## 2. ROI — Return on Investment

### ¿Qué es?

El ROI mide el retorno financiero de una inversión como porcentaje del costo.

```
ROI = (Beneficio Neto / Costo de la Inversión) x 100

ROI = ((Ingresos adicionales + Ahorros) - Costo) / Costo x 100
```

### El desafío en tecnología

Muchos beneficios tecnológicos son difíciles de cuantificar directamente:

| Beneficio | Difícil de medir | Proxy cuantificable |
|-----------|------------------|---------------------|
| "Mejor experiencia del estudiante" | ✓ | NPS, retención, referidos |
| "Mayor eficiencia" | ✓ | Horas/proceso, FTEs reasignados |
| "Mejores decisiones" | ✓ | Tiempo de reacción, % decisiones data-driven |
| "Menor riesgo" | ✓ | Incidentes evitados, costo de incidente promedio |

### Framework para calcular ROI de proyectos tech

**Paso 1: Identificar beneficios**

```
BENEFICIOS DUROS (cuantificables directamente)
├── Ahorro de costos
│   ├── Reducción de personal (cuidado: sensible)
│   ├── Reducción de licencias
│   └── Reducción de infraestructura
├── Aumento de ingresos
│   ├── Mejor conversión de leads
│   ├── Menor deserción
│   └── Nuevos productos/servicios
└── Evitar costos futuros
    ├── Multas regulatorias
    └── Costo de no escalar

BENEFICIOS BLANDOS (proxies)
├── Productividad
│   └── Horas liberadas x costo/hora
├── Satisfacción
│   └── NPS → correlación con retención → valor de retención
└── Velocidad
    └── Time-to-market → ventana de oportunidad
```

**Paso 2: Cuantificar conservadoramente**

| Beneficio | Estimación | Confianza | Valor usado |
|-----------|------------|-----------|-------------|
| Reducción deserción 2% | $500,000 | Alta | $500,000 |
| Ahorro administrativo | $100,000 | Media | $70,000 (70%) |
| Nuevos ingresos | $200,000 | Baja | $60,000 (30%) |
| **Total beneficios** | | | **$630,000** |

**Paso 3: Calcular ROI**

```
Costo del proyecto: $400,000
Beneficios año 1: $630,000
ROI año 1 = ($630,000 - $400,000) / $400,000 = 57.5%
```

### Ejemplo: CRM para reducir deserción

```
INVERSIÓN
─────────
Implementación CRM: $150,000
Integración con SIS: $50,000
Capacitación: $20,000
Operación año 1: $30,000
TOTAL: $250,000

BENEFICIOS (año 1)
──────────────────
Estudiantes actuales: 10,000
Deserción actual: 42% (4,200 estudiantes/año)
Ingreso promedio/estudiante: $3,000
Reducción esperada de deserción: 3% (300 estudiantes)
Ingreso retenido: 300 x $3,000 = $900,000

ROI = ($900,000 - $250,000) / $250,000 = 260%
Payback = $250,000 / $900,000 = 3.3 meses
```

---

## 3. CAPEX vs OPEX

### ¿Qué es?

| Tipo | Definición | Ejemplo tech | Tratamiento contable |
|------|------------|--------------|---------------------|
| **CAPEX** | Capital Expenditure — Inversión en activos | Comprar servidores, licencias perpetuas | Se deprecia en varios años |
| **OPEX** | Operating Expense — Gasto operativo | Suscripción SaaS, cloud | Se gasta en el período |

### Por qué importa

```
CAPEX                           OPEX
─────                           ────
• Inversión inicial alta        • Pagos distribuidos
• Aparece en balance            • Aparece en P&L
• Afecta ratios de deuda        • Afecta margen operativo
• Requiere aprobación capital   • Más fácil de aprobar
• Deprecia en 3-5 años          • Deducible inmediatamente
```

### El shift hacia OPEX (Cloud/SaaS)

| Aspecto | CAPEX (On-premise) | OPEX (Cloud/SaaS) |
|---------|-------------------|-------------------|
| Cash flow | Golpe inicial fuerte | Flujo predecible |
| Flexibilidad | Baja (ya invertiste) | Alta (escalás según uso) |
| Obsolescencia | Riesgo del comprador | Riesgo del proveedor |
| Balance sheet | Activos + deuda | Más limpio |
| Aprobación | Comité de inversiones | Presupuesto operativo |

### Implicancia para el CFO

> "El CFO suele preferir OPEX porque no compromete capital y es más predecible. Pero OPEX acumulado puede superar CAPEX a largo plazo."

### Análisis de ejemplo: Infraestructura

```
Escenario: 100 servidores por 5 años

OPCIÓN A: CAPEX (comprar servidores)
────────────────────────────────────
Año 0: $500,000 (compra)
Años 1-5: $50,000/año (mantenimiento) = $250,000
TCO 5 años: $750,000

OPCIÓN B: OPEX (cloud - AWS/Azure)
──────────────────────────────────
Años 1-5: $180,000/año = $900,000
TCO 5 años: $900,000

Pero...
• OPEX tiene flexibilidad de escalar ↑↓
• CAPEX requiere refresh en año 5
• OPEX incluye actualizaciones automáticas
• CAPEX requiere equipo de infraestructura
```

---

## 4. El Costo de la Inacción

### ¿Qué es?

El costo de NO invertir en tecnología. Es un argumento poderoso pero subutilizado.

### Framework para cuantificar

```
COSTO DE LA INACCIÓN =
    Costo de oportunidad perdida
  + Costo de ineficiencia acumulada
  + Costo de riesgo materializado
  + Costo de brecha competitiva
```

### Ejemplo: No invertir en analítica de retención

```
Situación actual:
• Deserción: 42%
• Estudiantes: 10,000
• Ingreso/estudiante: $3,000
• Pérdida anual por deserción: $12,600,000

Sin inversión en analítica (status quo):
• Deserción se mantiene o empeora
• Pérdida año 1: $12,600,000
• Pérdida año 2: $13,200,000 (mercado más competitivo)
• Pérdida año 3: $14,000,000

Con inversión en analítica ($300,000):
• Deserción baja a 35%
• Pérdida año 1: $10,500,000
• Ahorro: $2,100,000

COSTO DE LA INACCIÓN (3 años):
Escenario sin inversión: $39,800,000 en pérdidas
Escenario con inversión: $31,500,000 en pérdidas + $300,000 inversión
Diferencia: $8,000,000

"No invertir $300,000 hoy nos cuesta $8,000,000 en 3 años."
```

### El argumento para el board

> "La pregunta no es si podemos permitirnos esta inversión. La pregunta es si podemos permitirnos NO hacerla."

---

## 5. Deuda Técnica como Pasivo No Registrado

### ¿Qué es?

Deuda técnica son los atajos, parches y decisiones subóptimas acumuladas en tecnología que eventualmente hay que "pagar" con intereses.

### Analogía financiera

```
DEUDA FINANCIERA              DEUDA TÉCNICA
────────────────              ─────────────
Principal                     Costo de remediar
Intereses                     Costo de mantener parches
Default                       Falla catastrófica del sistema
Refinanciamiento              Reescribir / migrar
```

### Cómo cuantificar deuda técnica

| Indicador | Cómo medirlo | Costo implícito |
|-----------|--------------|-----------------|
| % tiempo en mantenimiento vs innovación | Horas IT | Si IT gasta 80% en "mantener", solo 20% en crecer |
| Sistemas sin soporte | Inventario | Riesgo de falla sin remedio |
| Integraciones manuales | Conteo de procesos | Horas x costo/hora x frecuencia |
| Incidentes por sistemas legacy | Tickets/mes | Costo de downtime + resolución |
| Conocimiento concentrado | # personas que entienden sistema X | Riesgo de persona clave |

### Ejemplo: ERP legacy

```
Sistema: ERP de 15 años
Costo de mantenimiento anual: $200,000
Incidentes/año: 24
Costo promedio por incidente: $15,000
Costo de incidentes: $360,000
Personal dedicado: 2 FTEs = $160,000
COSTO ANUAL TOTAL: $720,000

vs.

ERP moderno (SaaS)
Licencia anual: $300,000
Implementación (amortizada): $100,000
Incidentes esperados: 6 x $5,000 = $30,000
Personal: 0.5 FTE = $40,000
COSTO ANUAL TOTAL: $470,000

AHORRO ANUAL: $250,000
PAYBACK de migración ($500,000): 2 años
```

---

## 6. Cómo Presentar una Inversión Tech al Board

### Estructura de presentación (1 página)

```
┌─────────────────────────────────────────────────────────────────┐
│ TÍTULO: [Nombre del proyecto]                                   │
├─────────────────────────────────────────────────────────────────┤
│ PROBLEMA (2 líneas)                                             │
│ ¿Qué problema de negocio resuelve?                              │
├─────────────────────────────────────────────────────────────────┤
│ SOLUCIÓN (2 líneas)                                             │
│ ¿Qué proponemos hacer?                                          │
├─────────────────────────────────────────────────────────────────┤
│ INVERSIÓN                        │ RETORNO ESPERADO             │
│ • TCO 3 años: $X                 │ • ROI: X%                    │
│ • Año 1: $X                      │ • Payback: X meses           │
│ • Años 2-3: $X/año               │ • Beneficio año 1: $X        │
├──────────────────────────────────┴──────────────────────────────┤
│ RIESGOS Y MITIGACIÓN                                            │
│ • Riesgo 1 → Mitigación                                         │
│ • Riesgo 2 → Mitigación                                         │
├─────────────────────────────────────────────────────────────────┤
│ COSTO DE LA INACCIÓN                                            │
│ Si no invertimos: [consecuencia cuantificada]                   │
├─────────────────────────────────────────────────────────────────┤
│ DECISIÓN SOLICITADA                                             │
│ Aprobar inversión de $X para [alcance] con inicio en [fecha]    │
└─────────────────────────────────────────────────────────────────┘
```

### Las preguntas que hará el CFO

| Pregunta | Cómo prepararte |
|----------|----------------|
| "¿Cuál es el payback?" | Tener cálculo con supuestos explícitos |
| "¿Qué pasa si no funciona?" | Plan B, reversibilidad, pilotos |
| "¿Por qué ahora?" | Costo de la inacción, ventana de oportunidad |
| "¿Podemos hacerlo más barato?" | Alternativas evaluadas, trade-offs |
| "¿Quién es responsable?" | Ownership claro, governance |

---

## Checklist: ¿Está tu business case completo?

- [ ] TCO calculado (no solo precio de licencia)
- [ ] ROI con supuestos explícitos y conservadores
- [ ] Beneficios duros y blandos separados
- [ ] CAPEX vs OPEX clarificado
- [ ] Costo de la inacción cuantificado
- [ ] Riesgos identificados con mitigación
- [ ] Alternativas consideradas
- [ ] Alineación con estrategia de negocio
- [ ] Sponsor ejecutivo identificado
- [ ] Timeline realista con hitos

---

*Este anexo complementa el Módulo 2. Para volver: [← Módulo 2 — Estrategia Tecnológica](modulo-02-estrategia-tecnologica.md)*
