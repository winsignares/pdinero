from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.registro import registros

routes_registros = Blueprint("routes_registro", __name__)

@routes_registros.route('/indexregistros', methods=['GET'] )
def indexregistros():
    
    return render_template('/main/registro.html')