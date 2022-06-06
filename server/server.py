from flask import Flask, render_template, url_for, request, redirect
from flask_bcrypt import Bcrypt
import json
from db import db
from models import User, Destination, Hotel, Estate, Transport, Rent_A_Car

# initial setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'verysecretkeymuchwow123'
db.init_app(app)
bcrypt = Bcrypt(app)

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
                'updated_user': username
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
                'deleted_user': username
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
                'username': new_user.username
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


# Start Flask App
if __name__ == "__main__":
    app.run(port=4000, debug=True)
