from homebrain import db


class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    category = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    person = db.Column(db.Text, nullable=False)
    day = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Text, nullable=False)
    value = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, category, name, person, day, month, year, date, value):
        self.category = category
        self.name = name
        self.person = person
        self.day = day
        self.month = month
        self.year = year
        self.date = date
        self.value = value


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    item = db.relationship('Item', backref='user')

    def __init__(self, name, password):
        self.name = name
        self.password = password
