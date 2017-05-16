from flask import Flask, render_template, session, request, redirect
from datetime import datetime
import random

app = Flask(__name__)

app.secret_key = "SecretKey!"

@app.route('/')
def index():
    session['current_gold'] = 0 # To add on to this MUST INITIATE in page load METHOD!
    session['log'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST']) #POST:client submits data AND gets something back (login/username/password)
def process_money():
    if(request.form['building'] == 'farm'):
        q = random.randrange(10, 21)
        session['current_gold'] += q
        print q
        session['log'].insert(0,('You have earned {} gold from the farm @ {}'.format(q, datetime.now())))
        return render_template('index.html')
    elif(request.form['building'] == 'cave'):
        q = random.randrange(5, 11)
        session['current_gold'] += q
        print q
        session['log'].insert(0,('You have earned {} gold from the cave @ {}'.format(q, datetime.now())))
        return render_template('index.html')
    elif(request.form['building'] == 'house'):
        q = random.randrange(2, 6)
        session['current_gold'] += q
        print q
        session['log'].insert(0,('You have earned {} gold from the house @ {}'.format(q, datetime.now())))
        return render_template('index.html')
    elif(request.form['building'] == 'casino'):
        rand_int = random.randrange(1, 3)
        if(rand_int == 1):
            q = random.randrange(0, 51)
            session['current_gold'] += q
            session['log'].insert(0,('You have earned {} gold from the casino @ {}'.format(q, datetime.now())))
            return render_template('index.html')
        elif(rand_int == 2):
            q = random.randrange(0, 51)
            session['current_gold'] -= q
            session['log'].insert(0,('You have LOST {} gold from the casino @ {}'.format(q, datetime.now())))
            return render_template('index.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
