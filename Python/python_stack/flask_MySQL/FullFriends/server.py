from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)

mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    full_friends = mysql.query_db("SELECT CONCAT(first_name, ' ', last_name) as name, age, DATE_FORMAT(created_at, '%M %D %Y') as created_at FROM friends")
    print full_friends
    return render_template('index.html', full_friends = full_friends)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, age, created_at) VALUES (:first_name, :last_name, :age, NOW())"
    data = {
             'first_name': request.form['first_name'],
             'last_name': request.form['last_name'],
             'age': request.form['age']
           }
    # add a friend to the database!
    # Run query, with dictionary values injected into the query. YOU CAN SEE THIS IN MySQL Workbench!!!
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/remove_friend/<friend_id>')
def delete(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)

# Remember NEVER to RENDER from a POST route!
