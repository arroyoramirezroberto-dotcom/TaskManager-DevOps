const $ = id => document.getElementById(id);
const form = $("task-form");
let tasks = [];
async function api(path, options = {}) {
  const response = await fetch(path, {headers: {"Content-Type": "application/json"}, ...options});
  if (!response.ok) {
    const data = await response.json().catch(() => ({}));
    throw new Error(data.error || "Error en la solicitud");
  }
  return response.status === 204 ? null : response.json();
}
function reset() {
  form.reset(); $("task-id").value = ""; $("form-title").textContent = "Nueva tarea";
  $("cancel").hidden = true;
}
async function load() {
  tasks = await api("/api/tareas");
  $("counter").textContent = tasks.length + " tareas";
  const root = $("tasks"); root.replaceChildren();
  if (!tasks.length) { const p = document.createElement("p"); p.textContent = "Todavía no hay tareas. ¡Agrega la primera!"; root.append(p); }
  for (const task of tasks) {
    const item = document.createElement("article"); item.className = "task";
    const info = document.createElement("div");
    const title = document.createElement("h3"); title.textContent = task.nombre;
    const description = document.createElement("p"); description.textContent = task.descripcion;
    const meta = document.createElement("span"); meta.className = "meta"; meta.textContent = task.estado + " · Prioridad " + task.prioridad;
    info.append(title, description, meta);
    const actions = document.createElement("div"); actions.className = "task-actions";
    const edit = document.createElement("button"); edit.className = "secondary"; edit.textContent = "Editar";
    edit.onclick = () => { for (const key of ["nombre", "descripcion", "estado", "prioridad"]) $(key).value = task[key]; $("task-id").value = task.id; $("form-title").textContent = "Editar tarea"; $("cancel").hidden = false; window.scrollTo({top: 0, behavior: "smooth"}); };
    const next = document.createElement("button"); next.className = "secondary"; next.textContent = "Avanzar";
    next.onclick = async () => { try { const estado = task.estado === "Pendiente" ? "En proceso" : "Terminada"; await api("/api/tareas/" + task.id, {method: "PATCH", body: JSON.stringify({estado})}); await load(); } catch (e) { $("message").textContent = e.message; } };
    const del = document.createElement("button"); del.textContent = "Eliminar";
    del.onclick = async () => { if (!confirm("¿Eliminar esta tarea?")) return; try { await api("/api/tareas/" + task.id, {method: "DELETE"}); await load(); } catch (e) { $("message").textContent = e.message; } };
    actions.append(edit, next, del); item.append(info, actions); root.append(item);
  }
}
form.onsubmit = async event => {
  event.preventDefault();
  const id = $("task-id").value;
  const body = Object.fromEntries(["nombre", "descripcion", "estado", "prioridad"].map(k => [k, $(k).value]));
  try {
    await api(id ? "/api/tareas/" + id : "/api/tareas", {method: id ? "PUT" : "POST", body: JSON.stringify(body)});
    $("message").textContent = id ? "Tarea actualizada" : "Tarea registrada";
    reset(); await load();
  } catch (e) { $("message").textContent = e.message; }
};
$("cancel").onclick = reset;
load().catch(e => { $("message").textContent = e.message; });
