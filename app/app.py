from flask import Flask, render_template, redirect, url_for, request
import json
from flask_socketio import SocketIO

app = Flask(__name__)

global currentNum

currentNum = 0

testData = {"time": [0, 1, 2, 3, 4, 5], "velocity": [1, 5, 8, 10, 10, 10]}
testtext = ""
testJson = json.dumps(testData)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/features')
def features():
    return "FEATURES"


@app.route('/pricing')
def pricing():
    return str(currentNum)


@app.route('/button/<num>', methods=['POST'])
def getbutton(num):
  global currentNum
  currentNum = num
  return "good job!"


app.run(host='0.0.0.0', port=81)
