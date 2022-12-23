from utils.db import db

class Cliente(db.Model):
    rut = db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    correo = db.Column(db.String(100))

    def __init__(self,rut,nombre,apellido,correo):
        self.rut= rut
        self.nombre= nombre
        self.apellido = apellido
        self.correo = correo
    
    def get_rut(self):
        return self.rut
    def get_nombre(self):
        return self.nombre
    def get_apellido(self):
        return self.apellido
    def get_correo(self):
        return self.correo
    
