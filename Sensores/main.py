from sensorDistancia import * 
from servo import *
#Variables globales sobre las que trabajamos
PIN_IN = 21
PIN_OUT = 3


def main():
   """ MAX_DISTANCE = 13.0
    setupSensor(PIN_IN, PIN_OUT)
    distancia = calcularDistancia(PIN_IN, PIN_OUT)
    print(distancia)
    porcentaje = calcularPorcentaje(MAX_DISTANCE, distancia)
    print("Cantidad de cafe: {} %".format(100 - (porcentaje*100)))
    """
   
   setupServo(15)
   print("Iniciando movimiento hacia delante")
   moveInit()
   

main()



