"""Exercici 5: Alerta amb Buzzer i LED segons distància amb dues interrupcions
Enunciat: Dissenya un sistema que faci sonar un buzzer i encengui un LED vermell
quan la distància sigui inferior a 10 cm, indicant proximitat extrema. Quan la
distància sigui superior a 20 cm, el buzzer ha d’apagar-se i s'ha d'encendre un
LED verd, indicant que l'objecte es troba a una distància segura. Utilitza
interrupcions per detectar canvis en la distància i per activar o desactivar els
LEDs i el buzzer segons els intervals establerts."""

import RPi.GPIO as GPIO
import time
from llibreries_dispositius.distancia_classe import SensorDistancia
from llibreries_dispositius.led_classe import LED
from llibreries_dispositius.active_Buzzer_classe import Buzzer

GPIO.setmode(GPIO.BCM)

sensor_dist = SensorDistancia(trigger_pin=23, echo_pin=24)
led_rojo, led_verde = LED(17), LED(27)
buzzer = Buzzer(18)

def alerta_leds(pin_interrupcion):
    global distancia_actual
    led_rojo.apagar()
    led_verde.apagar()
    if distancia_actual < 10: led_rojo.encendre()
    elif distancia_actual >= 20:led_verde.encendre()

def alerta_buzzer():
    global distancia_actual
    if distancia_actual < 20: buzzer.encendre()
    else: buzzer.apagar()

#interrupcions
GPIO.add_event_detect(sensor_dist.echo_pin, GPIO.FALLING, callback=alerta_leds, bouncetime=50)

try:
    while True:
        distancia_actual = sensor_dist.mesura_distancia()
        alerta_buzzer()
        time.sleep(1)
except KeyboardInterrupt: print("Programa interrumpido por el usuario")
finally: 
    GPIO.cleanup()
    print("GPIO limpiado y programa finalizado")
