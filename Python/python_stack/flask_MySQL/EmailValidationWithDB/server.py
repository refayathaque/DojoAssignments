from flask import Flask, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)

mysql = MySQLConnector(app,'sakila')

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/friends', methods=['POST'])
# def create():
#     query = "INSERT INTO friends (first_name, last_name, age, created_at) VALUES (:first_name, :last_name, :age, NOW())"
#     data = {
#              'first_name': request.form['first_name'],
#              'last_name': request.form['last_name'],
#              'age': request.form['age']
#            }
#     # add a friend to the database!
#     # Run query, with dictionary values injected into the query. YOU CAN SEE THIS IN MySQL Workbench!!!
#     mysql.query_db(query, data)
#     return redirect('/')
#

@app.route('/email_processing', methods=['POST'])
def results():
    email = mysql.query_db('SELECT LCASE(email) FROM customer')
    # print email

    for i in email:
        if(request.form['email'] != i['LCASE(email)']):
            flash('Email is not valid!')
            return redirect('/')


app.run(debug=True)

# Remember never to render from a post route!
