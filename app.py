from flask import Flask, render_template, request
from DBcm import UseDatabase

import mysql.connector

app = Flask(__name__)

# baza: homeBrainDB
# identyfikator; homeBrain
# hasło: #W4lepsze
# tabela: bilance

dbconfig = {'host': '127.0.0.1',
            'user': 'homeBrain',
            'password': '#W4lepsze',
            'database': 'homeBrainDB'}


def bilance_requst(req: 'flask_request'):
    with UseDatabase(dbconfig) as cursor:
        _SQL = """insert into bilance
                (category, name, value, date)
                values 
                (%s, %s, %d, %s)"""
    cursor.execute(_SQL, req.form['select-type'], req.form['name'], req.form['value'], req.form['date'])

@app.route('/')
def index():
    # bilance_requst()
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
