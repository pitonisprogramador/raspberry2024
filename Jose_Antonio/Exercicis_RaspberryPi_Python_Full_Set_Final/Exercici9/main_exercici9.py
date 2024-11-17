from pir_classe import *
from led_classe import *
from Active_Buzzer_classe import *

def alert_with_time_slicing():
    while True:
        if pir.detecta_moviment():
            led.encendre()
            buzzer.encendre()
            time.sleep(0.5)
            led.apagar()
            buzzer.apagar()
            time.sleep(0.5)
        else:
            led.apagar()
            buzzer.apagar()
            time.sleep(0.5)

try:
    pir = SensorPIR(pir_pin = 4)
    led = LED(pin = 17)
    buzzer = Buzzer(buzzer_pin = 18)

    alert_with_time_slicing()

except KeyboardInterrupt:
    GPIO.cleanup()