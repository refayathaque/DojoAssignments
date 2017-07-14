from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt # from flask.ext.bcrypt import Bcrypt - if this doesn't work
import re

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex = re.compile(r'^[a-zA-Z]+$')
password_regex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,15}$')
# Password matching expression.

app = Flask(__name__)
mysql = MySQLConnector(app, 'LoginRegistration2') # CHANGE DB NAME
bcrypt = Bcrypt(app)
app.secret_key = 'NotSureWhyWeNeedThisButOkay'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods = ['POST'])
def create():
    # Do all validations here...
    validated_first_name = ""
    validated_last_name = ""
    validated_email = ""
    validated_hashed_password = ""
    counter = 0

    # Validations
    if name_regex.match(request.form['first_name']) && name_regex.match(request.form['first_name']):
        validated_first_name = request.form['first_name']
        validated_last_name = request.form['last_name']
        counter ++
    elif not name_regex.match(request.form['first_name']) || name_regex.match(request.form['first_name']):
        flash("Name invalid")
    else:
        flash("Name invalid")

    if email_regex.match(request.form['email']):
        validated_email = request.form['email']
        counter ++
    else:
        flash("Email invalid")

    if password_regex.match(request.form['password']):
        if request.form['password'] == request.form['confirm_password']:
            validated_hashed_password = bcrypt.generate_password_hash(request.form['confirm_password'])
            counter++
        else:
            flash("Passwords do not match")
    else:
        flash("Password invalid")

    if counter == 3
        query = "INSERT INTO users (first_name, last_name, email, password, updated_at, created_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {
             'first_name' : validated_first_name,
             'last_name' :  validated_last_name,
             'email' : validated_email,
             'password' : validated_hashed_password,
        }
        mysql.query_db(query, data)
        return render_template('/success')

# @app.route('/friends/<friend_id>')
# def show(friend_id):
#     # Write query to select specific user by id. At every point where
#     # we want to insert data, we write ":" and variable name.
#     query = "SELECT * FROM users WHERE id = :specific_id"
#     # Then define a dictionary with key that matches :variable_name in query.
#     data = {'specific_id': friend_id}
#     # Run query with inserted data.
#     one_friend = mysql.query_db(query, data)
#     # Friends should be a list with a single object,
#     # so we pass the value at [0] to our template under alias one_friend.
#     return render_template('index.html', one_friend = one_friend[0])

# @app.route('/friends/edit/<friend_id>')
# def edit(friend_id):
#     query = "SELECT * FROM users WHERE id = {}".format(friend_id)
#     user = mysql.query_db(query)
#     print user
#     return render_template('edit.html', friend = user)
#
# @app.route('/friends/update/<friend_id>', methods = ['POST'])
# def update(friend_id):
#     query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email_address = :email_address WHERE id = :id"
#     data = {
#         'first_name' : request.form['first_name'],
#         'last_name' : request.form['last_name'],
#         'email_address' : request.form['email_address'],
#         'id' : friend_id
#     }
#     user = mysql.query_db(query, data)
#     return redirect('/')
#
# @app.route('/friends/remove/<friend_id>', methods = ['POST'])
# def remove(friend_id):
#     query = "DELETE FROM users WHERE id = :id"
#     data = {'id' : friend_id}
#     mysql.query_db(query, data)
#     return redirect('/')

app.run(debug=True)
