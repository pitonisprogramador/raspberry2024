"""Exercici 2: Activació d'un buzzer segons distància amb interrupcions
Enunciat: Crea un sistema d'alerta amb un sensor de distància i un buzzer. Quan
la distància sigui menor de 15 cm, el buzzer ha de sonar, i quan la distància
superi aquest valor, s'ha de silenciar. Utilitza una interrupció que s'activa quan
hi ha un canvi de distància per controlar l'activació del buzzer de manera
eficient i només quan cal."""

import RPi.GPIO as GPIO
import time
from threading import Thread
from llibreries_dispositius.distancia_classe import SensorDistancia
from llibreries_dispositius.active_Buzzer_classe import Buzzer

GPIO.setmode(GPIO.BCM)

sensor_dist = SensorDistancia(trigger_pin=23, echo_pin=24)
buzzer = Buzzer(18)

def activar_buzzer(channel):
    if distancia["actual"] < 15: buzzer.encendre()
    else: buzzer.apagar()

GPIO.add_event_detect(sensor_dist.echo_pin, GPIO.FALLING, callback=activar_buzzer)

try:
    while True:
        #desem la mesura dins un objecte diccionari, per ser assequible dins de la funcio de callback
        distancia = {"actual": sensor_dist.mesura_distancia()}
        time.sleep(1)
except KeyboardInterrupt: print("Programa finalitzat per l'usuari")
finally: GPIO.cleanup()