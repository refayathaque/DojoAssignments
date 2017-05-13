from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/process', methods=['post'])
def printname():
    print request.form['name']
    return redirect('/')

app.run(debug=True)
