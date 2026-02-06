# Recomendaciones de Mejora — Curso de Estrategia Tecnológica

## Resumen Ejecutivo

El curso tiene una **estructura sólida** con buenos casos de estudio y dinámicas prácticas. Las siguientes recomendaciones buscan llevarlo al siguiente nivel en profundidad teórica, aplicabilidad práctica y experiencia del participante.

---

## A. Mejoras en Profundidad Teórica

### 1. Agregar Frameworks Reconocidos Internacionalmente

**Problema:** El curso usa frameworks propios que son buenos, pero los participantes se beneficiarían de conocer frameworks que pueden usar como lenguaje común con consultores, vendors y peers.

**Recomendaciones:**

| Framework | Dónde agregar | Por qué |
|-----------|---------------|---------|
| **Wardley Mapping** | Módulo 2 | Visualizar evolución de componentes tech (génesis → custom → producto → commodity) |
| **TOGAF simplificado** | Módulo 3 | Referencia de arquitectura empresarial que IT conoce |
| **Modelo de Madurez Digital (Deloitte/McKinsey)** | Módulo 4 | Benchmark estándar de la industria |
| **Gartner Hype Cycle** | Módulo 4 (IA) | Ubicar tecnologías en su ciclo de adopción |
| **Business Model Canvas + Tech Stack Canvas** | Módulo 2 | Conectar modelo de negocio con decisiones tech |

### 2. Agregar Perspectiva Financiera

**Problema:** El curso habla de decisiones pero no de cómo cuantificarlas o presentarlas al board.

**Contenido sugerido para nuevo bloque o integración:**

```
CONCEPTOS FINANCIEROS PARA DECISIONES TECH

1. TCO (Total Cost of Ownership)
   - Costos de adquisición + implementación + operación + salida
   - Ejemplo: SaaS vs On-premise a 5 años

2. ROI de proyectos tecnológicos
   - Cómo medir retorno en proyectos difíciles de cuantificar
   - Proxies: reducción de fricción, NPS, tiempo de resolución

3. CAPEX vs OPEX
   - Implicancias en flujo de caja y estados financieros
   - Por qué CFOs prefieren OPEX (cloud) vs CAPEX (servidores)

4. Costo de la inacción
   - Cuantificar el riesgo de no invertir
   - Deuda técnica como pasivo no registrado
```

### 3. Fortalecer Seguridad, Compliance y Riesgo

**Problema:** El Pilar 7 de Mindset Digital menciona seguridad pero no hay profundidad suficiente para un ejecutivo.

**Contenido sugerido:**

```
SEGURIDAD Y COMPLIANCE PARA EJECUTIVOS

1. Regulaciones clave
   - GDPR (Europa) y equivalentes LATAM
   - Ley de Protección de Datos Personales (Argentina, México, etc.)
   - SOC 2, ISO 27001 — qué significan para vendors

2. Riesgos concretos
   - Ransomware: qué hacer si pasa
   - Fuga de datos: costos reputacionales y legales
   - Vendor lock-in: estrategias de mitigación

3. Preguntas que el CEO debe hacer
   - ¿Tenemos un plan de respuesta a incidentes?
   - ¿Dónde están físicamente nuestros datos?
   - ¿Qué pasa si nuestro vendor principal quiebra?
```

### 4. Expandir el Framework de IA

**Problema:** El framework de 5 niveles es bueno pero falta guía práctica de implementación.

**Contenido sugerido:**

```
GUÍA PRÁCTICA DE ADOPCIÓN DE IA

1. Matriz de Casos de Uso (Impacto vs Esfuerzo)
   ┌─────────────────────────────────────────┐
   │ ALTO      │ ESTRATÉGICO │  TRANSFORMADOR │
   │ IMPACTO   │ (priorizar) │  (planificar)  │
   ├───────────┼─────────────┼────────────────┤
   │ BAJO      │ QUICK WIN   │  EVITAR        │
   │ IMPACTO   │ (hacer ya)  │  (no invertir) │
   └───────────┴─────────────┴────────────────┘
              BAJO ESFUERZO   ALTO ESFUERZO

2. Criterios de selección de vendors de IA
   - ¿Dónde se procesan los datos?
   - ¿Hay lock-in de datos/modelos?
   - ¿Qué pasa con la privacidad del estudiante?

3. Política de IA institucional (template)
   - Usos permitidos y prohibidos
   - Disclosure requirements
   - Governance y responsabilidades
```

---

## B. Mejoras en Aplicabilidad Práctica

### 1. Crear Canvas Visual de Diagnóstico Estratégico

**Problema:** Los templates actuales están en formato ASCII/texto, difíciles de usar en workshops.

**Solución:** Crear un **"Tech Strategy Canvas"** visual (similar al Business Model Canvas) con 9 bloques:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     TECH STRATEGY CANVAS                                 │
├──────────────┬──────────────┬──────────────┬──────────────┬─────────────┤
│   OBJETIVOS  │ CAPACIDADES  │ HABILITADORES│  INVERSIÓN   │   MÉTRICAS  │
│   DE NEGOCIO │  NECESARIAS  │ TECNOLÓGICOS │  REQUERIDA   │   DE ÉXITO  │
├──────────────┼──────────────┴──────────────┼──────────────┴─────────────┤
│   SISTEMAS   │        INTEGRACIONES        │         DATOS              │
│     CORE     │        (flujo de info)      │    (fuentes de verdad)     │
├──────────────┴─────────────────────────────┴────────────────────────────┤
│                    TALENTO + PARTNERS + VENDORS                          │
├─────────────────────────────────────────────────────────────────────────┤
│                    RIESGOS + DEUDA TÉCNICA + COMPLIANCE                  │
└─────────────────────────────────────────────────────────────────────────┘
```

### 2. Agregar Herramientas de Autoevaluación Cuantitativas

**Problema:** Las evaluaciones son cualitativas (semáforo). Falta benchmark.

**Solución:** Crear un **"Digital Maturity Score"** con escala 0-100:

```
DIGITAL MATURITY ASSESSMENT

Dimensión               Peso    Score (1-5)    Ponderado
─────────────────────────────────────────────────────────
Infraestructura         15%     ___           ___
Arquitectura            15%     ___           ___
Datos                   20%     ___           ___
Seguridad               15%     ___           ___
Talento                 15%     ___           ___
Innovación              10%     ___           ___
Mindset Digital         10%     ___           ___
─────────────────────────────────────────────────────────
SCORE TOTAL (0-100):                          ___

Benchmark por tipo de institución:
- Universidad tradicional LATAM: 35-45
- Universidad con transformación en curso: 50-65
- Universidad digital-first: 70-85
- EdTech nativa digital: 80-95
```

### 3. Agregar Role-Play / Simulaciones

**Problema:** Falta práctica de conversaciones difíciles.

**Dinámicas sugeridas:**

```
SIMULACIÓN 1: "Negociación con el CTO"
- Escenario: El CTO quiere construir un SIS propio. El CFO dice que no hay presupuesto.
- Roles: CEO, CTO, CFO
- Objetivo: Llegar a una decisión fundamentada en 15 minutos

SIMULACIÓN 2: "Presentación al Board"
- Escenario: Pedir aprobación para migrar a la nube
- Roles: CEO presentando, Board members cuestionando
- Objetivo: Convencer con datos y gestionar objeciones

SIMULACIÓN 3: "Vendor Pitch"
- Escenario: Tres vendors de LMS presentan en 5 minutos cada uno
- Roles: Participantes como vendors, otros como comité evaluador
- Objetivo: Identificar red flags y hacer las preguntas correctas
```

### 4. Fortalecer el Challenge con Deliverables Específicos

**Problema:** El Challenge Point no tiene entregables suficientemente definidos.

**Estructura sugerida:**

```
CHALLENGE ENTREGABLES

Entregable 1: Diagnóstico (30%)
- Tech Strategy Canvas completado
- Digital Maturity Score
- Top 3 brechas identificadas

Entregable 2: Roadmap (40%)
- 3 horizontes con iniciativas específicas
- Para cada iniciativa: objetivo, sistemas involucrados, estimación de inversión
- Dependencias críticas

Entregable 3: Quick Win (30%)
- Una iniciativa para los próximos 90 días
- Business case de 1 página
- Plan de implementación
```

---

## C. Contenido Adicional Sugerido

### 1. Glosario Ejecutivo de Términos Tech

Para que los participantes puedan "hablar el idioma" sin ser técnicos.

```
GLOSARIO EJECUTIVO

API: El "conector" entre sistemas. Como un enchufe universal.
Cloud: Alquilar infraestructura en vez de comprarla.
Microservicios: Dividir un sistema grande en piezas pequeñas e independientes.
DevOps: Equipos que construyen Y operan el software (no hay "paso a producción").
CI/CD: Automatización para que los cambios lleguen a producción rápido y seguro.
SaaS: Software que se paga por uso, como Netflix.
Legacy: Sistema viejo que nadie quiere tocar pero todos necesitan.
Technical Debt: Atajos que tomamos hoy y pagamos mañana.
Vendor Lock-in: Cuando cambiar de proveedor es tan caro que no podés.
```

### 2. Checklist de Preguntas para Hacer al Equipo de IT

```
10 PREGUNTAS QUE TODO CEO DEBERÍA HACER A SU CTO

1. ¿Cuál es nuestro sistema más crítico? ¿Qué pasa si falla?
2. ¿Cuánta deuda técnica tenemos? ¿Está creciendo o reduciéndose?
3. ¿Dónde están físicamente nuestros datos?
4. ¿Cuánto de nuestro presupuesto de IT va a "mantener las luces encendidas" vs innovar?
5. ¿Cuánto tardaríamos en cambiar de [sistema X] si quisiéramos?
6. ¿Tenemos un plan de disaster recovery? ¿Cuándo lo probamos por última vez?
7. ¿Qué porcentaje de nuestros procesos son manuales vs automatizados?
8. ¿Cuál es nuestro mayor riesgo de seguridad hoy?
9. ¿Tenemos las personas correctas o dependemos de proveedores externos?
10. Si empezáramos de cero hoy, ¿qué haríamos diferente?
```

### 3. Red Flags en Proyectos Tecnológicos

```
🚩 RED FLAGS QUE UN LÍDER DEBE RECONOCER

En el equipo:
- "Nadie más entiende este sistema" → Riesgo de persona clave
- "Funciona, mejor no tocarlo" → Deuda técnica acumulada
- "IT dice que es imposible" → Puede ser real o falta de capacidad

En el proyecto:
- Proyecto sin fecha de fin → Scope creep
- "Estamos al 90% hace 3 meses" → Síndrome del 90%
- Sin métricas de éxito definidas → Imposible medir ROI

En los vendors:
- "Somos los únicos que hacemos esto" → Posible lock-in
- Contrato de más de 3 años sin salida → Riesgo alto
- "La personalización es fácil" → Suele ser mentira
- No pueden dar referencias de clientes similares → Red flag mayor
```

---

## D. Mejoras en Formato y Experiencia

### 1. Crear Portal Web de Navegación

Un sitio HTML estático que permita navegar todo el contenido de forma elegante.

### 2. Versiones del Material

| Versión | Contenido | Formato |
|---------|-----------|---------|
| **Participante** | Conceptos + dinámicas + templates | PDF imprimible |
| **Facilitador** | Todo lo anterior + guías de facilitación + respuestas | MD privado |
| **Ejecutivo** | Resumen de 2 páginas por módulo | PDF ejecutivo |
| **Referencia** | Glosario + checklists + frameworks | Pocket guide |

### 3. Materiales Interactivos

- **Templates en Miro/FigJam** para workshops presenciales
- **Versión digital de assessments** con cálculo automático de scores
- **Video snippets** de 2-3 minutos explicando cada concepto clave

---

## Priorización Recomendada

| Prioridad | Mejora | Esfuerzo | Impacto |
|-----------|--------|----------|---------|
| 🔴 Alta | Portal web de navegación | Bajo | Alto |
| 🔴 Alta | Tech Strategy Canvas visual | Medio | Alto |
| 🔴 Alta | Glosario ejecutivo | Bajo | Alto |
| 🟡 Media | Assessment cuantitativo con benchmark | Medio | Alto |
| 🟡 Media | Contenido de finanzas (TCO, ROI) | Medio | Medio |
| 🟡 Media | Simulaciones/role-play | Bajo | Medio |
| 🟢 Baja | Wardley Mapping | Alto | Medio |
| 🟢 Baja | Videos explicativos | Alto | Medio |

---

## Próximos Pasos Sugeridos

1. **Inmediato:** Crear portal web de navegación
2. **Corto plazo:** Agregar glosario y checklists
3. **Mediano plazo:** Desarrollar Tech Strategy Canvas y assessment cuantitativo
4. **Largo plazo:** Grabar video snippets y crear templates en Miro
