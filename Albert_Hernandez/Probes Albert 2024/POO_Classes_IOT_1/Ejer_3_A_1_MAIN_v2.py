from distancia_classe import *                  # CLASE
from LED_v1_classe import *                     # CLASE

from multiprocessing import Process, Semaphore  # CLASE (necesarias para "Multiprocessing")
import RPi.GPIO as GPIO                         # CLASE (necesarias para "Multiprocessing")
import time                                     # CLASE (necesarias para "Multiprocessing")

#------------------------------------------------------------------- CONFIG. RASPBERRY

LED1 = LED(17)                                           # Assignació Nº PIN --> LED1 (enciende, apaga)
LED2 = LED(27)                                           # Assignació Nº PIN --> LED2 (enciende, apaga)

Sensores = SensorDistancia(trigger_pin=23, echo_pin=24)  # Assignació Nº PIN --> TRIG, ECHO

sem = Semaphore(1)                                       # Semàfor per coordinar accés al GPIO (necesario para "Multiprocessing")


#------------------------------------------------------------------- MAIN

def check_distance():
    while True:                                         # Bucle infinit
        sem.acquire()                                   # Bloquea semáforo (pide prioridad)
        try:
            dist = Sensores.mesura_distancia()          # Cálcula  la distància
            
            if dist < 10:                               # SI: dist < 10 cm
                LED1.encendre()                             # Enciende  LED1
                LED2.apagar()                               # Apaga     LED2
            else:                                       # SINO: dist < 10 cm
                LED1.apagar()                               # Apaga     LED1
                LED2.encendre()                             # Enciende  LED2
        finally:
            sem.release()                               # Libera semàforo (libera prioridad)
        time.sleep(1)                                   # Tiempo reposo (1 seg)



#------------------------------------------------------------------- MULTIPROCESSING

if __name__ == "__main__":
    try:
        p = Process(target=check_distance)
        p.start()
        p.join()                                        # Manté el procés principal actiu

    except KeyboardInterrupt:
        print("Aturant processos...")                   # print "Aturant processos..."
        
        p.terminate()                                   # Termina el procés fill
        p.join()                                        # Espera que el procés fill acabi
        GPIO.cleanup()                                  # Neteja la configuració dels pins GPIO
        
        print("Pins GPIO netejats!")                    # print("Pins GPIO netejats!")
