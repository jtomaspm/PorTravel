from flask import Flask, render_template, url_for, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import json
import requests
from settings import API_LINK
from functions import get_destination_id


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


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    item_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Cart %r>' % self.username

    def __init__(self, item_id, username):
        self.item_id = item_id
        self.username = username

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@login_required
@app.route('/addtocart/<id>')
def addtocart(id=None):
    cart = Cart(
        item_id=id,
        username=current_user.username
    )
    db.session.add(cart)
    db.session.commit()
    if 'url' in session:
        return redirect(session['url'])
    return redirect(url_for('cart'))


@login_required
@app.route('/removefromcart')
@app.route('/removefromcart/<id>')
def removefromcart(id=None):
    if id:
        cart = Cart.query.filter(
            Cart.username == current_user.username, Cart.item_id == id).first()
        db.session.delete(cart)
        db.session.commit()
    else:
        for cart in Cart.query.filter(Cart.username == current_user.username).all():
            db.session.delete(cart)
        db.session.commit()
    if 'url' in session:
        return redirect(session['url'])
    return redirect(url_for('cart'))

# home


@app.route('/')
def index():
    destinations = requests.get(url=API_LINK+'attraction').json()
    return render_template('index.html', destinations=destinations, current_user=current_user, API_LINK=API_LINK)

# destinos


@app.route('/destinos')
def destinos():
    destinations = requests.get(url=API_LINK+"destination/").json()
    print("--------------------------------------------------------------------------destinations")
    print(destinations)
    print("--------------------------------------------------------------------------destinations")
    new_dest = []
    for d in destinations:
        temp = requests.get(
            API_LINK+d['table']+'/'+str(d['table_id'])).json()
        temp['table'] = d['table']
        temp['details_id'] = d['id']
        new_dest.append(temp)
    return render_template('destinos.html', destinations=new_dest, current_user=current_user, API_LINK=API_LINK)

# hoteis


@app.route('/hoteis')
def hoteis():
    hotels = requests.get(url=API_LINK+"hotel/").json()
    for hotel in hotels:
        hotel['details_id'] = get_destination_id(hotel, 'hotel')
    print("--------------------------------------------------------------------------hotels")
    print(hotels)
    print("--------------------------------------------------------------------------hotels")
    return render_template('hoteis.html', hotels=hotels, current_user=current_user, API_LINK=API_LINK)

# imoveis


@app.route('/imoveis')
def imoveis():
    estates = requests.get(url=API_LINK+"estate/").json()
    for item in estates:
        item['details_id'] = get_destination_id(item, 'estate')
    print("--------------------------------------------------------------------------estates")
    print(estates)
    print("--------------------------------------------------------------------------estates")
    return render_template('imoveis.html', estates=estates, current_user=current_user, API_LINK=API_LINK)

# transportes


@app.route('/transportes')
def transportes():
    transports = requests.get(url=API_LINK+"transport/").json()
    for item in transports:
        item['details_id'] = get_destination_id(item, 'transport')
    print("--------------------------------------------------------------------------transports")
    print(transports)
    print("--------------------------------------------------------------------------transports")
    return render_template('transportes.html', transports=transports, current_user=current_user, API_LINK=API_LINK)

# carros


@app.route('/carros')
def carros():
    cars = requests.get(url=API_LINK+"rentacar/").json()
    for item in cars:
        item['details_id'] = get_destination_id(item, 'rentacar')
    print("--------------------------------------------------------------------------cars")
    print(cars)
    print("--------------------------------------------------------------------------cars")
    return render_template('carros.html', cars=cars, current_user=current_user, API_LINK=API_LINK)


@app.route('/details/<id>')
def details(id=None):
    if not id:
        return 'give id'
    item = requests.get(url=API_LINK+'destination/'+id).json()
    item_details = requests.get(
        url=API_LINK+item["table"]+'/'+str(item["table_id"])).json()
    return render_template('details.html', current_user=current_user, API_LINK=API_LINK, details=item_details, table=item['table'], id=id)


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


@login_required
@app.route('/cart', methods=["GET"])
def cart():
    carts = []
    querry = Cart.query.filter(Cart.username == current_user.username).all()
    for item in querry:
        destination = requests.get(
            url=API_LINK+'destination/'+str(item.item_id)).json()
        carts.append(requests.get(
            url=API_LINK+destination['table']+'/'+str(destination['table_id'])).json())
    return render_template('cart.html', current_user=current_user, API_LINK=API_LINK, carts=carts)


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
