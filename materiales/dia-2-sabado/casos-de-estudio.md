# Casos de Estudio — Transformación Digital en Educación Superior LATAM

## Para usar en: Bloque 6 (Sábado, 10:15 - 10:45)

Se proponen 3 casos. Recomendamos usar **1 caso principal** durante la clase y dejar los otros 2 como lectura complementaria.

---

## Caso 1: Universidad Siglo 21 — "Educación en la nube" (Argentina)

### Recomendado como caso principal

> Este caso tiene la ventaja de que los facilitadores lo conocen en profundidad y pueden aportar detalles de primera mano que no están en ningún documento público.

### Contexto

Universidad Siglo 21, fundada en 1995, es la universidad privada federal más elegida de Argentina y una de las líderes en educación online en LATAM. Con presencia en todo el país a través de Centros de Aprendizaje Universitario (CAUs), su modelo combina educación presencial y a distancia.

### El problema

- La infraestructura tecnológica on-premise no escalaba al ritmo del crecimiento.
- Sistemas fragmentados: el SIS (Student Information System), el LMS, el CRM, el ERP y otros sistemas críticos operaban de forma desconectada.
- Los procesos de inscripción, examinación y seguimiento académico tenían componentes manuales que generaban fricciones.
- La institución necesitaba poner al estudiante en el centro de su operación digital.

### Las decisiones estratégicas

1. **Migración a la nube (AWS):** Trasladaron la plataforma educativa y los sistemas de gestión a Amazon Web Services, apostando por elasticidad, disponibilidad y escalabilidad.

2. **Desarrollo de un SIS propio (Proyecto Algarrobo):** En vez de comprar un SIS de mercado, optaron por desarrollar uno a medida con arquitectura cloud-native, basado en microservicios. La decisión clave: desacoplar los componentes para poder evolucionar cada vertical de forma independiente.

3. **Integración del ecosistema:** El SIS se convirtió en el sistema "maestro" de datos del estudiante, integrándose con:
   - CRM (HubSpot) para marketing y soporte
   - LMS (Canvas) para cursado
   - ERP (SAP) para facturación
   - AMS (SistemaQ) para exámenes
   - FIS (HR Factor) para gestión docente
   - BI para inteligencia de negocio
   - IAM para identidad y acceso

4. **Arquitectura cloud-native:** Microservicios, contenedores, DevOps, CI/CD. Cada vertical (Planificación, Vida Académica, Administración, Trámites) con su propia base de datos y ciclo de releases independiente.

### Resultados

| Métrica | Resultado |
|---------|-----------|
| Crecimiento de nuevos estudiantes | **+35% en un año** (hito histórico para una universidad privada argentina) |
| NPS (Net Promoter Score) | **+31** |
| Incidentes operativos | Reducción drástica |
| Conversión lead → estudiante | Aumento significativo |
| Capacidad de exámenes digitales | **+30.000 exámenes diarios, 10.000 usuarios simultáneos, 60.000+ estudiantes** |

### Lecciones clave

1. **Build vs Buy:** Construir un SIS propio permitió adaptar la solución exactamente al modelo de negocio, pero requirió inversión sostenida y talento técnico.
2. **El SIS como "maestro de datos":** Tener una fuente única de verdad del estudiante habilitó integraciones y análisis que antes eran imposibles.
3. **Cloud ≠ solo infraestructura:** La migración a la nube fue también un cambio cultural y de procesos (DevOps, CI/CD, equipos autónomos).
4. **Desacople = agilidad:** La arquitectura de microservicios permitió ejecutar un proyecto de "desacople" (Unplugged) que con un monolito hubiera tardado 1-2 años.

### Preguntas para la discusión

1. ¿Su institución enfrenta alguno de estos problemas hoy? ¿Cuál es el más urgente?
2. ¿Cuándo tiene sentido construir vs. comprar un sistema core como el SIS?
3. ¿Qué rol juega el SIS en su institución? ¿Es realmente el "maestro" de datos o hay múltiples fuentes de verdad?
4. ¿Qué decisiones de este caso aplicarían y cuáles no a su contexto?

### Fuentes
- [Bitlogic — Educación en la nube: el caso de Siglo 21 y AWS](https://es.bitlogic.io/blog/potenciando-la-universidad-siglo-21-con-amazon-web-services/)
- [Bitlogic — Exámenes digitales integrados al SIS](https://es.bitlogic.io/blog/innovacion-educativa-nueva-plataforma-de-evaluaciones-para-la-universidad-siglo-21/)
- SIS WhitePaper v0.2 (material del curso)

---

## Caso 2: Tecnológico de Monterrey — "TECgpt: IA al servicio de la educación" (México)

### Recomendado como caso complementario o para el bloque de IA

### Contexto

El Tecnológico de Monterrey es una de las instituciones de educación superior más prestigiosas de LATAM. Con 25+ campus, 90.000 estudiantes y 35.000 empleados (incluyendo 11.000 profesores), ha sido pionero en innovación educativa desde 1996 cuando fundó su universidad virtual.

### El desafío

En 2023, con la irrupción de la IA generativa, la institución enfrentó una pregunta estratégica:

> *"Sabíamos desde el principio que la IA era un fenómeno de tal magnitud que cuanto antes nos subiéramos al tren y diseñáramos nuestro propio camino, mejor."*
> — Carles Abarca, VP de Transformación Digital

Las opciones eran: (a) prohibir la IA, (b) ignorarla, (c) dejar que cada quien haga lo suyo, o (d) **construir un ecosistema propio institucional**.

### La apuesta: TECgpt

Eligieron la opción (d). En menos de un año, construyeron **TECgpt**, un ecosistema de IA generativa institucional:

**Stack tecnológico:**
- Azure OpenAI Service + GPT-4o
- Azure AI Content Safety para moderación
- Integración con datos institucionales internos

**Componentes:**

| Herramienta | Usuarios | Función |
|-------------|----------|---------|
| **Chat administrativo** | Estudiantes y empleados | Consultas en lenguaje natural sobre matrículas, becas, horarios. Interacciones anónimas. |
| **Chat general** | Todos | Acceso a datos externos, resumen de textos, generación de imágenes. |
| **Skill Studio** | Profesores | Creación de materiales didácticos, ejercicios, quizzes y exámenes con nivel de dificultad configurable. |
| **Academic TECbot** | Estudiantes | Tutor personalizado 24/7 que explica conceptos complejos. |
| **Librarian TECbot** | Todos | Búsqueda en 60+ millones de fuentes bibliográficas. |

### Resultados (a ~1 año del lanzamiento)

| Métrica | Resultado |
|---------|-----------|
| Usuarios mensuales activos | 3.000 (fase inicial) |
| Profesores usando Skill Studio | 200 |
| Skills generadas | 250+ |
| Estudiantes en piloto del TECbot | ~500 |
| Cobertura digital del catálogo | 45% de las materias tienen versión digital |
| Estudiantes servidos digitalmente | 86.000 (grado) + 20.000 (posgrado) |

### Decisiones clave de mindset

1. **Construir, no solo consumir:** No adoptaron ChatGPT genérico — construyeron su propio ecosistema con datos institucionales.
2. **Personalización por rol:** La experiencia es diferente si sos estudiante, profesor o empleado.
3. **Ética y transparencia:** Los estudiantes deben citar el uso de IA en trabajos académicos. Los datos administrativos se manejan anónimamente.
4. **Velocidad sobre perfección:** Lanzaron en beta, iteraron con feedback real de usuarios.

### Preguntas para la discusión

1. En el framework de adopción de IA del curso, ¿en qué nivel ubicarían al Tec de Monterrey?
2. ¿Su institución ha tomado una postura oficial sobre IA generativa? ¿Cuál de las 4 opciones (prohibir/ignorar/laissez-faire/ecosistema propio)?
3. ¿Qué componente de TECgpt les generaría más valor en su institución?
4. ¿Qué riesgos ven en esta estrategia?

### Fuentes
- [Microsoft News — Tecnológico de Monterrey pioneers AI-powered learning ecosystem](https://news.microsoft.com/source/latam/features/ai/tecnologico-de-monterrey-ai-ecosystem/?lang=en)
- [Tec Conecta — Six success stories applying AI](https://conecta.tec.mx/en/news/national/education/six-success-stories-tec-professors-applying-artificial-intelligence)
- [Issuu — Reporte de Innovación Educativa y Educación Digital 2024](https://issuu.com/innovacion-educativa/docs/reporte_ieed_2024)

---

## Caso 3: Platzi — "Educación que escala" (Colombia/LATAM)

### Recomendado como caso de contraste: nativo digital vs. institución tradicional

### Contexto

Platzi fue fundada en 2013 por Freddy Vega (Colombia) y Christian Van Der Henst (Guatemala). Fue la primera empresa de origen latino en ser aceptada en Y Combinator. Su misión: romper el ciclo de pobreza en LATAM a través de educación online efectiva.

### El modelo

A diferencia de una universidad tradicional que se digitaliza, Platzi nació digital:

- **Producto:** Cursos en vivo por streaming en español y portugués, enfocados en habilidades técnicas (programación, marketing, diseño, negocios).
- **Modelo de negocio:** Suscripción mensual/anual con acceso a todo el catálogo.
- **Escala:** 1+ millón de estudiantes en toda LATAM.
- **Financiamiento:** USD 62M en Serie B (2021), incluyendo inversión de Y Combinator.

### Métricas disruptivas

| Métrica | Platzi | Universidad promedio LATAM |
|---------|--------|---------------------------|
| Tasa de completación | 50-70% | ~15% (MOOCs promedio) |
| Tiempo para lanzar un curso nuevo | Días/semanas | Meses/años |
| Impacto en ingresos del estudiante | +54% a 10x en 1 año | Variable, años después |
| Presencia geográfica | Todo LATAM (100% online) | Local/regional |
| Costo para el estudiante | ~USD 50/mes | USD 200-2000+/mes |

### Las decisiones que los diferencian

1. **Orientación a producto, no a programa:** Cada curso es un producto que se mide, itera y mejora basándose en datos de completación, engagement y feedback.
2. **Tecnología propia de streaming:** Construyeron su propia plataforma de streaming optimizada para conexiones lentas de LATAM.
3. **Datos como motor:** Cada interacción del estudiante genera datos que alimentan mejoras al producto.
4. **Velocidad > perfección académica:** Pueden lanzar un curso sobre una tecnología nueva en días, mientras una universidad tarda semestres en actualizar un plan de estudios.

### El contraste con la educación tradicional

| Dimensión | Platzi (nativo digital) | Universidad tradicional |
|-----------|------------------------|------------------------|
| Organización | Equipos de producto | Departamentos académicos |
| Métrica de éxito | Completación + impacto laboral | Matrícula + títulos otorgados |
| Ciclo de actualización | Continuo | Semestral/anual |
| Relación con el estudiante | Producto + comunidad | Administrativa |
| Tecnología | Core del negocio | Soporte al negocio |

### Preguntas para la discusión

1. ¿Platzi es competencia de sus instituciones? ¿Por qué sí o por qué no?
2. ¿Qué prácticas de Platzi podrían adoptar en una universidad tradicional? ¿Cuáles son imposibles de trasladar?
3. ¿La "orientación a producto" es compatible con la misión educativa de una universidad?
4. Si Platzi decidiera otorgar títulos universitarios, ¿cómo cambiaría el panorama competitivo?

### Fuentes
- [EdSurge — Platzi Raises $6 Million](https://www.edsurge.com/news/2019-06-18-platzi-raises-6-million-to-bring-more-online-education-to-latin-america)
- [TechCrunch — Platzi picks up $62M Series B](https://techcrunch.com/2021/12/06/platzi-picks-up-62-million-series-b-to-re-skill-latin-american-professionals/)
- [Al Día News — Freddy Vega interview](https://aldianews.com/en/leadership/entrepreneurs/educational-revolution)

---

## Recomendación de uso

| Momento del curso | Caso sugerido | Foco |
|-------------------|---------------|------|
| Bloque 3 (Arquitectura IT) | **Siglo 21** — como ejemplo de ecosistema SIS-céntrico | Arquitectura + integración |
| Bloque 4 (IA) | **Tec de Monterrey** — como ejemplo de adopción institucional de IA | IA + estrategia |
| Bloque 6 (Mindset Digital) | **Platzi** — como contraste de mindset nativo digital | Producto + datos + velocidad |
| Challenge | Los 3 como inspiración para los entregables | Integración de conceptos |

Con esta distribución, cada caso aparece en el momento del curso donde más valor aporta, y se refuerzan mutuamente.
