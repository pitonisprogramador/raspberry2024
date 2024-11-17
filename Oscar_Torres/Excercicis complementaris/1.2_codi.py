"""Exercici 2: Sistema Bicolor amb LEDs per a Dues Distàncies
Utilitzar dos LEDs (vermell i verd) per indicar si un objecte és a prop (menys de 10 cm) o
lluny (més de 10 cm)."""

import RPi.GPIO as GPIO
import time
from llibreries_dispositius.led_classe import LED
from llibreries_dispositius.distancia_classe import SensorDistancia

GPIO.setmode(GPIO.BCM)

sensor_dist = SensorDistancia(trigger_pin=23, echo_pin=24)
led_rojo = LED(17)
led_verde = LED(27)

try:
    while True:
        # Medir la distancia
        distancia = sensor_dist.mesura_distancia()
        print(f"Distancia: {distancia} cm")

        if distancia <= 10: 
            led_rojo.encendre()
            led_verde.apagar()
        else:
            led_rojo.apagar()
            led_verde.encendre()
        
        # Esperar 1 segundo antes de la siguiente medición
        time.sleep(1)

except KeyboardInterrupt: print("Programa finalitzat per l'usuari")
finally: GPIO.cleanup()