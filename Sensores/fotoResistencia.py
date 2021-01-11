import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN,pull_up_down=GPIO.PUD_UP)

read = GPIO.input(21)

while True:
    read = GPIO.input(21)
    if read == 1:
        print("Encendido")
    else:
        print("Apagado")
    time.sleep(1)