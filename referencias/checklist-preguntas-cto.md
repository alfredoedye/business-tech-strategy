# 10 Preguntas que Todo CEO Debería Hacer a su CTO

> Esta checklist te ayuda a mantener conversaciones productivas con tu equipo de tecnología. No necesitás entender todos los detalles técnicos — necesitás hacer las preguntas correctas.

---

## Cómo usar esta checklist

- **Frecuencia sugerida:** Una conversación mensual o trimestral usando estas preguntas
- **Objetivo:** Entender el estado real de la tecnología, no solo escuchar "todo bien"
- **Actitud:** Curiosidad genuina, no auditoría hostil

---

## Las 10 Preguntas Esenciales

### 1. ¿Cuál es nuestro sistema más crítico y qué pasa si falla?

**Por qué preguntar:** Identificar single points of failure y evaluar riesgo operativo.

**Qué esperar escuchar:**
- ✅ "El SIS es crítico. Tenemos redundancia y podemos recuperar en 4 horas."
- 🚩 "El SIS... si se cae, no sé cuánto tardaríamos en volver."

**Seguimiento:** "¿Cuándo fue la última vez que probamos la recuperación ante desastres?"

---

### 2. ¿Cuánta deuda técnica tenemos y está creciendo o reduciéndose?

**Por qué preguntar:** La deuda técnica acumulada eventualmente frena la innovación y aumenta costos.

**Qué esperar escuchar:**
- ✅ "Tenemos un backlog de deuda técnica priorizado. Dedicamos 20% del sprint a reducirla."
- 🚩 "No tenemos tiempo para eso, estamos enfocados en features nuevos."

**Seguimiento:** "¿Qué porcentaje del tiempo de IT va a mantener lo existente vs. construir cosas nuevas?"

---

### 3. ¿Dónde están físicamente nuestros datos y quién tiene acceso?

**Por qué preguntar:** Compliance, seguridad, y saber qué pasa si hay un incidente.

**Qué esperar escuchar:**
- ✅ "Datos de estudiantes en AWS región São Paulo. Acceso restringido a roles específicos con logs de auditoría."
- 🚩 "En varios lugares... algunos en laptops de gente del equipo..."

**Seguimiento:** "¿Cumplimos con las regulaciones de protección de datos de nuestro país?"

---

### 4. ¿Cuánto de nuestro presupuesto de IT va a "mantener las luces encendidas" vs. innovar?

**Por qué preguntar:** Si IT gasta 80%+ en mantenimiento, no hay capacidad para mejorar.

**Qué esperar escuchar:**
- ✅ "70% run, 30% grow. Estamos trabajando para llegar a 60/40."
- 🚩 "Casi todo va a mantener lo que tenemos funcionando."

**Seguimiento:** "¿Qué tendríamos que hacer para liberar más capacidad hacia innovación?"

---

### 5. ¿Cuánto tardaríamos en cambiar de [sistema X] si quisiéramos?

**Por qué preguntar:** Evaluar vendor lock-in y flexibilidad estratégica.

**Qué esperar escuchar:**
- ✅ "El LMS podríamos cambiarlo en 6 meses. El SIS sería un proyecto de 2 años."
- 🚩 "Sería prácticamente imposible, todo depende de ese sistema."

**Seguimiento:** "¿Hay algo que podamos hacer para reducir esa dependencia?"

---

### 6. ¿Tenemos un plan de recuperación ante desastres y cuándo lo probamos?

**Por qué preguntar:** Los planes no probados no funcionan cuando se necesitan.

**Qué esperar escuchar:**
- ✅ "Sí, hacemos simulacro cada 6 meses. El último fue hace 2 meses, recuperamos en 6 horas."
- 🚩 "Tenemos un documento de hace 3 años... no lo hemos probado."

**Seguimiento:** "¿Qué sería lo peor que podría pasar y cuánto tardaríamos en recuperarnos?"

---

### 7. ¿Qué porcentaje de nuestros procesos son manuales vs. automatizados?

**Por qué preguntar:** Procesos manuales son costosos, lentos y propensos a errores.

**Qué esperar escuchar:**
- ✅ "80% de inscripciones son self-service. El 20% restante son casos especiales."
- 🚩 "Mucho sigue siendo manual... alguien tiene que pasar datos entre sistemas."

**Seguimiento:** "¿Cuáles son los 3 procesos manuales que más tiempo consumen?"

---

### 8. ¿Cuál es nuestro mayor riesgo de seguridad hoy?

**Por qué preguntar:** Entender vulnerabilidades antes de que se conviertan en incidentes.

**Qué esperar escuchar:**
- ✅ "El mayor riesgo es phishing. Estamos implementando MFA y capacitación."
- 🚩 "No estoy seguro... no hemos hecho una evaluación de seguridad."

**Seguimiento:** "Si alguien quisiera atacarnos, ¿por dónde entraría?"

---

### 9. ¿Tenemos las personas correctas o dependemos de proveedores externos?

**Por qué preguntar:** Dependencia excesiva de externos es riesgo y costo.

**Qué esperar escuchar:**
- ✅ "El core lo manejamos interno. Para picos o especialidades usamos partners."
- 🚩 "Solo [nombre de persona] entiende el sistema principal..."

**Seguimiento:** "¿Qué pasa si [persona clave] se va mañana?"

---

### 10. Si empezáramos de cero hoy, ¿qué haríamos diferente?

**Por qué preguntar:** Revelar el gap entre la realidad y lo ideal, sin presión de defender decisiones pasadas.

**Qué esperar escuchar:**
- ✅ "Empezaríamos cloud-native, con un SIS moderno, e integraríamos todo desde el día 1."
- 🚩 "Haríamos todo diferente... pero ya es muy tarde."

**Seguimiento:** "¿Qué podemos empezar a hacer hoy para movernos en esa dirección?"

---

## Preguntas Bonus para Situaciones Específicas

### Cuando hay un proyecto grande en curso

- "¿Estamos en tiempo y presupuesto? ¿Cuál es el mayor riesgo?"
- "¿Qué decisiones necesitás de mí para avanzar?"
- "¿Qué no me estás contando porque pensás que no quiero escucharlo?"

### Cuando hay un incidente

- "¿Qué pasó exactamente y qué impacto tuvo?"
- "¿Por qué pasó y qué vamos a hacer para que no vuelva a pasar?"
- "¿Necesitamos comunicar algo a estudiantes o al board?"

### Cuando evalúan una inversión grande

- "¿Cuál es el TCO a 5 años, no solo el costo inicial?"
- "¿Qué alternativas evaluamos y por qué elegimos esta?"
- "¿Qué pasa si no funciona? ¿Podemos revertir?"

### Cuando el equipo parece sobrecargado

- "¿Qué deberíamos dejar de hacer para enfocarnos en lo importante?"
- "¿Tenemos las prioridades claras o estamos apagando incendios?"
- "¿Qué necesitás de mí para trabajar mejor?"

---

## Señales de Alerta en las Respuestas

| Si escuchás... | Puede significar... |
|----------------|---------------------|
| "Es muy técnico para explicar" | No quieren que entiendas o no lo entienden ellos |
| "Siempre lo hicimos así" | Resistencia al cambio, posible deuda técnica |
| "El vendor dijo que..." | Dependencia excesiva de externos |
| "Necesitamos más recursos" | Puede ser real o excusa para no priorizar |
| "Está en el roadmap" | Preguntá cuándo específicamente |
| "No es mi área" | Silos problemáticos en el equipo |
| Respuestas muy vagas | Falta de visibilidad o transparencia |

---

## Señales de que la Conversación va Bien

| Si escuchás... | Es buena señal porque... |
|----------------|-------------------------|
| "Déjame mostrarte los números" | Cultura de datos, transparencia |
| "Tenemos un plan pero necesito tu input en..." | Colaboración, ownership |
| "El riesgo es X y lo estamos mitigando con Y" | Gestión de riesgos madura |
| "No sé, voy a investigar y te respondo" | Honestidad, no inventar |
| "Necesito que priorices entre A y B" | Claridad en trade-offs |

---

## Template para la Conversación

```
REUNIÓN MENSUAL CEO-CTO

Fecha: _______________

1. Estado general (5 min)
   - ¿Cómo estamos? ¿Algo urgente?

2. Sistemas críticos (10 min)
   - Pregunta 1, 3 o 6 de la lista

3. Capacidad e innovación (10 min)
   - Pregunta 2, 4 o 7 de la lista

4. Riesgo y seguridad (10 min)
   - Pregunta 5 o 8 de la lista

5. Equipo y dependencias (10 min)
   - Pregunta 9 de la lista

6. Mirando hacia adelante (10 min)
   - Pregunta 10 de la lista
   - ¿Qué decisiones necesitás de mí?

7. Compromisos (5 min)
   - ¿Qué acordamos? ¿Quién hace qué?
```

---

*Volver a: [← Referencias y Recursos](lecturas-y-recursos.md)*
