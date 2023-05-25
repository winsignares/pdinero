from flask import Blueprint, request, jsonify, json
from common.toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.cuota  import cuotas, cuotasSchema

routes_cuotas = Blueprint("routes_cuotas", __name__)

#cuotas
cuotas_schema = cuotasSchema()
cuotas_schema = cuotasSchema(many=True)

#metodos para cuota inicio
#---------SAVE/CREAR------------
@routes_cuotas.route('/savecuotas', methods=['POST'])
def guardar_cuotas():    
    newcuotas = request.json['pago_cuota','valor','cuotas_restantes','fecha_pago']
    new_cuo = cuotas(newcuotas)
    db.session.add(new_cuo)
    db.session.commit()
    return redirect('/cuotas')

@routes_cuotas.route('/cuotas', methods=['GET'])
def obtenercuotas():    
    returnall = cuotas.query.all()
   
    resultado_cuotas = cuotasSchema.dump(returnall)
    return jsonify(resultado_cuotas)

@routes_cuotas.route('/eliminarcuotas/<id>', methods=['GET'] )
def eliminarP(id):
    prov = cuotas.query.get(id)
    db.session.delete(prov)
    db.session.commit()
    return jsonify(cuotas_schema.dump(prov)) 

@routes_cuotas.route('/actualizarcuotas', methods=['POST'] )
def actualizarP():
    id = request.json['id']
    cuo = request.json['pago_cuota','valor','cuotas_restantes','fecha_pago']
    cuousuario = cuotas.query.get(id)
    cuousuario.Nombre_cuotas = cuo
    db.session.commit()
    return redirect('/cuotas')
#metodos para cuotas final        