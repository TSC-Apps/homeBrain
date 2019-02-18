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


# @app.route('show_table', methods=['GET'])
# def show_table():
# pass
# with UseDatabase(app.config['dbconfig']) as cursor:
#     _SQL = """select name, value, date, results from log"""
#     cursor.execute(_SQL)
#     contents = cursor.fetchall()
# return render_template('index.html', the_data=contents)

@app.route('/')
def index():
    # bilance_requst()
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
