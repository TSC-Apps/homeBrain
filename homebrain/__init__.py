from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.secret_key = 'w4lepsze'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://homeBrain:#W4lepsze@127.0.0.1/homeBrainDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)
