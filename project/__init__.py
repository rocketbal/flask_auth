from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys,os
from flask_migrate import Migrate
from flask_login import UserMixin,LoginManager

# db = SQLAlchemy()


app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/flask_auth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# db.init_app(app)
# migrate = Migrate(app,db)
db = SQLAlchemy(app)
db.create_all()
migrate = Migrate(app,db)

class User(UserMixin,db.Model):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),nullable=False,unique=True)
    password = db.Column(db.String(80),nullable=False)
    name = db.Column(db.String(1000))

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

login_manager=LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # sinec the user_id is just the primary key of our user table, we will use it to query user
    return User.query.get(int(user_id))
