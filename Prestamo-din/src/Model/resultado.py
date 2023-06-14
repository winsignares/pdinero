from config.db import db, app, ma

class resultado (db.Model):
    __tablename__ = "tblresultados"
    
    
    id  = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Datetime)
    cuota = db.Column(db.Integer)
    capital = db.Column(db.Integer)
    interes = db.Column(db.Integer)
    saldo = db.Column(db.Integer)
    
    
    
    
    def __init__(self, fecha, cuota, capital, interes,saldo):
        
        self.fecha  = fecha 
        self.cuota = cuota
        self.dirección = capital
        self.interes = interes
        self.saldo = saldo
        
        
with app.app_context():
    db.create_all()

class resultadosSchema(ma.Schema):
    class Meta:
        fields = ('id','fecha', 'cuota', 'capital', 'interes','saldo')