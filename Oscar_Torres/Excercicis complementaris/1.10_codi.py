"""Exercici 10: Mesurador de Distància amb PIR, LED i Multiprocessing
Utilitzar tres processos paral·lels per activar LEDs segons la distància detectada per l'HCSR04 
i el moviment detectat pel PIR, on cada procés controla una resposta específica"""

import RPi.GPIO as GPIO
import time
from multiprocessing import Process, Lock
from llibreries_dispositius.distancia_classe import SensorDistancia
from llibreries_dispositius.pir_classe import SensorPIR
from llibreries_dispositius.led_classe import LED

GPIO.setmode(GPIO.BCM)

pir = SensorPIR(pir_pin=4)
sensor_dist = SensorDistancia(trigger_pin=23, echo_pin=24)
led_verde, led_amarillo, led_rojo = LED(17), LED(27), LED(22)
led_pins = [led_verde, led_amarillo, led_rojo]

# Crear el objeto de bloqueo
lock = Lock()

def control_leds_by_distance(led, min_dist, max_dist, lock):
    # Usar el bloqueo para asegurar acceso exclusivo
        with lock:
            dist_actual = sensor_dist.mesura_distancia()
            if min_dist <= dist_actual < max_dist:
                led.encendre()
            else:
                led.apagar()
        time.sleep(0.5)

def control_leds_by_pir():
    while True:
        if pir.detecta_moviment():
            for led in led_pins:
                led.encendre()
            time.sleep(1)
            for led in led_pins:
                led.apagar()
            time.sleep(1)

if __name__ == '__main__':
    processes = [
    Process(target=control_leds_by_distance, args=(led_rojo, 0, 10, lock)),
    Process(target=control_leds_by_distance, args=(led_amarillo, 10, 20, lock)),
    Process(target=control_leds_by_distance, args=(led_verde, 20, 100, lock)),
    Process(target=control_leds_by_pir)
    ]

    try:
        for p in processes: p.start()
        for p in processes: p.join()

    except KeyboardInterrupt: print("Programa finalizado por el usuario")

    finally:
        for p in processes: p.terminate()  # Asegura que todos los procesos se detengan
        GPIO.cleanup()