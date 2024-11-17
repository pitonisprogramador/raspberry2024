# Exercici 7: Sistema d'Alertes amb Threading (Múltiples Fils)
# Crear un sistema d'alerta on es monitoritzen dos intervals de distància amb dos fils. 
# Cada interval actua com una alerta independent: el primer fil activa un LED vermell per proximitats extremes, 
# i el segon fil activa un LED groc per distàncies moderades.

### Esta version utiliza una variable global para calcular la distancia. 
### Los procesos led solo acceden a esa variable en modo lectura

from led_classe import *
from distancia_classe import *
# from Active_Buzzer_classe import *
# from multiprocessing import Process, Semaphore, Value
from threading import Thread, Semaphore
from multiprocessing import Value
import RPi.GPIO as GPIO

# buzzer_pin = 26

# led_azul_pin = 7
# led_verde_pin = 12
led_rojo_pin = 16
led_amarillo_pin = 1

trigger_pin = 21
echo_pin = 20

distancia_minima = 5        # Distancia mínima 
# distancia_media = 10        # Distancia media
distancia_maxima = 15       # Distancia máxima

RANGO_MIN = 2               # Mínima distancia (2 cm) medible por el dispositivo
RANGO_MAX = 400             # Máxima distancia (400 cm) medible por el dispositivo

# Declaración de los dispositivos
# led_verde = LED(led_verde_pin)
led_amarillo = LED(led_amarillo_pin)
led_rojo = LED(led_rojo_pin)
# led_azul = LED(led_azul_pin)
sensor_distancia = SensorDistancia(trigger_pin, echo_pin)
# buzzer = Buzzer(buzzer_pin)

# Semáforo y variable global
sem = Semaphore(1)              # Semáforo para coordinar acceso al medidor (no es necesario declararlo como global en las funciones)
distancia = Value('f', 0.0)     # Variable compartida para calcular la distancia (no es necesario declararlo como global en las funciones)

def control_led(led, dmin, dmax):
    """
    Control de los LEDS
    Utiliza la variable global 'distancia' que actualiza el proceso que mide la distancia
    """
    while True:
        sem.acquire()           # Bloquea el semáforo
        try:
            if (dmin <= distancia.value < dmax):                # Lee la variable global
                led.encendre()
                # print(f"Distancia: {distancia:.1f} cm. [{dmin} cm. - {dmax} cm.]")
            else:
                led.apagar()         
        finally:
            sem.release()           # Libera semáforo
        # time.sleep(.2)              # Retardo antes de la siguiente medida

def medir_distancia():
    """ 
    Proceso para medir la distancia
    El resultado queda en variable global 'distancia'
    """
    while True:
        sem.acquire()
        try:
            distancia.value = sensor_distancia.mesura_distancia()
        finally:
            sem.release()
        time.sleep(0.2)


# if __name__ == '__main__' :
#     main()

if __name__ == '__main__':
    try:
        lista_threads = [
            Thread(target=medir_distancia),
            Thread(target=control_led, args=(led_rojo, RANGO_MIN, distancia_minima)),
            Thread(target=control_led, args=(led_amarillo, distancia_minima, RANGO_MAX)),
        ]
        for thread in lista_threads:
            thread.start()

        for thread in lista_threads:
            thread.join()

    except KeyboardInterrupt:
        print("\nAturant processos...")
        GPIO.cleanup()
        print("\nDispositius netejats!")

