from config.db import db, app, ma 

class index(db.Model):
    __tablename__ = "tblindex"
    
    
    id  = db.Column(db.Integer, primary_key=True)
    monto = db.Column(db.String(50))
    interes= db.Column(db.String(50))
    tiempo = db.Column(db.Date)
    
    def __init__(self, monto, interes, tiempo):
        
        self.monto = monto
        self.interes = interes
        self.tiempo = tiempo

        
        
        
with app.app_context():
    db.create_all()

class indexSchema(ma.Schema):
    class Meta:
        fields = ('id','monto','interes','tiempo')