import RPi.GPIO as GPIO
import time
from w1thermsensor import W1ThermSensor

def medirTemperatura():
    sensor = W1ThermSensor()
    temperature = sensor.get_temperature()
    return temperature

