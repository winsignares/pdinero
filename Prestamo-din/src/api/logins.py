from flask import Blueprint, request, jsonify, json
from common.toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.login  import logins, loginsSchema

routes_logins = Blueprint("routes_logins", __name__)

#logins
logins_schema = loginsSchema()
logins_schema = loginsSchema(many=True)

#metodos para login inicio
#---------SAVE/CREAR------------
@routes_logins.route('/savelogins', methods=['POST'])
def guardar_logins():    
    newlogins = request.json['usuario','contraseña']
    new_log = logins(newlogins)
    db.session.add(new_log)
    db.session.commit()
    return redirect('/logins')

@routes_logins.route('/logins', methods=['GET'])
def obtenerlogins():    
    returnall = logins.query.all()
   
    resultado_logins = loginsSchema.dump(returnall)
    return jsonify(resultado_logins)

@routes_logins.route('/eliminarlogins/<id>', methods=['GET'] )
def eliminarP(id):
    prov = logins.query.get(id)
    db.session.delete(prov)
    db.session.commit()
    return jsonify(logins_schema.dump(prov)) 

@routes_logins.route('/actualizar', methods=['POST'] )
def actualizarP():
    id = request.json['id']
    log = request.json['usuario','contraseña']
    logusuario = logins.query.get(id)
    logusuario.Nombre_cuotas = log
    db.session.commit()
    return redirect('/logins')
#metodos para logins final        