"""Exercici 9: Indicador de Moviment amb PIR, Buzzer Passiu i LED (Time Slicing)
Utilitzar un brunzidor passiu i un LED per alertar de moviments detectats pel sensor PIR,
amb *time slicing* per alternar el so i la llum."""

import RPi.GPIO as GPIO
import time
from llibreries_dispositius.active_Buzzer_classe import Buzzer
from llibreries_dispositius.pir_classe import SensorPIR
from llibreries_dispositius.led_classe import LED

GPIO.setmode(GPIO.BCM)

pir = SensorPIR(pir_pin=4)
buzzer = Buzzer(buzzer_pin=18)
led = LED(pin=17)

def alert_with_time_slicing():
    while True:
        if pir.detecta_moviment():
            buzzer.encendre()
            led.encendre()
            time.sleep(0.5)
            buzzer.apagar()
            led.apagar()
            time.sleep(0.5)
        else:
            buzzer.apagar()
            led.apagar()
            time.sleep(0.5)
try:
    alert_with_time_slicing()
except KeyboardInterrupt: print("Programa finalitzat per l'usuari")
finally: GPIO.cleanup()