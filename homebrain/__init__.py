from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.secret_key = 'w4lepsze'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://homeBrain:#W4lepsze@db/homeBrainDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()

login_manager.init_app(app)
Migrate(app, db)
