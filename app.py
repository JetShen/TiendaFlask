from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.contacts import contacts

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:0007@localhost/tienda"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

SQLAlchemy(app)


app.register_blueprint(contacts)