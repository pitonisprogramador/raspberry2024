"""Exercici 4: Alarma de Proximitat amb LED i So
Encendre un LED i activar un so d'alarma quan un objecte és a menys de 10 cm de distància."""

import RPi.GPIO as GPIO
import time
from llibreries_dispositius.led_classe import LED
from llibreries_dispositius.active_Buzzer_classe import Buzzer
from llibreries_dispositius.distancia_classe import SensorDistancia

GPIO.setmode(GPIO.BCM)

sensor_dist = SensorDistancia(trigger_pin=23, echo_pin=24)
led_rojo = LED(17)
buzzer = active_Buzzer_classe.Buzzer(18)

try:
    while True:
        # Medir la distancia
        distancia = sensor_dist.mesura_distancia()
        print(f"Distancia: {distancia} cm")

        if distancia < 10: 
            led_rojo.encendre()
            buzzer.sonar_durant(1)
        else:
            led_rojo.apagar()
            buzzer.apagar()
        
        time.sleep(1)

except KeyboardInterrupt: print("Programa finalitzat per l'usuari")
finally: GPIO.cleanup()
