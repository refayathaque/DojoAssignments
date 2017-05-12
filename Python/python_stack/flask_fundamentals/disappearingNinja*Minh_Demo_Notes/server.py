from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<poop>')
def ninja_color(poop):
    # if(poop == 'blue'):
    #     image_url = '/static/img/leonardo.jpg'
    # elif(poop == 'purple'):
    #     image_url = '/static/img/donatello.jpg'
    # elif(poop == 'red'):
    #     image_url = '/static/img/raphael.jpg'
    # elif(poop == 'orange'):
    #     image_url = '/static/img/michelangelo.jpg'
    # return render_template('showninja.html', image_url = image_url, view_color = poop)

    #DICTIONARY method is another way to do what we did above...
    dictionary = {
        "blue":"leonardo",
        "red":"raphael",
        "orange":"michelangelo",
        "purple":"donatello"
    }
    if poop in dictionary:
        image_url = "/static/img/" + dictionary[poop] + ".jpg"
        name_of_turtle = dictionary[poop]
    else:
        image_url = "/static/img/notapril.jpg"
    return render_template("showninja.html", image_url = image_url, view_color = poop, name = name_of_turtle)
    #format for what's passed to .html ^ - (htmlVAR = pyVAR(MUST BE initatilized WITHIN this method))

app.run(debug=True)
