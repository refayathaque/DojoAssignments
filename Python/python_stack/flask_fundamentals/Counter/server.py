from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)

app.secret_key = "SecretKey!" # CHANGING THIS BREAKS THIS CODE! DON'T KNOW WHY!

@app.route('/') # Default ALWAYS GET, GET here bc we're not taking anything from client
def counter():
    session['num'] = session['num'] + 1
    return render_template('index.html') # No args here bc we accessed session in HTML

app.run(debug=True)
