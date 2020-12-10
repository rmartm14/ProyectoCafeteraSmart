import RPi.GPIO as GPIO
import time


def setupServo(servoPIN):
    global p
    global stopingTime
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
    p.start(0) # Initialization
    stopingTime = 0.1
    
def moveInit():
    try:
        while 1:
            for dc in range(0, 16, 2):
                p.ChangeDutyCycle(dc)
                time.sleep(0.1)
            for dc in range(16, 0, -2):
                p.ChangeDutyCycle(dc)
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    p.stop()
    GPIO.cleanup()


        
  
