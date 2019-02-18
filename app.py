from flask import Flask, render_template, request, redirect, url_for
from DBcm import UseDatabase

import mysql.connector

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
                (category, name, value, date, person)
                values 
                (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (request.form['select-type'], request.form['name'], request.form['value'],
                              request.form['date'], request.form['select-person']))
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
        if sum_incomes[0] is not None and sum_expenses is not None:
            bilance = sum_incomes[0] - sum_expenses[0]

        elif sum_incomes[0] is None and sum_expenses is not None:
            bilance = 0 - sum_expenses[0]

        elif sum_incomes[0] is not None and sum_expenses is None:
            bilance = sum_expenses[0]

    return render_template('index.html', the_data_expenses=contents_expenses, the_data_incomes=contents_incomes,
                           sum_inc=sum_incomes[0], sum_exp=sum_expenses[0], final_bil=bilance)


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
