from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import json
import requests
from settings import API_LINK


# initial setup
app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'verysecretkeymuchwow123'


# Login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, unique=True)
    username = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# home
@app.route('/')
def index():
    return render_template('index.html', current_user=current_user, API_LINK=API_LINK)

# destinos


@app.route('/destinos')
def destinos():
    destinations = requests.get(url=API_LINK+"destination/").json()
    print("--------------------------------------------------------------------------destinations")
    print(destinations)
    print("--------------------------------------------------------------------------destinations")
    return render_template('destinos.html', destinations=destinations, current_user=current_user, API_LINK=API_LINK)

# hoteis


@app.route('/hoteis')
def hoteis():
    hotels = requests.get(url=API_LINK+"hotel/").json()
    print("--------------------------------------------------------------------------hotels")
    print(hotels)
    print("--------------------------------------------------------------------------hotels")
    return render_template('hoteis.html', hotels=hotels, current_user=current_user, API_LINK=API_LINK)

# imoveis


@app.route('/imoveis')
def imoveis():
    estates = requests.get(url=API_LINK+"estate/").json()
    print("--------------------------------------------------------------------------estates")
    print(estates)
    print("--------------------------------------------------------------------------estates")
    return render_template('imoveis.html', estates=estates, current_user=current_user, API_LINK=API_LINK)

# transportes


@app.route('/transportes')
def transportes():
    transports = requests.get(url=API_LINK+"transport/").json()
    print("--------------------------------------------------------------------------transports")
    print(transports)
    print("--------------------------------------------------------------------------transports")
    return render_template('transportes.html', transports=transports, current_user=current_user, API_LINK=API_LINK)

# carros


@app.route('/carros')
def carros():
    cars = requests.get(url=API_LINK+"rentacar/").json()
    print("--------------------------------------------------------------------------cars")
    print(cars)
    print("--------------------------------------------------------------------------cars")
    return render_template('carros.html', cars=cars, current_user=current_user, API_LINK=API_LINK)

# login


@app.route('/login', methods=["GET", "POST"])
def login(username=None, password=None):
    if request.method == "POST":
        data = request.form
        r = requests.post(url=API_LINK+"user/"+data["username"], data=data)
        if r.json()["verified"]:
            query = User.query.filter(
                User.username == data['username']).first()
            if query:
                user = query
            else:
                user_json = requests.get(
                    API_LINK+'user/'+data['username']).json()
                user = User(user_id=user_json['id'], username=data['username'])
                db.session.add(user)
                db.session.commit()
            login_user(user)
            print("____________________________________________LOGED IN ", current_user)
            return redirect(url_for('index'))

    return render_template('login.html', current_user=current_user, API_LINK=API_LINK)


@login_required
@app.route('/logout', methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for('login'))


@login_required
@app.route('/profile', methods=["GET"])
def profile():
    return render_template('profile.html', current_user=current_user, API_LINK=API_LINK)


# register


@ app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.form
        r = requests.post(url=API_LINK+"user/", data=data)
        print(data)
        return r.json()
    return render_template('register.html', current_user=current_user, API_LINK=API_LINK)


# Start Flask App
if __name__ == "__main__":
    app.run(debug=True)
