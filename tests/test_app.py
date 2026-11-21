import pytest
from app import app

@pytest.fixture
def client(tmp_path):
    app.config.update(TESTING=True, DATABASE=str(tmp_path / "test.db"))
    with app.test_client() as client:
        yield client

def test_inicio_y_salud(client):
    assert client.get("/").status_code == 200
    assert client.get("/health").json["status"] == "ok"

def test_registrar_y_consultar(client):
    r = client.post("/api/tareas", json={"nombre": "Actividad DevOps", "descripcion": "Prueba", "prioridad": "Alta"})
    assert r.status_code == 201
    assert r.json["estado"] == "Pendiente"
    assert len(client.get("/api/tareas").json) == 1

def test_nombre_obligatorio(client):
    assert client.post("/api/tareas", json={"nombre": ""}).status_code == 400

def test_editar(client):
    task = client.post("/api/tareas", json={"nombre": "Original"}).json
    r = client.put(f"/api/tareas/{task['id']}", json={"nombre": "Editada", "estado": "En proceso", "prioridad": "Baja"})
    assert r.status_code == 200
    assert r.json["nombre"] == "Editada"

def test_estado_y_prioridad(client):
    task = client.post("/api/tareas", json={"nombre": "Prueba"}).json
    r = client.patch(f"/api/tareas/{task['id']}", json={"estado": "Terminada", "prioridad": "Alta"})
    assert r.json["estado"] == "Terminada"
    assert r.json["prioridad"] == "Alta"
    assert client.patch(f"/api/tareas/{task['id']}", json={"estado": "Otro"}).status_code == 400

def test_eliminar(client):
    task = client.post("/api/tareas", json={"nombre": "Temporal"}).json
    assert client.delete(f"/api/tareas/{task['id']}").status_code == 204
    assert client.get("/api/tareas").json == []
    assert client.delete(f"/api/tareas/{task['id']}").status_code == 404
