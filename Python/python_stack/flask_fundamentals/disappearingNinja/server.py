from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    #render
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    #render
    return render_template('ninja.html')

@app.route('/ninja/<poop>')
def ninja_color(poop):
    #render
    if(poop == 'blue'):
        image_url = '/static/img/leonardo.jpg'
    elif(poop == 'purple'):
        image_url = '/static/img/donatello.jpg'
    elif(poop == 'red'):
        image_url = '/static/img/raphael.jpg'
    elif(poop == 'orange'):
        image_url = '/static/img/michelangelo.jpg'
    return render_template('showninja.html', image_url = image_url, view_color = poop)

app.run(debug=True)
