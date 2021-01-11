import RPi.GPIO as GPIO
import time


def setupRelay(PIN_OUT):
    #Setup de los pines de salida y entrada
    print("Waiting for the sensor to start...")
    time.sleep(2)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_OUT, GPIO.OUT) #Pin echo
    GPIO.output(PIN_OUT, GPIO.LOW)

def pressRelay(PIN_OUT):
    print("Changing state")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_OUT, GPIO.OUT) #Pin echo

def RelayLow(PIN_OUT):
    GPIO.setup(PIN_OUT, GPIO.IN)

def especialRelayPress(PIN_OUT, signal):
    print("Changing special state")
    GPIO.output(PIN_OUT, signal)



