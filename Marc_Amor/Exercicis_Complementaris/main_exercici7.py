from distancia_classe import *
from led_classe import *
import threading

distancia_lock = threading.Lock()

def red_alert():
    while True:
        with distancia_lock:
            dist = distancia.mesura_distancia()
        
        if dist < 5:
            red_led.encendre()
        else:
            red_led.apagar()
        time.sleep(0.5)

def green_alert():
    while True:
        with distancia_lock:
            dist = distancia.mesura_distancia()

        if 5 <= dist < 15:
            green_led.encendre()
        else:
            green_led.apagar()
        time.sleep(0.5)

try:
    distancia = SensorDistancia(trigger_pin = 23, echo_pin = 24)
    red_led = LED(pin = 17)
    green_led = LED(pin = 27)

    red_thread = threading.Thread(target=red_alert)
    green_thread = threading.Thread(target=green_alert)
    
    red_thread.start()
    green_thread.start()

    red_thread.join()
    green_thread.join()

except KeyboardInterrupt:
    GPIO.cleanup()
