# Módulo 3 — Arquitectura IT Educativa

---

## Objetivo del módulo

Que los participantes puedan **leer, cuestionar y discutir** la arquitectura tecnológica de una organización, aunque no sean técnicos. No se trata de aprender a diseñar sistemas, sino de entender cómo funcionan por dentro para tomar mejores decisiones y hacer mejores preguntas.

---

## Pregunta guía

> ¿Cómo funciona realmente una institución educativa moderna por dentro?

---

### Dinámica Disparadora 

Es el último día de exámenes finales y miles de estudiantes acceden al sistema de exámenes.
El sistema de Examinación + Proctoring se cae, las notas no se guardan, estudiantes protestan, redes sociales estallan.
El call center no pueden comunicarse con el CRM para gestionar reclamos y los sistemas internos no tienen unificadas los datos de los estudiantes

#### Se divide a los directivos en 3 grupos:
#### Grupo 1 --- Académico
-   ¿Qué perciben los estudiantes?
-   ¿Qué impacta en la calidad de servicio?
  
#### Grupo 2 --- Operaciones / Tecnología
-   ¿Qué falló a nivel de sistema y flujos de datos?
-   ¿Qué dependencias existen entre Examinación/Proctoring y otros sistemas?

#### Grupo 3 --- Negocio / Dirección
-   ¿Cuánto puede costar esta crisis?
-   ¿Qué decisiones deberían haberse tomado antes?
------------------------------------------------------------------------
#### Salidas de la Dinamica
   Principales puntos de falla (técnicos y de negocio)
   Decisiones que hubieran evitado el problema
   2 prioridades inmediatas para mitigarlo

El facilitador cierra conectando cada punto con la arquitectura de sistemas (qué es, cómo se mapea, dónde están las fronteras e interdependencias)

---

## Conceptos clave

### 1. ¿Qué es una arquitectura IT?

Una arquitectura IT es el **mapa** de todos los sistemas tecnológicos de una organización: qué sistemas existen, qué hace cada uno, cómo se conectan entre sí y cómo fluye la información.

**Analogía:** pensá en tu organización como una ciudad.
- Los sistemas son los edificios (cada uno cumple una función).
- Las integraciones son las calles (conectan los edificios entre sí).
- Los datos son las personas que circulan por la ciudad (si las calles están cortadas, no llegan a destino).
- La arquitectura IT es el plano de la ciudad completa.

Un directivo no necesita saber construir edificios. Pero sí necesita poder leer el plano de la ciudad para decidir dónde construir el próximo, cuál demoler y cuál renovar.

> 💡 **Para participantes de empresas no educativas:** Los conceptos de arquitectura IT son universales. Donde dice "estudiante", pensá en "cliente" o "usuario". Donde dice "SIS", pensá en tu sistema core de gestión. El principio es el mismo: los sistemas deben estar integrados y alineados al negocio.

### 2. Los sistemas clave de una organización educativa

Toda organización educativa moderna opera con un ecosistema de sistemas. Los principales son:

| Sistema | Qué hace | Analogía |
|---------|----------|----------
| **CMS** (Content Managemnt System) | Presenta la Institución en la WEB, publica la oferta académica y puede contener el e-commerce  | El "sitio" de la Institución |
| **SIS** (Student Information System) | Gestiona toda la vida académica del estudiante: inscripción, cursada, notas, título | El "DNI" del estudiante en la institución |
| **LMS** (Learning Management System) | Plataforma donde se da la experiencia de aprendizaje: contenidos, actividades, foros | El "aula" virtual |
| **EXAM** (Exam & Proctoring) | Plataforma de examinación segura, con auditorías de fraude | La validación del proceso de aprendizaje |
| **CRM** (Customer Relationship Management) | Gestiona la relación con prospectos y estudiantes: campañas, seguimiento, comunicación | La "memoria" de todas las interacciones |
| **ERP** (Enterprise Resource Planning) | Gestiona administración y finanzas: facturación, pagos, contabilidad, RRHH | La "administración" del negocio |
| **BI** (Business Intelligence) | Analítica y reportes: dashboards, indicadores, tendencias | Los "ojos" de la organización |
| **IA** (Inteligencia Artificial) | Capa transversal: chatbots, analítica predictiva, personalización | El "asistente inteligente" |

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

#### 3.1 El "doble-click" en la plataforma Core : el SIS
El "Student Information System" es el sistema Core: modela la estrategia académica y los procesos académicos má importantes: 

![Funcionalidades del SIS.](https://github.com/alfredoedye/business-tech-strategy/blob/main/assets/Funcionalidades%20SIS.png)

### 4. Cuadrante de Tecnologia en Modelo MII

El modelo MII, en su cuadrante de Tecnología define la linea base de stack tecnológico para el grupo R'Evolution, como la arquitectura recomendada y deseada en cada institución, para garantizar la calidad y excelencia en la experiencia del estudiante , y la escalabilidad y eficiencia en su modelo academico mediado por tecnologia. 

![Linea base](https://github.com/alfredoedye/business-tech-strategy/blob/main/assets/Linea%20base%20Revolution.png)

### 5. Integraciones: el sistema nervioso de la organización

Los sistemas individuales son importantes, pero lo que realmente define la madurez de una arquitectura es **cómo se conectan entre sí**.
**Cada quiebre en la integración es una mala experiencia para el estudiante y un costo operativo para la organización.**

**Niveles de integración:**

| Nivel | Cómo funciona | Ejemplo |
|-------|--------------|---------|
| **Manual** | Alguien exporta un Excel y lo importa en otro sistema | Pasar notas del LMS al SIS a mano |
| **Archivos** | Un sistema genera un archivo que otro consume automáticamente | CSV de inscriptos que se importa cada noche |
| **APIs** | Los sistemas se hablan en tiempo real | Cuando un estudiante se inscribe en el SIS, automáticamente se crea su cuenta en el LMS |
| **Eventos** | Los sistemas reaccionan a lo que pasa en otros sistemas | Cuando un estudiante no ingresa al LMS en 7 días, el CRM genera una alerta automática |

**Para el líder ejecutivo, las preguntas clave son:**
- ¿Cuántos procesos dependen de carga manual? (Cada uno es un riesgo y un costo)
- ¿Los datos del estudiante están en un solo lugar o fragmentados en 5 sistemas?
- ¿Cuánto tiempo pasa entre que algo sucede y se refleja en todos los sistemas?
### 6. La arquitectura como herramienta de decisión

Una arquitectura IT bien entendida permite al líder evaluar:

**Escalabilidad:** ¿puede mi infraestructura soportar el doble de estudiantes? ¿O necesito cambiar sistemas antes de crecer?

**Gobierno:** ¿quién es el "dueño" de cada dato? ¿Quién decide qué sistema se reemplaza? ¿Hay una visión unificada o cada área compra lo que necesita?

**Costos:** ¿cuánto cuesta mantener sistemas que no se integran? ¿Cuántas horas-persona se pierden en procesos manuales que podrían automatizarse?

**Riesgo:** ¿qué pasa si cae el sistema central? ¿Hay plan B? ¿Los datos están respaldados?

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

- Puede nombrar y describir los sistemas principales de una institución educativa (SIS, LMS, CRM, ERP, BI, IAM).
- Entiende el ciclo de vida del estudiante como un flujo que depende de la integración entre sistemas.
- Puede leer un mapa de arquitectura IT y hacer preguntas relevantes.
- Tiene un diagnóstico visual de su propia arquitectura, con brechas y dolores identificados.
- Comprende que la arquitectura no es un tema de IT — es un tema de gobierno y competitividad.

---

*Anterior: [← Módulo 2 — Estrategia Tecnológica](modulo-02-estrategia-tecnologica.md)*
*Siguiente: [Módulo 4 — Transformación Digital e IA →](modulo-04-transformacion-digital-ia.md)*
