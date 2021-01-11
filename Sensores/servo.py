
import RPi.GPIO as GPIO
import time


def setupServo(servoPIN):
    global p
    global stopingTime

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
    p.start(4) # Initialization
    stopingTime = 0.1

def moveInit(movimientos):
    try:
        for i in range(0, movimientos):
             for dc in range(10,4,-1):
                     p.ChangeDutyCycle(dc)
                     time.sleep(0.1)
             for dc in range(4,10,1):
                     p.ChangeDutyCycle(dc)
                     time.sleep(0.1)
        time.sleep(1)
    except KeyboardInterrupt:
        pass
    p.stop()
    GPIO.cleanup()



