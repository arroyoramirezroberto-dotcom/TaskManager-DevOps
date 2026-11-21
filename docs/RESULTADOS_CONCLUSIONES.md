# Resultados y conclusiones — Remedial DevOps

**Proyecto:** TaskManager, caso TechSolutions  
**Fecha:** 21 de noviembre de 2026  
**Repositorio:** https://github.com/arroyoramirezroberto-dotcom/TaskManager-DevOps  
**Sitio:** https://taskmanager-devops-arroyo.onrender.com

## Introducción
TechSolutions requería un sistema web para registrar y organizar tareas. El objetivo de la práctica fue aplicar las fases de DevOps usando GitHub para controlar versiones, probar cambios, preparar entregas y desplegar una aplicación.

## Objetivos
Desarrollar las seis funcionalidades RF01-RF06 y documentar las fases Plan, Code, Build, Test, Release, Deploy, Operate y Monitor.

## Tecnologías
Flask, SQLite, HTML, CSS, JavaScript, Git, GitHub, Pytest, GitHub Actions, Gunicorn y Render.

## Desarrollo y resultados
- **Plan:** Issues #1-#6 con responsables, etiquetas de fase, prioridad y estado; historias y criterios de aceptación en `docs/PLAN.md`. Tablero GitHub Projects aún pendiente.
- **Code:** frontend y API Flask para registrar, consultar, editar, eliminar, cambiar estado y prioridad. Ramas feature y PR #7 fusionado a main.
- **Build/Test:** GitHub Actions ejecutó `pytest -v` exitosamente: https://github.com/arroyoramirezroberto-dotcom/TaskManager-DevOps/actions/runs/44959725348
- **Incidencia corregida:** error `ModuleNotFoundError: No module named 'app'` al recolectar pruebas; solución en `pytest.ini`.
- **Release:** workflow `.github/workflows/release.yml` preparado y notas en `docs/RELEASE_V1.0.0.md`; falta publicar el Release real `v1.0.0` y verificar el artefacto.
- **Deploy:** servicio Render creado, despliegue inicial con estado `live` y log de solicitud `HEAD /` HTTP 200. URL pública: https://taskmanager-devops-arroyo.onrender.com
- **Operate/Monitor:** endpoint `/health`, workflow `.github/workflows/monitor.yml` programado cada 6 horas; faltan capturas de ejecución y seguimiento de métricas.
- **Pruebas manuales:** las capturas proporcionadas muestran registro, validación de nombre obligatorio, listado y prioridad alta; el estado «Terminada» es visible. Falta demostrar con capturas la edición guardada y eliminación. Ver `docs/MATRIZ_PRUEBAS.md`.

## Riesgos y limitaciones
Render gratuito no garantiza persistencia de SQLite tras reinicios o redespliegues. No se ha demostrado la conservación de tareas después de un reinicio. Se recomienda una base de datos persistente.

## Propuestas de mejora para v1.1.0
1. Migrar a almacenamiento persistente con migraciones de base de datos.
2. Añadir búsqueda, filtros y paginación de tareas.
3. Añadir autenticación y separación de tareas por usuario.
4. Agregar pruebas de extremo a extremo y alertas de disponibilidad.

## Conclusiones
El proyecto permitió aplicar un flujo real de desarrollo: cambios en ramas, revisión mediante Pull Request, corrección de fallos detectados por CI y publicación de una aplicación Flask. El uso de GitHub Actions ayudó a detectar un problema de importación antes de dar por aprobadas las pruebas. El despliegue en Render mostró la importancia de comprobar el entorno real y reconocer sus limitaciones. Para completar la entrega es necesario publicar el Release, crear el tablero Projects y reunir las evidencias manuales faltantes.

## Evidencias y anexos
- Código: https://github.com/arroyoramirezroberto-dotcom/TaskManager-DevOps
- Pull Request: https://github.com/arroyoramirezroberto-dotcom/TaskManager-DevOps/pull/7
- CI: https://github.com/arroyoramirezroberto-dotcom/TaskManager-DevOps/actions/runs/44959725348
- Despliegue: https://dashboard.render.com/web/srv-dc12753l550s73d5ul4g
- Sitio: https://taskmanager-devops-arroyo.onrender.com
- Matriz: `docs/MATRIZ_PRUEBAS.md`
- Monitoreo: `docs/MONITOREO.md`
- Preguntas de análisis: `docs/PREGUNTAS_ANALISIS.md`

**Pendientes de verificación final:** tablero Projects, Release publicado y artefacto, ejecución de monitor, edición/eliminación manual, persistencia y capturas correspondientes.
