import RPi.GPIO as GPIO
import time

def setupSensor(PIN_IN, PIN_OUT):
    #Setup de los pines de salida y entrada
    print("Waiting for the sensor to start...")
    time.sleep(2)
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_IN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Pin Trigger
    GPIO.setup(PIN_OUT, GPIO.OUT) #Pin echo

    GPIO.output(PIN_OUT, GPIO.LOW) #?
    print("Fin Setup")

def calcularDistancia(PIN_IN, PIN_OUT):
    print("Init Calculo Distancia")
    #Encendemos el sensor para que empiece a calcular la distancia
    GPIO.output(PIN_OUT, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(PIN_OUT, GPIO.LOW)

    #Ahora lo que tenemos que hacer es calcular la distancia de inicio y fin para calcular la distancia final

    while GPIO.input(PIN_IN) == 0:
        startTime = time.time()
    while GPIO.input(PIN_IN) == 1:
        finalTime = time.time()

    fTime = finalTime - startTime

    #Calculamos la distancia midiendola con el tiempo
    distancia = round(fTime * 17150, 2)

    return distancia

def calcularPorcentaje(MAX_CAP_DIST, distancia):  
    percentage = (MAX_CAP_DIST - distancia)/MAX_CAP_DIST
    return percentage









