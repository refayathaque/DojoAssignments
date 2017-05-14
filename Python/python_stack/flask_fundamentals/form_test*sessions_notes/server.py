from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'thisissecret' # secret key ALWAYS with SESSIONS

@app.route('/')
def index():
    return render_template('index.html')

# Route below handles our form submission

# Defined which HTTP methods are allowed by this route (GET/POST)

# GET request for insensitive information, POST request for sensitive information

@app.route('/users', methods=['POST']) #POST:client submits data AND gets something back (login/username/password)
def create_user():
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/show') # we changed where we redirect to so we can go to
                             # the page that displays the name and email!

    # Below is everything we did before SESSIONS lesson...
    # name = request.form['name'] # 'name' attr in HTML form
    # email = request.form['email'] # 'name' attr in HTML form
    # return redirect('/') # Redirects back to the ROOT route ('/'), so back to index.html
        # return render_template('success.html')

    # key/value pairs with the name attributes as the keys and
        # the data the user enters as the values

    # note that the typeof anything that comes in through request.form will be
        # "String" no matter what. If you want that value to be identified as an actual
        # number you'll have to type cast it.

@app.route('/show', methods=['GET']) # GET:client ONLY gets something back (regular http request, also DEFAULT)
def show_user():
    # return render_template('user.html', name=session['name'], email=session['email'])
    return render_template('user.html') # when using SESSION in templates don't need to pass arguments
                                        # bc we can access SESSION directly from the templates!

app.run(debug=True) # RUNS THE SERVER!

# SESSION! Same way we create variables in our functions to solve problems,
    # we keep STATE DATA in SESSION to solve problems down the line, like in
    # subsequent HTTP REQ/RESP cycle instances

# COOKIES! - Flask use COOKIES to STORE DATA like SESSIONS. Flask uses secure
    # hashing of session data to send a packet of information from server to client.
    # This packet is the COOKIE. Once your browser has received this cookie, it writes
    # the information contained in it to a small file on your hard drive

# META-DATA: Data ABOUT data

# We can also access session in our templates!

# Store only what you need in the session. Once we incorporate a database you
# should be limiting what you store in sessions to the most minimal amount of
# data possible
