from flask import Flask, render_template, request
import time
import datetime
import sys
sys.path.insert(0, '/home/pi/Desktop/ProyectoCafetera/Sensores')
from sondaTemperatura import *
from sensorDistancia import *
from servo import *
from coffeeMaker import *

#Inicio del servidor
app = Flask(__name__)
app.static_folder = 'static'

#Init app on index
@app.route("/")
def initApp():
     return render_template("ControlCafetera.html")

#Control tab with water and coffee readings
@app.route("/control")
def control():
    #TODO: Implement with the readings of the sensors.
    readCoffee = 66
    readWater  = 66
    waterTemperature = medirTemperatura()
    remainingCups = 0
    condition = 0
    
    if readCoffee > 50 and readWater > 50 and waterTemperature < 90 and remainingCups >0:
        condition = 1   #To show the perfect state
    return render_template("control.html", coffeeLevel=readCoffee, waterLevel=readWater, 
        temperature = waterTemperature, remainingCups = remainingCups, condition=condition)

#About tab with the information of the coffee machine
@app.route("/about")
def about():
    return render_template("about.html")

#Contact tab to contact with us
@app.route("/contact")
def contact():
    return render_template("contact.html")

#New coffee to init the method of the coffee machine
@app.route("/nCoffee", methods=['GET', 'POST'])
def newCoffee():
    if request.method == 'POST':
        hora = request.form['appt']
        
        return coffeeDone(hora)
    else:
        t = datetime.datetime.now()
        current_time = t + datetime.timedelta(minutes = 20)
        return render_template("coffee.html", minHora= current_time)

#Coffee machinedone coffee
@app.route("/coffeeDone/<hour>", methods=['GET', 'POST'])
def coffeeDone(hour):
    return render_template("coffeeDone.html", time=hour)

#Semi-constructor of the app
if __name__ == '__main__':
    app.run(port=80, host="0.0.0.0", debug=True)