# 4 Alarma de Proximitat amb LED i So 
# Encendre un LED i activar un so d'alarma quan un objecte és a menys de 5 cm de distància. 
# Solució en codi: 
# Solució en codi Python 
import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BCM)

LED_PIN = 17 
BUZZER_PIN = 18 
TRIG = 23 
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT) 
GPIO.setup(ECHO, GPIO.IN) 
GPIO.setup(LED_PIN, GPIO.OUT) 
GPIO.setup(BUZZER_PIN, GPIO.OUT)

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
            GPIO.output(LED_PIN, True) 
            GPIO.output(BUZZER_PIN, True) 
        else: 
            GPIO.output(LED_PIN, False) 
            GPIO.output(BUZZER_PIN, False) 
        time.sleep(0.5)
        
except KeyboardInterrupt: 
    GPIO.cleanup()