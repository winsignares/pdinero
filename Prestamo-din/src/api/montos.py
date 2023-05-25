     
from flask import Blueprint, request, jsonify, json
from common.toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.monto  import montos, montosSchema

routes_montos = Blueprint("routes_montos", __name__)

#montos
montos_schema = montosSchema()
montos_schema = montosSchema(many=True)

#metodos para monto inicio
#---------SAVE/CREAR------------
@routes_montos.route('/savemontos', methods=['POST'])
def guardar_montos():    
    newmontos = request.json['fecha','cuota','capital','interes']
    new_mon = montos(newmontos)
    db.session.add(new_mon)
    db.session.commit()
    return redirect('/montos')

@routes_montos.route('/montos', methods=['GET'])
def obtenermontos():    
    returnall = montos.query.all()
   
    resultado_montos = montosSchema.dump(returnall)
    return jsonify(resultado_montos)

@routes_montos.route('/eliminarmontos/<id>', methods=['GET'] )
def eliminarP(id):
    prov = montos.query.get(id)
    db.session.delete(prov)
    db.session.commit()
    return jsonify(montos_schema.dump(prov)) 

@routes_montos.route('/actualizarmontos', methods=['POST'] )
def actualizarP():
    id = request.json['id']
    mon = request.json['fecha','cuota','capital','interes']
    monusuario = montos.query.get(id)
    monusuario.Nombre_cuotas = cuo
    db.session.commit()
    return redirect('/montos')
#metodos para monto final 
       