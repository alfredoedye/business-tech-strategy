# Glosario Ejecutivo de Términos Tecnológicos

> Este glosario está diseñado para que líderes no técnicos puedan entender y usar correctamente la terminología tecnológica en conversaciones con sus equipos de IT, consultores y vendors.

---

## Cómo usar este glosario

- **Definición simple:** Explicación en lenguaje cotidiano
- **Analogía:** Comparación con algo familiar
- **Por qué importa:** Relevancia para decisiones de negocio
- **Pregunta al CTO:** Qué preguntarle a tu equipo técnico

---

## A

### API (Application Programming Interface)

**Definición:** Un "conector" que permite que dos sistemas se comuniquen entre sí de manera automatizada.

**Analogía:** Como un enchufe universal. Así como un enchufe tiene un formato estándar para que cualquier aparato se conecte a la corriente, una API tiene un formato estándar para que cualquier sistema se conecte a otro.

**Por qué importa:** Si tus sistemas no tienen APIs o no las usan, la información no fluye. Terminas con procesos manuales, Excel, y datos desactualizados.

**Pregunta al CTO:** "¿Nuestros sistemas principales tienen APIs? ¿Las estamos usando para integrarnos?"

---

### Arquitectura de microservicios

**Definición:** Una forma de construir software donde el sistema está dividido en piezas pequeñas e independientes, cada una haciendo una función específica.

**Analogía:** Como una cocina modular vs. una cocina de una sola pieza. Si se rompe el horno modular, lo cambias sin tocar lo demás. Si se rompe algo en la cocina de una pieza, tenés que cambiar todo.

**Por qué importa:** Permite escalar y cambiar partes del sistema sin afectar todo. Si tu SIS está en microservicios, podés actualizar el módulo de inscripciones sin tocar el de notas.

**Pregunta al CTO:** "¿Nuestro sistema principal es monolítico o está en microservicios? ¿Qué implicancias tiene para cambios futuros?"

---

## B

### Backend / Frontend

**Definición:**
- **Frontend:** Lo que ve y usa el usuario (la interfaz, los botones, las pantallas)
- **Backend:** Lo que pasa "detrás de escena" (bases de datos, lógica de negocio, integraciones)

**Analogía:** Frontend es el salón del restaurante (lo que ve el cliente). Backend es la cocina (donde se prepara todo).

**Por qué importa:** A veces un problema de "la plataforma anda lenta" puede ser de frontend (interfaz mal diseñada) o de backend (base de datos sobrecargada). Saber distinguirlo ayuda a priorizar.

**Pregunta al CTO:** "Este problema, ¿es de frontend o de backend? ¿Qué equipo lo resuelve?"

---

### Business Intelligence (BI)

**Definición:** Herramientas y procesos para convertir datos crudos en información útil para tomar decisiones (dashboards, reportes, análisis).

**Analogía:** Como el tablero de instrumentos del auto. Muestra velocidad, combustible, temperatura en tiempo real para que tomes decisiones de manejo.

**Por qué importa:** Sin BI, las decisiones se toman por intuición o con datos desactualizados. Con BI, podés ver la deserción en tiempo real, no 3 meses después.

**Pregunta al CTO:** "¿Cuánto tardamos en tener un dato que necesito para decidir? ¿Tenemos un dashboard de KPIs actualizado?"

---

## C

### CI/CD (Continuous Integration / Continuous Deployment)

**Definición:** Prácticas de desarrollo donde los cambios al software se integran y despliegan de forma automatizada y frecuente.

**Analogía:** En vez de hacer una mudanza completa cada año, hacer pequeños envíos todos los días. Si algo sale mal, es fácil identificar qué fue y revertirlo.

**Por qué importa:** Permite que los cambios lleguen a producción más rápido y con menos riesgo. Si tu equipo despliega "una vez por mes con mucho estrés", probablemente no tienen CI/CD.

**Pregunta al CTO:** "¿Con qué frecuencia desplegamos cambios a producción? ¿Es un proceso automatizado o manual?"

---

### Cloud (Nube)

**Definición:** Infraestructura tecnológica (servidores, almacenamiento, servicios) que se alquila a proveedores como AWS, Azure o Google Cloud, en vez de comprar y mantener servidores propios.

**Analogía:** Alquilar un departamento vs. comprar una casa. El departamento viene con mantenimiento incluido, podés cambiarte fácil, pero no sos dueño. La casa es tuya pero vos te ocupás de todo.

**Por qué importa:** Cloud permite escalar sin inversión inicial grande, pero genera dependencia del proveedor y costos que pueden crecer.

**Variantes:**
- **IaaS (Infrastructure as a Service):** Alquilás la infraestructura (AWS EC2)
- **PaaS (Platform as a Service):** Alquilás la plataforma para desarrollar (Heroku)
- **SaaS (Software as a Service):** Alquilás el software listo (Canvas, HubSpot)

**Pregunta al CTO:** "¿Qué porcentaje de nuestra infraestructura está en cloud? ¿Cuál es el costo mensual y cómo está evolucionando?"

---

### CRM (Customer Relationship Management)

**Definición:** Sistema para gestionar todas las interacciones con clientes (en educación: prospectos y estudiantes), desde el primer contacto hasta la relación de largo plazo.

**Analogía:** La "memoria institucional" de todas las conversaciones con cada persona. Quién habló con quién, cuándo, sobre qué, y qué quedó pendiente.

**Por qué importa:** Sin CRM, perdés leads, duplicás esfuerzos, y no tenés visibilidad del embudo de conversión.

**Ejemplos:** HubSpot, Salesforce, Zoho

**Pregunta al CTO:** "¿Tenemos una única fuente de verdad para la relación con prospectos y estudiantes? ¿Cuántos sistemas tienen datos de contacto?"

---

## D

### Data Lake / Data Warehouse

**Definición:**
- **Data Lake:** Repositorio que almacena datos en bruto, sin estructurar, para análisis futuro
- **Data Warehouse:** Repositorio de datos ya procesados, estructurados, listos para reportes

**Analogía:** Data Lake es como un depósito donde guardás todo por si acaso. Data Warehouse es como un archivo organizado donde encontrás lo que buscás rápidamente.

**Por qué importa:** Si querés hacer analítica avanzada o IA, necesitás tus datos en algún lugar centralizado. La pregunta es si están organizados o no.

**Pregunta al CTO:** "¿Tenemos los datos de estudiantes centralizados? ¿Podemos cruzar datos de SIS, LMS y CRM para análisis?"

---

### Deuda técnica

**Definición:** Los "atajos" o decisiones subóptimas acumuladas en el código o la arquitectura que eventualmente hay que "pagar" con trabajo adicional.

**Analogía:** Como deuda financiera. Tomar atajos es como tomar un préstamo: te da velocidad ahora pero pagás intereses después. Si acumulás mucha, llegás al default (el sistema se vuelve imposible de mantener).

**Por qué importa:** Un sistema con mucha deuda técnica es lento para cambiar, propenso a errores, y consume recursos de IT en "apagar incendios" en vez de innovar.

**Pregunta al CTO:** "¿Qué porcentaje del tiempo de IT va a mantener sistemas vs. construir cosas nuevas? ¿Tenemos un plan para reducir deuda técnica?"

---

### DevOps

**Definición:** Cultura y prácticas donde los equipos que desarrollan software (Dev) y los que lo operan (Ops) trabajan juntos, no en silos separados.

**Analogía:** Como si el chef del restaurante también fuera responsable de que el plato llegue bien a la mesa, no solo de cocinarlo y pasárselo a otro.

**Por qué importa:** Reduce el "no es mi problema" y acelera la entrega. Si hay problemas en producción, el mismo equipo que construyó el software lo resuelve.

**Pregunta al CTO:** "¿Quién es responsable cuando algo falla en producción? ¿Hay un equipo que construye y otro que opera, o son los mismos?"

---

## E

### ERP (Enterprise Resource Planning)

**Definición:** Sistema integrado que gestiona los procesos administrativos y financieros: facturación, contabilidad, pagos, RRHH, compras.

**Analogía:** El "sistema nervioso administrativo" de la organización. Todo lo que tiene que ver con plata y administración pasa por ahí.

**Por qué importa:** Si el ERP no está integrado con el SIS, hay duplicación de datos, errores de facturación, y procesos manuales para conciliar.

**Ejemplos:** SAP, Oracle, Microsoft Dynamics, Odoo

**Pregunta al CTO:** "¿Nuestro ERP está integrado con el SIS? ¿Cuánto trabajo manual hay para conciliar datos entre sistemas?"

---

## I

### IAM (Identity and Access Management)

**Definición:** Sistemas y procesos que controlan quién puede acceder a qué dentro de la organización.

**Analogía:** Como el sistema de llaves y cerraduras de un edificio. Define quién tiene llave de qué oficina, quién puede entrar al estacionamiento, quién puede acceder a la caja fuerte.

**Por qué importa:** Sin IAM robusto, hay contraseñas compartidas, accesos que no se revocan cuando alguien se va, y riesgo de acceso no autorizado a datos sensibles.

**Pregunta al CTO:** "¿Tenemos Single Sign-On (SSO)? Cuando alguien deja la organización, ¿se le revocan todos los accesos automáticamente?"

---

### Integración

**Definición:** El proceso de conectar sistemas para que compartan datos y funcionalidades de manera automatizada.

**Niveles:**
| Nivel | Cómo funciona | Ejemplo |
|-------|--------------|---------|
| Manual | Alguien exporta e importa | Export Excel del LMS, import al SIS |
| Archivos | Transferencia automatizada de archivos | CSV de inscriptos cada noche |
| API | Comunicación en tiempo real | Inscripción en SIS crea cuenta en LMS |
| Eventos | Sistemas reaccionan a cambios en otros | Si no entra al LMS en 7 días, alerta en CRM |

**Por qué importa:** Cada integración que falta es trabajo manual, datos desactualizados, y fricción para el usuario.

**Pregunta al CTO:** "¿Cuántas integraciones tenemos entre sistemas principales? ¿Cuántos procesos siguen siendo manuales?"

---

## L

### Legacy (Sistema legacy)

**Definición:** Sistema antiguo que sigue en uso porque "funciona", aunque sea difícil de mantener, integrar o evolucionar.

**Analogía:** Como un auto viejo que todavía anda pero nadie fabrica repuestos, el mecánico que lo conoce se jubiló, y no tiene aire acondicionado.

**Por qué importa:** Los sistemas legacy consumen recursos de IT desproporcionados, limitan la innovación, y representan riesgo de falla o seguridad.

**Pregunta al CTO:** "¿Cuáles son nuestros sistemas legacy? ¿Cuánto nos cuesta mantenerlos? ¿Hay plan de reemplazo?"

---

### LMS (Learning Management System)

**Definición:** Plataforma donde ocurre la experiencia de aprendizaje: contenidos, actividades, foros, evaluaciones, seguimiento de progreso.

**Analogía:** El "aula virtual". Es donde el estudiante pasa tiempo interactuando con el contenido y los docentes.

**Por qué importa:** El LMS es uno de los principales touchpoints con el estudiante. Si la experiencia es mala, el NPS sufre.

**Ejemplos:** Canvas, Moodle, Blackboard, Brightspace

**Pregunta al CTO:** "¿Nuestro LMS está integrado con el SIS? ¿Las notas fluyen automáticamente o hay carga manual?"

---

## M

### MVP (Minimum Viable Product)

**Definición:** La versión más simple de un producto que permite probar una hipótesis con usuarios reales.

**Analogía:** Antes de construir un restaurante, poner un food truck para ver si a la gente le gusta tu comida.

**Por qué importa:** Permite validar ideas con baja inversión antes de comprometer recursos grandes. Evita construir algo que nadie quiere.

**Pregunta al CTO:** "¿Podemos hacer un MVP de esta idea antes de invertir en el proyecto completo?"

---

## O

### On-premise

**Definición:** Infraestructura tecnológica que está físicamente en las instalaciones de la organización (servidores propios, data center propio).

**Analogía:** Tener tu propia planta de energía vs. comprar electricidad de la red.

**Por qué importa:** On-premise da más control pero requiere inversión inicial, equipo de infraestructura, y hacerse cargo de mantenimiento, actualizaciones y seguridad.

**Pregunta al CTO:** "¿Qué tenemos on-premise y por qué? ¿Tiene sentido migrarlo a cloud?"

---

## S

### SaaS (Software as a Service)

**Definición:** Software que se usa a través de internet y se paga por suscripción, sin necesidad de instalar ni mantener nada.

**Analogía:** Como Netflix. Pagás una suscripción, usás el servicio, y ellos se encargan de que funcione.

**Por qué importa:** SaaS reduce la carga de IT pero genera dependencia del proveedor y costos recurrentes. A largo plazo puede ser más caro que licencia perpetua.

**Pregunta al CTO:** "¿Cuánto gastamos en SaaS por mes? ¿Estamos usando todas las herramientas que pagamos?"

---

### SIS (Student Information System)

**Definición:** El sistema central que gestiona toda la vida académica del estudiante: inscripción, cursada, notas, título, historial.

**Analogía:** El "DNI académico" del estudiante. Todo lo que hace un estudiante queda registrado ahí.

**Por qué importa:** El SIS es (o debería ser) la fuente de verdad del estudiante. Si está desactualizado, fragmentado o no integrado, hay caos de datos.

**Ejemplos:** Banner, PeopleSoft, sistemas propios (ej: Algarrobo de Siglo 21)

**Pregunta al CTO:** "¿El SIS es la fuente de verdad del estudiante? ¿Todos los demás sistemas lo reconocen así?"

---

### SSO (Single Sign-On)

**Definición:** Sistema que permite acceder a múltiples aplicaciones con una única credencial.

**Analogía:** Una llave maestra que abre todas las puertas que tenés permiso de abrir.

**Por qué importa:** Sin SSO, los usuarios tienen múltiples contraseñas (y las olvidan), o peor, usan la misma contraseña débil en todos lados.

**Pregunta al CTO:** "¿Tenemos SSO implementado? ¿A cuántos sistemas puede acceder un estudiante con un solo login?"

---

## T

### Tech stack

**Definición:** El conjunto de tecnologías (lenguajes, frameworks, bases de datos, herramientas) que usa una organización.

**Analogía:** Los ingredientes y utensilios de una cocina. Cada cocina tiene su combinación según lo que cocina.

**Por qué importa:** Un tech stack coherente es más fácil de mantener y contratar talento. Un stack fragmentado genera complejidad y dependencia de especialistas.

**Pregunta al CTO:** "¿Cuál es nuestro tech stack? ¿Es fácil encontrar talento que lo maneje?"

---

## V

### Vendor lock-in

**Definición:** Situación donde cambiar de proveedor tecnológico es tan costoso o complejo que quedás "atrapado" con el actual.

**Analogía:** Como una línea de teléfono donde perder el número significa perder contactos de años. No te vas porque el costo de irte es muy alto.

**Por qué importa:** Lock-in reduce tu poder de negociación y te expone a aumentos de precio arbitrarios.

**Señales de lock-in:**
- Datos en formato propietario difícil de exportar
- Contrato de largo plazo con penalidades de salida
- Integraciones que solo funcionan con ese vendor
- Conocimiento concentrado en el equipo del vendor

**Pregunta al CTO:** "¿Qué tan difícil sería cambiar de [sistema X]? ¿Cuánto tardaríamos y cuánto costaría?"

---

## Términos de uso frecuente en reuniones

| Término | Significado real | Cuándo preocuparse |
|---------|------------------|-------------------|
| "Escalable" | Puede crecer sin rediseñar | Si no pueden explicar cómo |
| "Robusto" | Resistente a fallas | Si no hay métricas de uptime |
| "Ágil" | Entregas incrementales | Si siguen en proyectos de 2 años |
| "En la nube" | Hosted externamente | Si no saben dónde específicamente |
| "Integrado" | Se comunica con otros sistemas | Si es con archivos manuales |
| "Tiempo real" | Instantáneo | Si hay delay de horas o días |
| "Enterprise" | Para organizaciones grandes | Si es excusa para complejidad innecesaria |
| "Best practice" | Lo que todos hacen | Si no aplica a tu contexto |

---

*Volver a: [← Referencias y Recursos](lecturas-y-recursos.md)*
