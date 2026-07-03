<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Clientes ERP</title>

<style>


body{
    margin:0;
    font-family:Arial;
    background: linear-gradient(135deg, #0066ff, #00c6ff);
}


h1{
    text-align:center;
    color:white;
    margin:20px;
}


.container{
    width:92%;
    margin:auto;
}


.card{
    background:white;
    padding:20px;
    border-radius:15px;
    margin-bottom:20px;
    box-shadow:0 10px 25px rgba(0,0,0,0.2);
}


input{
    padding:10px;
    margin:5px;
    border:1px solid #ddd;
    border-radius:8px;
}


.btn{
    padding:10px 14px;
    border:none;
    border-radius:8px;
    cursor:pointer;
}

.primary{ background:linear-gradient(135deg,#0066ff,#00c6ff); color:white; }
.danger{ background:#e74c3c; color:white; }
.warning{ background:#f0ad4e; color:white; }

/* TOOLBAR */
.toolbar{
    display:flex;
    gap:10px;
    margin-bottom:15px;
}

/* TABLA */
table{
    width:100%;
    border-collapse:collapse;
}

th{
    background:#1f4e79;
    color:white;
    padding:12px;
}

td{
    padding:10px;
    text-align:center;
    border-bottom:1px solid #eee;
}

tr:hover{
    background:#f1f5ff;
    cursor:pointer;
}

/* MODAL */
.modal{
    display:none;
    position:fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    background:rgba(0,0,0,0.5);
}

.modal-content{
    background:white;
    width:420px;
    margin:8% auto;
    padding:20px;
    border-radius:12px;
    position:relative;
}

.close{
    position:absolute;
    right:10px;
    top:10px;
    font-size:22px;
    cursor:pointer;
}

.selected{
    background:#dbe9ff !important;
}

</style>
</head>

<body>

<h1>GESTIÓN DE CLIENTES</h1>

<div class="container">

<!-- ➕ FORM -->
<div class="card">
<form action="/clientes/crear" method="POST">

    <input name="nombres" placeholder="Nombres" required>
    <input name="apellidos" placeholder="Apellidos" required>
    <input name="direccion" placeholder="Dirección">
    <input name="telefono" placeholder="Teléfono">
    <input name="correo" placeholder="Correo" required>
    <input name="clave" placeholder="Clave" required>

    <button class="btn primary">Agregar Cliente</button>
</form>
</div>

<!-- 🧠 ACCIONES GLOBALES -->
<div class="card toolbar">
    <button class="btn warning" onclick="editar()">✏ Editar</button>
    <button class="btn danger" onclick="eliminar()">🗑 Eliminar</button>
</div>

<!-- 📄 TABLA -->
<div class="card">

<table>
<tr>
    <th>ID</th>
    <th>Nombres</th>
    <th>Apellidos</th>
    <th>Dirección</th>
    <th>Teléfono</th>
    <th>Correo</th>
</tr>

{% for c in clientes %}
<tr onclick="selectRow(this, {{ c[0] }})">
    <td>{{ c[0] }}</td>
    <td>{{ c[1] }}</td>
    <td>{{ c[2] }}</td>
    <td>{{ c[3] }}</td>
    <td>{{ c[4] }}</td>
    <td>{{ c[5] }}</td>
</tr>
{% endfor %}

</table>

</div>
</div>

<!-- 🟣 MODAL -->
<div class="modal" id="modal">
  <div class="modal-content">

    <span class="close" onclick="closeModal()">&times;</span>

    <form id="formEdit" method="POST">

        <input id="nombres" name="nombres">
        <input id="apellidos" name="apellidos">
        <input id="direccion" name="direccion">
        <input id="telefono" name="telefono">
        <input id="correo" name="correo">

        <button class="btn primary">Guardar</button>
    </form>

  </div>
</div>

<script>

let selectedId = null;
let selectedRow = null;

function selectRow(row,id){

    if(selectedRow){
        selectedRow.classList.remove("selected");
    }

    selectedRow = row;
    selectedRow.classList.add("selected");

    selectedId = id;
}

function eliminar(){
    if(selectedId){
        if(confirm("¿Eliminar cliente?")){
            window.location = "/clientes/eliminar/" + selectedId;
        }
    } else {
        alert("Selecciona un cliente");
    }
}

function editar(){
    if(!selectedId){
        alert("Selecciona un cliente");
        return;
    }

    document.getElementById("modal").style.display="block";

    let cells = selectedRow.children;

    document.getElementById("nombres").value = cells[1].innerText;
    document.getElementById("apellidos").value = cells[2].innerText;
    document.getElementById("direccion").value = cells[3].innerText;
    document.getElementById("telefono").value = cells[4].innerText;
    document.getElementById("correo").value = cells[5].innerText;

    document.getElementById("formEdit").action="/clientes/editar/"+selectedId;
}

function closeModal(){
    document.getElementById("modal").style.display="none";
}

window.onclick = function(e){
    let modal = document.getElementById("modal");
    if(e.target == modal){
        modal.style.display="none";
    }
}

</script>

</body>
</html>
