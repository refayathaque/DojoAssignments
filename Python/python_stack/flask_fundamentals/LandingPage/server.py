from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def dojos():
    return render_template('dojos.html')

# @app.route('/ninja/<poop>')
# def ninja_color(poop):
#     return render_template("showninja.html", image_url = image_url, view_color = poop, name = name_of_turtle)
#     #format for what's passed to .html ^ - (htmlVAR = pyVAR(MUST BE initatilized WITHIN this method))

app.run(debug=True)
