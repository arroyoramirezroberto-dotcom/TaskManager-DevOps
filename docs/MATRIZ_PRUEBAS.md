# Matriz de pruebas funcionales — TaskManager

| ID | Prueba | Resultado esperado | Evidencia disponible | Estado |
|---|---|---|---|---|
| CP01 | Registrar una tarea | Se guarda y muestra en la lista | Captura de usuario 21/11/2026: tarea «Prueba de TaskManager» y mensaje «Tarea registrada» | Observado |
| CP02 | Registrar sin nombre | Aparece una validación | Captura de usuario 21/11/2026: «Rellena este campo» | Observado |
| CP03 | Consultar tareas | Aparece el listado | Captura de usuario: «Mis tareas», 1 tarea | Observado |
| CP04 | Editar una tarea | Se actualiza su información | Captura muestra formulario en modo edición; no demuestra guardado de edición | Pendiente de confirmar |
| CP05 | Eliminar una tarea | Desaparece del listado | Botón visible; falta captura posterior a eliminar | Pendiente |
| CP06 | Cambiar estado | El estado se actualiza | Captura muestra «Terminada», sin secuencia antes/después | Parcial |
| CP07 | Seleccionar prioridad | Se guarda prioridad elegida | Captura muestra «Prioridad Alta» | Observado |

## Pruebas automáticas
Workflow: https://github.com/arroyoramirezroberto-dotcom/TaskManager-DevOps/actions/runs/44959725348
Resultado: success. Incluye ejecución de `pytest -v`.

## Registro de error y corrección
En la ejecución inicial de CI, pytest falló durante la recolección por `ModuleNotFoundError: No module named 'app'`. Se corrigió agregando `pytest.ini` con `pythonpath = .` y `testpaths = tests`. La ejecución posterior #14 pasó.

## Cómo terminar la evidencia
1. Editar la tarea y guardar un nombre diferente; capturar el listado actualizado.
2. Eliminarla y capturar el listado vacío.
3. Cambiar una nueva tarea de Pendiente a En proceso y Terminada, capturando antes y después.
4. Guardar capturas en el informe final o adjuntarlas al Issue de pruebas.

No marcar como aprobada una prueba manual que no se haya observado.
