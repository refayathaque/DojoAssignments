from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

#Route below handles our form submission

#Defined which HTTP methods are allowed by this route (GET/POST)

#GET request for insensitive information, POST request for sensitive information

@app.route('/users', methods=['POST'])

def create_user():
    name = request.form['name'] #'name' attr in HTML form
    email = request.form['email'] #'name' attr in HTML form

    #key/value pairs with the name attributes as the keys and
    #the data the user enters as the values

    #note that the typeof anything that comes in through request.form will be
    #"String" no matter what. If you want that value to be identified as an actual
    #number you'll have to type cast it.

    return redirect('/') #Redirects back to the ROOT route ('/'), so back to index.html
    #return render_template('success.html')
app.run(debug=True) #RUNS THE SERVER!
