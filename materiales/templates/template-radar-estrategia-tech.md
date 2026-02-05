# Template: Radar de Estrategia Tecnológica

## Actividad: "Audit Exprés" — Bloque 2

### Instrucciones
1. Evalúen cada dimensión del 1 al 5 según la situación **actual** de su institución.
2. Marquen con un punto en el radar.
3. Conecten los puntos para visualizar el perfil.
4. Comparen con su par: ¿dónde coinciden? ¿dónde difieren?

---

## Rúbrica de evaluación

### 1. INFRAESTRUCTURA
*¿Dónde viven sus sistemas y datos?*

| Nivel | Descripción |
|-------|-------------|
| 1 | Todo on-premise, servidores propios, sin redundancia |
| 2 | Mayoría on-premise, algún servicio SaaS aislado |
| 3 | Híbrido: algunos sistemas en la nube, otros on-premise |
| 4 | Cloud-first: nuevos sistemas van a la nube, migración en curso |
| 5 | Cloud-native: todo en la nube, con elasticidad y alta disponibilidad |

**Mi institución:** ___/5

---

### 2. ARQUITECTURA
*¿Cómo están organizados sus sistemas?*

| Nivel | Descripción |
|-------|-------------|
| 1 | Sistemas aislados, sin integración, islas de datos |
| 2 | Algunas integraciones punto a punto (archivos, exports manuales) |
| 3 | Hay un sistema central pero no todos se integran con él |
| 4 | Ecosistema integrado con APIs, hay un "maestro de datos" definido |
| 5 | Arquitectura orientada a servicios, event-driven, desacoplada |

**Mi institución:** ___/5

---

### 3. DATOS
*¿Cómo usan los datos para tomar decisiones?*

| Nivel | Descripción |
|-------|-------------|
| 1 | No tenemos reportes confiables, cada área tiene sus propios Excel |
| 2 | Reportes básicos (matrícula, ingresos) pero manuales y con demora |
| 3 | Dashboard operativo con datos actualizados regularmente |
| 4 | BI integrado: dashboards en tiempo real, KPIs definidos, análisis de tendencias |
| 5 | Data-driven: modelos predictivos (deserción, demanda), datos como activo estratégico |

**Mi institución:** ___/5

---

### 4. SEGURIDAD
*¿Qué tan protegidos están sus datos y sistemas?*

| Nivel | Descripción |
|-------|-------------|
| 1 | Sin políticas formales, contraseñas compartidas, sin backups regulares |
| 2 | Backups básicos, antivirus, pero sin políticas de acceso claras |
| 3 | IAM implementado, políticas de acceso por rol, backups automatizados |
| 4 | Seguridad gestionada: monitoreo, auditorías, plan de respuesta a incidentes |
| 5 | Zero-trust, compliance con regulaciones (ley de datos personales), cultura de seguridad |

**Mi institución:** ___/5

---

### 5. TALENTO
*¿Tienen las personas y las capacidades para gestionar la tecnología?*

| Nivel | Descripción |
|-------|-------------|
| 1 | IT = 1-2 personas que "apagan incendios", sin equipo formal |
| 2 | Equipo IT operativo pero sin capacidad de desarrollo ni innovación |
| 3 | Equipo IT con roles definidos + algunos proveedores estratégicos |
| 4 | Equipo híbrido (interno + partners), con capacidad de desarrollo y evolución |
| 5 | Cultura tech: equipos multidisciplinarios, producto + ingeniería + datos + diseño |

**Mi institución:** ___/5

---

### 6. INNOVACIÓN
*¿Cómo incorporan nuevas tecnologías?*

| Nivel | Descripción |
|-------|-------------|
| 1 | No hay presupuesto ni tiempo para innovar, reaccionamos a problemas |
| 2 | Innovamos cuando un vendor nos propone algo o por presión del mercado |
| 3 | Hay interés pero no hay proceso: pilotos aislados sin seguimiento |
| 4 | Proceso de evaluación de tecnologías, pilotos controlados, roadmap de innovación |
| 5 | Cultura de experimentación: hipótesis → piloto → escala, con métricas de impacto |

**Mi institución:** ___/5

---

## Radar visual

```
              INFRAESTRUCTURA
                    5
                    |
                    4
                    |
                    3
                    |
                    2
                    |
INNOVACIÓN ----1----+----1---- ARQUITECTURA
                    |
                    2
                    |
                    3
                    |
                    4
                    |
        TALENTO     5     DATOS
                    |
               SEGURIDAD
```

> Dibujen su perfil conectando los 6 puntos. Las "puntas" son fortalezas. Las "muescas" son gaps prioritarios.

---

## Reflexión en parejas (10 min)

1. ¿Cuál es su **dimensión más fuerte**? ¿Por qué?
2. ¿Cuál es su **gap más crítico**? ¿Qué consecuencia tiene para el negocio?
3. Si pudieran mejorar **solo una dimensión** el próximo año, ¿cuál elegirían?
