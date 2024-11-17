from distancia_classe import *
from pir_classe import *
from Active_Buzzer_classe import *
import threading

def pir_alarm():
    while True:
        if pir.detecta_moviment():
            dist = distancia.mesura_distancia()
            if dist < 5:
                buzzer.encendre()
            else:
                buzzer.apagar()
        else:
            buzzer.apagar()
        time.sleep(0.1)

try:
    pir = SensorPIR(pir_pin = 4)
    distancia = SensorDistancia(trigger_pin = 23, echo_pin = 24)
    buzzer = Buzzer(buzzer_pin = 18)

    alarm_thread = threading.Thread(target=pir_alarm)
    alarm_thread.start()
    alarm_thread.join()
except KeyboardInterrupt:
    GPIO.cleanup()