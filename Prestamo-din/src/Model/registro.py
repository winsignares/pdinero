from config.db import db, app, ma 

class registros (db.Model):
    __tablename__ = "tblregistros"
    
    
    id  = db.Column(db.Integer, primary_key=True)
    usuario1 = db.Column(db.String(110))
    contrasena1= db.Column(db.String(110))
    confirmar1 = db.Column(db.String(110))

    
    
    def __init__(self, usuario1, contrasena1, confirmar1):
        
        self.usuario1 = usuario1
        self.contrasena1 = contrasena1
        self.confirmar1 = confirmar1
        
        
with app.app_context():
    db.create_all()

class registrosSchema(ma.Schema):
    class Meta:
        fields = ('id','usuario1', 'contrasena1', 'confirmar1')