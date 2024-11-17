from distancia_classe import *  # CLASE
from LED_v1_classe import *    # CLASE
from multiprocessing import Process, Semaphore
import RPi.GPIO as GPIO
import time

# Configuració Raspberry Pi
LED1 = LED(17)  # Assignació Nº PIN --> LED1 (enciende, apaga)
LED2 = LED(27)  # Assignació Nº PIN --> LED2 (enciende, apaga)

Sensores = SensorDistancia(trigger_pin=23, echo_pin=24)  # Assignació Nº PIN --> TRIG, ECHO
sem = Semaphore(1)  # Semàfor per coordinar accés al GPIO

# Funció principal per verificar la distància
def check_distance():
    while True:  # Bucle infinit
        sem.acquire()  # Bloqueja el semàfor
        try:
            dist = Sensores.mesura_distancia()  # Mesura la distància
            if dist < 15:  # Si dist < 15 cm
                LED1.encendre()  # Encén LED1
                LED2.apagar()   # Apaga LED2
            else:
                LED1.apagar()   # Apaga LED1
                LED2.encendre() # Encén LED2
        finally:
            sem.release()  # Allibera el semàfor
        time.sleep(1)  # Temps abans de la següent mesura

if __name__ == "__main__":
    try:
        p = Process(target=check_distance)
        p.start()

        # Manté el procés principal actiu
        p.join()

    except KeyboardInterrupt:
        print("Aturant processos...")
        p.terminate()  # Termina el procés fill
        p.join()       # Espera que el procés fill acabi
        GPIO.cleanup() # Neteja la configuració dels pins GPIO
        print("Pins GPIO netejats!")
