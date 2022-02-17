from flask import Flask
from flask import render_template
from datetime import datetime
from MeasurementCatalog import MeasureCatalog


app = Flask(__name__)
WD = MeasureCatalog() 
@app.route("/") 
def home():
    return "hello flask. Dice result: "  + " time: " + str(datetime.now())

@app.route("/MaxWind/") 
def MaxWind():
    return "Max wind = " + str(WD.GetWinMaxValue())

@app.route("/WindData/") 
def WindData():
    return render_template("WindData.html", winddata = WD.GetWindData())  
app.run()  