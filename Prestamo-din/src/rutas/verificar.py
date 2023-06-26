from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template 
from Model.login  import logins, loginsSchema
from Model.registro  import registros, registrosSchema


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

@routes_login.route('/saveregistro', methods=['POST'])
def saveregistro():
    usuario1 = request.form['usuario1']
    contrasena1 = request.form['contrasena1']
    confirmar1 = request.form['confirmar1']

    # Verificar si el usuario ya existe en la tabla logins
    verificacion_usuario = db.session.query(logins).filter(logins.usuario == usuario1).first()

    if verificacion_usuario:
        return "El usuario ya está registrado. Por favor, inicia sesión."
    else:
        # Guardar los datos en la tabla registros
        new_regs = registros(usuario1, contrasena1, confirmar1)
        db.session.add(new_regs)
        db.session.commit()

        # Crear una entrada en la tabla logins utilizando los datos del registro
        new_log = logins(usuario1, contrasena1, new_regs.id)
        db.session.add(new_log)
        db.session.commit()

        return "Registro exitoso"



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