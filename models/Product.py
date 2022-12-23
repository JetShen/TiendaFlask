from utils.db import db

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(100))
    precio = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    descripcion = db.Column(db.String(100))

    def __init__(self,nombre,precio,stock,descripcion):
        self.nombre= nombre
        self.precio = precio
        self.stock = stock
        self.descripcion = descripcion
    
    #lista de funciones get que retornaran los datos de la base de datos
    def get_id(self):
        return self.id
    def get_nombre(self):
        return self.nombre
    def get_precio(self):
        return self.precio
    def get_stock(self):
        return self.stock