# 6 Sistema de Distància amb Indicador LED (Sense PWM) 
# Utilitzar el sensor HC-SR04 per mesurar la proximitat d'un objecte i encendre un LED quan 
# aquest es trobi a menys de 15 cm. Si l'objecte és més lluny, el LED s'apaga. 
# Solució en codi: 
# Solució en codi Python 
import RPi.GPIO as GPIO 
import time 
 
GPIO.setmode(GPIO.BCM)

LED_PIN = 17 
TRIG = 23 
ECHO = 24 
 
GPIO.setup(TRIG, GPIO.OUT) 
GPIO.setup(ECHO, GPIO.IN) 
GPIO.setup(LED_PIN, GPIO.OUT) 
 
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
        if dist < 15: 
            GPIO.output(LED_PIN, True) 
        else: 
            GPIO.output(LED_PIN, False) 
        time.sleep(0.5)
        
except KeyboardInterrupt: 
    GPIO.cleanup()