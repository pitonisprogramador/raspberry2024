from led_classe import *
from pir_classe import *

def encendre_led(channel):
    led.encendre()
    time.sleep(2) # LED encès per 2 segons
    led.apagar()

if __name__ == "__main__":
    led = LED(pin = 17)
    pir = SensorPIR(pir_pin = 23)

    GPIO.add_event_detect(pir.pir_pin, GPIO.RISING, callback=encendre_led)

    try:
        while True:
            time.sleep(1) # Manté el programa actiu
    except KeyboardInterrupt:
        print("Programa finalitzat")
    finally:
        GPIO.cleanup()