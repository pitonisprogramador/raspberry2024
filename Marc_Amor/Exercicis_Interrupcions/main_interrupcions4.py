from led_classe import *
from pir_classe import *
from Active_Buzzer_classe import *

def alarma_seqüencial(channel):
    buzzer.encendre()
    time.sleep(1)
    buzzer.apagar()

    led.encendre()
    time.sleep(2)
    led.apagar()

if __name__ == "__main__":
    led = LED(pin = 17)
    pir = SensorPIR(pir_pin = 23)
    buzzer = Buzzer(buzzer_pin = 18)

    GPIO.add_event_detect(pir.pir_pin, GPIO.RISING, callback=alarma_seqüencial)
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Programa finalitzat")
    finally:
        GPIO.cleanup()