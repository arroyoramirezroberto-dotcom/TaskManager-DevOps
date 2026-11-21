# Primera versión estable de TaskManager — v1.0.0

## Funcionalidades
- RF01: registro de tareas.
- RF02: listado de tareas.
- RF03: edición de tareas.
- RF04: eliminación de tareas.
- RF05: estados Pendiente, En proceso y Terminada.
- RF06: prioridades Alta, Media y Baja.

## Tecnología
Flask, SQLite, HTML, CSS, JavaScript, pytest y GitHub Actions.

## Verificación
CI aprobado en https://github.com/arroyoramirezroberto-dotcom/TaskManager-DevOps/actions/runs/44959725348
Pull Request integrado: https://github.com/arroyoramirezroberto-dotcom/TaskManager-DevOps/pull/7
Servicio público: https://taskmanager-devops-arroyo.onrender.com

## Limitaciones conocidas
En Render gratuito, SQLite no tiene persistencia garantizada entre reinicios y despliegues. El servicio está publicado para fines de demostración y evaluación.

## Pasos para publicar la versión
1. En GitHub, abrir Releases > Draft a new release.
2. Crear el tag `v1.0.0` desde `main`.
3. Título: `Primera versión estable de TaskManager`.
4. Copiar estas notas y publicar.
5. Verificar que el workflow `release.yml` se ejecute y genere el artefacto.

Estas notas preparan la publicación; el Release no se considera creado hasta publicarlo en GitHub.
