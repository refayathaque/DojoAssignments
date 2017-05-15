from flask import Flask, render_template, redirect, request, session, flash

import re # REGEX (Regular Expression) module

# Python regex for matching an email address based on the above criteria
# looks something like this:
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# ^ created a REGEX object that we can use run operations on

app = Flask(__name__)

app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_name', methods=['Post'])
def process():
    if(len(request.form['name']) < 1):
        flash('Name cannot be empty!') #FLASH MESSAGING!
    else:
        flash('Success! Your name is {}'.format(request.form['name']))
        # flash('Success! Your name is %s' % (request.form['name']))
    return redirect('/')

@app.route('/process_email', methods=['POST'])
def submit():
    if(len(request.form['email']) < 1):
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
    # elif EMAIL_REGEX.match(request.form['email']) == False: WHY WONT THIS WORK!?!?!
    # Using EMAIL_REGEX object we created and running "MATCH" method that will
    # return a BOOLEAN indicating whether argument matches the REGEX or not
        flash("Invalid Email Address!")
    else:
        flash("Success!")
    return redirect('/')


app.run(debug=True)

# Check EMAIL with REGEX
