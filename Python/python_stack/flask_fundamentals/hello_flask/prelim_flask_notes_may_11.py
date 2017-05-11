from flask import Flask #importing flask allows us to create our application
                        #used to create our 'app' variable, always need this

app = Flask(__name__) #global variable __name__ tells Flask if we are running the
                      #file directly, or importing it as a module

                      #using 'Flask' module to create 'app' variable, this
                          #variable always used to attach a routing rule using
                          #DECORATOR
                      #Always need this line when building apps

@app.route('/') #'@' is the DECORATOR, and it will attach our function below to the
                #('/') route. So whenever we send a request to localhost:5000/
                #we will run the function below

def hello_world():
    return "Hello World!" #returning this string as a response
app.run(debug=True) #runs the app in debug mode

@app.route('/greeting/<yourname>') #parameters can be set in the URL

def greeting(yourname): #parameters have to match what is ^
    return "Hello %s!" % (yourname)
app.run(debug=True)

# CANT RUN BOTH THESE APPS TOGETHER, COMMENT ONE OUT!
