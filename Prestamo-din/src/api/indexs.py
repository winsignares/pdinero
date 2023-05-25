from flask import Blueprint, request, jsonify, json
from common.toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.index import indexs, indexSchema

routes_indexs = Blueprint("routes_indexs", __name__)

#indexs
indexs_schema = indexSchema()
indexs_schema = indexSchema(many=True)

#metodos para login inicio
#---------SAVE/CREAR------------
@routes_indexs.route('/saveindexs', methods=['POST'])
def guardar_indexs():    
    newindexs = request.json['fecha','cuota','capital','interes','saldo']
    new_ind = indexs(newindexs)
    db.session.add(new_ind)
    db.session.commit()
    return redirect('/indexs')

@routes_indexs.route('/indexs', methods=['GET'])
def obtenerindexs():    
    returnall = indexs.query.all()
   
    resultado_indexs = indexSchema.dump(returnall)
    return jsonify(resultado_indexs)

@routes_indexs.route('/eliminarindexs/<id>', methods=['GET'] )
def eliminarP(id):
    prov = indexs.query.get(id)
    db.session.delete(prov)
    db.session.commit()
    return jsonify(indexs_schema.dump(prov)) 

@routes_indexs.route('/actualizar', methods=['POST'] )
def actualizarP():
    id = request.json['id']
    ind = request.json['fecha','cuota','capital','interes','saldo']
    indusuario = indexs.query.get(id)
    indusuario.Nombre_index = ind
    db.session.commit()
    return redirect('/indexs')
#metodos para indexs final        