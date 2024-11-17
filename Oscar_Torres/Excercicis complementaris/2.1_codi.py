"""Exercici 1: Control d'un LED amb un sensor PIR usant interrupcions
Enunciat: Configura un sistema on un LED s'encengui cada vegada que es
detecti moviment amb un sensor PIR. Quan el PIR detecti moviment, el LED
s'activarà automàticament durant uns segons i després s'apagarà. Utilitza una
interrupció configurada per una pujada de senyal que permeti controlar
l'activació del LED en funció del senyal del PIR."""

import RPi.GPIO as GPIO
import time
from llibreries_dispositius.pir_classe import SensorPIR
from llibreries_dispositius.led_classe import LED

GPIO.setmode(GPIO.BCM)

pir = SensorPIR(pir_pin=4)
led_rojo = LED(17)

def encendre_led(channel):
    print("interrupció llençada")
    led_rojo.encendre()
    time.sleep(2) # LED encès per 2 segons
    led_rojo.apagar()

GPIO.add_event_detect(pir.pir_pin, GPIO.RISING, callback=encendre_led)

try:
    while True: time.sleep(1) # Manté el programa actiu
except KeyboardInterrupt: print("Programa finalitzat")
finally: GPIO.cleanup()