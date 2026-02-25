# Módulo 3 — Arquitectura IT Educativa

---

## 1 Introduccion

### 1.1 Objetivo del módulo
Que los participantes puedan **leer, cuestionar y discutir** la arquitectura tecnológica de una organización, aunque no sean técnicos. No se trata de aprender a diseñar sistemas, sino de entender cómo funcionan por dentro para tomar mejores decisiones y hacer mejores preguntas.

La arquitectura IT no es un tema de infraestructura. Es un tema de gobierno, competitividad y riesgo estratégico.

---

### 1.2 Pregunta guía

> ¿Cómo funciona realmente una institución educativa moderna por dentro?

---

### 1.3 Dinámica Disparadora "Tu Stack en una servilleta" 

TODO: agregar intro y link a dinamica "tu-stack-en-servilleta.md"
---

## 2 Conceptos claves

### 1. ¿Qué es una arquitectura IT?

Una arquitectura IT es el **mapa** de todos los sistemas tecnológicos de una organización: qué sistemas existen, qué hace cada uno, cómo se conectan entre sí y cómo fluye la información.


TODO:  Agregar imagen campus-03

**Analogía:** pensá en tu organización como el campus.
- Los "sistemas" son los espacios o edificios (cada uno cumple una función especifica). Biblioteca, Bedelia, Administracion, Rectoria, etc. 
- Las integraciones son los pasillos (conectan los edificios entre sí). E.g. no cumplen ninguna funcion mas que llevar datos de un lugar a otro.
- Los datos son las personas que circulan por el campus (si los pasillos están cortadas, no llegan a destino).
- La arquitectura IT es el plano de la campus completo.

Un directivo no necesita saber construir edificios. Pero sí necesita poder leer el plano de la ciudad para decidir dónde construir el próximo, cuál demoler y cuál renovar.

**¿Por qué importa entender la arquitectura?**

Porque las decisiones de arquitectura tienen consecuencias que se extienden por años. Una institución que elige un SIS sin pensar en integraciones va a pagar ese error durante una década. Una que construye sus sistemas como islas va a necesitar personas que "traducen" entre sistemas — generando cuellos de botella, errores y dependencias de individuos específicos.

La arquitectura no solo determina cómo funciona la tecnología. Determina qué es posible hacer como organización.

> 💡 **Para participantes de empresas no educativas:** Los conceptos de arquitectura IT son universales. Donde dice "estudiante", pensá en "cliente" o "usuario". Donde dice "SIS", pensá en tu sistema core de gestión. El principio es el mismo: los sistemas deben estar integrados y alineados al negocio.

---

### 2. Los sistemas clave de una organización educativa

Toda organización educativa moderna opera con un ecosistema de sistemas. Los principales son:

| Sistema | Qué hace | Analogía |
|---------|----------|----------|
| **CMS** (Content Management System) | Presenta la Institución en la web, publica la oferta académica y puede contener el e-commerce | El "sitio" de la Institución |
| **SIS** (Student Information System) | Gestiona toda la vida académica del estudiante: inscripción, cursada, notas, título | El "DNI" del estudiante en la institución |
| **LMS** (Learning Management System) | Plataforma donde se da la experiencia de aprendizaje: contenidos, actividades, foros | El "aula" virtual |
| **EXAM** (Exam & Proctoring) | Plataforma de examinación segura, con auditorías de fraude | La validación del proceso de aprendizaje |
| **CRM** (Customer Relationship Management) | Gestiona la relación con prospectos y estudiantes: campañas, seguimiento, comunicación | La "memoria" de todas las interacciones |
| **ERP** (Enterprise Resource Planning) | Gestiona administración y finanzas: facturación, pagos, contabilidad, RRHH | La "administración" del negocio |
| **BI** (Business Intelligence) | Analítica y reportes: dashboards, indicadores, tendencias | Los "ojos" de la organización |
| **IA** (Inteligencia Artificial) | Capa transversal: chatbots, analítica predictiva, personalización | El "asistente inteligente" |

#### Un zoom sobre el SIS: el sistema más estratégico

El Student Information System (SIS) merece atención especial porque es el **sistema de registro oficial** de la institución. No es una herramienta de soporte — es el núcleo del modelo académico.

Un SIS bien implementado:
- Reduce errores en la gestión de matrículas y calificaciones
- Permite automatizar flujos administrativos (inscripciones, actas, diplomas)
- Habilita la toma de decisiones basada en datos reales del estudiante
- Es la fuente de verdad que alimenta al LMS, CRM, ERP y BI

Un SIS mal implementado (o ausente) se convierte en un laberinto de Excel, correos y trámites manuales que escala de forma lineal: más estudiantes = más personas procesando datos. No hay crecimiento sostenible sin un SIS sólido.

**Ejemplo:** Universidad Siglo 21 decidió construir su propio SIS (Proyecto Algarrobo) porque ninguna solución de mercado se adaptaba a su modelo federal con más de 15 sedes y modalidades mixtas. La inversión fue significativa pero estratégica: permitió pasar de 30.000 a 60.000+ estudiantes sin perder control operativo.

#### ¿Qué pasa con el LMS?

El LMS (Learning Management System) es la cara visible de la institución para el estudiante. Sin embargo, muchas instituciones cometen el error de tratar el LMS como un repositorio de PDFs y videos — cuando su verdadero valor está en los **datos de aprendizaje** que genera.

Un LMS moderno bien utilizado produce:
- Datos de engagement (¿el estudiante abrió el material? ¿cuánto tiempo estuvo activo?)
- Señales de riesgo (¿no ingresa hace 5 días? ¿no entregó la tarea?)
- Datos de desempeño (¿en qué conceptos tiene más dificultad?)

Cuando esos datos se conectan con el CRM, se puede intervenir antes de que el estudiante abandone. Cuando se conectan con BI, se pueden tomar decisiones de diseño curricular basadas en evidencia.

**El LMS no es un aula virtual. Es un generador de inteligencia sobre el aprendizaje.** La diferencia entre usarlo como repositorio vs. como sistema de datos es la diferencia entre digitalizar y transformar.

---

### 3. El ciclo de vida del estudiante visto desde los sistemas

La experiencia del estudiante es un viaje que atraviesa múltiples sistemas. Cada etapa depende de que los sistemas correctos funcionen y estén conectados:

```
Captación → Evaluación → Admisión → Onboarding → Cursada → Servicios al Est → Evaluación → Graduación → Alumni
 CRM/Mktg     CMS/Web      SIS        SIS/LMS      LMS       CRM/Services        EXAM        SIS         CRM
```

**Los problemas reales surgen en las transiciones:**
- El prospecto que se inscribe en el CRM pero sus datos no llegan al SIS → tiene que cargar todo de nuevo.
- El estudiante que aprueba en el LMS pero la nota no se refleja en el SIS → necesita un trámite manual.
- El graduado que no recibe seguimiento porque el CRM no tiene datos de ex-alumnos → oportunidad perdida.

Cada una de estas transiciones que falla tiene un nombre en el negocio: **fricción**. Y la fricción tiene costos directos (tiempo operativo, errores, reclamos) e indirectos (NPS, deserción, reputación).

Un estudio de Salesforce encontró que el 76% de los clientes espera interacciones consistentes entre áreas. En educación, el equivalente es que el asesor académico, el sistema de pagos y la plataforma de aprendizaje "conozcan" al mismo estudiante. Cuando no es así, el estudiante lo nota — y eventualmente se va.

#### 3.1 El "doble-click" en la plataforma Core: el SIS

El "Student Information System" es el sistema Core: modela la estrategia académica y los procesos académicos más importantes.

![Funcionalidades del SIS.](https://github.com/alfredoedye/business-tech-strategy/blob/main/assets/Funcionalidades%20SIS.png)

---

### 4. Cuadrante de Tecnología en Modelo MII

El modelo MII, en su cuadrante de Tecnología define la línea base de stack tecnológico para el grupo R'Evolution, como la arquitectura recomendada y deseada en cada institución, para garantizar la calidad y excelencia en la experiencia del estudiante, y la escalabilidad y eficiencia en su modelo académico mediado por tecnología.

![Linea base](https://github.com/alfredoedye/business-tech-strategy/blob/main/assets/Linea%20base%20Revolution.png)

---

### 5. Integraciones: el sistema nervioso de la organización

Los sistemas individuales son importantes, pero lo que realmente define la madurez de una arquitectura es **cómo se conectan entre sí**.

**Cada quiebre en la integración es una mala experiencia para el estudiante y un costo operativo para la organización.**

Hay cuatro niveles de integración, y cada salto hacia arriba representa un cambio cualitativo — no solo de velocidad, sino de qué es posible hacer:

| Nivel | Cómo funciona | Ejemplo | Limitación |
|-------|--------------|---------|------------|
| **Manual** | Alguien exporta un Excel y lo importa en otro sistema | Pasar notas del LMS al SIS a mano | Errores humanos, lentitud, escala lineal |
| **Archivos** | Un sistema genera un archivo que otro consume automáticamente | CSV de inscriptos que se importa cada noche | Datos desactualizados, sin tiempo real |
| **APIs** | Los sistemas se hablan en tiempo real | Cuando un estudiante se inscribe en el SIS, automáticamente se crea su cuenta en el LMS | Requiere desarrollo técnico, documentación |
| **Eventos** | Los sistemas reaccionan a lo que pasa en otros sistemas | Cuando un estudiante no ingresa al LMS en 7 días, el CRM genera una alerta automática | Mayor complejidad arquitectural |

**¿Qué significa pasar de manual a APIs en la práctica?**

Una institución con 10.000 estudiantes que procesa notas manualmente necesita aproximadamente 3 personas trabajando a tiempo parcial en ese proceso. Con integración por APIs, ese proceso es instantáneo y libre de errores. El ahorro no es solo de tiempo: es de riesgo. Los errores en datos académicos tienen consecuencias legales y reputacionales.

Pero la integración no es solo un tema técnico. **Es un tema de gobierno.** Alguien tiene que decidir quién es el "dueño" de cada dato, qué sistema es la fuente de verdad, y qué pasa cuando dos sistemas tienen información contradictoria sobre el mismo estudiante.

#### El concepto de "fuente de verdad única" (Single Source of Truth)

Una de las causas más comunes de caos en organizaciones educativas es tener el mismo dato en múltiples sistemas — y que esos datos no coincidan.

¿La fecha de nacimiento del estudiante está en el SIS, en el CRM o en ambos? ¿Cuál es la correcta si difieren? ¿Qué pasa si el estudiante cambia su email en uno pero no en el otro?

La arquitectura madura define para cada dato cuál es el sistema maestro (la fuente de verdad) y cómo se propaga esa información al resto de los sistemas. Sin esa definición, cada área trabaja con su propia "versión de la verdad" — y las decisiones se toman sobre datos inconsistentes.

**Para el líder ejecutivo, las preguntas clave son:**
- ¿Cuántos procesos dependen de carga manual? (Cada uno es un riesgo y un costo)
- ¿Los datos del estudiante están en un solo lugar o fragmentados en 5 sistemas?
- ¿Cuánto tiempo pasa entre que algo sucede y se refleja en todos los sistemas?
- ¿Si mañana un estudiante llama preguntando por su situación, cuántos sistemas hay que consultar?

---

### 6. La arquitectura como herramienta de decisión

Una arquitectura IT bien entendida permite al líder evaluar y anticipar problemas antes de que se conviertan en crisis.

**Escalabilidad:** ¿puede mi infraestructura soportar el doble de estudiantes? ¿O necesito cambiar sistemas antes de crecer?

Muchas instituciones descubren sus limitaciones de arquitectura en el peor momento posible: durante un período de inscripción récord, en el que el sistema se cae bajo la carga, o cuando una fusión con otra institución revela que los sistemas son incompatibles. La arquitectura pensada con anticipación convierte el crecimiento en una oportunidad en lugar de una crisis.

**Gobierno:** ¿quién es el "dueño" de cada dato? ¿Quién decide qué sistema se reemplaza? ¿Hay una visión unificada o cada área compra lo que necesita?

El "shadow IT" — sistemas comprados por áreas sin coordinación con IT — es uno de los riesgos más subestimados en organizaciones educativas. Marketing compra su herramienta de email. Académico compra su plataforma de contenidos. Finanzas su sistema de pagos. El resultado: 15 sistemas, 3 integrados, datos en silos y nadie con la visión completa.

**Costos:** ¿cuánto cuesta mantener sistemas que no se integran? ¿Cuántas horas-persona se pierden en procesos manuales que podrían automatizarse?

McKinsey estima que la deuda técnica consume en promedio el 40% del presupuesto de IT en empresas medianas. En educación, esa deuda se manifiesta en sistemas legacy que "nadie quiere tocar" porque hay un solo técnico que los entiende, en procesos manuales que consumen horas que podrían ir a innovación, y en la incapacidad de responder rápidamente a cambios del mercado.

**Riesgo:** ¿qué pasa si cae el sistema central? ¿Hay plan B? ¿Los datos están respaldados?

La continuidad operativa es una conversación que muchos equipos directivos evitan porque implica invertir en algo que "puede que nunca se necesite". Hasta que se necesita. Un ransomware que cifra los datos de 50.000 estudiantes, un data center que pierde energía durante un período de exámenes, una actualización mal ejecutada que corrompe la base de datos de matrículas — son escenarios que ocurren, y que sin un plan de recuperación pueden convertirse en crisis institucionales.

---

## Dinámica: "Mapeá tu arquitectura"

**Duración:** 40 minutos (20 individual/grupal + 20 presentación y debate)

**Instrucciones:**
1. Cada participante (o grupo por institución) completa el [Template Mapa de Arquitectura IT](../materiales/templates/template-mapa-arquitectura-it.md).
2. Mapear:
   - Qué sistemas tiene la organización.
   - Cómo se conectan (o no).
   - Cuál es el "dueño" de los datos del estudiante.
   - Los top 3 dolores.
3. Cada grupo presenta en 3 minutos:
   - Su descubrimiento principal.
   - Su dolor #1.
   - La pregunta que se llevan.

**Debrief facilitador:**
- Buscar patrones comunes entre las organizaciones.
- Señalar que mapear la arquitectura es un acto de gobierno, no un ejercicio técnico.
- Destacar que muchos líderes hacen este ejercicio por primera vez — y eso es parte del problema.

---

## Resultado esperado

Al terminar este módulo, el participante:

- Puede nombrar y describir los sistemas principales de una institución educativa (SIS, LMS, CRM, ERP, BI, EXAM).
- Entiende el ciclo de vida del estudiante como un flujo que depende de la integración entre sistemas.
- Puede leer un mapa de arquitectura IT y hacer preguntas relevantes.
- Comprende el concepto de "fuente de verdad única" y sus implicancias para la toma de decisiones.
- Tiene un diagnóstico visual de su propia arquitectura, con brechas y dolores identificados.
- Comprende que la arquitectura no es un tema de IT — es un tema de gobierno y competitividad.

---

## Reflexión final

> La arquitectura IT de tu institución es como el sistema circulatorio de una persona.
> Cuando funciona bien, no lo notás.
> Cuando falla, todo se detiene.
> ¿Sabés cómo está el tuyo?

---

## Referencias y lecturas recomendadas

### Frameworks y metodologías
- **TOGAF (The Open Group Architecture Framework):** El framework más utilizado para diseñar arquitecturas IT empresariales. Su versión simplificada es una excelente referencia para líderes no técnicos. [opengroup.org/togaf](https://www.opengroup.org/togaf)
- **Wardley Maps:** Metodología para visualizar el estado de una arquitectura tecnológica y su evolución estratégica. Creada por Simon Wardley. [learnwardleymapping.com](https://learnwardleymapping.com)

### Sistemas educativos (SIS / LMS)
- **Ellucian:** El proveedor de SIS más grande del mercado para educación superior. Sus reportes anuales sobre tendencias tecnológicas en educación son una referencia clave. [ellucian.com](https://www.ellucian.com)
- **Instructure (Canvas):** Uno de los LMS líderes globales. Sus estudios sobre engagement estudiantil y uso de datos de aprendizaje son valiosos. [instructure.com](https://www.instructure.com)
- **Moodle:** La plataforma LMS open source más utilizada en LATAM. [moodle.org](https://moodle.org)

### Integraciones y arquitectura de datos
- **"Designing Data-Intensive Applications" — Martin Kleppmann (2017):** El libro de referencia sobre cómo construir sistemas que manejan datos a escala. Técnico pero accesible para líderes con curiosidad.
- **APIs and the Modern EdTech Stack — EDUCAUSE:** Reportes sobre cómo las instituciones están modernizando su arquitectura con APIs. [educause.edu](https://www.educause.edu)

### Casos de estudio
- **Salesforce Research — "State of the Connected Customer":** Estadísticas sobre expectativas de los clientes en experiencias conectadas, aplicables directamente a la experiencia del estudiante. [salesforce.com/research](https://www.salesforce.com/research)
- **McKinsey — "Curing the Addiction to Growth":** Análisis sobre deuda técnica y su impacto en organizaciones. [mckinsey.com/capabilities/mckinsey-digital](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights)

### Gobernanza de datos en educación
- **FERPA (Family Educational Rights and Privacy Act):** El marco regulatorio de EE.UU. para privacidad de datos educativos, referencia global. [studentprivacy.ed.gov](https://studentprivacy.ed.gov)
- **IMS Global Learning Consortium:** Estándares de interoperabilidad para sistemas educativos (APIs, formatos de datos). [imsglobal.org](https://www.imsglobal.org)

---

*Anterior: [← Módulo 2 — Estrategia Tecnológica](modulo-02-estrategia-tecnologica.md)*
*Siguiente: [Módulo 4 — Transformación Digital e IA →](modulo-04-transformacion-digital-ia.md)*
