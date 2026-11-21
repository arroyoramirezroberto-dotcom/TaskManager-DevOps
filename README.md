# TaskManager-DevOps
Sistema web de gestión de tareas de TechSolutions.

## Funciones
Crear, consultar, editar y eliminar tareas; estados Pendiente, En proceso y Terminada; prioridades Alta, Media y Baja. Almacenamiento SQLite.

## Ejecutar
Python 3.12:
```bash
pip install -r requirements.txt
python app.py
```
Abrir http://127.0.0.1:5000

## Pruebas
```bash
pytest -v
```

## DevOps
- CI: `.github/workflows/ci.yml`.
- Entrega: `.github/workflows/release.yml` al publicar una versión.
- Render: `render.yaml` (requiere configurar el servicio y comprobar disponibilidad de disco persistente).
- Healthcheck: `/health`.
- Plan e historias: `docs/PLAN.md`.
- Matriz de pruebas: `docs/PRUEBAS.md`.

## API
GET/POST `/api/tareas`; PUT/PATCH/DELETE `/api/tareas/<id>`.

## Evidencias pendientes
Tablero Projects, responsables reales, Issues, ramas y PR revisados, ejecución exitosa de Actions, release v1.0.0 y URL pública verificada.
