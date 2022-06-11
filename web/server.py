from flask import Flask, render_template, url_for, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import json
import requests
from settings import *
from functions import get_destination_id, filter_data
from werkzeug.utils import secure_filename
import os

# initial setup
app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'verysecretkeymuchwow123'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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


def get_cart_size(username):
    return len(Cart.query.filter(Cart.username == username).all())


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


@login_required
@app.route('/cart', methods=["GET"])
def cart():
    session['url'] = url_for('cart')
    carts = []
    querry = Cart.query.filter(Cart.username == current_user.username).all()
    total_price = 0
    for item in querry:
        destination = requests.get(
            url=API_LINK+'destination/'+str(item.item_id)).json()
        temp = requests.get(
            url=API_LINK+destination['table']+'/'+str(destination['table_id'])).json()
        temp['details_id'] = destination['id']
        total_price += float(temp['price'])
        carts.append(temp)
    return render_template('cart.html', current_user=current_user, API_LINK=API_LINK, carts=carts, cart_size=get_cart_size(current_user.username), total_price=total_price)


# home


@app.route('/')
def index():
    session['url'] = url_for('index')
    destinations = requests.get(url=API_LINK+'attraction').json()
    if current_user.is_authenticated:
        return render_template('index.html', destinations=destinations, current_user=current_user, API_LINK=API_LINK, cart_size=get_cart_size(current_user.username))
    else:
        return render_template('index.html', destinations=destinations, current_user=current_user, API_LINK=API_LINK, cart_size=None)

# destinos


@app.route('/destinos', methods=["GET", "POST"])
def destinos():
    session['url'] = url_for('destinos')
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
    if request.method == "POST":
        new_dest = filter_data(request.form['query'], new_dest)
    if current_user.is_authenticated:
        return render_template('destinos.html', destinations=new_dest, current_user=current_user, API_LINK=API_LINK, cart_size=get_cart_size(current_user.username))
    else:
        return render_template('destinos.html', destinations=new_dest, current_user=current_user, API_LINK=API_LINK, cart_size=None)


# hoteis


@app.route('/hoteis', methods=["GET", "POST"])
def hoteis():
    session['url'] = url_for('hoteis')
    hotels = requests.get(url=API_LINK+"hotel/").json()
    for hotel in hotels:
        hotel['details_id'] = get_destination_id(hotel, 'hotel')
    print("--------------------------------------------------------------------------hotels")
    print(hotels)
    print("--------------------------------------------------------------------------hotels")
    if request.method == "POST":
        hotels = filter_data(request.form['query'], hotels)
    if current_user.is_authenticated:
        return render_template('hoteis.html', hotels=hotels, current_user=current_user, API_LINK=API_LINK, cart_size=get_cart_size(current_user.username))
    else:
        return render_template('hoteis.html', hotels=hotels, current_user=current_user, API_LINK=API_LINK, cart_size=None)


# imoveis


@app.route('/imoveis', methods=["GET", "POST"])
def imoveis():
    session['url'] = url_for('imoveis')
    estates = requests.get(url=API_LINK+"estate/").json()
    for item in estates:
        item['details_id'] = get_destination_id(item, 'estate')
    print("--------------------------------------------------------------------------estates")
    print(estates)
    print("--------------------------------------------------------------------------estates")
    if request.method == "POST":
        estates = filter_data(request.form['query'], estates)
    if current_user.is_authenticated:
        return render_template('imoveis.html', estates=estates, current_user=current_user, API_LINK=API_LINK, cart_size=get_cart_size(current_user.username))
    else:
        return render_template('imoveis.html', estates=estates, current_user=current_user, API_LINK=API_LINK, cart_size=None)

# transportes


@app.route('/transportes', methods=["GET", "POST"])
def transportes():
    session['url'] = url_for('transportes')
    transports = requests.get(url=API_LINK+"transport/").json()
    for item in transports:
        item['details_id'] = get_destination_id(item, 'transport')
    print("--------------------------------------------------------------------------transports")
    print(transports)
    print("--------------------------------------------------------------------------transports")
    if request.method == "POST":
        transports = filter_data(request.form['query'], transports)
    if current_user.is_authenticated:
        return render_template('transportes.html', transports=transports, current_user=current_user, API_LINK=API_LINK, cart_size=get_cart_size(current_user.username))
    else:
        return render_template('transportes.html', transports=transports, current_user=current_user, API_LINK=API_LINK, cart_size=None)


# carros


@app.route('/carros', methods=["GET", "POST"])
def carros():
    session['url'] = url_for('carros')
    cars = requests.get(url=API_LINK+"rentacar/").json()
    for item in cars:
        item['details_id'] = get_destination_id(item, 'rentacar')
    print("--------------------------------------------------------------------------cars")
    print(cars)
    print("--------------------------------------------------------------------------cars")
    if request.method == "POST":
        cars = filter_data(request.form['query'], cars)
    if current_user.is_authenticated:
        return render_template('carros.html', cars=cars, current_user=current_user, API_LINK=API_LINK, cart_size=get_cart_size(current_user.username))
    else:
        return render_template('carros.html', cars=cars, current_user=current_user, API_LINK=API_LINK, cart_size=None)


@app.route('/details/<id>')
def details(id=None):
    if not id:
        return 'give id'
    item = requests.get(url=API_LINK+'destination/'+id).json()
    item_details = requests.get(
        url=API_LINK+item["table"]+'/'+str(item["table_id"])).json()
    if current_user.is_authenticated:
        return render_template('details.html', current_user=current_user, API_LINK=API_LINK, details=item_details, table=item['table'], id=id, cart_size=get_cart_size(current_user.username))
    else:
        return render_template('details.html', current_user=current_user, API_LINK=API_LINK, details=item_details, table=item['table'], id=id, cart_size=None)


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
@app.route('/profile', methods=["GET", "POST"])
def profile():
    user_json = requests.get(url=API_LINK+'user/'+current_user.username).json()
    if request.method == 'POST':
        data = request.form
        for d in data:
            if data[d]:
                user_json[d] = data[d]
        ver = requests.post(
            url=API_LINK+'user/'+current_user.username, data={'password': data['password']}).json()
        if ver['verified']:
            requests.patch(url=API_LINK+'user/' +
                           current_user.username, data=user_json)

    return render_template('profile.html', current_user=current_user, API_LINK=API_LINK, cart_size=get_cart_size(current_user.username), user=user_json)


# register


@ app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.form
        r = requests.post(url=API_LINK+"user/", data=data)
        print(data)
        return url_for('login')
    return render_template('register.html', current_user=current_user, API_LINK=API_LINK)


@login_required
@app.route('/addestate', methods=["GET", "POST"])
def addestate():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            data = dict(request.form)
            fn = UPLOAD_FOLDER+file.filename
            file = {'file': open(fn, 'rb')}
            data['photos'] = requests.post(API_LINK+'upload', files=file).text
            data['owner_username'] = current_user.username
            os.remove(fn)
            r = requests.post(url=API_LINK+"estate/", data=data)
            return url_for('profile')
    return render_template('addestate.html', current_user=current_user, API_LINK=API_LINK, cart_size=get_cart_size(current_user.username))

    #Payment 
@app.route ('/payment', methods=["GET", "POST"])
def payment():
    return render_template('pagamento.html' , current_user=current_user, API_LINK=API_LINK )

    # Start Flask App
if __name__ == "__main__":
    app.run(debug=True)
