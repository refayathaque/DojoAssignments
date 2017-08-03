from flask import Flask, request, redirect, render_template, flash, session
from mysqlconnection import MySQLConnector
import re # REGEX (Regular Expression) module
import md5

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)

app.secret_key = "SecretKey!"

mysql = MySQLConnector(app,'login_registration')

# print md5.new('password').hexdigest() # 5f4dcc3b5aa765d61d8327deb882cf99

## WILL'S MODULAR FLASK GUIDE ## START

class LoginRegistration(object): # What is objects?
    def login(self, first_name, last_name, email, password):
        pass
    def register(self):
        pass

User = LoginRegistration()

def create(self, name, email):
    errors = []

    if len(first_name) < 1:
        errors.append('Name is required')
    elif len(first_name < 3):
        errors.append('Name must be 3 characters or more')

    if len(last_name) < 1:
        errors.append('Name is required')
    elif len(last_name < 3):
        errors.append('Name must be 3 characters or more')

    if len(email) < 1:
        errors.append('Email is required')
    elif not EMAIL_REGEX.match(email):
        errors.append('Not a valid email')

    if len(errors) > 0:
        return False, errors
    else:
        query = 'INSERT INTO users (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :password)'
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password
        }
        return True, mysql.query_db(query, data)

@app.route('/new', methods=['POST'])
def new():
    new_user = User.create(request.form['first_name'], request.form['last_name'], request.form['email'], request.form['password'])

    if new_user[0]:
        return render_template('success.html')
    else:
        flash(new_user[1].errors)
        return redirect('/')

## WILL'S MODULAR FLASK GUIDE ## END

@app.route('/')
def index():
    return render_template('index.html')

def info_insertion():
    query = "INSERT INTO users (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :password)"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': md5.new(request.form['password']).hexdigest()
        }
    session['user_id'] = mysql.query_db(query, data) # store in session logged in users id

@app.route('/signing_in', methods=['POST'])
def signing_in():
    es = mysql.query_db('SELECT first_name, email, password FROM users')
    print es
    counter = 0

    #EMAIL
    if(len(request.form['email_es']) < 1):
        flash("EMAIL CANNOT BE BLANK!")
    elif not EMAIL_REGEX.match(request.form['email_es']):
        flash("EMAIL NOT VALID!")
    else:
        for i in range(0, len(es)):
            if es[i]['email'] == request.form['email_es']:
                counter += 1
                break

    #PASSWORD
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
        return render_template('success.html', logged_in_user = logged_in_user, greeting = 'Welcome back!')
    else:
        return redirect('/')

@app.route('/registration', methods=['POST'])
def processing():
    counter = 0

    #EMAIL
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

    #PASSWORD
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
        flash('You are now a member of LoginRegistration.com')
        info_insertion()
        return friendly_login()

    return redirect('/')

def friendly_login():
    query = "SELECT * FROM users WHERE id = :user_id"
    data = {
        'user_id': session['user_id']
        }
    logged_in_user = mysql.query_db(query, data)
    print logged_in_user
    return render_template("success.html", logged_in_user=logged_in_user, greeting = 'We are so excited to have you!')

@app.route('/reset')
def reset():
    return redirect('/')

app.run(debug=True)

# Remember NEVER to RENDER from a POST route!
