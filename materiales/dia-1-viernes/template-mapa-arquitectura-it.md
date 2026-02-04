# Template: Mapa de Arquitectura IT Educativa

## Actividad: "Mapeá tu arquitectura" — Bloque 3

### Instrucciones
1. Completen cada casillero con el nombre del sistema/herramienta que usan en su institución.
2. Si no tienen un sistema para esa función, escriban "MANUAL" o "NO EXISTE".
3. Para cada sistema, marquen: P = Propio | S = SaaS | L = Legacy (quieren reemplazarlo).
4. Dibujen las flechas de integración entre sistemas que SÍ se comunican.

---

## El ecosistema educativo

### Capa de contacto con el estudiante

```
┌─────────────────────────────────────────────────────────────────┐
│                    PORTALES / TOUCHPOINTS                       │
│                                                                 │
│  Web institucional: ___________________ (P / S / L)            │
│  Campus virtual:    ___________________ (P / S / L)            │
│  App móvil:         ___________________ (P / S / L)            │
│  E-commerce:        ___________________ (P / S / L)            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Sistemas core — Ciclo de vida del estudiante

```
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ MARKETING    │   │ ADMISIÓN E   │   │ CURSADO Y    │   │ EVALUACIÓN   │   │ TITULACIÓN   │
│ & CAPTACIÓN  │──▶│ INSCRIPCIÓN  │──▶│ AUTOGESTIÓN  │──▶│ & EXÁMENES   │──▶│ & EGRESO     │
│              │   │              │   │              │   │              │   │              │
│ Sistema:     │   │ Sistema:     │   │ Sistema:     │   │ Sistema:     │   │ Sistema:     │
│ ___________  │   │ ___________  │   │ ___________  │   │ ___________  │   │ ___________  │
│ (P / S / L)  │   │ (P / S / L)  │   │ (P / S / L)  │   │ (P / S / L)  │   │ (P / S / L)  │
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘
```

### Sistemas de soporte

```
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│     CRM      │   │     LMS      │   │     ERP      │   │   SOPORTE    │
│  (Marketing  │   │ (Plataforma  │   │ (Facturación │   │ (Tickets,    │
│  & Ventas)   │   │  de cursado) │   │  & Pagos)    │   │  consultas)  │
│              │   │              │   │              │   │              │
│ Sistema:     │   │ Sistema:     │   │ Sistema:     │   │ Sistema:     │
│ ___________  │   │ ___________  │   │ ___________  │   │ ___________  │
│ (P / S / L)  │   │ (P / S / L)  │   │ (P / S / L)  │   │ (P / S / L)  │
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘

┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│   GESTIÓN    │   │     BI /     │   │     IAM      │   │    OTRO      │
│   DOCENTE    │   │  REPORTES    │   │ (Identidad   │   │              │
│   (FIS/HR)   │   │              │   │  & Acceso)   │   │              │
│              │   │              │   │              │   │              │
│ Sistema:     │   │ Sistema:     │   │ Sistema:     │   │ Sistema:     │
│ ___________  │   │ ___________  │   │ ___________  │   │ ___________  │
│ (P / S / L)  │   │ (P / S / L)  │   │ (P / S / L)  │   │ (P / S / L)  │
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘
```

---

## Diagnóstico rápido

### ¿Quién es el "maestro de datos" del estudiante?

```
El sistema que tiene la versión más completa y confiable
de los datos del estudiante es: ___________________________

¿Todos los demás sistemas lo reconocen como fuente de verdad?  SÍ / NO / PARCIAL
```

### Integraciones

Dibujen flechas entre los sistemas que están integrados. Para cada integración, indiquen el mecanismo:

| Sistema A | Sistema B | Mecanismo |
|-----------|-----------|-----------|
| ___________ | ___________ | API / Archivo / Manual / Evento / Otro: ___ |
| ___________ | ___________ | API / Archivo / Manual / Evento / Otro: ___ |
| ___________ | ___________ | API / Archivo / Manual / Evento / Otro: ___ |
| ___________ | ___________ | API / Archivo / Manual / Evento / Otro: ___ |
| ___________ | ___________ | API / Archivo / Manual / Evento / Otro: ___ |

### Conteo

| Pregunta | Respuesta |
|----------|-----------|
| ¿Cuántos sistemas tienen en total? | ___ |
| ¿Cuántos están integrados entre sí? | ___ |
| ¿Cuántos quieren reemplazar (L)? | ___ |
| ¿Cuántos procesos siguen siendo manuales (Excel/email/WhatsApp)? | ___ |

---

## Top 3 dolores

Basándose en el mapa que acaban de completar, identifiquen los 3 mayores dolores:

| # | Dolor | Impacto en el negocio |
|---|-------|----------------------|
| 1 | _________________________________ | _________________________________ |
| 2 | _________________________________ | _________________________________ |
| 3 | _________________________________ | _________________________________ |

---

## Presentación al grupo (3 minutos)

Cada equipo comparte:
1. Su "descubrimiento" más importante al mapear la arquitectura.
2. Su dolor #1.
3. Una pregunta que les surgió.
