from flask import Flask, request, redirect, render_template, session, flash # HAVE ALL THESE
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'test') # CHANGE DB NAME
# an example of running a query
# print mysql.query_db("SELECT * FROM users")

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM users")
    return render_template('index.html', friends = friends)

@app.route('/friends/create', methods = ['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO users (first_name, last_name, email_address) VALUES (:first_name, :last_name, :email_address)"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email_address': request.form['email_address']
           }
    # Run query, with dictionary values injected into the query.
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
