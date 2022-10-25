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
global myfvc
global myfev
global myfevfvc
#currentResult = ""
currentResult = {"time":[0],"velocity":[0,0,0,0,0,0,0,0,0,0,0,0],"ticks":552}
myfvc = 0
myfev = 0
myfevfvc = 0

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
    global currentResult
    global myfvc
    global myfev
    global myfevfvc
    data = currentResult
    
    if(data == ""):
      return redirect(url_for("index"))
    
    #tdata = [0, 1, 2, 3, 4, 5]
    #vdata = [1, 5, 8, 10, 10, 10]
    return render_template("results.html", data=data, myfvc=myfvc, myfev=myfev, myfevfvc=myfevfvc)

@app.route('/instructions')
def instructions():

    #Send TEXT "Your test results are ready to view..."
    return render_template("instructions.html")


@app.route('/button', methods=['POST'])
def getbutton():
    global currentResult
    global myfvc
    global myfev
    global myfevfvc
    currentResult = request.get_json()


    area = 0.0000580644
    sum = 0
    for velo in currentResult["velocity"]:
      sum = sum + (velo * area)

    myfvc = sum
    fev1 = 0
    for i in range(0,9):
      fev1 = (currentResult["velocity"][i] * area) + fev1
      
    myfev = fev1
    myfevfvc = 0
    if(myfvc != 0):
      myfevfvc = myfev/myfvc
    message = client.messages.create(body='Your results have been processed.' + '\nYour FVC is: ' + str(myfvc) + '\nYour FEV is: ' + str(myfev) + '\nYour FEV/FVC is: ' + str(myfevfvc), from_='+14632558992', to='12569988636')
    return "good job!"
    
  
app.run(host='0.0.0.0', port=81)

