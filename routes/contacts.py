from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.cliente import Cliente
from models.Product import Producto
from models.venta import venta
from utils.db import db

contacts = Blueprint("contacts", __name__)

@contacts.route('/')
def index():
    return render_template('home.html')
#---------------------CLIENTES---------------------
@contacts.route('/new', methods=['POST'])
def add_contact():
    rut=request.form['rut']
    nombre=request.form['Nombre']
    apelldio=request.form['Apellido']
    correo=request.form['Correo']

    cl = Cliente(rut,nombre,apelldio,correo)

    db.session.add(cl)
    db.session.commit()
    return redirect(url_for('contacts.index'))

@contacts.route('/delete/<rut>')
def delete_contact(rut):
    contacts = Cliente.query.get(rut)
    db.session.delete(contacts)
    db.session.commit()
    return redirect(url_for('contacts.lista'))

@contacts.route('/update/<rut>', methods=['POST', 'GET'])
def update_contact(rut):
    if request.method == 'POST':
        contacts = Cliente.query.get(rut)
        contacts.rut = request.form['rut']
        contacts.nombre = request.form['Nombre']
        contacts.apellido = request.form['Apellido']
        contacts.correo = request.form['Correo']
        db.session.commit()
        return redirect(url_for('contacts.lista'))
    
    contact = Cliente.query.get(rut)
    return render_template('update.html', contact=contact)
@contacts.route('/añadir')
def añadir():
    return render_template('añadir.html')
@contacts.route('/lista')
def lista():
    contacts = Cliente.query.all()
    return render_template('lista.html',contacts=contacts)
#---------------------PRODUCTOS---------------------    
@contacts.route('/add_product', methods=['POST'])
def add_product():
    nombre=request.form['nombre']
    precio=request.form['precio']
    stock=request.form['stock']
    descripcion=request.form['descripcion']

    pr = Producto(nombre,precio,stock,descripcion)

    db.session.add(pr)
    db.session.commit()
    return redirect(url_for('contacts.index'))

@contacts.route('/añadir_producto')
def añadir_producto():
    return render_template('product.html')

@contacts.route('/lista_productos')
def lista_productos():
    product = Producto.query.all()
    return render_template('lista_productos.html',products=product)

@contacts.route('/delete_product/<id>')
def delete_product(id):
    product = Producto.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('contacts.lista_productos'))

@contacts.route('/update_product/<id>', methods=['POST', 'GET'])
def update_product(id):
    if request.method == 'POST':
        product = Producto.query.get(id)
        product.nombre = request.form['nombre']
        product.precio = request.form['precio']
        product.stock = request.form['stock']
        product.descripcion = request.form['descripcion']
        db.session.commit()
        return redirect(url_for('contacts.lista_productos'))
    
    product = Producto.query.get(id)
    return render_template('update_product.html', product=product)

#---------------------VENTAS---------------------
@contacts.route('/add_venta', methods=['POST', 'GET'])
def add_venta():
    user_id=request.form['user_id']
    product_id=request.form['p_id']
    products=Producto.query.get(product_id)
    users=Cliente.query.get(user_id)
    rut=users.rut
    nombre=users.nombre
    apellido=users.apellido
    correo=users.correo

    nombre_producto=products.nombre
    total_precio=int(products.precio)*int(request.form['cantidad'])
    
    ve = venta(rut,nombre,apellido,correo,nombre_producto,total_precio)

    db.session.add(ve)
    db.session.commit()
    return redirect(url_for('contacts.index'))


@contacts.route('/añadir_venta')
def añadir_venta():
    products=Producto.query.all()
    users=Cliente.query.all()
    return render_template('venta.html',users=users,products=products)


@contacts.route('/lista_ventas')
def lista_ventas():
    ventas = venta.query.all()
    return render_template('lista_ventas.html',ventas=ventas)

@contacts.route('/delete_venta/<id>')
def delete_venta(id):
    ventas = venta.query.get(id)
    db.session.delete(ventas)
    db.session.commit()
    return redirect(url_for('contacts.lista_ventas'))

