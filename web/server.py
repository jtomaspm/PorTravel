from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
import json
import requests
from settings import API_LINK
from user import User


# initial setup
app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'verysecretkeymuchwow123'


# Login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# home
@app.route('/')
def index():
    return render_template('index.html')

# destinos


@app.route('/destinos')
def destinos():
    destinations = requests.get(url=API_LINK+"destination/").json()
    print("--------------------------------------------------------------------------destinations")
    print(destinations)
    print("--------------------------------------------------------------------------destinations")
    return render_template('destinos.html', destinations=destinations)

# hoteis


@app.route('/hoteis')
def hoteis():
    hotels = requests.get(url=API_LINK+"hotel/").json()
    print("--------------------------------------------------------------------------hotels")
    print(hotels)
    print("--------------------------------------------------------------------------hotels")
    return render_template('hoteis.html', hotels=hotels)

# imoveis


@app.route('/imoveis')
def imoveis():
    estates = requests.get(url=API_LINK+"estate/").json()
    print("--------------------------------------------------------------------------estates")
    print(estates)
    print("--------------------------------------------------------------------------estates")
    return render_template('imoveis.html', estates=estates)

# transportes


@app.route('/transportes')
def transportes():
    transports = requests.get(url=API_LINK+"transport/").json()
    print("--------------------------------------------------------------------------transports")
    print(transports)
    print("--------------------------------------------------------------------------transports")
    return render_template('transportes.html', transports=transports)

# carros


@app.route('/carros')
def carros():
    cars = requests.get(url=API_LINK+"rentacar/").json()
    print("--------------------------------------------------------------------------cars")
    print(cars)
    print("--------------------------------------------------------------------------cars")
    return render_template('carros.html', cars=cars)

# login


@app.route('/login', methods=["GET", "POST"])
def login(username=None, password=None):
    if request.method == "POST":
        data = request.form
        r = requests.post(url=API_LINK+"user/"+data["username"], data=data)
        return r.json()

    return render_template('login.html')

# register


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.form
        r = requests.post(url=API_LINK+"user/", data=data)
        print(data)
        return r.json()
    return render_template('register.html')


# Start Flask App
if __name__ == "__main__":
    app.run(debug=True)
