from led_classe import *
from distancia_classe import *

def controlar_leds(channel):
    dist = distancia.mesura_distancia()
    if dist < 10:
        red_led.encendre()
        yellow_led.apagar()
    elif 10 <= dist <= 20:
        red_led.apagar()
        yellow_led.encendre()
    else:
        red_led.apagar()
        yellow_led.apagar()        

if __name__ == "__main__":
    distancia = SensorDistancia(trigger_pin = 23, echo_pin = 24)
    red_led = LED(pin = 17)
    yellow_led = LED(pin = 27)
     
    GPIO.add_event_detect(distancia.echo_pin, GPIO.BOTH, callback=controlar_leds)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Programa finalitzat")
        GPIO.cleanup()