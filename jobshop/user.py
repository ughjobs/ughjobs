from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    city = db.Column(db.String(50))
    street = db.Column(db.String(50))
    street_number = db.Column(db.String(50))
    apartment = db.Column(db.String(50))
    admin = db.Column(db.Boolean)