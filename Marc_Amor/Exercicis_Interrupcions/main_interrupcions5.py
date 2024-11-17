from distancia_classe import *
from led_classe import *
from Active_Buzzer_classe import *

def alerta_buzzer_leds(channel):
    dist = distancia.mesura_distancia()
    if dist < 10:
        buzzer.encendre()
        green_led.encendre()
        blue_led.apagar() 
    elif dist > 20:
        buzzer.apagar()
        green_led.apagar()
        blue_led.encendre()
    else:
        buzzer.apagar()
        green_led.apagar()
        blue_led.apagar()

if __name__ == "__main__":
    distancia = SensorDistancia(trigger_pin = 23, echo_pin = 24)
    green_led = LED(pin = 17)
    blue_led = LED(pin = 27)    
    buzzer = Buzzer(buzzer_pin = 18)

    GPIO.add_event_detect(distancia.echo_pin, GPIO.BOTH, callback=alerta_buzzer_leds)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Programa finalitzat")
    finally:
        GPIO.cleanup()