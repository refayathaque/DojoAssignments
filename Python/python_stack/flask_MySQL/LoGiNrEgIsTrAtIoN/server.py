from flask import Flask, request, redirect, render_template, flash, session
from mysqlconnection import MySQLConnector
import re # REGEX (Regular Expression) module
import md5

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)

app.secret_key = "SecretKey!"

mysql = MySQLConnector(app,'login_registration')

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
    mysql.query_db(query, data)

@app.route('/signing_in', methods=['POST'])
def signing_in():
    es = mysql.query_db('SELECT email, password FROM users')
    print es
    counter = 0

    if(len(request.form['email_es']) < 1):
        flash("EMAIL CANNOT BE BLANK!")
    elif not EMAIL_REGEX.match(request.form['email_es']):
        flash("EMAIL NOT VALID!")
    else:
        for i in range(0, len(es)):
            if es[i]['email'] == request.form['email_es']:
                print '***********************EMAIL VALIDATED YAO~~~~~~~~~~~~~~~~~~~~~~~~~'
                flash("EMAIL VALID!")
                counter += 1
                break

# {'password': request.form['password_es'], 'email': request.form['email_es']} in es:

# [{u'password': u'password', u'email': u'refayathaque@gmail.com'}, {u'password': u'23b431acfeb41e15d466d75de822307c', u'email': u'jsmith@email.com'}]

    #PASSWORD
    if(len(request.form['password_es']) < 8):
        flash("PASSWORD NOT VALID!")
    else:
        for i in range(0, len(es)):
            if es[i]['password'] == md5.new(request.form['password_es']).hexdigest():
                print '**********************PASSWORD VALIDATED YAO~~~~~~~~~~~~~~~~~~~~~~~'
                flash("PASSWORD VALID!")
                counter += 1
                break

    if counter == 2:
        flash("YOU ARE LOGGED IN! WELCOME BACK!")
        print '***********************~~~~~~~~~~~~~~~~~~~~~~~~~'

    # [{u'password': u'password', u'email': u'refayathaque@gmail.com'}, {u'password': u'23b431acfeb41e15d466d75de822307c', u'email': u'jsmith@email.com'}]

    return redirect('/')

@app.route('/registration', methods=['POST'])
def processing():
    counter = 0
    if request.form['first_name'].isalpha() and len(request.form['first_name']) > 2:
        flash('FIRST NAME VALID!')
        counter += 1
    elif request.form['first_name'].isalpha() and len(request.form['first_name']) < 2:
        flash('FIRST NAME NOT VALID!')

    if request.form['last_name'].isalpha() and len(request.form['last_name']) > 2:
        flash('LAST NAME VALID!')
        counter += 1
    elif request.form['last_name'].isalpha() and len(request.form['last_name']) < 2:
        flash('LAST NAME NOT VALID!')

    if(len(request.form['email']) < 1):
        flash("EMAIL CANNOT BE BLANK!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("EMAIL NOT VALID!")
    else:
        flash("EMAIL VALID!")
        counter += 1

    #PASSWORD
    if(len(request.form['password']) >= 8):
        flash("PASSWORD VALID!")
        counter += 1
    elif(len(request.form['password']) < 8):
        flash("PASSWORD NOT VALID!")

    if(request.form['password'] == request.form['password_confirmation']):
        flash('PASSWORDS MATCH!')
        counter += 1
    elif(request.form['password'] != request.form['password_confirmation']):
        flash('PASSWORDS DO NOT MATCH!')

    if counter == 5:
        print '***********************VALIDATED~~~~~~~~~~~~~~~~~~~~~~~~~'
        info_insertion()

    return redirect('/')

app.run(debug=True)

# Remember NEVER to RENDER from a POST route!
