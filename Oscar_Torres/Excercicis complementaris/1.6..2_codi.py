"""Exercici 6: Indicador de Distància amb Multiprocessing (Múltiples Processos)
Utilitzar tres processos paral·lels per controlar tres LEDs diferents, cadascun associat a un
interval de distància diferent (0-10 cm, 10-20 cm i més de 20 cm). Cada procés controla un
LED en funció d'un interval de distància específic, permetent que els LEDs s'encenguin i
s'apaguin independentment segons la distància de l'objecte detectat.
En aquest exemple usarem 4 processos y compartirem dist_actual entre ells com un objecte Value"""

import RPi.GPIO as GPIO
import time
from multiprocessing import Process, Value
from llibreries_dispositius.led_classe import LED
from llibreries_dispositius.distancia_classe import SensorDistancia

# Configurar el modo de numeración de pines
GPIO.setmode(GPIO.BCM)

echo_pin, trigger_pin = 24, 23
sensor_dist = SensorDistancia(trigger_pin, echo_pin)
led_verde = LED(17)
led_amarillo = LED(27)
led_rojo = LED(22)
leds_dic = {17: led_verde, 27: led_amarillo, 22: led_rojo}

def bucle_distancia(dist_actual):
    while True:
        dist_actual.value = sensor_dist.mesura_distancia()
        time.sleep(0.5)
        
def control_led(led_num, min_dist, max_dist, dist_actual):
    while True:
        led = leds_dic[led_num]
        if (min_dist <= dist_actual.value < max_dist):
            led.encendre()
            #print("distancia: ", dist_actual.value, "/nled num:", led_num)
        else:
            led.apagar()
        
try:
    #creem una objecte Value per compartir la distancia entre els processos
    dist_actual = Value('f', 101)  # Valor float compartido inicial superio a la maxima distancia que enciende leds
    # Creació de tres processos, un per a cada LED
    processes = [
        Process(target=control_led, args=(led_verde.pin, 0, 10, dist_actual)),
        Process(target=control_led, args=(led_amarillo.pin, 10, 20, dist_actual)),
        Process(target=control_led, args=(led_rojo.pin, 20, 100, dist_actual)),
        Process(target=bucle_distancia, args=(dist_actual,))
        ]
    for p in processes: p.start()
    for p in processes: p.join()
except KeyboardInterrupt: print("Programa finalitzat per l'usuari")
finally: GPIO.cleanup()