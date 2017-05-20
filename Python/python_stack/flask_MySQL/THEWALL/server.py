from flask import Flask, request, redirect, render_template, flash, session
from mysqlconnection import MySQLConnector
import re # REGEX (Regular Expression) module
import md5
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "SecretKey!"
mysql = MySQLConnector(app,'thewall')

#### functions start ####

def info_insertion():
    query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': md5.new(request.form['password']).hexdigest()
        }
    session['user_id'] = mysql.query_db(query, data) # store in session logged in users id

def friendly_login():
    query = "SELECT * FROM users WHERE id = :user_id"
    data = {
        'user_id': session['user_id']
        }
    logged_in_user = mysql.query_db(query, data)
    print logged_in_user
    return render_template("wall.html", logged_in_user=logged_in_user, greeting = 'We are so excited to have you!')

#### functions end ####

#### routes start ####

@app.route('/')
def index():
    # if 'user_id' in session and 'name' in session:
    #     return redirect('/wall')
    # else:
        return render_template('index.html')

@app.route('/wall')
def wall():
    display_messages = mysql.query_db('SELECT message, created_at, updated_at, user_id FROM messages ORDER BY id DESC')

    return render_template('wall.html', display_messages = display_messages)









@app.route('/submit_message', methods=['POST'])
def submit_message():
    query = "INSERT INTO messages (message, user_id, created_at, updated_at) VALUES (:message, :user_id, :created_at, NOW())"
    data = {
        'message': request.form['message'],
        'user_id': session['user_id'] #FOREIGN KEY! MUST HAVE THIS!
        'created_at': DATE_FORMAT(NOW(),'%b %d %Y %h:%i %p')
        }
    mysql.query_db(query, data)
    # session['user_id'] = mysql.query_db(query, data) # store in session logged in users id
    return redirect('/wall')









@app.route('/login', methods=['POST'])
def login():
    es = mysql.query_db('SELECT first_name, email, password FROM users')
    print es
    counter = 0

    if(len(request.form['email_es']) < 1):
        flash("EMAIL CANNOT BE BLANK!")
    elif not EMAIL_REGEX.match(request.form['email_es']):
        flash("EMAIL NOT VALID!")
    else:
        for i in range(0, len(es)):
            if es[i]['email'] == request.form['email_es']:
                counter += 1
                break

    if(len(request.form['password_es']) < 8 and len(request.form['password_es']) >= 1):
        flash("PASSWORD NOT VALID!")
    elif(len(request.form['password_es']) < 1):
        flash("PASSWORD CANNOT BE BLANK!")
    else:
        for i in range(0, len(es)):
            if es[i]['password'] == md5.new(request.form['password_es']).hexdigest():
                counter += 1
                break
            elif es[i]['password'] != md5.new(request.form['password_es']).hexdigest():
                flash("PASSWORD NOT VALID!")
                break

    if counter == 2:
        flash("You are logged in")
        query = "SELECT * FROM users WHERE id = :user_id"
        data = {
        'user_id': session['user_id']
            }
        logged_in_user = mysql.query_db(query, data) # ^ gets current user_id! SUPER USEFUL!
        print logged_in_user
        return render_template('wall.html', logged_in_user = logged_in_user, greeting = 'Welcome back!')
    else:
        return redirect('/')

@app.route('/registration', methods=['POST'])
def processing():
    counter = 0
    if request.form['first_name'].isalpha() and len(request.form['first_name']) > 2:
        counter += 1
    elif request.form['first_name'].isalpha() and len(request.form['first_name']) < 2:
        flash('FIRST NAME NOT VALID!')
    elif len(request.form['first_name']) < 1:
        flash('FIRST NAME CANNOT BE BLANK!')

    if request.form['last_name'].isalpha() and len(request.form['last_name']) > 2:
        counter += 1
    elif request.form['last_name'].isalpha() and len(request.form['last_name']) < 2:
        flash('LAST NAME NOT VALID!')
    elif len(request.form['last_name']) < 1:
        flash('LAST NAME CANNOT BE BLANK!')

    if(len(request.form['email']) < 1):
        flash("EMAIL CANNOT BE BLANK!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("EMAIL NOT VALID!")
    else:
        counter += 1

    if(len(request.form['password']) >= 8):
        counter += 1
    elif(len(request.form['password']) < 8 and len(request.form['password']) >= 1):
        flash("PASSWORD IS TOO SHORT!")
    elif(len(request.form['password']) < 1):
        flash("PASSWORD CANNOT BE BLANK!")

    if(request.form['password'] == request.form['password_confirmation'] and len(request.form['password']) > 0 and len(request.form['password_confirmation']) > 0 ):
        counter += 1
    elif(request.form['password'] != request.form['password_confirmation']):
        flash('PASSWORDS DO NOT MATCH!')

    if counter == 5:
        flash('You are now a member of TheWall.com')
        info_insertion()
        return friendly_login()

    return redirect('/')

@app.route('/reset')
def reset():
    return redirect('/')

#### routes end ####

app.run(debug=True)

# Remember NEVER to RENDER from a POST route!
