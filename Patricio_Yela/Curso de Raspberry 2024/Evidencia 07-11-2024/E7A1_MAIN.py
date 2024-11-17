from distancia_classe import *     # CLASE para medir distancia
from LED_v1_classe import *        # CLASE para controlar LEDs
from threading import *                  # Para crear hilos y semaforo
import time                        # Para pausas

# Configuracion de pines para los LEDs
RED_LED_PIN = 17
YELLOW_LED_PIN = 27

# Instancia de los LEDs
red_led = LED(RED_LED_PIN)
yellow_led = LED(YELLOW_LED_PIN)

# Sensor de distancia
Sensores = SensorDistancia(trigger_pin=23, echo_pin=24)

# Semaforo para coordinar el acceso al sensor
sem = Semaphore(1)

# Variable de control para detener los hilos
stop_threads = False

# Funcion para activar el LED rojo para proximidades extremas
def red_alert():
    global stop_threads
    while not stop_threads:
        sem.acquire()  # Bloquea el semoforo para medir la distancia
        try:
            dist = Sensores.mesura_distancia()
        finally:
            sem.release()  # Libera el semaforo despues de medir

        if dist < 5:  # Si la distancia es menor a 5 cm
            red_led.encendre()
        else:
            red_led.apagar()
        
        time.sleep(0.5)

# Funcion para activar el LED amarillo para distancias moderadas
def yellow_alert():
    global stop_threads
    while not stop_threads:
        sem.acquire()  # Bloquea el semaforo para medir la distancia
        try:
            dist = Sensores.mesura_distancia()
        finally:
            sem.release()  # Libera el semaforo despues de medir

        if 5 <= dist < 15:  # Si la distancia esta entre 5 y 15 cm
            yellow_led.encendre()
        else:
            yellow_led.apagar()
        
        time.sleep(0.5)

# Creacion de los hilos para las alertas
try:
    red_thread = Thread(target=red_alert)
    yellow_thread = Thread(target=yellow_alert)

    red_thread.start()
    yellow_thread.start()

    # Mantener el programa en ejecucion hasta recibir una interrupcion
    red_thread.join()
    yellow_thread.join()

except KeyboardInterrupt:
    print("Espere por favor, cerrando procesos...")
    stop_threads = True  # Cambia la variable de control para detener los hilos
    red_thread.join()
    yellow_thread.join()
    red_led.apagar()
    yellow_led.apagar()
    print("Pines limpios")
