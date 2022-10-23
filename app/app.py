from flask import Flask, render_template, redirect, url_for, request
import json
from flask_socketio import SocketIO
from twilio.rest import Client
import os


auth_token = os.environ['auth_token']
account_sid = os.environ['account_sid']

client = Client(account_sid, auth_token)


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


@app.route('/test')
def test():
    return render_template("justChart.html")


@app.route('/results')
def results():
    data = {'time':["0", "1", "2", "3", "4", "5"], 'Velocity':["1", "5", "8", "10", "10", "20"]}
    
    #tdata = [0, 1, 2, 3, 4, 5]
    #vdata = [1, 5, 8, 10, 10, 10]
    return render_template("results.html", data = data)

@app.route('/instructions')
def instructions():

    #Send TEXT "Your test results are ready to view..."
    #message = client.messages.create(
                    #body='Your test results are ready to be viewed',
                    #from_='+14632558992',
                    #to='+12569988636'
                          #)

  

    return render_template("instructions.html")


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
