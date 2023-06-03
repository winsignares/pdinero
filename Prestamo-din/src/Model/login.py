from config.db import db, app, ma

class logins(db.Model):
    __tablename__ = "tbllogins"
    
    
    id  = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50))
    contraseña = db.Column(db.String(50))

    
    def __init__(self, usuario, contraseña):
        
        self.usuario = usuario
        self.contraseña = contraseña
       
        
        
with app.app_context():
    db.create_all()

class loginsSchema(ma.Schema):
    class Meta:
        fields = ('id','usuario','contraseña')