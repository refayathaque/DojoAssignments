from flask import Flask, request, redirect, render_template, flash

app = Flask(__name__)

app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/results', methods = ['post'])
def results():
    name = request.form["name"]
    dojo_location = request.form["dojo_location"]
    favorite_language = request.form["favorite_language"]
    comment = request.form["comment"]

    if(len(request.form['name']) < 1):
        flash('Name cannot be empty!')
        return redirect('/')
    elif(len(request.form['comment']) < 1):
        flash('Comment field cannot be empty!')
        return redirect('/')
    elif(len(request.form['comment']) > 120):
        flash('Comment is too long! Must be under 120 characters')
        return redirect('/')
    else:
        return render_template('results.html', name = name, dojo_location = dojo_location, favorite_language = favorite_language, comment = comment)

@app.route('/return_to_index', methods = ['post'])
def return_to_index():
    return redirect('/')

app.run(debug=True)
