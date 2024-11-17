"""Exercici 5: Patró de Senyalització Seqüencial amb LEDs
Crear un patró seqüencial d'encesa de quatre LEDs en funció de la proximitat de l'objecte
detectat."""

import RPi.GPIO as GPIO
import time
from llibreries_dispositius.led_classe import LED
from llibreries_dispositius.distancia_classe import SensorDistancia

# Configurar el modo de numeración de pines
GPIO.setmode(GPIO.BCM)

sensor_dist = SensorDistancia(trigger_pin=23, echo_pin=24)
leds_l = [led_verde, led_amarillo, led_rojo, led_azul] = [LED(17), LED(27), LED(22), LED(5)]

def lanza_rafaga():
    for led in leds_l:
        led.encendre()
        time.sleep(0.1)
        led.apagar()
    time.sleep(0.5)

try:
    while True:
        # Medir la distancia
        distancia = sensor_dist.mesura_distancia()
        print(f"Distancia: {distancia} cm")
        if distancia < 5: lanza_rafaga()
        
        # Esperar 1 segundo antes de la siguiente medición
        time.sleep(1)
except KeyboardInterrupt: print("Programa finalitzat per l'usuari")
finally: GPIO.cleanup()
