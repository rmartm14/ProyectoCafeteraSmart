import RPi.GPIO as GPIO
import time

#Setup de los pines de salida y entrada
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Pin Sensor

if GPIO.input(21) == 0:
    print("No hay agua")
else:
    print("Hay agua")
