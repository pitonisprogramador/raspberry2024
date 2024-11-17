from distancia_classe import *     # CLASE para medir distancia
from LED_v1_classe import *        # CLASE para controlar LEDs
from threading import *    # Para crear hilos y semáforo
import time                        # Para pausas

#-------------------------------------- Configuración de pines para los LEDs
RED_LED_PIN    = 17                   # Asignación Nº PIN --> RED_LED_PIN
YELLOW_LED_PIN = 27                   # Asignación Nº PIN --> YELLOW_LED_PIN 

#------------------------------------- Objeto de cada LED
red_led = LED(RED_LED_PIN)
yellow_led = LED(YELLOW_LED_PIN)

#------------------------------------- Sensor de distancia
Sensores = SensorDistancia(23,24)

#------------------------------------- Semáforo para coordinar el acceso al sensor
sem = Semaphore(1)

# Función para activar el LED rojo para proximidades extremas
def red_alert():
    while True:
        sem.acquire()               # Bloquea el semáforo para medir la distancia
        try:
            dist = Sensores.mesura_distancia()
        finally:
            sem.release()           # Libera el semáforo después de medir

        if dist < 5:                # Si la distancia es menor a 5 cm
            red_led.encendre()
        else:
            red_led.apagar()
        
        time.sleep(0.5)

# Función para activar el LED amarillo para distancias moderadas
def yellow_alert():
    while True:
        sem.acquire()               # Bloquea el semáforo para medir la distancia
        try:
            dist = Sensores.mesura_distancia()
        finally:
            sem.release()           # Libera el semáforo después de medir

        if 5 <= dist < 15:          # Si la distancia está entre 5 y 15 cm
            yellow_led.encendre()
        else:
            yellow_led.apagar()
        
        time.sleep(0.5)

# Creación de los hilos para las alertas
try:
    red_thread = Thread(target=red_alert)
    yellow_thread = Thread(target=yellow_alert)

    red_thread.start()
    yellow_thread.start()

    # Mantener los hilos activos
    red_thread.join()
    yellow_thread.join()

except KeyboardInterrupt:
    print("Espere por favor, cerrando procesos...")
    red_thread.join()
    yellow_thread.join()
    red_led.apagar()
    yellow_led.apagar()
    print("¡Pines limpios!")
