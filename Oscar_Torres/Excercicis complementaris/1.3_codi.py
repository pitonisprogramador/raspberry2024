"""Exercici 3: Indicador de Tres Zones amb Multiprocessing
Indicar tres intervals de distància amb tres LEDs diferents, on cada LED indica una zona de
proximitat."""

import RPi.GPIO as GPIO
import time
from llibreries_dispositius.led_classe import LED
from llibreries_dispositius.distancia_classe import SensorDistancia

# Configurar el modo de numeración de pines
GPIO.setmode(GPIO.BCM)

sensor_dist = SensorDistancia(trigger_pin=23, echo_pin=24)
led_verde = LED(17)
led_amarillo = LED(27)
led_rojo = LED(22)

def cambiar_leds(distancia_actual):
# Lógica de alerta según la distancia medida
    led_verde.apagar()
    led_amarillo.apagar()
    led_rojo.apagar()
    
    if distancia_actual < 10: led_rojo.encendre()
    elif distancia_actual > 20: led_verde.encendre()
    else: led_amarillo.encendre()

def check_distance():
    try:
    # Enviar un pulso de disparo cada segundo para medir la distancia
        while True:
            # Obtener la distancia actual usando la clase `SensorDistancia`
            distancia_actual = sensor_dist.mesura_distancia()
            cambiar_leds(distancia_actual)
            time.sleep(1)  # Espera de 1 segundo entre mediciones
    except KeyboardInterrupt: print("Programa finalitzat per l'usuari")
    finally:
        GPIO.cleanup()
        print("GPIO limpiado y programa finalizado")

if __name__ == '__main__':
    p = Process(target=check_distance)
    p.start()
    p.join()

    print("proceso acabado")

