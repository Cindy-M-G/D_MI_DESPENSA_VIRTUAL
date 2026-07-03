from flask import Blueprint, render_template, request, session, redirect
from db import get_connection

auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        clave = request.form['clave']

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT Id_cliente, Nombres
            FROM CLIENTE
            WHERE Correo=:1 AND CLAVE=:2
        """, (email, clave))

        user = cur.fetchone()

        if user:
            session['user'] = user[1]
            session['role'] = "ADMIN"
            return redirect('/dashboard')

    return render_template("login.html")
