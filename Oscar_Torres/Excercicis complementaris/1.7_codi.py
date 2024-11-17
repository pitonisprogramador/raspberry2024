"""Exercici 7: Sistema d'Alertes amb Threading (Múltiples Fils)
Crear un sistema d'alerta on es monitoritzen dos intervals de distància amb dos fils. Cada
interval actua com una alerta independent: el primer fil activa un LED vermell per
proximitats extremes, i el segon fil activa un LED groc per distàncies moderades."""

import RPi.GPIO as GPIO
import time
from threading import Thread
from llibreries_dispositius.led_classe import LED
from llibreries_dispositius.distancia_classe import SensorDistancia

# Configurar el modo de numeración de pines
GPIO.setmode(GPIO.BCM)

sensor_dist = SensorDistancia(trigger_pin=23, echo_pin=24)
led_amarillo, led_rojo = LED(27), LED(22)

def red_alert():
    while True:
        dist_actual = sensor_dist.mesura_distancia()
        if dist_actual < 5: led_rojo.encendre()
        else: led_rojo.apagar()
        time.sleep(0.5)

def yellow_alert():
    while True:
        dist_actual = sensor_dist.mesura_distancia()
        if (5 <= dist_actual < 15): led_amarillo.encendre()
        else: led_amarillo.apagar()
        time.sleep(0.5)

try:
    # Creació de dos fils per a les alertes
    red_thread = threading.Thread(target=red_alert)
    yellow_thread = threading.Thread(target=yellow_alert)
    red_thread.start()
    yellow_thread.start()
    red_thread.join()
    yellow_thread.join()
except KeyboardInterrupt: print("Programa finalitzat per l'usuari")
finally: GPIO.cleanup()