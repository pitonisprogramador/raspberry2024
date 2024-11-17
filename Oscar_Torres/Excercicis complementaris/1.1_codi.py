"""Exercici 1: Sistema de Distància amb Indicador LED (Sense PWM)
Utilitzar el sensor HC-SR04 per mesurar la proximitat d'un objecte i encendre un LED quan
aquest es trobi a menys de 15 cm. Si l'objecte és més lluny, el LED s'apaga"""

import RPi.GPIO as GPIO
import time
from llibreries_dispositius.led_classe import LED
from llibreries_dispositius.distancia_classe import SensorDistancia

GPIO.setmode(GPIO.BCM)

sensor_dist = SensorDistancia(trigger_pin=23, echo_pin=24)
led_rojo = LED(17)

try:
    while True:
        # Medir la distancia
        distancia = sensor_dist.mesura_distancia()
        print(f"Distancia: {distancia}cm")

        if distancia < 15: led_rojo.encendre()  
        else: led_rojo.apagar()

        # Esperar 1 segundo antes de la siguiente medición
        time.sleep(1)

except KeyboardInterrupt: print("Programa finalitzat per l'usuari")
finally: GPIO.cleanup()
