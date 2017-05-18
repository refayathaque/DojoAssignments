from flask import Flask, request, redirect, render_template, flash, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)

app.secret_key = "SecretKey!"

mysql = MySQLConnector(app,'sakila')

@app.route('/')
def index():
    return render_template('index.html')

def email_addition():
    query = "INSERT INTO same_emails (email, created_at) VALUES (:email, NOW())"
    data = {
             'email': request.form['email']
           }
    mysql.query_db(query, data)

@app.route('/email_processing', methods=['POST'])
def email_processing():
    email = mysql.query_db('SELECT LCASE(email) FROM customer')
    print email

    if {'LCASE(email)': request.form['email']} in email:
        flash('Email is valid!')

        email_addition()

        display_emails = mysql.query_db('SELECT email, created_at FROM same_emails')
        print display_emails

        return render_template('success.html', display_emails = display_emails)
    else:
        flash('Email is NOT valid!')
        return redirect('/')

app.run(debug=True)
