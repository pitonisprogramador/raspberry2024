from distancia_classe import *
from pir_classe import *
from led_classe import *
from Active_Buzzer_classe import *
import threading

lock = threading.Lock()

def proximity_alert():
    while True:
        dist = distancia.mesura_distancia()
        with lock:
            if dist < 5:
                led.encendre()
                buzzer.encendre()
            else:
                led.apagar()
                buzzer.apagar()
            time.sleep(0.5)

def movement_alert():
    while True:
        if pir.detecta_moviment():
            with lock:
                led.encendre()
                time.sleep(1)
        else:
            with lock:            
                led.apagar()
        time.sleep(0.5)

try:
    pir = SensorPIR(pir_pin = 4)
    distancia = SensorDistancia(trigger_pin = 23, echo_pin = 24)
    led = LED(pin = 17)
    buzzer = Buzzer(buzzer_pin = 18)

    proximity_thread = threading.Thread(target=proximity_alert)
    movement_thread = threading.Thread(target=movement_alert)

    proximity_thread.start()
    movement_thread.start()

    proximity_thread.join()
    movement_thread.join()

except KeyboardInterrupt:
    GPIO.cleanup()