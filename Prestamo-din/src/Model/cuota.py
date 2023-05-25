from config.db import db, app, ma 

class cuotas(db.Model):
    __tablename__ = "tblcuotas"
    
    
    id  = db.Column(db.Integer, primary_key=True)
    pago_cuota = db.Column(db.Float)
    valor= db.Column(db.Float)
    cuotas_restantes = db.Column(db.Float)
    fecha_pago = db.Column(db.Date)
    
    
    def __init__(self, pago_cuota, valor, cuotas_restantes, fecha_pago):
        
        self.pago_cuota = pago_cuota
        self.valor = valor
        self.cuotas_restantes = cuotas_restantes
        self.fecha_pago = fecha_pago
        
        
with app.app_context():
    db.create_all()

class cuotasSchema(ma.Schema):
    class Meta:
        fields = ('id','pago_cuota','valor','cuotas_restantes','fecha_pago')