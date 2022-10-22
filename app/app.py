from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/features')
def features():
    return "FEATURES"

@app.route('/pricing')
def pricing():
    return "PRICING"

app.run(host='0.0.0.0', port=81)
