import os
import sqlite3
from flask import Flask, render_template, request, jsonify, g

app = Flask(__name__)
app.config["DATABASE"] = os.environ.get("DATABASE_PATH", os.path.join(app.instance_path, "tasks.db"))
ESTADOS = ("Pendiente", "En proceso", "Terminada")
PRIORIDADES = ("Alta", "Media", "Baja")

def db():
    if "db" not in g:
        os.makedirs(os.path.dirname(os.path.abspath(app.config["DATABASE"])), exist_ok=True)
        g.db = sqlite3.connect(app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    connection = g.pop("db", None)
    if connection is not None:
        connection.close()

def init_db():
    db().execute("""CREATE TABLE IF NOT EXISTS tareas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL, descripcion TEXT NOT NULL DEFAULT '',
        estado TEXT NOT NULL DEFAULT 'Pendiente',
        prioridad TEXT NOT NULL DEFAULT 'Media'
    )""")
    db().commit()

@app.before_request
def setup():
    init_db()

def serialize(row):
    return dict(row)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/api/tareas")
def listar():
    return jsonify([serialize(r) for r in db().execute("SELECT * FROM tareas ORDER BY id DESC")])

def validar(data, parcial=False):
    if not isinstance(data, dict):
        return "Se requiere un objeto JSON"
    if (not parcial or "nombre" in data) and (not isinstance(data.get("nombre"), str) or not data["nombre"].strip()):
        return "El nombre es obligatorio"
    if "descripcion" in data and not isinstance(data["descripcion"], str):
        return "Descripción inválida"
    if "estado" in data and data["estado"] not in ESTADOS:
        return "Estado inválido"
    if "prioridad" in data and data["prioridad"] not in PRIORIDADES:
        return "Prioridad inválida"
    return None

@app.post("/api/tareas")
def crear():
    data = request.get_json(silent=True)
    error = validar(data)
    if error:
        return jsonify(error=error), 400
    cursor = db().execute("INSERT INTO tareas (nombre, descripcion, estado, prioridad) VALUES (?, ?, ?, ?)",
        (data["nombre"].strip(), data.get("descripcion", ""), data.get("estado", "Pendiente"), data.get("prioridad", "Media")))
    db().commit()
    return jsonify(serialize(db().execute("SELECT * FROM tareas WHERE id=?", (cursor.lastrowid,)).fetchone())), 201

@app.route("/api/tareas/<int:task_id>", methods=["PUT", "PATCH"])
def editar(task_id):
    row = db().execute("SELECT * FROM tareas WHERE id=?", (task_id,)).fetchone()
    if row is None:
        return jsonify(error="Tarea no encontrada"), 404
    data = request.get_json(silent=True)
    error = validar(data, parcial=request.method == "PATCH")
    if error:
        return jsonify(error=error), 400
    fields = {k: data[k] for k in ("nombre", "descripcion", "estado", "prioridad") if k in data}
    if "nombre" in fields:
        fields["nombre"] = fields["nombre"].strip()
    if fields:
        db().execute("UPDATE tareas SET " + ", ".join(k + "=?" for k in fields) + " WHERE id=?",
            (*fields.values(), task_id))
        db().commit()
    return jsonify(serialize(db().execute("SELECT * FROM tareas WHERE id=?", (task_id,)).fetchone()))

@app.delete("/api/tareas/<int:task_id>")
def eliminar(task_id):
    cursor = db().execute("DELETE FROM tareas WHERE id=?", (task_id,))
    db().commit()
    if not cursor.rowcount:
        return jsonify(error="Tarea no encontrada"), 404
    return "", 204

if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
