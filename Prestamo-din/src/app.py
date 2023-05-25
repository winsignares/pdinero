from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma
import os


#importar routes de las tablas 

from api.cuotas import routes_cuotas
from api.montos import routes_montos
from api.logins import routes_logins




#ubicacion del api de las tablas 
app.register_blueprint(routes_cuotas, url_prefix="/api") 
app.register_blueprint(routes_montos, url_prefix="/api")
app.register_blueprint(routes_logins, url_prefix="/api")

# tablas de modelo 

#importar routes de los html
from rutas.index import routes_index
# from Model.index import routes_index

#ubicacion de los html
app.register_blueprint(routes_index, url_prefix="/fronted")





#------------------------------------------------

@app.route("/")
def index():
    titulo= "tasa de amortización"
    return render_template('/index.html', titles=titulo)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')