from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/results', methods = ['post'])
def results():
    name = request.form["name"]
    dojo_location = request.form["dojo_location"]
    favorite_language = request.form["favorite_language"]
    comment = request.form["comment"]
    return render_template('results.html', name = name, dojo_location = dojo_location, favorite_language = favorite_language, comment = comment)

# #format for what's passed to .html ^ - (htmlVAR = pyVAR(pyVAR MUST BE initatilized WITHIN this method))

@app.route('/return_to_index', methods = ['post'])
def return_to_index():
    # return render_template('index.html') - Also works...
    return redirect('/')
    # REDIRECT only returning to ROOT (index.html)

app.run(debug=True)

#REDIRECT - for ROUTES only, CANNOT take in arguments
#RENDER_TEMPLATE - for TEMPLATES only, CAN take in arguments
