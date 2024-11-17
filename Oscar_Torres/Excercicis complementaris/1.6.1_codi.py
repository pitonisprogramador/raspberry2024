"""Exercici 6: Indicador de Distància amb Multiprocessing (Múltiples Processos)
Utilitzar tres processos paral·lels per controlar tres LEDs diferents, cadascun associat a un
interval de distància diferent (0-10 cm, 10-20 cm i més de 20 cm). Cada procés controla un
LED en funció d'un interval de distància específic, permetent que els LEDs s'encenguin i
s'apaguin independentment segons la distància de l'objecte detectat."""

import RPi.GPIO as GPIO
import time
from multiprocessing import Process
from llibreries_dispositius.led_classe import LED
from llibreries_dispositius.distancia_classe import SensorDistancia

# Configurar el modo de numeración de pines
GPIO.setmode(GPIO.BCM)

echo_pin, trigger_pin = 24, 23
sensor_dist = SensorDistancia(trigger_pin, echo_pin)
led_verde = LED(17)
led_amarillo = LED(27)
led_rojo = LED(22)
leds_dic = {17: led_verde, 27: led_amarillo, 22: led_rojo}

# Variable compartida para la distancia actual
dist_actual = 101  # Valor inicial mayor al rango máximo

def bucle_distancia():
    global dist_actual
    while True:
        dist_actual = sensor_dist.mesura_distancia()
        time.sleep(0.5)

def control_led(led_num, min_dist, max_dist):
    global dist_actual
    while True:
        led = leds_dic[led_num]
        if min_dist <= dist_actual < max_dist:
            led.encendre()
        else:
            led.apagar()

# Crear los procesos para los LEDs
processes = [
    Process(target=control_led, args=(led_verde.pin, 0, 10)),
    Process(target=control_led, args=(led_amarillo.pin, 10, 20)),
    Process(target=control_led, args=(led_rojo.pin, 20, 100)),
]

try:
    # Iniciar todos los procesos de control de LEDs
    for p in processes:
        p.start()

    # Ejecutar el bucle de distancia en el hilo principal
    bucle_distancia()
except KeyboardInterrupt: print("Programa finalizado por el usuario")
finally:
    # Terminar todos los procesos de LEDs y limpiar GPIO
    for p in processes: p.terminate()
    GPIO.cleanup()