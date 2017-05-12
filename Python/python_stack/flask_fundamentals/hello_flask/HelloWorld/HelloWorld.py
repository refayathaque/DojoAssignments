from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def hello_world():
    return render_template('index.html', name="Jeremy")
    # Flask uses a templating engine called Jinja2 to parse through files
    # looking for {{}}, replace variables with real values, and send a complete
    # HTML file back to the client.
app.run(debug=True)
