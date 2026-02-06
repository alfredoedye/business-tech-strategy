# Anexo — Frameworks Estratégicos de Referencia

> Este anexo complementa el Módulo 2 (Estrategia Tecnológica) con frameworks reconocidos internacionalmente que permiten hablar un lenguaje común con consultores, vendors y pares de la industria.

---

## 1. Wardley Mapping — Visualizar la Evolución Tecnológica

### ¿Qué es?

Wardley Mapping es una técnica de visualización estratégica creada por Simon Wardley que permite mapear los componentes de un negocio según dos ejes:

- **Eje Y (Visibilidad):** Qué tan visible es el componente para el usuario final
- **Eje X (Evolución):** En qué etapa de madurez se encuentra

### Las 4 etapas de evolución

```
GÉNESIS ────────► CUSTOM ────────► PRODUCTO ────────► COMMODITY
(Nuevo, único)    (A medida)      (Diferenciado)     (Estándar)

Características:
- Incertidumbre    - Específico      - Competitivo      - Estandarizado
- Experimentación  - Costoso         - Diferenciado     - Barato
- Alto riesgo      - Requiere skills - Muchos vendors   - Utility/SaaS
```

### Ejemplo aplicado a educación

| Componente | Hace 10 años | Hoy | En 5 años |
|------------|--------------|-----|-----------|
| LMS | Custom → Producto | Producto → Commodity | Commodity |
| Analítica predictiva | Génesis | Custom → Producto | Producto |
| Tutor IA personalizado | No existía | Génesis → Custom | Producto |
| Email | Producto | Commodity | Commodity |
| Campus virtual | Custom | Producto | Commodity |

### Implicancias para decisiones

| Etapa | Estrategia de sourcing | Inversión |
|-------|------------------------|-----------|
| **Génesis** | Build (si es core) o piloto con startup | Alta incertidumbre, bajo volumen |
| **Custom** | Build si es diferenciador, partner si no | Media-alta, requiere equipo |
| **Producto** | Buy y personalizar | Media, selección de vendor |
| **Commodity** | Buy estándar (SaaS) | Baja, optimizar costo |

### La pregunta clave

> "¿Estamos invirtiendo en construir algo que en 3 años será commodity? ¿O estamos comprando commodity algo que debería ser nuestro diferenciador?"

---

## 2. Gartner Hype Cycle — Ubicar Tecnologías en su Ciclo

### ¿Qué es?

El Hype Cycle de Gartner es un modelo que describe las fases típicas que atraviesa una tecnología desde su concepción hasta su adopción madura.

### Las 5 fases

```
                    PICO DE
                  EXPECTATIVAS
                  INFLADAS
                      /\
                     /  \
                    /    \
                   /      \    RAMPA DE
    DISPARADOR    /        \   ILUMINACIÓN
    TECNOLÓGICO  /          \     /
        •       /            \   /     MESETA DE
               /              \ /      PRODUCTIVIDAD
              /                X        ___________
             /            ABISMO DE    /
            /             DESILUSIÓN  /
           /                         /
──────────/─────────────────────────/────────────────►
                                                  TIEMPO
```

### Fases explicadas

| Fase | Qué pasa | Riesgo para el líder |
|------|----------|---------------------|
| **1. Disparador** | Nueva tecnología emerge, mucha prensa | Invertir demasiado temprano |
| **2. Pico de expectativas** | Sobreexcitación, promesas exageradas | Creer el hype, sobreinvertir |
| **3. Abismo de desilusión** | Los pilotos fallan, la prensa es negativa | Abandonar prematuramente |
| **4. Rampa de iluminación** | Casos de éxito reales, mejores prácticas | No retomar a tiempo |
| **5. Meseta de productividad** | Adopción mainstream, valor comprobado | Llegar tarde, perder ventaja |

### IA Generativa en Educación (2024-2025)

**Ubicación actual:** Pasando del Pico de Expectativas hacia el Abismo de Desilusión

**Implicancias:**
- Los pilotos iniciales están mostrando resultados mixtos
- Las expectativas se están ajustando a la realidad
- Es el momento de invertir con criterio, no de abandonar
- Las instituciones que persistan saldrán fortalecidas

### La pregunta clave

> "¿Estamos invirtiendo porque hay valor real o porque hay hype? ¿Tenemos la paciencia para atravesar el abismo de desilusión?"

---

## 3. TOGAF Simplificado — Arquitectura Empresarial

### ¿Qué es?

TOGAF (The Open Group Architecture Framework) es el framework más usado para arquitectura empresarial. Para ejecutivos, lo relevante es entender sus 4 dominios.

### Los 4 dominios de arquitectura

```
┌─────────────────────────────────────────────────────────────┐
│                  ARQUITECTURA DE NEGOCIO                     │
│     Estrategia • Procesos • Capacidades • Organización      │
├─────────────────────────────────────────────────────────────┤
│                  ARQUITECTURA DE DATOS                       │
│     Entidades • Flujos • Gobernanza • Calidad               │
├─────────────────────────────────────────────────────────────┤
│               ARQUITECTURA DE APLICACIONES                   │
│     Sistemas • Integraciones • Portafolio • Roadmap         │
├─────────────────────────────────────────────────────────────┤
│                ARQUITECTURA TECNOLÓGICA                      │
│     Infraestructura • Redes • Seguridad • Cloud             │
└─────────────────────────────────────────────────────────────┘
```

### Las preguntas por dominio

| Dominio | Pregunta ejecutiva clave |
|---------|-------------------------|
| **Negocio** | ¿Nuestra arquitectura tech soporta la estrategia de negocio? |
| **Datos** | ¿Tenemos una única fuente de verdad para decisiones clave? |
| **Aplicaciones** | ¿Nuestros sistemas se comunican o son silos? |
| **Tecnología** | ¿Nuestra infraestructura puede escalar al ritmo del negocio? |

### ADM: El ciclo de arquitectura

```
            ┌─────────────────┐
            │    VISIÓN       │
            │  (Fase A)       │
            └────────┬────────┘
                     │
    ┌────────────────┼────────────────┐
    │                │                │
    ▼                ▼                ▼
┌───────┐      ┌───────┐      ┌───────┐
│NEGOCIO│      │ DATOS │      │  IT   │
│(Fase B│◄────►│(Fase C│◄────►│(Fase D│
│   )   │      │   )   │      │   )   │
└───┬───┘      └───┬───┘      └───┬───┘
    │              │              │
    └──────────────┼──────────────┘
                   │
            ┌──────▼──────┐
            │IMPLEMENTACIÓN│
            │  (Fases E-G) │
            └─────────────┘
```

### La pregunta clave

> "¿Tenemos una visión de arquitectura que conecte la estrategia de negocio con las decisiones tecnológicas? ¿O cada proyecto decide su propia arquitectura?"

---

## 4. Modelo de Madurez Digital (Deloitte/MIT)

### ¿Qué es?

Un framework para evaluar qué tan avanzada está una organización en su transformación digital, basado en dos dimensiones:

- **Intensidad Digital:** Inversión en iniciativas tecnológicas
- **Intensidad de Transformación:** Capacidad de liderazgo para impulsar el cambio

### La matriz de madurez

```
                        INTENSIDAD DE TRANSFORMACIÓN
                        (Liderazgo, Cultura, Governance)
                              BAJA          ALTA
                         ┌───────────┬───────────┐
              ALTA       │FASHIONISTA│  DIGIRATI │
   INTENSIDAD            │ Mucha tech│ Tech +    │
   DIGITAL               │ sin rumbo │ liderazgo │
   (Inversión            ├───────────┼───────────┤
    en tech)    BAJA     │ BEGINNER  │CONSERVATIVE│
                         │ Sin tech  │ Liderazgo │
                         │ ni vision │ sin tech  │
                         └───────────┴───────────┘
```

### Características de cada cuadrante

| Cuadrante | Características | Riesgo |
|-----------|-----------------|--------|
| **Beginners** | Poca inversión digital, sin visión clara | Quedarse atrás |
| **Fashionistas** | Mucha inversión tech pero sin estrategia | Malgastar recursos |
| **Conservatives** | Buen liderazgo pero poca inversión tech | Perder oportunidades |
| **Digirati** | Inversión + liderazgo alineados | El objetivo |

### Autoevaluación rápida

**Intensidad Digital (0-5):**
- [ ] Tenemos sistemas modernos integrados
- [ ] Usamos datos para decisiones
- [ ] Automatizamos procesos clave
- [ ] Experimentamos con tecnologías nuevas
- [ ] Tenemos presupuesto dedicado a innovación tech

**Intensidad de Transformación (0-5):**
- [ ] El liderazgo tiene visión digital clara
- [ ] Hay governance de tecnología
- [ ] La cultura acepta experimentación
- [ ] Hay talento digital en roles clave
- [ ] Los incentivos están alineados con transformación

### La pregunta clave

> "¿Somos Digirati, o estamos gastando en tecnología sin transformar el negocio (Fashionistas)?"

---

## 5. Business Model Canvas + Tech Stack

### ¿Qué es?

Una extensión del Business Model Canvas de Osterwalder que conecta cada bloque del modelo de negocio con los sistemas tecnológicos que lo habilitan.

### Canvas integrado

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ PARTNERS CLAVE        │ ACTIVIDADES CLAVE      │ PROPUESTA DE VALOR         │
│ ¿Con quién?           │ ¿Qué hacemos?          │ ¿Qué ofrecemos?            │
│                       │                        │                            │
│ Tech: Integraciones   │ Tech: Workflows,       │ Tech: LMS, Plataforma      │
│ APIs, Vendors         │ Automatización         │ de experiencia             │
├───────────────────────┼────────────────────────┼────────────────────────────┤
│ RECURSOS CLAVE        │                        │ RELACIÓN CON CLIENTE       │
│ ¿Qué necesitamos?     │                        │ ¿Cómo nos relacionamos?    │
│                       │                        │                            │
│ Tech: Infraestructura │                        │ Tech: CRM, Chatbots,       │
│ Datos, Talento IT     │                        │ Comunicaciones             │
├───────────────────────┴────────────────────────┼────────────────────────────┤
│ ESTRUCTURA DE COSTOS                           │ FUENTES DE INGRESOS        │
│ ¿Cuánto cuesta?                                │ ¿Cómo monetizamos?         │
│                                                │                            │
│ Tech: TCO de sistemas, Licencias, Infra        │ Tech: E-commerce, Billing  │
└────────────────────────────────────────────────┴────────────────────────────┘
```

### Mapeo para institución educativa

| Bloque del Canvas | Sistemas involucrados |
|-------------------|----------------------|
| Propuesta de valor | LMS, Contenido, Plataforma de experiencia |
| Segmentos de cliente | CRM (segmentación), Analytics |
| Canales | Web, App, Campus virtual, Marketing automation |
| Relación con cliente | CRM, Soporte, Chatbots, Comunicaciones |
| Fuentes de ingreso | E-commerce, ERP (facturación), Pasarelas de pago |
| Recursos clave | SIS, Infraestructura, Datos, IAM |
| Actividades clave | Workflows, Integraciones, Automatización |
| Partners clave | APIs, Integraciones con terceros |
| Estructura de costos | Licencias, Infraestructura, Equipo IT |

### La pregunta clave

> "¿Cada bloque de nuestro modelo de negocio está habilitado por tecnología? ¿Dónde están los gaps?"

---

## Cómo usar estos frameworks

### En una conversación con consultores

| Si te dicen... | Podés preguntar... |
|----------------|-------------------|
| "Necesitan modernizar" | "¿Dónde estamos en el Wardley Map? ¿Qué debemos build vs buy?" |
| "Esta tecnología es el futuro" | "¿Dónde está en el Hype Cycle? ¿Ya pasó el abismo de desilusión?" |
| "Hay que rediseñar la arquitectura" | "¿Qué dominio de TOGAF priorizamos? ¿Datos, aplicaciones, infra?" |
| "Están atrasados digitalmente" | "¿Somos Beginners o Conservatives? ¿Qué eje debemos mejorar?" |

### En una decisión de inversión

1. **Ubicar en Wardley:** ¿Es génesis, custom, producto o commodity?
2. **Evaluar Hype Cycle:** ¿Estamos comprando en el pico o en la meseta?
3. **Revisar arquitectura:** ¿Cómo impacta en los 4 dominios de TOGAF?
4. **Medir madurez:** ¿Esta inversión nos mueve hacia Digirati?

---

## Recursos para profundizar

| Framework | Recurso recomendado |
|-----------|---------------------|
| Wardley Mapping | [learnwardleymapping.com](https://learnwardleymapping.com/) — Curso gratuito |
| Gartner Hype Cycle | Informes anuales de Gartner (buscar "Hype Cycle for Education") |
| TOGAF | [The Open Group](https://www.opengroup.org/togaf) — Versión simplificada |
| Madurez Digital | MIT Sloan + Deloitte — "Strategy, not Technology, Drives Digital Transformation" |
| Business Model Canvas | Strategyzer — [strategyzer.com](https://www.strategyzer.com/) |

---

*Este anexo complementa el Módulo 2. Para volver: [← Módulo 2 — Estrategia Tecnológica](modulo-02-estrategia-tecnologica.md)*
