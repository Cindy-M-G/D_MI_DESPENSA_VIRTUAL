from flask import Flask, render_template, request, redirect
import oracledb

app = Flask(__name__)

def obtener_conexion():
    return oracledb.connect(
        user="MI_DESPENSA_VIRTUAL",
        password="MI_DESPENSA_VIRTUAL",
        dsn="localhost/XE"
    )

# LISTAR
@app.route('/clientes')
def clientes():
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT Id_cliente, Nombres, Apellidos, Direccion, Telefono, Correo
        FROM CLIENTE
    """)

    datos = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("clientes.html", clientes=datos)

# CREAR
@app.route('/clientes/crear', methods=['POST'])
def crear_cliente():
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO CLIENTE (Nombres, Apellidos, Direccion, Telefono, Correo, CLAVE)
        VALUES (:1,:2,:3,:4,:5,:6)
    """, (
        request.form['nombres'],
        request.form['apellidos'],
        request.form['direccion'],
        request.form['telefono'],
        request.form['correo'],
        request.form['clave']
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/clientes')

# EDITAR
@app.route('/clientes/editar/<int:id>', methods=['POST'])
def editar_cliente(id):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE CLIENTE
        SET Nombres=:1, Apellidos=:2, Direccion=:3, Telefono=:4, Correo=:5
        WHERE Id_cliente=:6
    """, (
        request.form['nombres'],
        request.form['apellidos'],
        request.form['direccion'],
        request.form['telefono'],
        request.form['correo'],
        id
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/clientes')

# ELIMINAR
@app.route('/clientes/eliminar/<int:id>')
def eliminar_cliente(id):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM CLIENTE WHERE Id_cliente=:1", (id,))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/clientes')

if __name__ == "__main__":
    app.run(debug=True)
