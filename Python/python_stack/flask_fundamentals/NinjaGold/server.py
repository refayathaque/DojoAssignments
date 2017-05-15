from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)

app.secret_key = "SecretKey!"

@app.route('/')
def index():
    session['current_gold'] = 0 # To add on to this MUST INITIATE in page load METHOD!
    return render_template('index.html')

@app.route('/process_money', methods=['POST']) #POST:client submits data AND gets something back (login/username/password)
def process_money():
    if(request.form['building'] == 'farm'):
        q = random.randrange(10, 21)
        session['current_gold'] += q
        print q
        return render_template('index.html', earned = "Golds earned from farm: ", golds = q)
    elif(request.form['building'] == 'cave'):
        q = random.randrange(5, 11)
        session['current_gold'] += q
        print q
        return render_template('index.html', earned = "Golds earned from cave: ", golds = q)
    elif(request.form['building'] == 'house'):
        q = random.randrange(2, 6)
        session['current_gold'] += q
        print q
        return render_template('index.html', earned = "Golds earned from house: ", golds = q)
    elif(request.form['building'] == 'casino'):
        if(random.randrange(1, 3) == 1):
            q = random.randrange(0, 51)
            session['current_gold'] += q
            return render_template('index.html', earned = "Golds earned from casino: ", golds = q)
        elif(random.randrange(1, 3) == 2):
            q = random.randrange(0, 51)
            session['current_gold'] -= q
            return render_template('index.html', earned = "Golds LOST from casino: ", golds = q)
        print session['current_gold']
        # return render_template('index.html')

app.run(debug=True)
