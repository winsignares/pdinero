from config.db import db, app, ma 

class montos(db.Model):
    __tablename__ = "tblmontos"
    
    
    id  = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Float)
    cuota= db.Column(db.Float)
    capital = db.Column(db.Float)
    interes= db.Column(db.Date)
    # id_cuotas= db.column(db.Integer, db.Foreignkey('tblcuotas.id'))
    
    
    def __init__(self, fecha, cuota, capital, interes,id_cuotas):
        
        self.fecha = fecha
        self.cuota = cuota
        self.capital = capital
        self.interes = interes
        self.id_cuotas = id_cuotas
        
        
with app.app_context():
    db.create_all()

class montosSchema(ma.Schema):
    class Meta:
        fields = ('id','fecha','cuota','capital','interes','id_cuotas')