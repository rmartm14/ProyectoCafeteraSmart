from sondaTemperatura import *
from sensorDistancia import *
from servo import *
from rele import *
from coffeeMaker import *

PIN_OUT_DISTANCIA = 4
PIN_IN_DISTANCIA = 5
PIN_OUT_SERVO = 26
PIN_RELE = 20
PIN_RELE_2 = 21
PIN_SONDA = 16
MAX_CAFE = 100
def setupGeneral():
    GPIO.cleanup()
    setupRelay(PIN_RELE)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_RELE_2, GPIO.OUT)
    setupSensor(PIN_IN_DISTANCIA, PIN_OUT_DISTANCIA)
    setupServo(PIN_OUT_SERVO)
    RelayLow(PIN_RELE)
def makeCoffee():
    #Primer paso:  Comprobar que se cumplen las condiciones para hacer cafe.
#    cantidadCafe =100 #calcularPorcentaje(MAX_CAFE, calcularDistancia(PIN_IN_DISTANCIA, PIN_OUT_DISTANCIA))
#    cantidadAgua = 100 #?¿?¿?¿?¿
#    cafeRetirado = True #Foto resistencia en el filtro yo creo
#    condicionSalida = False

#    if cantidadCafe > 25 and cantidadAgua > 75 and cafeRetirado == True:
#        condicionSalida = True

    #if condicionSalida == False:
#        return -1
    print("Servo en movimiento")
    moveInit(2)
    #Segundo paso: Calentar el agua
    temperaturaAgua = medirTemperatura()
    if temperaturaAgua < 90:
        print("Activación calentador")
        pressRelay(PIN_RELE)

    while temperaturaAgua < 75:
        temperaturaAgua = medirTemperatura()
        print("La temperatura del agua es: {} º".format(temperaturaAgua))
        time.sleep(2)

    #Ya ha alcanzado la temperatura
    print("Temperatura lista")
    RelayLow(PIN_RELE)

    #Tercer paso: Echar el cafe dentro del filtro con el servo
     #Mover el servo con 6 movimientos
     #Cuarto paso: Bombear el agua con la bomba
    #TODO CON LA BOMBA
    print("Comienza la bomba")
    especialRelayPress(PIN_RELE_2, GPIO.HIGH)
    time.sleep(60)
    especialRelayPress(PIN_RELE_2,GPIO.LOW)
    #Quinto paso: Mandar mensaje de cafe hecho
    print("Cafe hecho")
    return 0

setupGeneral()
makeCoffee()
