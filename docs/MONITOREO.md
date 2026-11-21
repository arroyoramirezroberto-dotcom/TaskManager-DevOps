# Operación y monitoreo

## Disponibilidad
La aplicación expone `GET /health`, que devuelve HTTP 200 y `{"status":"ok"}`.
Workflow: `.github/workflows/monitor.yml`; comprobación automática cada 6 horas y ejecución manual desde Actions.
Si falla, revisar el historial de ejecuciones y abrir un Issue de incidencia.

## Rendimiento
El workflow imprime la latencia de cada solicitud en milisegundos. El servicio gratuito de Render puede suspenderse y demorar al despertar; un tiempo alto no implica necesariamente un fallo.

## Registro de incidencias
Para cada incidente registrar fecha, síntomas, impacto, logs, solución y resultado de la nueva verificación.

## Persistencia
El servicio Render gratuito utiliza SQLite sin disco persistente. Los datos pueden desaparecer al reiniciar o redesplegar. **No afirmar persistencia permanente en la demostración.** Para resolverlo, migrar a una base de datos persistente y añadir pruebas después del reinicio.

## Mejoras
1. PostgreSQL persistente y migraciones.
2. Alertas automáticas ante fallos de salud.
3. Métricas de latencia y errores por endpoint.

## Evidencias pendientes
Captura de una ejecución del workflow de monitoreo, latencias registradas y prueba CRUD manual en el sitio público.
