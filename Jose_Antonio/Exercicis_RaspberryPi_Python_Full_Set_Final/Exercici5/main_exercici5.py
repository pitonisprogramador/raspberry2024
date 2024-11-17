from distancia_classe import *
from led_classe import *

if __name__ == "__main__":
    distancia = SensorDistancia(trigger_pin = 23, echo_pin = 24)
    leds = [LED(pin = 17), LED(pin = 27), LED(pin = 22), LED(pin = 18)]

    try:
        while True:
            dist = distancia.mesura_distancia()
            if dist < 5:
                for led in leds:
                    led.encendre()
                    time.sleep(0.1)
                    led.apagar()
            time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()