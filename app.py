from flask import Flask, render_template, request, redirect, url_for
from DBcm import UseDatabase

import mysql.connector

app = Flask(__name__)

# baza: homeBrainDB
# identyfikator; homeBrain
# hasło: #W4lepsze
# tabela: bilance

app.debug = True
dbconfig = {'host': '127.0.0.1',
            'user': 'homeBrain',
            'password': '#W4lepsze',
            'database': 'homeBrainDB'}


@app.route('/post_item', methods=['POST'])
def post_item():
    with UseDatabase(dbconfig) as cursor:
        _SQL = """insert into bilance
                (category, name, value, date)
                values 
                (%s, %s, %s, %s)"""
        cursor.execute(_SQL, (request.form['select-type'], request.form['name'], request.form['value'], request.form['date']))
    return redirect(url_for('index'))

@app.route('/')
def index():
    # bilance_requst()
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
