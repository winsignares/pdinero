from flask import Blueprint, request, jsonify, json
from common.toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.registro  import registros, registrosSchema

routes_registros = Blueprint("routes_registros", __name__)

#registros
registro_schema = registrosSchema()
registros_schema = registrosSchema(many=True)

#metodos para registro inicio
#---------SAVE/CREAR------------
@routes_registros.route('/saveregistros', methods=['POST'])
def guardar_registros():    
    newregistros = request.json['nombre', 'apellido', 'dirección', 'correo','telefono']
    new_reg = registros(newregistros)
    db.session.add(new_reg)
    db.session.commit()
    return redirect('/registros')

@routes_registros.route('/registros', methods=['GET'])
def obtenerregistros():    
    returnall = registros.query.all()
   
    resultado_registros = registrosSchema.dump(returnall)
    return jsonify(resultado_registros)

@routes_registros.route('/eliminarregistros/<id>', methods=['GET'] )
def eliminarP(id):
    prov = registros.query.get(id)
    db.session.delete(prov)
    db.session.commit()
    return jsonify(registros_schema.dump(prov)) 

@routes_registros.route('/actualizarregistros', methods=['POST'] )
def actualizarP():
    id = request.json['id']
    reg = request.json['nombre', 'apellido', 'dirección', 'correo','telefono']
    regusuario = registros.query.get(id)
    regusuario.Nombre_cuotas = reg
    db.session.commit()
    return redirect('/registros')

@routes_registros.route('/saveregistros', methods=['POST'])
def guardar():    
    newregistros = request.json['nombre', 'apellido', 'dirección', 'correo','telefono']
    new_reg = registros(newregistros)
    db.session.add(new_reg)
    db.session.commit()
    return redirect('/registros')
#metodos para registro final 
       