from distancia_classe import *     # CLASE para medir distancia
from LED_v1_classe import *        # CLASE para controlar LEDs
from threading import *            # Para crear hilos y semáforo
import time                        # Para pausas

#-------------------------------------- CONFIG. PINs LEDs
RED_LED_PIN    = 17                # Asignación Nº PIN --> RED_LED_PIN
YELLOW_LED_PIN = 27                # Asignación Nº PIN --> YELLOW_LED_PIN 

#------------------------------------- CREO "Objetos"
red_led     = LED(RED_LED_PIN)
yellow_led  = LED(YELLOW_LED_PIN)

Sensores = SensorDistancia(23,24)

sem = Semaphore(1)

#-------------------------------------- MAIN
def red_alert():
    while True:
        sem.acquire()               # Activo semaforo
        
        try:
            dist = Sensores.mesura_distancia() # Acceso a los ojitos
        finally:
            sem.release()           # desactivo semaforo

        if dist < 5:                # SI: "dist" < 5 cm
            red_led.encendre()      #       LED_red ON
        else:                       # SINO:
            red_led.apagar()        #       LED_red OFF 
        
        time.sleep(0.5)

# Función para activar el LED amarillo para distancias moderadas
def yellow_alert():
    while True:
        sem.acquire()                           # Activo semaforo
        try:
            dist = Sensores.mesura_distancia()  # Acceso a los ojitos
        finally:
            sem.release()                       # desactivo semaforo

        if 5 <= dist < 15:                      # SI: "dist"  5 y 15 cm
            yellow_led.encendre()               #       LED_yellow ON
        else:                                   # SINO:
            yellow_led.apagar()                 #       LED_yellow OFF 
        
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
