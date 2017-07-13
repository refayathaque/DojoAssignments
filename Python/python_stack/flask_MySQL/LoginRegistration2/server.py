from flask import Flask, request, redirect, render_template, session, flash #
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex = re.compile(r'^[a-zA-Z]+$')
password_regex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,15}$')

app = Flask(__name__)
mysql = MySQLConnector(app, 'LoginRegistration2') # CHANGE DB NAME
bcrypt = Bcrypt(app)
app.secret_key = 'NotSureWhyWeNeedThisButOkay'

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM users")
    return render_template('index.html', friends = friends)

@app.route('/create', methods = ['POST'])
def create():
    query = "INSERT INTO users (first_name, last_name, email, password, updated_at, created_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
    data = {
             'first_name' : ,
             'last_name' :  ,
             'email' : ,
             'password' : ,
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<friend_id>')
def show(friend_id):
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM users WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': friend_id}
    # Run query with inserted data.
    one_friend = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('index.html', one_friend = one_friend[0])

# @app.route('/friends', methods=['POST'])
# def create():
#     # add a friend to the database!
#     return redirect('/')

@app.route('/friends/edit/<friend_id>')
def edit(friend_id):
    query = "SELECT * FROM users WHERE id = {}".format(friend_id)
    user = mysql.query_db(query)
    print user
    return render_template('edit.html', friend = user)

@app.route('/friends/update/<friend_id>', methods = ['POST'])
def update(friend_id):
    query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email_address = :email_address WHERE id = :id"
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email_address' : request.form['email_address'],
        'id' : friend_id
    }
    user = mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/remove/<friend_id>', methods = ['POST'])
def remove(friend_id):
    query = "DELETE FROM users WHERE id = :id"
    data = {'id' : friend_id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
