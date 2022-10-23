from flask import Flask, render_template, redirect, url_for, request
import json
from flask_socketio import SocketIO

app = Flask(__name__)

global currentNum

currentNum = 0

testData = {"time": [0, 1, 2, 3, 4, 5], "velocity": [1, 5, 8, 10, 10, 10]}
testtext = {"Hello, World!": [0, 1, 2, 3, 4]}
testJson = json.dumps(testData)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/features')
def features():
    return "FEATURES"


@app.route('/test2')
def test2():
    return render_template("justChart.html")


@app.route('/test')
def test():
    return render_template("test.html")


@app.route('/pricing')
def pricing():
    return testtext["Hello, World!"]


@app.route('/button', methods=['POST'])
def getbutton():
    global currentNum
    global testtext
    testtext = request.json
    return "good job!"


app.run(host='0.0.0.0', port=81)
