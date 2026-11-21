# Informe de entrega y evidencias DevOps — TaskManager

Fecha de verificación: 21 de noviembre de 2026.

## Plan
Repositorio público: https://github.com/arroyoramirezroberto-dotcom/TaskManager-DevOps
Historias: docs/PLAN.md. Issues de seguimiento #1 a #6.
Pendiente: crear tablero GitHub Projects y configurar campos, responsables y fechas.

## Code
Aplicación Flask + SQLite, frontend HTML/CSS/JS. Funcionalidades RF01 a RF06 implementadas.
Pull Request #7 integrado a main: https://github.com/arroyoramirezroberto-dotcom/TaskManager-DevOps/pull/7

## Build y Test
Workflow CI: .github/workflows/ci.yml
Prueba automatizada aprobada: https://github.com/arroyoramirezroberto-dotcom/TaskManager-DevOps/actions/runs/44959725348
La ejecución #14 concluyó con éxito, incluido el paso pytest -v.
Pruebas manuales CP01-CP07: pendiente realizar en navegador y adjuntar capturas reales.

## Release
Workflow para publicación de release: .github/workflows/release.yml
Pendiente crear Release v1.0.0 desde GitHub y verificar el artefacto publicado.
Título propuesto: Primera versión estable de TaskManager.

## Deploy
Servicio Render: https://dashboard.render.com/web/srv-dc12753l550s73d5ul4g
Aplicación: https://taskmanager-devops-arroyo.onrender.com
Despliegue dep-dc1275bl550s73d5um60 con estado live, finalizado el 21/11/2026.
Logs confirmaron build exitoso, inicio de gunicorn y respuesta HEAD / HTTP 200.

**Limitación importante:** el servicio usa el plan gratuito y SQLite en /tmp/taskmanager.db, sin almacenamiento persistente garantizado tras reinicios o redespliegues. Para producción, usar PostgreSQL persistente o disco compatible.

## Operate y Monitor
Punto de salud: GET /health, responde JSON con status ok.
Pendiente: monitoreo periódico, tiempos de respuesta y evidencias de solicitudes reales de CRUD.

## Tres mejoras propuestas
1. Base de datos PostgreSQL persistente y migraciones.
2. Autenticación y roles para aislar tareas de usuarios.
3. Filtros por prioridad/estado y búsqueda con paginación.

## Evidencias por capturar
- Capturas del tablero y los campos del proyecto.
- Capturas de pruebas manuales CP01-CP07.
- Captura del release y artefacto.
- Capturas del servicio público y su funcionamiento CRUD.
- Registro de monitoreo y resolución de incidencias.

No se deben presentar como completadas actividades sin evidencia real.
