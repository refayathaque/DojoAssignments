from flask import Flask, request, redirect, render_template, flash, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)

app.secret_key = "SecretKey!"

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

@app.route('/email_processing')
def results():
    email = mysql.query_db('SELECT LCASE(email) FROM customer')
    print email

    # {u'LCASE(email)': u'philip.causey@sakilacustomer.org'}

    for i in range(0, len(email)):
        print i
        if(request.form['email'] == email[i][u'LCASE(email)']):
            flash('Email is valid!')
            print request.form['email']
            print email[i][u'LCASE(email)']
            break
        elif(request.form['email'] != email[i][u'LCASE(email)']):
            flash('Email is not valid!')
            print request.form['email']
            print email[i][u'LCASE(email)']
            break

    return redirect('/')


app.run(debug=True)

# Remember never to render from a post route!
