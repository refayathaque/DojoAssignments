from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/users/<username>/<id>') #can have more than 1 variable passed in URL

#placeholders are designated in <> tags where the name inside of the tags should match
#the parameter name that is passed to the route handler function

def show_user_profile(username, id): #should be SAME AS PLACEHOLDERS ABOVE
    print username
    print id
    #we could do other things with this information from this point on such as:
    #use it to retrieve some records from the database
    #render a particular template

    #CONSOLE
    #Refayat
    #12345
    #127.0.0.1 - - [11/May/2017 20:51:39] "GET /users/Refayat/12345 HTTP/1.1" 200 -

    return render_template('user.html')
app.run(debug=True)
