# Módulo 2 — Estrategia Tecnológica del negocio

---

## Objetivo del módulo

Que los participantes adquieran el vocabulario, los criterios y los frameworks necesarios para participar activamente en la definición de la estrategia tecnológica de su organización. No se trata de aprender tecnología, sino de aprender a **decidir sobre tecnología**.

---

## Tesis del módulo

> No existen decisiones "puramente tecnológicas".
> Toda decisión tecnológica es una decisión de negocio con consecuencias en costos, velocidad, dependencia y diferenciación.
>
> El directivo que no participa en estas decisiones no está delegando — está abdicando.

---

## Pregunta guía

> ¿Qué decisiones tecnológicas son estratégicas y cuáles son tácticas?

---

## El costo de las decisiones tecnológicas equivocadas

*3 minutos de contexto antes de entrar en los frameworks.*

- **La deuda técnica consume el 40% del presupuesto de IT** en la empresa promedio (McKinsey, 2024). Cada peso que se va en mantener sistemas viejos es un peso que no va a innovación.
- **2U invirtió USD 800M en adquirir edX** con la estrategia de "comprar" la plataforma. Hoy tiene USD 900M en deuda. La decisión Build vs Buy más cara de la historia de EdTech.
- **Universidad Siglo 21 tomó la decisión opuesta** — construir su propio SIS. Resultado: de 30,000 a 60,000+ estudiantes con NPS de +31.

La diferencia entre ambos casos no es técnica. Es estratégica. Es la diferencia entre tener criterio para decidir y delegar sin entender.

**Pregunta para la sala:**
*¿En tu organización, quién toma las decisiones tecnológicas estructurales? ¿El equipo directivo o el área de IT sola?*

---

## Conceptos clave

### 1. Decisiones estratégicas que todo directivo debe dominar

No todas las decisiones tecnológicas son iguales. Algunas son operativas (qué herramienta de videoconferencia usar) y otras son estructurales (en qué plataforma vamos a construir nuestro futuro). Un líder debe saber distinguirlas.

#### Build vs. Buy (Construir vs. Comprar)

| | Build (Construir) | Buy (Comprar) |
|---|---|---|
| **Qué es** | Desarrollar software a medida internamente | Contratar una solución de mercado (SaaS, licencia) |
| **Ventaja** | Control total, diferenciación, propiedad de los datos | Velocidad de implementación, menor riesgo inicial |
| **Riesgo** | Costos altos, requiere equipo técnico, tiempo | Dependencia del proveedor, limitaciones de personalización |
| **Cuándo conviene** | Cuando el proceso es parte de tu ventaja competitiva | Cuando el proceso es estándar en la industria |

**Ejemplo educativo:** El SIS (Student Information System) es el corazón de una institución educativa. Universidad Siglo 21 decidió construir el suyo propio (Proyecto Algarrobo) porque ninguna solución de mercado se adaptaba a su modelo federal. Resultado: flexibilidad total para escalar de 30,000 a 60,000+ estudiantes.

**La regla de oro:** Comprá lo que es commodity. Construí lo que es tu ventaja competitiva.

**Impacto financiero:** Build = CAPEX (inversión de capital) + equipo permanente. Buy = OPEX predecible (gasto operativo mensual). La decisión no es solo técnica — cambia el modelo financiero. Para profundizar: [Anexo: Finanzas para Decisiones Tech](../anexos/finanzas-para-decisiones-tech.md).

#### Cloud vs. On-premise

| | Cloud | On-premise |
|---|---|---|
| **Qué es** | Infraestructura alquilada (AWS, Azure, Google Cloud) | Servidores propios en tu edificio |
| **Analogía** | Alquilar un departamento: flexible, mantenimiento incluido | Comprar una casa: control total, pero vos te ocupás de todo |
| **Ventaja** | Escalabilidad, sin inversión inicial grande, actualizaciones automáticas | Control total, costos predecibles a largo plazo |
| **Riesgo** | Costos que pueden crecer, dependencia del proveedor | Obsolescencia, necesidad de equipo de infraestructura |
| **Tendencia** | La mayoría de las organizaciones están migrando a cloud | Se mantiene para regulaciones específicas |

**Ejemplo educativo:** Universidad Siglo 21 migró a AWS. Esto le permitió escalar de cientos a 10,000 usuarios simultáneos sin comprar servidores. Durante picos de inscripción o exámenes, la infraestructura escala automáticamente.

**Impacto financiero:** Cloud convierte CAPEX en OPEX. Se elimina la inversión inicial grande (comprar servidores) pero se genera un costo recurrente mensual. El CFO necesita entender esta transición porque cambia cómo se planifica y aprueba el presupuesto tecnológico.

#### Core vs. Commodity

No todos los sistemas tienen el mismo valor estratégico:

- **Core:** sistemas que definen tu ventaja competitiva. Si los perdés, perdés diferenciación.
  - Ejemplo: tu plataforma de aprendizaje personalizado, tu motor de analítica de retención.
- **Commodity:** sistemas que necesitás pero que no te diferencian. Cualquier proveedor los resuelve.
  - Ejemplo: email, herramienta de videoconferencia, sistema contable.

**La trampa común:** invertir tiempo y recursos en personalizar commodities (crear tu propio sistema de email interno) y al mismo tiempo usar soluciones genéricas para lo que es core (un LMS sin personalización).

#### Velocidad vs. Control

| Priorizar velocidad | Priorizar control |
|---|---|
| Lanzar rápido, iterar después | Planificar en detalle, lanzar cuando esté listo |
| Aceptar deuda técnica a corto plazo | Minimizar deuda técnica desde el inicio |
| Funciona para validar hipótesis | Funciona para sistemas críticos |
| Riesgo: acumulación de problemas | Riesgo: nunca lanzar, parálisis por análisis |

**La clave para líderes:** no hay una respuesta correcta universal. La decisión depende del momento de la organización, el riesgo del proyecto y la reversibilidad de la decisión.

### 2. Las 6 dimensiones de una estrategia tecnológica

Una estrategia tecnológica no es una lista de herramientas. Es un modelo que conecta seis dimensiones. Estas mismas dimensiones son las que vas a evaluar en el [Radar de Estrategia Tecnológica](../materiales/templates/template-radar-estrategia-tech.md).

#### Infraestructura

- ¿Dónde viven tus sistemas y datos? ¿Cloud, on-premise, o híbrido?
- ¿Tu infraestructura puede escalar en picos (inscripciones, exámenes)?
- ¿Cuán dependiente sos de servidores físicos o de un proveedor cloud?

#### Arquitectura

- ¿Cómo están organizados tus sistemas? ¿Se hablan entre sí o son islas?
- ¿La información fluye automáticamente o requiere carga manual?
- ¿Cuántos procesos dependen de un Excel o un email para funcionar?

#### Datos
- ¿Qué datos tenemos? ¿Son confiables?
- ¿Quién los gobierna? ¿Están centralizados o fragmentados?
- ¿Tomamos decisiones basadas en datos o en intuición?

#### Seguridad
- ¿Tenemos políticas de seguridad definidas?
- ¿Quién tiene acceso a qué? ¿Lo sabemos?
- ¿Estamos preparados para un incidente (fuga de datos, ransomware)?

#### Talento
- ¿Tenemos las personas correctas para ejecutar la estrategia?
- ¿Nuestro equipo de IT es de "apaga incendios" o de construcción estratégica?
- ¿El negocio y la tecnología hablan el mismo idioma?

#### Innovación

- ¿Cómo incorporamos nuevas tecnologías? ¿Hay un proceso o es ad hoc?
- ¿Quién identifica oportunidades tecnológicas? ¿Solo IT o también el negocio?
- ¿Tenemos espacio para experimentar o toda inversión requiere un business case completo?

### 3. Alineación tecnología-negocio

La estrategia tecnológica no existe en el vacío. Debe estar alineada con:

- **El modelo de negocio:** ¿Cómo genera valor la organización? ¿Qué rol juega la tecnología en esa generación de valor?
- **La etapa de crecimiento:** Una startup EdTech necesita velocidad. Una universidad establecida necesita estabilidad y migración gradual.
- **Los objetivos a 3-5 años:** ¿Queremos crecer en matrícula? ¿Expandir a nuevos mercados? ¿Mejorar retención? La respuesta define las prioridades tecnológicas.

**Framework de alineación:**

```
Objetivos de negocio → Capacidades necesarias → Habilitadores tecnológicos → Inversión y priorización
```

Ejemplo:
- Objetivo: reducir deserción del 42% al 25% en 2 años.
- Capacidad: detectar estudiantes en riesgo antes de que abandonen.
- Habilitador: analítica predictiva conectada al LMS y al SIS.
- Inversión: integración de datos + modelo de alertas + equipo de intervención.

> Para profundizar en frameworks estratégicos (Wardley Maps, Hype Cycle, TOGAF simplificado), ver el [Anexo: Frameworks Estratégicos](../anexos/frameworks-estrategicos.md).

---

## Ejemplos aplicados al sector educativo (LATAM)

### Universidad Siglo 21: Build como ventaja competitiva
Decidieron construir su SIS propio cuando el mercado no ofrecía una solución para su modelo federal (15+ sedes, modalidades presencial y online, 60,000+ estudiantes). La inversión fue significativa, pero el retorno fue claro: control total del dato, flexibilidad para crecer, y NPS que subió a +31.

### El dilema de los sistemas heredados
Muchas universidades en LATAM operan con sistemas que tienen 15-20 años. No se reemplazan porque "funcionan" — pero la realidad es que limitan el crecimiento, fragmentan los datos y generan dependencia de personas específicas. La decisión de migrar es difícil pero cada año que pasa la hace más costosa.

### El costo oculto del "gratis"
Instituciones que adoptan herramientas gratuitas de Google o Microsoft para todo (email, documentos, aula virtual, formularios) descubren tarde que no tienen control sobre los datos de sus estudiantes, no pueden personalizar la experiencia, y dependen completamente de decisiones de un tercero.

---

## Dinámica: Auditoría Express — Radar de Estrategia Tecnológica

**Duración:** 30 minutos (15 individual + 15 en pares)

**Instrucciones:**
1. Cada participante completa el [Template Radar de Estrategia Tecnológica](../materiales/templates/template-radar-estrategia-tech.md), calificando las 6 dimensiones (Infraestructura, Arquitectura, Datos, Seguridad, Talento, Innovación) del 1 al 5.
2. Conectá los puntos para visualizar tu perfil.
3. En pares, comparen sus radares y discutan:
   - ¿Cuál es tu dimensión más fuerte?
   - ¿Cuál es la brecha más crítica?
   - ¿Cuál priorizarías mejorar en el próximo año y por qué?

**Debrief grupal:**
- ¿Aparecieron patrones comunes entre organizaciones?
- ¿Hay brechas que sorprendieron?
- ¿Qué decisiones estratégicas emergen de este diagnóstico?

---

## Dinámica: Trade-offs en acción

**Duración:** 20 minutos

**Instrucciones:**
1. Se presentan 4 escenarios. Cada grupo debe decidir y argumentar:

**Escenario 1:** Tu LMS actual cumple el 70% de lo que necesitás. Un competidor ofrece un LMS nuevo que promete el 95%. Migrar cuesta USD 200K y 6 meses. ¿Migrás o mejorás lo que tenés?

**Escenario 2:** Tu equipo de IT propone construir un chatbot de IA para atención a estudiantes. Costo estimado: USD 80K + 4 meses. Existen alternativas SaaS por USD 500/mes. ¿Build o Buy?

**Escenario 3:** Tenés 3 sistemas que no se integran (SIS, LMS, CRM). Podés invertir en integrarlos o reemplazarlos por una suite integrada. Integrar cuesta menos pero deja deuda técnica. Reemplazar cuesta más pero es limpio. ¿Qué elegís?

**Escenario 4:** Tu competidor acaba de lanzar una app móvil para estudiantes. Tu equipo dice que pueden hacer una en 3 meses. Marketing dice que es urgente. IT dice que la infraestructura no está lista. ¿Velocidad o control?

2. Cada grupo presenta su decisión en 2 minutos. No hay respuesta correcta — lo importante es el criterio.

---

## Resultado esperado

Al terminar este módulo, el participante:

- Maneja el vocabulario de decisiones tecnológicas estratégicas (Build vs. Buy, Cloud vs. On-premise, Core vs. Commodity).
- Puede distinguir entre una decisión táctica y una decisión estructural.
- Entiende las 6 dimensiones de una estrategia tecnológica integral.
- Comprende el impacto financiero de las decisiones tecnológicas (CAPEX vs. OPEX, deuda técnica).
- Tiene un primer diagnóstico visual (radar) de la madurez tecnológica de su organización.
- Puede participar activamente en una conversación sobre estrategia tecnológica con su equipo de IT.

---

## Reflexión final

> Cada decisión tecnológica que tomás (o que dejás que otros tomen por vos)
> define la estructura de costos, la velocidad y la dependencia de tu organización por los próximos 3-5 años.
> ¿Estás eligiendo… o estás heredando?

---

*Anterior: [← Módulo 1 — Hello World](modulo-01-hello-world.md)*
*Siguiente: [Módulo 3 — Arquitectura IT Educativa →](modulo-03-arquitectura-it.md)*
