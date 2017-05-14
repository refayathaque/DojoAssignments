from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)

app.secret_key = "SecretKey!"

@app.route('/')
def index():
    session['random_number'] = random.randrange(1, 101)
    print session['random_number']
    return render_template('index.html')

@app.route('/number_input', methods=['POST']) #POST:client submits data AND gets something back (login/username/password)
def number_input():
    session['number_input'] = int(request.form['answer'])
    a = session['number_input']
    print a
    b = session['random_number']
    print b
    if(session['number_input'] > session['random_number']):
        return render_template('index.html', too_high = "Too High!")
    elif(session['number_input'] < session['random_number']):
        return render_template('index.html', too_low = "Too Low!")
    elif(session['number_input'] == session['random_number']):
        session['random_number'] = random.randrange(1, 101) # RESETS SESSION
        return render_template('index.html', correct = "Correct! It was ", number = session['number_input'])

app.run(debug=True)
