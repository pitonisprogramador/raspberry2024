"""Exercici 11: Sistema d’Alarma Completa amb PIR, Buzzer i LEDs (Amb Threading)
Crear una alarma completa que inclogui el sensor PIR, el sensor ultrasònic, diversos LEDs i
un brunzidor per senyalitzar la proximitat i el moviment en paral·lel utilitzant *threading*."""

import RPi.GPIO as GPIO
import time
from threading import Thread
from llibreries_dispositius.distancia_classe import SensorDistancia
from llibreries_dispositius.pir_classe import SensorPIR
from llibreries_dispositius.led_classe import LED
from llibreries_dispositius.active_Buzzer_classe import Buzzer

GPIO.setmode(GPIO.BCM)

pir = SensorPIR(pir_pin=4)
sensor_dist = SensorDistancia(trigger_pin=23, echo_pin=24)
led_rojo = LED(17)
buzzer = Buzzer(18)

def proximity_alert():
    while True:
        dist_actual = sensor_dist.mesura_distancia()
        if dist_actual < 5:
            led_rojo.encendre()
            buzzer.encendre()
        else:
            led_rojo.apagar()
            buzzer.apagar()
        time.sleep(0.5)

def movement_alert():
    while True:
        if pir.detecta_moviment():
            led_rojo.encendre()
            time.sleep(1)
        else:
            led_rojo.apagar()
        time.sleep(0.5)

try:
    proximity_thread = Thread(target=proximity_alert)
    movement_thread = Thread(target=movement_alert)
    proximity_thread.start()
    movement_thread.start()
    proximity_thread.join()
    movement_thread.join()
except KeyboardInterrupt: print("Programa finalitzat per l'usuari")
finally: GPIO.cleanup()