from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
import json



#initial setup
app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'verysecretkeymuchwow123'



#Login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



#Database classes
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id



#Form templates
class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=1, max=20)], render_kw={"paceholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=1, max=20)], render_kw={"paceholder": "Password"})
    submit = SubmitField("Register")

    def validate_username(self, username):
        db_usernames = User.query.filter_by(
            username=username.data
        ).first()
        if db_usernames:
            raise ValidationError("Username already exists")

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=1, max=20)], render_kw={"paceholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=1, max=20)], render_kw={"paceholder": "Password"})
    submit = SubmitField("Login")



#Home
@app.route('/')
def index():
    return render_template('index.html')





#Start Flask App
if __name__ == "__main__":
    app.run(debug=True)