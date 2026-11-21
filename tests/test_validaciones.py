import pytest
from app import app

@pytest.fixture
def client(tmp_path):
    app.config.update(TESTING=True, DATABASE=str(tmp_path / "validaciones.db"))
    with app.test_client() as client:
        yield client

def test_json_invalido(client):
    response = client.post("/api/tareas", data="invalid", content_type="application/json")
    assert response.status_code == 400

def test_prioridad_invalida(client):
    response = client.post("/api/tareas", json={"nombre": "Tarea", "prioridad": "Urgentísima"})
    assert response.status_code == 400

def test_nombre_solo_espacios(client):
    response = client.post("/api/tareas", json={"nombre": "   "})
    assert response.status_code == 400

def test_cambios_persisten_entre_solicitudes(client):
    response = client.post("/api/tareas", json={"nombre": "Persistente", "prioridad": "Alta"})
    task_id = response.json["id"]
    assert client.get("/api/tareas").json[0]["id"] == task_id
    response = client.patch(f"/api/tareas/{task_id}", json={"estado": "En proceso"})
    assert response.status_code == 200
    assert client.get("/api/tareas").json[0]["estado"] == "En proceso"

def test_editar_inexistente(client):
    assert client.patch("/api/tareas/9999", json={"estado": "Terminada"}).status_code == 404
