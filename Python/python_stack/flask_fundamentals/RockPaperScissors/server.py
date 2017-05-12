from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "asdfasdfjlw;ekrj;laksjdfjn,m.z"

@app.route('/')
def index():
    if(session["win"]):
        return render_template('index.html', win=session["win"])
    else:
        return render_template("index.html")

@app.route('/process_play/<player_choice>', methods=['post', 'GET'])
def get_input(player_choice):
    if(True):
        session["win"] = True
    # paper = request.form['paper']
    # scissors = request.form['scissors']
    return redirect('/')
# @app.route()
app.run(debug=True)

# @app.route('/process_play/<result>')
#
# def get_input():
#
#     return render_template('user.html')
