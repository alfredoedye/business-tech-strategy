# Anexo — Framework Expandido de Adopción de IA

> Este anexo complementa el Módulo 4 (Transformación Digital e IA) con herramientas prácticas para evaluar, priorizar e implementar iniciativas de IA en instituciones educativas.

---

## 1. Matriz de Priorización de Casos de Uso

### El framework Impacto vs Esfuerzo

No todos los casos de uso de IA son iguales. Esta matriz ayuda a priorizar:

```
                            ESFUERZO DE IMPLEMENTACIÓN
                                BAJO           ALTO
                         ┌─────────────────┬─────────────────┐
                         │                 │                 │
              ALTO       │   QUICK WINS    │  ESTRATÉGICOS   │
                         │   ★ Prioridad 1 │  ★ Prioridad 2  │
   IMPACTO               │                 │                 │
   EN EL                 │  Hacer ahora    │  Planificar     │
   NEGOCIO               │                 │  cuidadosamente │
                         ├─────────────────┼─────────────────┤
                         │                 │                 │
              BAJO       │   FILL-INS      │    EVITAR       │
                         │   ★ Prioridad 3 │  ✗ No invertir  │
                         │                 │                 │
                         │  Si hay tiempo  │  Costo > valor  │
                         │                 │                 │
                         └─────────────────┴─────────────────┘
```

### Casos de uso clasificados para educación

| Caso de uso | Impacto | Esfuerzo | Cuadrante | Prioridad |
|-------------|---------|----------|-----------|-----------|
| Chatbot FAQ estudiantes | Alto | Bajo | Quick Win | ★★★ |
| Generación de quizzes | Medio | Bajo | Quick Win | ★★★ |
| Resumen de materiales | Medio | Bajo | Quick Win | ★★★ |
| Detección de deserción | Alto | Medio | Estratégico | ★★☆ |
| Tutor personalizado 24/7 | Alto | Alto | Estratégico | ★★☆ |
| Corrección automática essays | Medio | Alto | Evaluar | ★☆☆ |
| Asistente administrativo | Medio | Medio | Fill-in | ★☆☆ |
| Generación de contenido completo | Bajo | Alto | Evitar | ✗ |

### Template de evaluación

Para cada caso de uso, evaluar:

```
CASO DE USO: ________________________________

IMPACTO (1-5)
─────────────
[ ] Afecta métrica clave de negocio (retención, NPS, conversión)
[ ] Beneficia a gran cantidad de usuarios
[ ] Reduce costos significativamente
[ ] Genera diferenciación competitiva
[ ] Alineado con prioridades estratégicas
SCORE IMPACTO: ___/5

ESFUERZO (1-5, invertido: 5=bajo esfuerzo)
──────────────────────────────────────────
[ ] Datos necesarios están disponibles
[ ] No requiere integración compleja
[ ] Existe solución de mercado (no hay que construir)
[ ] Equipo tiene capacidad para implementar
[ ] Riesgo regulatorio/ético bajo
SCORE ESFUERZO: ___/5

UBICACIÓN EN MATRIZ: Impacto ___ / Esfuerzo ___
RECOMENDACIÓN: [ ] Quick Win [ ] Estratégico [ ] Fill-in [ ] Evitar
```

---

## 2. Criterios de Selección de Vendors de IA

### Framework de evaluación

| Dimensión | Peso | Preguntas clave |
|-----------|------|-----------------|
| **Funcionalidad** | 25% | ¿Resuelve el problema? ¿Qué tan bien? |
| **Datos y privacidad** | 25% | ¿Dónde se procesan? ¿Quién es dueño? |
| **Integración** | 20% | ¿Se conecta con nuestros sistemas? |
| **Costo y modelo** | 15% | ¿TCO? ¿Escala con uso? |
| **Vendor viability** | 15% | ¿Van a existir en 3 años? |

### Preguntas específicas por dimensión

#### Funcionalidad
- [ ] ¿Demo con nuestros datos reales?
- [ ] ¿Qué tan personalizable es?
- [ ] ¿Roadmap de producto alineado con nuestras necesidades?
- [ ] ¿Referencias de clientes similares (educación LATAM)?

#### Datos y privacidad
- [ ] ¿Dónde se almacenan físicamente los datos?
- [ ] ¿Los datos de nuestros estudiantes se usan para entrenar el modelo?
- [ ] ¿Podemos eliminar datos si el estudiante lo solicita (GDPR)?
- [ ] ¿Qué certificaciones de seguridad tienen (SOC 2, ISO 27001)?
- [ ] ¿Cómo manejan datos de menores de edad?

#### Integración
- [ ] ¿APIs disponibles y documentadas?
- [ ] ¿Integración nativa con nuestro LMS/SIS/CRM?
- [ ] ¿Soporte para SSO (Single Sign-On)?
- [ ] ¿Tiempo estimado de implementación?

#### Costo y modelo
- [ ] ¿Precio por usuario, por uso, o fijo?
- [ ] ¿Cómo escala el costo con el volumen?
- [ ] ¿Costos ocultos (implementación, soporte, extras)?
- [ ] ¿Período de prueba o piloto?

#### Vendor viability
- [ ] ¿Cuánto tiempo llevan en el mercado?
- [ ] ¿Financiamiento / estabilidad financiera?
- [ ] ¿Clientes de referencia que podamos contactar?
- [ ] ¿Qué pasa con nuestros datos si cierran?

### Red flags en vendors de IA

| Red flag | Por qué preocupa |
|----------|------------------|
| "Nuestro modelo es propietario y secreto" | No podés auditar sesgos ni entender decisiones |
| "Los datos mejoran el modelo para todos" | Tus datos de estudiantes entrenan a competidores |
| No pueden dar referencias | Producto inmaduro o clientes insatisfechos |
| Contrato de 3+ años sin salida | Lock-in en tecnología que evoluciona rápido |
| "La implementación es trivial" | Subestimación que lleva a fracaso |
| Precio demasiado bueno | Modelo no sostenible, van a subir o cerrar |

---

## 3. Template de Política de IA Institucional

### Estructura recomendada

```
POLÍTICA DE USO DE INTELIGENCIA ARTIFICIAL
[Nombre de la Institución]
Versión: 1.0 | Fecha: [Fecha] | Aprobado por: [Autoridad]

═══════════════════════════════════════════════════════════════

1. PROPÓSITO
   Esta política establece los principios, lineamientos y
   responsabilidades para el uso de IA en [institución].

2. ALCANCE
   Aplica a: estudiantes, docentes, personal administrativo,
   y proveedores que usen IA en nombre de la institución.

3. PRINCIPIOS RECTORES
   3.1 Transparencia: El uso de IA debe ser declarado
   3.2 Privacidad: Protección de datos personales
   3.3 Equidad: Evitar sesgos y discriminación
   3.4 Responsabilidad: Humano siempre responsable final
   3.5 Mejora continua: Monitoreo y ajuste permanente

4. USOS PERMITIDOS
   4.1 Para estudiantes:
       ✓ Asistencia en investigación y estudio
       ✓ Herramientas de accesibilidad
       ✓ Práctica y ejercitación
       ✗ Presentar contenido generado como propio sin declarar

   4.2 Para docentes:
       ✓ Generación de materiales y actividades
       ✓ Asistencia en evaluación (con revisión humana)
       ✓ Personalización de contenidos
       ✗ Evaluación final automatizada sin supervisión

   4.3 Para administración:
       ✓ Automatización de procesos repetitivos
       ✓ Análisis de datos agregados
       ✗ Decisiones automatizadas sobre estudiantes sin revisión

5. REQUISITOS DE DISCLOSURE
   5.1 Trabajos académicos: Declarar uso de IA y cómo se usó
   5.2 Comunicaciones: Identificar si fue generado por IA
   5.3 Decisiones: Documentar si IA influyó en una decisión

6. DATOS Y PRIVACIDAD
   6.1 No ingresar datos personales en herramientas no aprobadas
   6.2 No ingresar información confidencial institucional
   6.3 Herramientas aprobadas: [lista de herramientas]
   6.4 Proceso para solicitar aprobación de nueva herramienta

7. RESPONSABILIDADES
   7.1 Comité de Ética y IA: Supervisión y actualización
   7.2 Dirección de Tecnología: Aprobación de herramientas
   7.3 Dirección Académica: Lineamientos pedagógicos
   7.4 Usuarios: Cumplimiento de esta política

8. CONSECUENCIAS DEL INCUMPLIMIENTO
   [Definir según reglamento institucional]

9. REVISIÓN Y ACTUALIZACIÓN
   Esta política se revisará semestralmente o ante cambios
   significativos en la tecnología o regulación.

═══════════════════════════════════════════════════════════════
```

---

## 4. Framework de Gobernanza de IA

### Estructura organizacional sugerida

```
┌─────────────────────────────────────────────────────────────┐
│                    COMITÉ EJECUTIVO                          │
│         (CEO, CAO, CTO, CFO, CDO si existe)                 │
│         Decisiones estratégicas y presupuesto               │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│               COMITÉ DE IA Y ÉTICA                           │
│    (Académico, Legal, IT, Estudiantes, Docentes)            │
│    Políticas, evaluación de riesgos, casos complejos        │
└─────────────────────────┬───────────────────────────────────┘
                          │
          ┌───────────────┼───────────────┐
          │               │               │
          ▼               ▼               ▼
┌─────────────────┐ ┌───────────┐ ┌─────────────────┐
│   GRUPO DE      │ │  EQUIPO   │ │   CHAMPIONS     │
│   TRABAJO       │ │  TÉCNICO  │ │   POR ÁREA      │
│   ACADÉMICO     │ │           │ │                 │
│                 │ │           │ │                 │
│ Casos de uso    │ │ Implement.│ │ Adopción y      │
│ pedagógicos     │ │ Seguridad │ │ capacitación    │
└─────────────────┘ └───────────┘ └─────────────────┘
```

### Proceso de aprobación de iniciativas IA

```
┌──────────────────┐
│ 1. PROPUESTA     │ Cualquier área puede proponer
│    (Template)    │ caso de uso de IA
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ 2. TRIAGE        │ Equipo técnico evalúa factibilidad
│    (1 semana)    │ y esfuerzo inicial
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ 3. EVALUACIÓN    │ Comité de IA evalúa impacto,
│    DE RIESGO     │ riesgos éticos, privacidad
│    (2 semanas)   │
└────────┬─────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌───────┐ ┌───────┐
│APROBADO│ │RECHAZADO│
│        │ │(con     │
│        │ │feedback)│
└────┬───┘ └────────┘
     │
     ▼
┌──────────────────┐
│ 4. PILOTO        │ Implementación controlada
│    (1-3 meses)   │ con grupo limitado
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ 5. EVALUACIÓN    │ Métricas, feedback,
│    DE PILOTO     │ ajustes necesarios
└────────┬─────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌───────┐ ┌───────┐
│ESCALAR │ │AJUSTAR │
│        │ │o       │
│        │ │DESCART.│
└────────┘ └────────┘
```

---

## 5. Métricas para Iniciativas de IA

### KPIs por tipo de caso de uso

| Caso de uso | Métricas de éxito | Métricas de riesgo |
|-------------|-------------------|-------------------|
| **Chatbot FAQ** | Tasa de resolución, NPS, tickets evitados | Escalaciones, errores, frustración |
| **Detección deserción** | Precisión predicción, intervenciones exitosas | Falsos positivos/negativos, sesgo |
| **Tutor personalizado** | Engagement, mejora notas, satisfacción | Dependencia, reducción pensamiento crítico |
| **Generación contenido** | Tiempo ahorrado, calidad percibida | Errores factuales, homogeneización |
| **Corrección automática** | Consistencia, tiempo ahorrado | Errores de evaluación, apelaciones |

### Dashboard de IA institucional

```
┌─────────────────────────────────────────────────────────────┐
│            DASHBOARD DE IA - [Institución]                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ADOPCIÓN                    IMPACTO                        │
│  ──────────                  ───────                        │
│  Usuarios activos: 2,500     Horas ahorradas: 450/mes       │
│  % staff usando IA: 45%      Tickets evitados: 1,200/mes    │
│  Herramientas activas: 4     NPS chatbot: +42               │
│                                                              │
│  RIESGO                      INVERSIÓN                      │
│  ──────                      ─────────                      │
│  Incidentes mes: 3           Costo mensual: $8,500          │
│  Escalaciones: 12%           Costo/usuario: $3.40           │
│  Quejas privacidad: 0        ROI estimado: 340%             │
│                                                              │
│  INICIATIVAS EN CURSO                                        │
│  ─────────────────────                                       │
│  ● Chatbot FAQ v2 ████████████░░░░ 75% (en tiempo)          │
│  ● Piloto tutor IA ████████░░░░░░░░ 50% (con riesgo)        │
│  ● Detección deserción █████░░░░░░░░░ 30% (planificando)    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 6. Checklist de Lanzamiento de IA

### Antes del piloto

- [ ] Caso de uso definido y acotado
- [ ] Sponsor ejecutivo identificado
- [ ] Presupuesto aprobado
- [ ] Evaluación de riesgo completada
- [ ] Vendor/herramienta seleccionado
- [ ] Datos necesarios identificados y accesibles
- [ ] Plan de privacidad aprobado por legal
- [ ] Grupo piloto definido
- [ ] Métricas de éxito definidas
- [ ] Plan de comunicación a participantes
- [ ] Proceso de feedback definido
- [ ] Plan de contingencia si falla

### Durante el piloto

- [ ] Monitoreo diario de métricas clave
- [ ] Canal de feedback activo
- [ ] Revisión semanal con equipo
- [ ] Documentación de incidentes
- [ ] Ajustes iterativos

### Antes de escalar

- [ ] Métricas de éxito alcanzadas
- [ ] Feedback procesado y actuado
- [ ] Riesgos identificados mitigados
- [ ] Capacitación de usuarios lista
- [ ] Soporte de nivel 1 capacitado
- [ ] Documentación completa
- [ ] Aprobación de comité para escalar
- [ ] Plan de rollout por fases

---

*Este anexo complementa el Módulo 4. Para volver: [← Módulo 4 — Transformación Digital e IA](modulo-04-transformacion-digital-ia.md)*
