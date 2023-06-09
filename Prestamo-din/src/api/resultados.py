from flask import Blueprint, request, jsonify, json
from common.toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.resultado import resultado, resultadosSchema

routes_resultados = Blueprint("routes_resultados", __name__)

#resultados
resultado_schema = resultadosSchema()
resultados_schema = resultadosSchema(many=True)

#metodos para resultado inicio
#---------SAVE/CREAR------------
@routes_resultados.route('/saveresultados', methods=['POST'])
def guardar_resultados():    
    newresultados = request.json['fecha', 'cuota', 'capital', 'interes','saldo']
    new_res = resultado(newresultados)
    db.session.add(new_res)
    db.session.commit()
    return redirect('/resultados')

@routes_resultados.route('/resultados', methods=['GET'])
def obtenerresultados():    
    returnall = resultado.query.all()
   
    resultado_resultados = resultadosSchema.dump(returnall)
    return jsonify(resultado_resultados)

@routes_resultados.route('/eliminarresultados/<id>', methods=['GET'] )
def eliminarP(id):
    prov = resultado.query.get(id)
    db.session.delete(prov)
    db.session.commit()
    return jsonify(resultados_schema.dump(prov)) 

@routes_resultados.route('/actualizarresultados', methods=['POST'] )
def actualizarP():
    id = request.json['id']
    res = request.json['fecha', 'cuota', 'capital', 'interes','saldo']
    resusuario = resultado.query.get(id)
    resusuario.Nombre_cuotas = res
    db.session.commit()
    return redirect('/resultados')

@routes_resultados.route('/saveresultados', methods=['POST'])
def guardar_monton():
    monto = float(request.json.get('monto'))
    interes = float(request.json.get('interes'))
    tiempo = int(request.json.get('tiempo'))

    new_res = resultado(monto=monto, interes=interes, tiempo=tiempo)
    db.session.add(new_res)
    db.session.commit()
    
@routes_resultados.route('/saveArray', methods=['POST'])
def guardar_arrayw():
    monto = float(request.json.get('monto'))
    interes = float(request.json.get('interes'))
    tiempo = int(request.json.get('tiempo'))

    new_res = resultado(monto=monto, interes=interes, tiempo=tiempo)
    db.session.add(new_res)
    db.session.commit()


#metodos para resultado final 