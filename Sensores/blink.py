import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

"""def blink():
    print("Comenzamos la ejecución")
    
    tiempo = 0
    
    while tiempo < 60:
        print("Encendiendo un LED...")
        time.sleep(1)
        GPIO.output(17, True)
        print("Apagando un LED...")
        time.sleep(1)
        GPIO.output(17, False)
        tiempo+=1
    
blink()
"""
GPIO.output(17, True)