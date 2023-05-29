from config.db import db, app, ma 

class registros (db.Model):
    __tablename__ = "tblregistros"
    
    
    id  = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    apellido= db.Column(db.String(30))
    dirección = db.Column(db.Float)
    correo= db.Column(db.String(30))
    telefono= db.Column(db.Integer)
    id_logins= db.Column(db.Integer, db.ForeignKey('tbllogins.id'))
    
    
    def __init__(self, nombre, apellido, dirección, correo,telefono):
        
        self.nombre = nombre
        self.apellido = apellido
        self.dirección = dirección
        self.correo = correo
        self.telefono = telefono
        
        
with app.app_context():
    db.create_all()

class registrosSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'apellido', 'dirección', 'correo','telefono')