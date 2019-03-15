from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from checker import check_logged_in
from datetime import datetime
from flask_migrate import Migrate

app = Flask(__name__)

app.secret_key = 'w4lepsze'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://homeBrain:#W4lepsze@127.0.0.1/homeBrainDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)


class Item(db.Model):
    __tablename__ = 'bilance'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    category = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    person = db.Column(db.Text, nullable=False)
    day = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Text, nullable=False)
    value = db.Column(db.Float, nullable=False)

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
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)

    def __init__(self, name, password):
        self.name = name
        self.password = password


@app.route('/post_item', methods=['POST'])
def post_item():
    date = request.form['date'].split('-')
    if date is not None:
        year = date[0]
        month = date[1]
        day = date[2]
    item = Item(request.form['select-type'], request.form['name'], session['username'], day, month, year,
                request.form['date'], request.form['value'])
    db.session.add(item)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/')
@check_logged_in
def index():
    now = datetime.now()
    month = now.month
    year = now.year

    # zabieg mający na celu sprawdzenie czy kazaliśmy filtrować rekordy
    if 'select-months' and 'select-years' in request.args:
        month = request.args['select-months']
        year = request.args['select-years']

    # Ogolne wydatki i przychody z danego miesiaca
    content_expenses = Item.query.filter_by(month=month).filter_by(year=year).filter_by(category='Wydatek').order_by(
        Item.date.desc()).all()
    content_incomes = Item.query.filter_by(month=month).filter_by(year=year).filter_by(category='Przychod').order_by(
        Item.date.desc()).all()

    # bilans miesięczny
    sum_expenses = 0
    for i in content_expenses:
        sum_expenses += i.value

    sum_incomes = 0
    for i in content_incomes:
        sum_incomes += i.value

    # Stan budzetu - bilans calosciowy
    budget_expenses = Item.query.filter_by(category='Wydatek').all()
    budget_incomes = Item.query.filter_by(category='Przychod').all()

    sum_budget_expenses = 0
    if budget_expenses:
        for i in budget_expenses:
            sum_budget_expenses += i.value

    sum_budget_incomes = 0
    if budget_incomes:
        for i in budget_incomes:
            sum_budget_incomes += i.value

    bilance = sum_budget_incomes - sum_budget_expenses

    header_content = ['', 'id', 'nazwa', 'wartość', 'osoba', 'data']

    return render_template('index.html', the_data_expenses=content_expenses, the_data_incomes=content_incomes,
                           sum_inc=round(sum_incomes, 2), sum_exp=round(sum_expenses, 2),
                           final_bil=round(bilance, 2), header_content=header_content)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].title()
        password_candidate = request.form['password']

        result = User.query.filter_by(name=username).first()

        # TODO sha256 encrypting
        if result:
            if password_candidate == result.password:
                session['logged_in'] = True
                session['username'] = username
                return redirect(url_for('index'))
            else:
                flash("Podałeś złe hasło.")
                return redirect(url_for('index'))
        else:
            flash("Nie ma takiego użytkownika.")
            return render_template('login.html')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
