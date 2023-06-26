from config.db import db, app, ma

class logins(db.Model):
    __tablename__ = "tbllogins"
    
    
    id  = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(110))
    contraseña = db.Column(db.String(110))
    id_registros = db.Column(db.Integer, db.ForeignKey('tblregistros.id'))

    
    def __init__(self, usuario, contraseña,id_registros):
        
        self.usuario = usuario
        self.contraseña = contraseña
        self.id_registros = id_registros
       
        
        
with app.app_context():
    db.create_all()

class loginsSchema(ma.Schema):
    class Meta:
        fields = ('id','usuario','contraseña','id_registros')