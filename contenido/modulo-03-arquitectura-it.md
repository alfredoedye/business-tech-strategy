# Módulo 3 — Arquitectura IT Educativa

---

## Objetivo del módulo

Que los participantes puedan **leer, cuestionar y discutir** la arquitectura tecnológica de una institución educativa, aunque no sean técnicos. No se trata de aprender a diseñar sistemas, sino de entender cómo funcionan por dentro para tomar mejores decisiones y hacer mejores preguntas.

---

## Pregunta guía

> ¿Cómo funciona realmente una institución educativa moderna por dentro?

---

## Conceptos clave

### 1. ¿Qué es una arquitectura IT?

Una arquitectura IT es el **mapa** de todos los sistemas tecnológicos de una organización: qué sistemas existen, qué hace cada uno, cómo se conectan entre sí y cómo fluye la información.

**Analogía:** pensá en tu organización como una ciudad.
- Los sistemas son los edificios (cada uno cumple una función).
- Las integraciones son las calles (conectan los edificios entre sí).
- Los datos son las personas que circulan por la ciudad (si las calles están cortadas, no llegan a destino).
- La arquitectura IT es el plano de la ciudad completa.

Un CEO no necesita saber construir edificios. Pero sí necesita poder leer el plano de la ciudad para decidir dónde construir el próximo, cuál demoler y cuál renovar.

### 2. Los sistemas clave de una institución educativa

Toda institución educativa moderna opera con un ecosistema de sistemas. Los principales son:

| Sistema | Qué hace | Analogía |
|---------|----------|----------|
| **SIS** (Student Information System) | Gestiona toda la vida académica del estudiante: inscripción, cursada, notas, título | El "DNI" del estudiante en la institución |
| **LMS** (Learning Management System) | Plataforma donde se da la experiencia de aprendizaje: contenidos, actividades, foros | El "aula" virtual |
| **CRM** (Customer Relationship Management) | Gestiona la relación con prospectos y estudiantes: campañas, seguimiento, comunicación | La "memoria" de todas las interacciones |
| **ERP** (Enterprise Resource Planning) | Gestiona administración y finanzas: facturación, pagos, contabilidad, RRHH | La "administración" del negocio |
| **BI** (Business Intelligence) | Analítica y reportes: dashboards, indicadores, tendencias | Los "ojos" de la organización |
| **IAM** (Identity & Access Management) | Gestiona identidades y permisos: quién puede acceder a qué | La "seguridad" del edificio |
| **IA** (Inteligencia Artificial) | Capa transversal: chatbots, analítica predictiva, personalización | El "asistente inteligente" |

### 3. El ciclo de vida del estudiante visto desde los sistemas

La experiencia del estudiante es un viaje que atraviesa múltiples sistemas. Cada etapa depende de que los sistemas correctos funcionen y estén conectados:

```
Descubrimiento → Evaluación → Admisión → Onboarding → Cursada → Evaluación → Graduación → Alumni
     CRM           CRM/Web      SIS        SIS/LMS      LMS       SIS/LMS      SIS         CRM
```

**Los problemas reales surgen en las transiciones:**
- El prospecto que se inscribe en el CRM pero sus datos no llegan al SIS → tiene que cargar todo de nuevo.
- El estudiante que aprueba en el LMS pero la nota no se refleja en el SIS → necesita un trámite manual.
- El graduado que no recibe seguimiento porque el CRM no tiene datos de ex-alumnos → oportunidad perdida.

**Cada quiebre en la integración es una mala experiencia para el estudiante y un costo operativo para la organización.**

### 4. Integraciones: el sistema nervioso de la organización

Los sistemas individuales son importantes, pero lo que realmente define la madurez de una arquitectura es **cómo se conectan entre sí**.

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

### 5. La arquitectura como herramienta de decisión

Una arquitectura IT bien entendida permite al líder evaluar:

**Escalabilidad:** ¿puede mi infraestructura soportar el doble de estudiantes? ¿O necesito cambiar sistemas antes de crecer?

**Gobierno:** ¿quién es el "dueño" de cada dato? ¿Quién decide qué sistema se reemplaza? ¿Hay una visión unificada o cada área compra lo que necesita?

**Costos:** ¿cuánto cuesta mantener sistemas que no se integran? ¿Cuántas horas-persona se pierden en procesos manuales que podrían automatizarse?

**Riesgo:** ¿qué pasa si cae el sistema central? ¿Hay plan B? ¿Los datos están respaldados?

---

## Ejemplos aplicados al sector educativo (LATAM)

### Universidad Siglo 21: Ecosistema integrado

Siglo 21 construyó una arquitectura donde el SIS propio (Algarrobo) es el centro del ecosistema y se conecta con:
- **HubSpot** (CRM) para gestión comercial
- **Canvas** (LMS) para la experiencia de aprendizaje
- **SAP** (ERP) para administración y finanzas
- **SistemaQ** (AMS) para mesa de ayuda
- **BI** para analítica y reportes
- **IAM** para gestión de identidades

El SIS opera con arquitectura de microservicios: módulos independientes (Planificación, Vida Académica, Administración, Trámites) con bases de datos propias que se comunican mediante eventos.

**Lo que esto significa para el negocio:** pueden cambiar el LMS sin afectar la inscripción. Pueden escalar la atención sin tocar la facturación. Cada pieza puede evolucionar de forma independiente.

### El caso típico: la "ensalada de sistemas"

Muchas universidades en LATAM acumularon sistemas durante años sin un plan de arquitectura:
- Un SIS de los 2000 que nadie se anima a tocar.
- Un LMS elegido por el área académica sin consultar a IT.
- Un CRM que marketing compró por su cuenta.
- Planillas de Excel como "integración" entre todos.
- 3 personas en IT que son las únicas que entienden cómo funciona todo.

**El resultado:** 12 sistemas, 2 integrados, 40% de procesos manuales, y un equipo de IT que pasa el 90% del tiempo apagando incendios en lugar de construyendo capacidades.

### UVD (caso simulado): Un diagnóstico revelador

Universidad del Valle Digital tiene:
- SIS legacy de 2010 (parcialmente funcional)
- Moodle como LMS (sin integración)
- Google Sheets como "CRM"
- Sin BI real
- Sin IAM formal (contraseñas compartidas)

Con 8,000 estudiantes y una tasa de deserción del 42%, la falta de integración no es un problema técnico — es un problema de negocio.

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

## Dinámica: "Walkthrough de una arquitectura de referencia"

**Duración:** 20 minutos

**Instrucciones:**
1. El facilitador presenta una arquitectura de referencia (basada en el caso Siglo 21 o en una arquitectura genérica educativa).
2. Se recorre cada capa:
   - Capa de touchpoints (web, campus virtual, app, e-commerce)
   - Capa de ciclo de vida del estudiante
   - Capa de sistemas de soporte
   - Capa de datos e inteligencia
3. Preguntas al grupo:
   - ¿Qué les sorprende?
   - ¿Qué tienen y qué les falta?
   - ¿Qué sistema querrían agregar primero?

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
