from flask import Flask, render_template, request, redirect, url_for, session
from DBcm import UseDatabase

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
                              request.form['select-person'], day, month, year, request.form['date'],
                              request.form['value']))
    return redirect(url_for('index'))


@app.route('/')
def index():
    with UseDatabase(dbconfig) as cursor:
        _SQL = """select name, value, person, date from bilance where category='Wydatek'"""
        cursor.execute(_SQL)
        contents_expenses = cursor.fetchall()

        _SQL = """select name, value, person, date from bilance where category='Przychod'"""
        cursor.execute(_SQL)
        contents_incomes = cursor.fetchall()

        _SQL = """select sum(value) from bilance where category='Wydatek'"""
        cursor.execute(_SQL)
        sum_expenses = cursor.fetchone()

        _SQL = """select sum(value) from bilance where category='Przychod'"""
        cursor.execute(_SQL)
        sum_incomes = cursor.fetchone()

        bilance = 0
        if sum_incomes[0] is not None and sum_expenses[0] is not None:
            bilance = sum_incomes[0] - sum_expenses[0]
        elif sum_incomes[0] is None and sum_expenses[0] is not None:
            bilance = 0 - sum_expenses[0]
        elif sum_incomes[0] is not None and sum_expenses[0] is None:
            bilance = sum_incomes[0]

        header_content = ['', 'nazwa', 'wartość', 'osoba', 'data']

    return render_template('index.html', the_data_expenses=contents_expenses, the_data_incomes=contents_incomes,
                           sum_inc=sum_incomes[0], sum_exp=sum_expenses[0], final_bil=bilance,
                           header_content=header_content, current_user=session['username'])


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']

        with UseDatabase(dbconfig) as cursor:
            _SQL = """select password from users where name = (%s)"""
            cursor.execute(_SQL, [username])
            result = cursor.fetchone()

            # TODO sha256
            if result is not None:
                if password_candidate == result[0]:
                    session['logged_in'] = True
                    session['username'] = username
                    return redirect(url_for('index'))
                else:
                    return render_template('login.html')
            else:
                return render_template('login.html')

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
