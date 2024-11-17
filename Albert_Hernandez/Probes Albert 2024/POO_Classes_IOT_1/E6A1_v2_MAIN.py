from distancia_classe import *                      # CLASE Distancia
from LED_v1_classe    import *                      # CLASE LED
from multiprocessing import Process, Semaphore      # CLASE Multiprocesing

import RPi.GPIO as GPIO                             # 
import time                                         #

#---------------------------------------------------------- CONFIG. RASPABERRY
LED_PINS = [17, 27, 22]                             # Pins LEDs
LEDs     = [LED(pin) for pin in LED_PINS]           # Crear "objetos" de la "Clase LED"

Sensores = SensorDistancia(23,24)                   # Asignación de pines para TRIG y ECHO
sem = Semaphore(1)                                  # Creación de 1 semaforo

#---------------------------------------------------------- MAIN
def control_led(led, dist_min, dist_max):
    while True:
        sem.acquire()                               # Activo al semaforo
        
        try:
            dist = Sensores.mesura_distancia()      # Mide la distancia
            
            if dist_min <= dist < dist_max:         # IF: "Margenes de distancias <=>"
                led.encendre()                      #   Enciende el LED 
            else:                                   # SINO:
                led.apagar()                        #   Apaga el LED
        
        finally:                                
            sem.release()                           # Desactivo el semaforo
        
        time.sleep(0.5)                             # Tiempo de espera antes de la siguiente verificación




#----------------------------------------------------------- MULTIPROCESSING
if __name__ == "__main__":
    try:
        # Crear tres procesos, uno para cada LED, con diferentes rangos de distancia
        processes = [
                    Process(target=control_led, args=(LEDs[0], 0, 10)),
                    Process(target=control_led, args=(LEDs[1], 10, 20)),
                    Process(target=control_led, args=(LEDs[2], 20, 100))
                    ]

                                
        for p in processes:     # Iniciar los procesos
            p.start()

        
        for p in processes:     # Mantener el proceso principal activo
            p.join()


#------------------------------------------------------------- EXCEPCIONES
    except KeyboardInterrupt:
        print("Espere por favor, cerrando procesos...")
        
        for p in processes:
            p.terminate()            # Termina cada proceso
            p.join()                 # Espera que cada proceso termine
        GPIO.cleanup()               # Limpia la configuración de los pines GPIO
        
        print("¡Pines limpios!")
