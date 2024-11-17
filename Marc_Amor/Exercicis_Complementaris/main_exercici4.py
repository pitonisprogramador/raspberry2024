from distancia_classe import *
from led_classe import *
from Active_Buzzer_classe import *

if __name__ == "__main__":
    distancia = SensorDistancia(trigger_pin = 23, echo_pin = 24)
    led = LED(pin = 17)
    buzzer = Buzzer(buzzer_pin = 18)

    try:
        while True:
            dist = distancia.mesura_distancia()
            if dist < 5:
                led.encendre()
                buzzer.encendre()

            else:
                led.apagar()
                buzzer.apagar()
            time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()