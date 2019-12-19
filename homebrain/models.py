from homebrain import db
from flask_login import UserMixin


class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    category = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    date = db.Column(db.Text, nullable=False)
    value = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    item = db.relationship('Item', backref='user')
