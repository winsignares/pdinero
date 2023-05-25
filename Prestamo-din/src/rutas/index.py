from db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.index import index

routes_index = Blueprint("routes_index", __name__)

@routes_index.route('/indexindex', methods=['GET'] )
def indexindex():
    
    return render_template('/main/index.html')

@routes_index.route('/guardar',methods=['POST'])
def saveprovider():
    #request.form['title']
    monto = request.form['monto']
    interes = request.form['interes']
    tiempo = request.form['tiempo']
    print(monto,interes,tiempo)
    
    new_inde = index(monto,interes,tiempo)
    db.session.add(new_inde)
    db.session.commit()
    return monto,interes,tiempo
    