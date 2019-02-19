from flask import Flask, render_template, request, redirect, url_for
from DBcm import UseDatabase

app = Flask(__name__)

app.debug = True
dbconfig = {'host': '127.0.0.1',
            'user': 'homeBrain',
            'password': '#W4lepsze',
            'database': 'homeBrainDB'}


@app.route('/post_item', methods=['POST'])
def post_item():
    with UseDatabase(dbconfig) as cursor:
        _SQL = """insert into bilance
                (category, name, value, person, day, month, year, date)
                values 
                (%s, %s, %s, %s, %s, %s, %s, %s)"""
        date = request.form['date'].split('-')
        if date is not None:
            year = date[0]
            month = date[1]
            day = date[2]
        cursor.execute(_SQL, (request.form['select-type'], request.form['name'], request.form['value'],
                              request.form['select-person'], day, month, year, request.form['date']))
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
                           header_content=header_content)


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
