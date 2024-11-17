# 5 Patró de Senyalització Seqüencial amb LEDs 
# Crear un patró seqüencial d'encesa de quatre LEDs en funció de la proximitat de l'objecte 
# detectat. 
# Solució en codi: 
# Solució en codi Python 
import RPi.GPIO as GPIO 
import time 
 
GPIO.setmode(GPIO.BCM) 
LED_PINS = [17, 27, 22, 5] 
TRIG = 23 
ECHO = 24 
 
GPIO.setup(TRIG, GPIO.OUT) 
GPIO.setup(ECHO, GPIO.IN) 
for pin in LED_PINS: 
    GPIO.setup(pin, GPIO.OUT) 
 
def distance(): 
    GPIO.output(TRIG, True) 
    time.sleep(0.00001) 
    GPIO.output(TRIG, False) 
    start, stop = time.time(), time.time() 
     
    while GPIO.input(ECHO) == 0: 
        start = time.time() 
    while GPIO.input(ECHO) == 1: 
        stop = time.time() 
 
    return (stop - start) * 34300 / 2 
 
try: 
    while True: 
        dist = distance() 
        if dist < 5: 
            for pin in LED_PINS: 
                GPIO.output(pin, True) 
                time.sleep(0.1) 
                GPIO.output(pin, False) 
        time.sleep(0.5) 

except KeyboardInterrupt: 
    GPIO.cleanup() 