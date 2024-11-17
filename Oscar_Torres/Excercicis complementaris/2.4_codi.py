"""Exercici 4: Alarmes seqüencials amb PIR i buzzer
Enunciat: Crea un sistema on, cada vegada que el sensor PIR detecti moviment,
s'activi un buzzer per 1 segon i un LED per 2 segons en seqüència. Això actua
com una alarma seqüencial on el buzzer s'activa primer per avisar del
moviment detectat i, tot seguit, el LED s'encén per mantenir la indicació visual
durant més temps. Utilitza interrupcions per detectar el moviment i activar els
dispositius de manera seqüencial."""

import RPi.GPIO as GPIO
import time
from llibreries_dispositius.pir_classe import SensorPIR
from llibreries_dispositius.led_classe import LED
from llibreries_dispositius.active_Buzzer_classe import Buzzer

pir = SensorPIR(pir_pin=23)
led_rojo = LED(17)
buzzer = Buzzer(18)

def alarma_seqüencial(channel):
    buzzer.sonar_durant(1)
    led_rojo.encendre()
    time.sleep(2)
    led_rojo.apagar()

GPIO.add_event_detect(pir.pir_pin, GPIO.RISING, callback=alarma_seqüencial)

try:
    while True: time.sleep(1)
except KeyboardInterrupt: print("Programa finalitzat")
finally: GPIO.cleanup()