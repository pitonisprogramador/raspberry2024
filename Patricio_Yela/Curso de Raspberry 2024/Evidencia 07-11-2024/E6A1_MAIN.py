from distancia_classe import *  # CLASE
from LED_v1_classe import *     # CLASE
from multiprocessing import Process, Semaphore
import RPi.GPIO as GPIO
import time

# Configuración Raspberry Pi
LED_PINS = [17, 27, 22]                                       # Pines GPIO para los LEDs
LEDs = [LED(pin) for pin in LED_PINS]                         # Crear instancia para cada LED

Sensores = SensorDistancia(23,24)       # Asignación de pines para TRIG y ECHO
sem = Semaphore(1)                                            # Semáforo para coordinar acceso al GPIO

# Función para controlar cada LED en un rango de distancia específico
def control_led(led, dist_min, dist_max):
    while True:
        sem.acquire()
        try:
            dist = Sensores.mesura_distancia()                # Mide la distancia
            if dist_min <= dist < dist_max:
                led.encendre()                                  # Enciende el LED si la distancia está en el rango
            else:
                led.apagar()                                    # Apaga el LED si la distancia está fuera del rango
        finally:
            sem.release()
        time.sleep(0.5)                                       # Tiempo de espera antes de la siguiente verificación

if __name__ == "__main__":
    try:
        # Crear tres procesos, uno para cada LED, con diferentes rangos de distancia
        processes = [
            Process(target=control_led, args=(LEDs[0], 0, 10)),
            Process(target=control_led, args=(LEDs[1], 10, 20)),
            Process(target=control_led, args=(LEDs[2], 20, 100))
        ]

        # Iniciar los procesos
        for p in processes:
            p.start()

        # Mantener el proceso principal activo
        for p in processes:
            p.join()

    except KeyboardInterrupt:
        print("Espere por favor, cerrando procesos...")
        for p in processes:
            p.terminate()                                     # Termina cada proceso
            p.join()                                          # Espera que cada proceso termine
        GPIO.cleanup()                                        # Limpia la configuración de los pines GPIO
        print("¡Pines limpios!")
