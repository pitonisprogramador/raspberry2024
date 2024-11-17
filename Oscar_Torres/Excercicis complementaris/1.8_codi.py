"""Exercici 8: Sistema d'Alerta amb PIR i Buzzer Actiu (Amb Threading)
Activar un brunzidor actiu com a alarma quan el sensor PIR detecti moviment a menys de 5
cm del sensor HC-SR04, gestionat amb *threading*."""

import RPi.GPIO as GPIO
import time
from threading import Thread
from llibreries_dispositius.active_Buzzer_classe import Buzzer
from llibreries_dispositius.pir_classe import SensorPIR
from llibreries_dispositius.distancia_classe import SensorDistancia

GPIO.setmode(GPIO.BCM)

buzzer = Buzzer(buzzer_pin=18)
pir = SensorPIR(pir_pin=4)
sensor_dist = SensorDistancia(trigger_pin=23, echo_pin=24)

def pir_alarm():
    while True:
        if pir.detecta_moviment():
            dist_actual = sensor_dist.mesura_distancia()
            if dist_actual < 5:
                buzzer.encendre()
                time.sleep(1)
        else:
            buzzer.apagar()
        time.sleep(0.1)
try:
    alarm_thread = threading.Thread(target=pir_alarm)
    alarm_thread.start()
    alarm_thread.join()
except KeyboardInterrupt: print("Programa finalitzat per l'usuari")
finally: GPIO.cleanup()