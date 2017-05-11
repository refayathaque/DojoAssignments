from flask import Flask, render_template #allows us to return rendered HTML
                                         #in TEMPLATES folder
app = Flask(__name__)

@app.route('/') #handling ROOT route ('/'), ALSO all routes DEFAULT to GET
#If you have ONLY ONE ROUTE your server is listening for, it MUST be ROOT route ('/')

def hello_world():
    return render_template('index.html') #index.html is in TEMPLATES

@app.route('/success')

def success():
    return render_template('success.html') #this is ALSO in TEMPLATEs
app.run(debug=True) #CAN ONLY HAVE ONE app.run! MUST be with LAST FUNCTION,
                    #otherwise won't work
