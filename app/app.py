from flask import Flask, render_template, redirect, url_for, request
import json
from flask_socketio import SocketIO
from twilio.rest import Client
import os


auth_token = os.environ['auth_token']
account_sid = os.environ['account_sid']

client = Client(account_sid, auth_token)


app = Flask(__name__)

global currentResult
#currentResult = ""
currentResult = {"time":[],"velocity":[],"ticks":552}
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
    data = currentResult
    if(data == ""):
      return redirect(url_for("index"))
    
    #tdata = [0, 1, 2, 3, 4, 5]
    #vdata = [1, 5, 8, 10, 10, 10]
    return render_template("results.html", data=data)

@app.route('/instructions')
def instructions():

    #Send TEXT "Your test results are ready to view..."
    return render_template("instructions.html")


@app.route('/button', methods=['POST'])
def getbutton():
    global currentResult
    currentResult = request.get_json()
    print(currentResult["time"])
    return "good job!"
  #message = client.messages.create(
#                     #body='Your results have been processed. Please go to this link to view them',
#                     #from_='+14632558992',
#                     #to='ENTER-PHONE-NUMBER'
#                           #)
  
app.run(host='0.0.0.0', port=81)

def calcFVC(times, velos):
  #at each time we have velocity
  #convert veto m/s
  return 5

def calcFEV(times, velos):
  
  return 5

def calcFVCFEV(times, velos):
  
  return 5