from flask import Flask, request, redirect, render_template, flash, session
from mysqlconnection import MySQLConnector
import re # REGEX (Regular Expression) module
import md5
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "SecretKey!"
mysql = MySQLConnector(app,'refs_wall')

#### FUNCTIONS ####

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
    user = mysql.query_db(query, data)
    return render_template("wall.html", user = user, greeting = 'We are so excited to have you!')

#### ####

#### $$$$ ROUTES $$$$ ####

#### INDEX / LOGIN PAGE ####

@app.route('/')
def index():
    # if 'user_id' in session and 'name' in session:
    #     return redirect('/wall')
    # else:
        return render_template('index.html')

#### ####

#### DISPLAYING WALL ####

@app.route('/wall')
def wall():
    display_messages = mysql.query_db('SELECT messages.message, messages.id AS message_id, messages.created_at, messages.updated_at, users.first_name, users.last_name, users.id AS user_id FROM messages LEFT JOIN users ON messages.user_id = users.id')

    display_comments = mysql.query_db('SELECT comments.comment, comments.message_id, comments.user_id, comments.id AS comment_id, users.first_name, users.last_name, users.id AS user_id FROM comments LEFT JOIN users ON comments.user_id = users.id')

    return render_template('wall.html', display_messages = display_messages, display_comments = display_comments)

#### ####

#### POPULATING WALL ####

@app.route('/submit_message', methods=['POST'])
def submit_message():
    query = "INSERT INTO messages (message, user_id, created_at, updated_at) VALUES (:message, :user_id, NOW(), NOW())"
    # current_time = datetime.datetime.now().strftime("%B %d %Y at %I:%M %p")
    data = {
        'message': request.form['message'],
        'user_id': session['user_id'], #FOREIGN KEY! MUST HAVE THIS!
        # 'created_at': current_time #CHANGE from DATETIME in MySQLWorkbench!
        }
    mysql.query_db(query, data)
    # session['user_id'] = mysql.query_db(query, data) # store in session logged in users id
    return redirect('/wall')

#### ####

#### LOGIN ####

@app.route('/login', methods=['POST'])
def login():
    # Saving entire list to variable 'es' to use below for validating
    # email and password
    es = mysql.query_db('SELECT first_name, email, password FROM users')
    counter = 0
    # DON'T TOUCH ^

    # Email validation
    if(len(request.form['email_es']) < 1):
        flash("EMAIL CANNOT BE BLANK!")
    elif not EMAIL_REGEX.match(request.form['email_es']):
        flash("EMAIL NOT VALID!")
    else:
        for i in range(0, len(es)):
            if es[i]['email'] == request.form['email_es']:
                counter += 1
                break
                # DON'T TOUCH ^

    # Password validation
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
                # DON'T TOUCH ^

    # Checking if all validations pass
    if counter == 2:
        flash("You are logged in")

        # Getting information of person logging in
        query = "SELECT * FROM users WHERE email = :email"
        data = {
            'email': request.form['email_es']
        }
        user = mysql.query_db(query, data)
        # DON'T TOUCH ^

        # Matching email to id then saving id as session[user_id]
        query = "SELECT id FROM users WHERE email = :email"
        data = {
            'email': request.form['email_es']
        }
        list_with_one_dictionary_inside = mysql.query_db(query, data)
        id_of_user_logging_in = list_with_one_dictionary_inside[0]['id']
        session['user_id'] = id_of_user_logging_in
        # DON'T TOUCH ^

        # Passing in information of person logging in
        return render_template('wall.html', user = user, greeting = 'Welcome back!')
        # DON'T TOUCH ^

    # Staying at login (index) page if validations fail
    else:
        return redirect('/')
        # DON'T TOUCH ^

#### ####

#### REGISTRATION ####

@app.route('/registration', methods=['POST'])
def registration():

    counter = 0

    # First name validation
    if request.form['first_name'].isalpha() and len(request.form['first_name']) > 2:
        counter += 1
    elif request.form['first_name'].isalpha() and len(request.form['first_name']) < 2:
        flash('FIRST NAME NOT VALID!')
    elif len(request.form['first_name']) < 1:
        flash('FIRST NAME CANNOT BE BLANK!')

    # Last name validation
    if request.form['last_name'].isalpha() and len(request.form['last_name']) > 2:
        counter += 1
    elif request.form['last_name'].isalpha() and len(request.form['last_name']) < 2:
        flash('LAST NAME NOT VALID!')
    elif len(request.form['last_name']) < 1:
        flash('LAST NAME CANNOT BE BLANK!')

    # Email name validation
    if(len(request.form['email']) < 1):
        flash("EMAIL CANNOT BE BLANK!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("EMAIL NOT VALID!")
    else:
        counter += 1

    # Password validation
    if(len(request.form['password']) >= 8):
        counter += 1
    elif(len(request.form['password']) < 8 and len(request.form['password']) >= 1):
        flash("PASSWORD IS TOO SHORT!")
    elif(len(request.form['password']) < 1):
        flash("PASSWORD CANNOT BE BLANK!")

    # Password match validation
    if(request.form['password'] == request.form['password_confirmation'] and len(request.form['password']) > 0 and len(request.form['password_confirmation']) > 0 ):
        counter += 1
    elif(request.form['password'] != request.form['password_confirmation']):
        flash('PASSWORDS DO NOT MATCH!')

    # Checking if all validations pass...
    if counter == 5:
        flash('You are now a member of TheWall.com')
        info_insertion()
        return friendly_login()

    return redirect('/')

#### ####

@app.route("/postComment/<message_id>", methods=['POST'])
def postComment(message_id):
    query = "INSERT into comments (comment, message_id, user_id, created_at, updated_at) VALUES (:comment, :message_id, :user_id, NOW(), NOW())"

    data = {
        "user_id": session['user_id'],
        "message_id":message_id,
        "comment": request.form['comment']
    }

    mysql.query_db(query, data)
    return redirect("/wall")




#### RESET / RETURN TO LOGIN PAGE ####

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

#### ####

app.run(debug=True)

# Remember NEVER to RENDER from a POST route!
