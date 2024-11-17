"""Exercici 3: Control de dos LEDs amb intervals de distància
Enunciat: Dissenya un sistema amb dos LEDs que reaccionen a diferents
intervals de distància. El primer LED s'encendrà quan la distància sigui inferior a
10 cm, indicant proximitat extrema, mentre que el segon LED s'encendrà quan
la distància estigui entre 10 cm i 20 cm, indicant una proximitat moderada.
Utilitza interrupcions per activar i desactivar els LEDs segons aquests intervals
de distància."""

import RPi.GPIO as GPIO
import time
from llibreries_dispositius.led_classe import LED
from llibreries_dispositius.distancia_classe import SensorDistancia

GPIO.setmode(GPIO.BCM)

sensor_dist = SensorDistancia(trigger_pin=23, echo_pin=24)
led_rojo = LED(17)
led_amarillo = LED(27)

def alerta_leds(pin_interrupcion):
    global distancia_actual
    print("interrupcion lanzada")
 
    # Lógica de alerta según la distancia medida
    if distancia_actual < 10:
        print("proximitat extrema")
        led_rojo.encendre()
        led_amarillo.apagar()
    elif (10 <= distancia_actual <= 20):
        print("proximitat moderada")
        led_amarillo.encendre()
        led_rojo.apagar()
    else:
        print("fora de perill")
        led_amarillo.apagar()
        led_rojo.apagar()

# Configurar la interrupción en el `ECHO_PIN` para que se dispare cuando regrese el pulso
GPIO.add_event_detect(sensor_dist.echo_pin, GPIO.FALLING, callback=alerta_leds, bouncetime=50)

try:
    while True:
        distancia_actual = sensor_dist.mesura_distancia()
        time.sleep(1)
except KeyboardInterrupt: print("Programa interromput per l'usuari")
finally:
    GPIO.cleanup()
    print("GPIO limpiado y programa finalizado")