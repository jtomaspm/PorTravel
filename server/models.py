# Models
from db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    bithdate = db.Column(db.String(100), nullable=False)
    postal = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin_city = db.Column(db.String(100), nullable=False)
    origin_country = db.Column(db.String(100), nullable=False)
    destination_city = db.Column(db.String(100), nullable=False)
    destination_country = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    package = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Destination %r>' % self.destination_country+', '+self.destination_city


class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    persons = db.Column(db.Integer, nullable=False)
    photos = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Estate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    owner_username = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    persons = db.Column(db.Integer, nullable=False)
    photos = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
