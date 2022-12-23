from utils.db import db

class venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String(100))
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    correo = db.Column(db.String(100))
    nombre_producto = db.Column(db.String(100))
    total_precio = db.Column(db.Integer)

    def __init__(self,rut,nombre,apellido,correo,nombre_producto,total_precio):
        self.rut= rut
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.nombre_producto = nombre_producto
        self.total_precio = total_precio