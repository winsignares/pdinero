from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.registro import registros

routes_mostrar = Blueprint("routes_mostrar", __name__)

'''
hacer histrial por medio de los datos user e index(monto)
'''


@routes_mostrar.route('/historial', methods=['GET','POST'] )
def historial():
    id = request.form.get('id')
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    monto = request.form.get('monto')
    interes = request.form.get('interes')
    tiempo = request.form.get('tiempo')


    usuario = .query.get(id)
    usuario.nombre = nombre
    usuario.apellido = apellido
    usuario.monto = monto
    usuario.interes = interes
    usuario.tiempo = tiempo

    # Guardar los cambios en la base de datos
    db.session.commit()
      
    # Enviar una respuesta exitosa
    return jsonify({'message': 'historial guardado correctamente'})
