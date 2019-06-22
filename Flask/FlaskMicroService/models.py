from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

db = SQLAlchemy()

def init_app(app):
    db.app = app
    db.init_app(app)
    return db

def create_tables(app):
    engine = create_engine(app.config(app.config['SQLALCHEMY_DATABASE_URI']))
    db.metadata.create_all(engine)
    return engine

class Customer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(120),unique=True,nullable=False)
    firstName = db.Column(db.String(120),unique=True,nullable=True)
    lastName = db.Column(db.String(120),unique=False,nullable=True)
    orders = db.relationship('Order',backred='order')
    dateAdded = db.relationship(db.DateTime,unique=False,nullable=True)
    dateUpdated = db.Column(db.DateTime,onupdate=datetime.utcnow)

    def to_json(self):
        return {
            'first_name':self.firstName,
            'last_name':self.lastName,
            'email_address':self.email
        }

class Prodcut(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120),unique=True,nullable=False)
    slug = db.Column(db.String(120),unique=True,nullable=True)
    price = db.Column(db.Integer(120),nullable=False)
    image = db.Column(db.String(120),unique=True,nullable=True)
    dateAdded = db.Column(db.DateTime,default=datetime.utcnow)
    dateUpdated = db.Column(db.DateTime,onupdate=datetime.utcnow)

class Order(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    customer_id = db.Column(db.Integer,db.ForeignKey('customer.id'))
    image = db.Column(db.String(120),unique=True,nullable=True)
    items = db.relationship('OrderItem',unique=False,nullable=True)
    dateAdded = db.Column(db.DateTime,default=datetime.utcnow)
    dateUpdated = db.Column(db.DateTime,onupdate=datetime.utcnow)

class OrderItem(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    order_id = db.Column(db.Integer,db.ForeignKey('customer.id'))
    product_id = db.Column(db.String(120),unique=True,nullable=True)
    dateAdded = db.Column(db.DateTime,default=datetime.utcnow)
    dateUpdated = db.Column(db.DateTime,onupdate=datetime.utcnow)