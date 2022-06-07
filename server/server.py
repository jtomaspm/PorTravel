from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_bcrypt import Bcrypt
import json
from flask_sqlalchemy import SQLAlchemy


# initial setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'verysecretkeymuchwow123'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


# Database Models

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

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table = db.Column(db.String(100), nullable=False)
    table_id = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Destination %r>' % self.country+', '+self.table

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    persons = db.Column(db.Integer, nullable=False)
    photos = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Hotel %r>' % self.name

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Estate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    owner_username = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    persons = db.Column(db.Integer, nullable=False)
    photos = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Estate %r>' % self.name + ' from ' + self.owner_username

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Transport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin_city = db.Column(db.String(100), nullable=False)
    origin_country = db.Column(db.String(100), nullable=False)
    destination_city = db.Column(db.String(100), nullable=False)
    destination_country = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    method = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Transport %r>' % self.destination_country+', '+self.destination_city + ' by ' + self.method

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Rent_A_Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    model = db.Column(db.String(100), nullable=False)
    photos = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Rent-A-Car %r>' % self.brand

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Attraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    photos = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Attraction %r>' % self.name

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# home


@app.route('/')
def home():
    return 'Welcome to PorTravel Api!'

# user


@app.route('/user/', methods=["GET", "POST"])
@app.route('/user/<username>/', methods=["GET", "POST", "PATCH", "DELETE"])
def user(username=None):
    if username:
        if request.method == "POST":
            user_found = User.query.filter(
                User.username == username, User.password == request.form['password']).first()
            if user_found:
                return {
                    'verified': True
                }
            return {
                'verified': False
            }

        if request.method == "GET":
            user = User.query.filter(User.username == username).first()
            if not user:
                return {
                    'errors': [
                        'user not found'
                    ]
                }
            return {
                'username': user.username,
                'name': user.name,
                'address': user.address,
                'bithdate': user.bithdate,
                'postal': user.postal,
                'city': user.city,
                'country': user.country,
                'email': user.email,
                'phone': user.phone
            }

        if request.method == "PATCH":
            data = request.form
            user = User.query.filter(
                User.username == username, User.password == request.form['password']).first()
            if not user:
                return {
                    'errors': [
                        'user authentication incorrect'
                    ]
                }
            user.username = data['username']
            user.password = data['new_password']
            user.name = data['name']
            user.address = data['address']
            user.bithdate = data['bithdate']
            user.postal = data['postal']
            user.city = data['city']
            user.country = data['country']
            user.email = data['email']
            user.phone = data['phone']
            db.session.commit()
            return {
                'updated': username
            }

        if request.method == "DELETE":
            user = User.query.filter(
                User.username == username, User.password == request.form['password']).first()
            if not user:
                return {
                    errors: [
                        'user authentication incorrect'
                    ]
                }
            db.session.delete(user)
            db.session.commit()
            return {
                'deleted': username
            }

    else:
        if request.method == "POST":
            data = request.form
            new_user = None
            try:
                new_user = User(
                    username=data['username'],
                    password=data['password'],
                    name=data['name'],
                    address=data['address'],
                    bithdate=data['bithdate'],
                    postal=data['postal'],
                    city=data['city'],
                    country=data['country'],
                    email=data['email'],
                    phone=data['phone']
                )
            except:
                return {
                    'errors': [
                        'invalid user information'
                    ]
                }

            try:
                db.session.add(new_user)
                db.session.commit()
            except:
                return {
                    'errors': [
                        'username or email already in use'
                    ]
                }
            return {
                'added': new_user.username
            }

        if request.method == "GET":
            all_users = User.query.all()
            all_users_json = [
                {
                    'username': user.username,
                    'email': user.email
                } for user in all_users
            ]
            return json.dumps(all_users_json)

    return "Hello from User Page"


# destination


@app.route('/destination/', methods=["GET", "POST"])
@app.route('/destination/<id>/', methods=["GET", "PATCH", "DELETE"])
def destination(id=None):
    if not id == None:
        if request.method == "GET":
            elem = Destination.query.filter(Destination.id == id).first()
            if not elem:
                return {
                    'errors': [
                        'destination not found'
                    ]
                }

            return elem.as_dict()

        if request.method == "PATCH":
            data = request.form
            elem = Destination.query.filter(
                Destination.id == id).first()
            if not elem:
                return {
                    'errors': [
                        'destination not found'
                    ]
                }
            elem.origin_city = data['origin_city']
            elem.origin_country = data['origin_country']
            elem.destination_city = data['destination_city']
            elem.destination_country = data['destination_country']
            elem.company = data['company']
            elem.price = data['price']
            elem.package = data['package']
            elem.description = data['description']
            db.session.commit()
            return {
                'updated': id
            }

        if request.method == "DELETE":
            elem = Destination.query.filter(
                Destination.id == id).first()
            if not elem:
                return {
                    errors: [
                        'destination not found'
                    ]
                }
            db.session.delete(elem)
            db.session.commit()
            return {
                'deleted': id
            }

    else:
        if request.method == "POST":
            data = request.form
            new_elem = None
            try:
                new_elem = Destination(
                    origin_city=data['origin_city'],
                    origin_country=data['origin_country'],
                    destination_city=data['destination_city'],
                    destination_country=data['destination_country'],
                    company=data['company'],
                    price=data['price'],
                    package=data['package'],
                    description=data['description']
                )
            except:
                return {
                    'errors': [
                        'invalid destination information'
                    ]
                }

            try:
                db.session.add(elem)
                db.session.commit()
            except:
                return {
                    'errors': [
                        'unique field already in use'
                    ]
                }
            return {
                'added': elem.id
            }

        if request.method == "GET":
            all_elems = Destination.query.all()
            all_elems_json = [
                elem.as_dict() for elem in all_elems
            ]
            return json.dumps(all_elems_json)

    return "Hello from Destination Page"


# hotel


@app.route('/hotel/', methods=["GET", "POST"])
@app.route('/hotel/<id>/', methods=["GET", "PATCH", "DELETE"])
def hotel(id=None):
    if not id == None:
        if request.method == "GET":
            elem = Hotel.query.filter(Hotel.id == id).first()
            if not elem:
                return {
                    'errors': [
                        'hotel not found'
                    ]
                }

            return elem.as_dict()

        if request.method == "PATCH":
            data = request.form
            elem = Hotel.query.filter(
                Hotel.id == id).first()
            if not elem:
                return {
                    'errors': [
                        'hotel not found'
                    ]
                }
            elem.name = data['name']
            elem.city = data['city']
            elem.country = data['country']
            elem.price = data['price']
            elem.persons = data['persons']
            elem.photos = data['photos']
            elem.description = data['description']
            db.session.commit()
            return {
                'updated': id
            }

        if request.method == "DELETE":
            elem = Hotel.query.filter(
                Hotel.id == id).first()
            if not elem:
                return {
                    errors: [
                        'hotel not found'
                    ]
                }
            db.session.delete(elem)
            db.session.commit()
            return {
                'deleted': id
            }

    else:
        if request.method == "POST":
            data = request.form
            new_elem = None
            try:
                new_elem = Hotel(
                    name=data['name'],
                    city=data['city'],
                    country=data['country'],
                    price=data['price'],
                    persons=data['persons'],
                    photos=data['photos'],
                    description=data['description']
                )
            except:
                return {
                    'errors': [
                        'invalid hotel information'
                    ]
                }

            try:
                db.session.add(elem)
                db.session.commit()
            except:
                return {
                    'errors': [
                        'unique field already in use'
                    ]
                }
            return {
                'added': elem.id
            }

        if request.method == "GET":
            all_elems = Hotel.query.all()
            all_elems_json = [
                elem.as_dict() for elem in all_elems
            ]
            return json.dumps(all_elems_json)

    return "Hello from Hotel Page"


# estate


@app.route('/estate/', methods=["GET", "POST"])
@app.route('/estate/<id>/', methods=["GET", "PATCH", "DELETE"])
def estate(id=None):
    if not id == None:
        if request.method == "GET":
            elem = Estate.query.filter(Estate.id == id).first()
            if not elem:
                return {
                    'errors': [
                        'estate not found'
                    ]
                }

            return elem.as_dict()

        if request.method == "PATCH":
            data = request.form
            elem = Estate.query.filter(
                Estate.id == id).first()
            if not elem:
                return {
                    'errors': [
                        'estate not found'
                    ]
                }
            elem.name = data['name']
            elem.owner_username = data['owner_username']
            elem.city = data['city']
            elem.country = data['country']
            elem.price = data['price']
            elem.persons = data['persons']
            elem.photos = data['photos']
            elem.description = data['description']
            db.session.commit()
            return {
                'updated': id
            }

        if request.method == "DELETE":
            elem = Estate.query.filter(
                Estate.id == id).first()
            if not elem:
                return {
                    errors: [
                        'estate not found'
                    ]
                }
            db.session.delete(elem)
            db.session.commit()
            return {
                'deleted': id
            }

    else:
        if request.method == "POST":
            data = request.form
            new_elem = None
            try:
                new_elem = Estate(
                    name=data['name'],
                    owner_username=data['owner_username'],
                    city=data['city'],
                    country=data['country'],
                    price=data['price'],
                    persons=data['persons'],
                    photos=data['photos'],
                    description=data['description']
                )
            except:
                return {
                    'errors': [
                        'invalid estate information'
                    ]
                }

            try:
                db.session.add(elem)
                db.session.commit()
            except:
                return {
                    'errors': [
                        'unique field already in use'
                    ]
                }
            return {
                'added': elem.id
            }

        if request.method == "GET":
            all_elems = Estate.query.all()
            all_elems_json = [
                elem.as_dict() for elem in all_elems
            ]
            return json.dumps(all_elems_json)

    return "Hello from Estate Page"


# transport


@app.route('/transport/', methods=["GET", "POST"])
@app.route('/transport/<id>/', methods=["GET", "PATCH", "DELETE"])
def transport(id=None):
    if not id == None:
        if request.method == "GET":
            elem = Transport.query.filter(Transport.id == id).first()
            if not elem:
                return {
                    'errors': [
                        'estate not found'
                    ]
                }

            return elem.as_dict()

        if request.method == "PATCH":
            data = request.form
            elem = Transport.query.filter(
                Transport.id == id).first()
            if not elem:
                return {
                    'errors': [
                        'transport not found'
                    ]
                }
            elem.origin_city = data['origin_city']
            elem.origin_country = data['origin_country']
            elem.destination_city = data['destination_city']
            elem.destination_country = data['destination_country']
            elem.company = data['company']
            elem.price = data['price']
            elem.method = data['method']
            elem.description = data['description']
            db.session.commit()
            return {
                'updated': id
            }

        if request.method == "DELETE":
            elem = Transport.query.filter(
                Transport.id == id).first()
            if not elem:
                return {
                    errors: [
                        'transport not found'
                    ]
                }
            db.session.delete(elem)
            db.session.commit()
            return {
                'deleted': id
            }

    else:
        if request.method == "POST":
            data = request.form
            new_elem = None
            try:
                new_elem = Transport(
                    origin_city=data['origin_city'],
                    origin_country=data['origin_country'],
                    destination_city=data['destination_city'],
                    destination_country=data['destination_country'],
                    company=data['company'],
                    price=data['price'],
                    method=data['method'],
                    description=data['description']
                )
            except:
                return {
                    'errors': [
                        'invalid estate information'
                    ]
                }

            try:
                db.session.add(elem)
                db.session.commit()
            except:
                return {
                    'errors': [
                        'unique field already in use'
                    ]
                }
            return {
                'added': elem.id
            }

        if request.method == "GET":
            all_elems = Transport.query.all()
            all_elems_json = [
                elem.as_dict() for elem in all_elems
            ]
            return json.dumps(all_elems_json)

    return "Hello from Transport Page"


# rent_a_car


@app.route('/rentacar/', methods=["GET", "POST"])
@app.route('/rentacar/<id>/', methods=["GET", "PATCH", "DELETE"])
def rent_a_car(id=None):
    if not id == None:
        if request.method == "GET":
            elem = Rent_A_Car.query.filter(Rent_A_Car.id == id).first()
            if not elem:
                return {
                    'errors': [
                        'estate not found'
                    ]
                }

            return elem.as_dict()

        if request.method == "PATCH":
            data = request.form
            elem = Rent_A_Car.query.filter(
                Rent_A_Car.id == id).first()
            if not elem:
                return {
                    'errors': [
                        'car not found'
                    ]
                }
            elem.city = data['city']
            elem.country = data['country']
            elem.company = data['company']
            elem.price = data['price']
            elem.model = data['model']
            elem.description = data['description']
            db.session.commit()
            return {
                'updated': id
            }

        if request.method == "DELETE":
            elem = Rent_A_Car.query.filter(
                Rent_A_Car.id == id).first()
            if not elem:
                return {
                    errors: [
                        'car not found'
                    ]
                }
            db.session.delete(elem)
            db.session.commit()
            return {
                'deleted': id
            }

    else:
        if request.method == "POST":
            data = request.form
            new_elem = None
            try:
                new_elem = Rent_A_Car(
                    city=data['city'],
                    country=data['country'],
                    company=data['company'],
                    price=data['price'],
                    model=data['model'],
                    description=data['description']
                )
            except:
                return {
                    'errors': [
                        'invalid car information'
                    ]
                }

            try:
                db.session.add(elem)
                db.session.commit()
            except:
                return {
                    'errors': [
                        'unique field already in use'
                    ]
                }
            return {
                'added': elem.id
            }

        if request.method == "GET":
            all_elems = Rent_A_Car.query.all()
            all_elems_json = [
                elem.as_dict() for elem in all_elems
            ]
            return json.dumps(all_elems_json)

    return "Hello from Rent a Car Page"


# Start Flask App
if __name__ == "__main__":
    app.run(port=4000, debug=True)
