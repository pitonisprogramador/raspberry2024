from distancia_classe import *
from led_classe import *

if __name__ == "__main__":
    distancia = SensorDistancia(trigger_pin = 23, echo_pin = 24)
    green_led = LED(pin = 27)
    red_led = LED(pin = 17)

    try:
        while True:
            dist = distancia.mesura_distancia()
            if dist < 15:
                red_led.encendre()
                green_led.apagar()

            else:
                red_led.apagar()
                green_led.encendre()
            time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()