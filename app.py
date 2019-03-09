from flask import Flask, render_template, request, redirect, url_for, session, flash
from DBcm import UseDatabase
from checker import check_logged_in
from datetime import datetime

app = Flask(__name__)

app.debug = True
dbconfig = {'host': '127.0.0.1',
            'user': 'homeBrain',
            'password': '#W4lepsze',
            'database': 'homeBrainDB'}
app.secret_key = 'w4lepsze'


@app.route('/post_item', methods=['POST'])
def post_item():
    with UseDatabase(dbconfig) as cursor:
        _SQL = """insert into bilance
                (category, name, person, day, month, year, date, value)
                values 
                (%s, %s, %s, %s, %s, %s, %s, %s)"""
        date = request.form['date'].split('-')
        if date is not None:
            year = date[0]
            month = date[1]
            day = date[2]
        cursor.execute(_SQL, (request.form['select-type'], request.form['name'],
                              session['username'], day, month, year, request.form['date'],
                              request.form['value']))
    return redirect(url_for('index'))


@app.route('/')
@check_logged_in
def index():
    with UseDatabase(dbconfig) as cursor:
        now = datetime.now()
        month = now.month
        year = now.year

        #zabieg mający na celu sprawdzenie czy kazaliśmy filtrować rekordy
        if 'select-months' and 'select-years' in request.args:
            month = request.args['select-months']
            year = request.args['select-years']

        _SQL = """select id, name, value, person, date from bilance where month = (%s) and year = (%s) 
        and category = 'Wydatek' order by date desc"""
        cursor.execute(_SQL, (month, year))
        contents_expenses = cursor.fetchall()

        _SQL = """select id, name, value, person, date from bilance where month = (%s) and year = (%s)
         and category='Przychod' order by date desc"""
        cursor.execute(_SQL, (month, year))
        contents_incomes = cursor.fetchall()

        # bilans miesięczny
        _SQL = """select sum(value) from bilance where month = (%s) and year = (%s)
         and category='Wydatek'"""
        cursor.execute(_SQL, (month, year))
        sum_expenses = cursor.fetchone()

        _SQL = """select sum(value) from bilance where month = (%s) and year = (%s)
         and category='Przychod'"""
        cursor.execute(_SQL, (month, year))
        sum_incomes = cursor.fetchone()

        # bilans całościowy
        _SQL = """select sum(value) from bilance where category='Wydatek'"""
        cursor.execute(_SQL)
        sum_all_expenses = cursor.fetchone()

        _SQL = """select sum(value) from bilance where  category='Przychod'"""
        cursor.execute(_SQL)
        sum_all_incomes = cursor.fetchone()


        # Zabieg konieczny ze wzgledu zwracania przez kursor krotki...
        expenses = 0
        if sum_expenses[0] is not None:
            expenses = sum_expenses[0]

        incomes = 0
        if sum_incomes[0] is not None:
            incomes = sum_incomes[0]

        bilance = 0
        if sum_all_incomes[0] is not None and sum_all_expenses[0] is not None:
            bilance = sum_all_incomes[0] - sum_all_expenses[0]
        elif sum_all_incomes[0] is None and sum_all_expenses[0] is not None:
            bilance = 0 - sum_all_expenses[0]
        elif sum_incomes[0] is not None and sum_all_expenses[0] is None:
            bilance = sum_all_incomes[0]

        header_content = ['', 'id', 'nazwa', 'wartość', 'osoba', 'data']

    return render_template('index.html', the_data_expenses=contents_expenses, the_data_incomes=contents_incomes,
                           sum_inc=round(incomes, 2), sum_exp=round(expenses, 2),
                           final_bil=round(bilance, 2), header_content=header_content)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].title()
        password_candidate = request.form['password']

        with UseDatabase(dbconfig) as cursor:
            _SQL = """select password from users where name = (%s)"""
            cursor.execute(_SQL, [username])
            result = cursor.fetchone()

            # TODO sha256 encrypting
            if result is not None:
                if password_candidate == result[0]:
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
