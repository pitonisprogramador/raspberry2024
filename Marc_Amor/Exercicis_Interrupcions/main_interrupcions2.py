from Active_Buzzer_classe import *
from distancia_classe import *

def activar_buzzer(channel):
    dist = distancia.mesura_distancia()
    if dist < 15:
        buzzer.encendre()
    else:
        buzzer.apagar()

if __name__ == "__main__":
    distancia = SensorDistancia(trigger_pin = 23, echo_pin = 24)
    buzzer = Buzzer(buzzer_pin = 18)
    
    GPIO.add_event_detect(distancia.echo_pin, GPIO.BOTH, callback=activar_buzzer)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Programa finalitzat")
    finally:
        GPIO.cleanup()