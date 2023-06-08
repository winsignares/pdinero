from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template 
from Model.login  import logins, loginsSchema

routes_login = Blueprint("routes_login", __name__)

@routes_login.route("/indexlogin", methods=['GET'])
def login():
    return render_template("/main/login.html")
#logins
logins_schema = loginsSchema()
logins_schema = loginsSchema(many=True)

#metodos para login inicio
#---------SAVE/CREAR------------
@routes_login.route('/savelogins', methods=['POST'])
def guardar_logins():    
    usuario = request.form['usuario']
    contraseña = request.form['contraseña']
    new_log = logins(usuario,contraseña)
    db.session.add(new_log)
    db.session.commit()
    
    # Devolver una respuesta JSON
    return jsonify({'message': 'Datos guardados correctamente'})

@routes_login.route('/verificarlogin', methods=['POST'])
def verificarlogin():    
    usuario = request.form['usuario']
    contraseña = request.form['contraseña']
 
    verificacion = db.session.query(logins).filter(logins.usuario == usuario,logins.contraseña == contraseña).first()

    # Busca el usuario en la base de datos
    if verificacion:  
        return "Correcto"
    else:
        return "malo"