# 14: Control de dos LEDs amb intervals de distància 
# Enunciat: Dissenya un sistema amb dos LEDs que reaccionen a diferents 
# intervals de distància. El primer LED s'encendrà quan la distància sigui inferior a 
# 10 cm, indicant proximitat extrema, mentre que el segon LED s'encendrà quan 
# la distància estigui entre 10 cm i 20 cm, indicant una proximitat moderada. 
# Utilitza interrupcions per activar i desactivar els LEDs segons aquests intervals 
# de distància. 

import RPi.GPIO as GPIO 
import time 
TRIG = 23 
ECHO = 24 
RED_LED_PIN = 17 
YELLOW_LED_PIN = 27 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(TRIG, GPIO.OUT) 
GPIO.setup(ECHO, GPIO.IN) 
GPIO.setup(RED_LED_PIN, GPIO.OUT) 
GPIO.setup(YELLOW_LED_PIN, GPIO.OUT) 
def mesurar_distancia(): 
GPIO.output(TRIG, True) 
time.sleep(0.00001) 
    GPIO.output(TRIG, False) 
 
    while GPIO.input(ECHO) == 0: 
        start_time = time.time() 
    while GPIO.input(ECHO) == 1: 
        end_time = time.time() 
 
    duration = end_time - start_time 
    distance = (duration * 34300) / 2 
    return distance 
 
def controlar_leds(channel): 
    distancia = mesurar_distancia() 
    if distancia < 10: 
        GPIO.output(RED_LED_PIN, True) 
        GPIO.output(YELLOW_LED_PIN, False) 
    elif 10 <= distancia <= 20: 
        GPIO.output(RED_LED_PIN, False) 
        GPIO.output(YELLOW_LED_PIN, True) 
    else: 
        GPIO.output(RED_LED_PIN, False) 
        GPIO.output(YELLOW_LED_PIN, False) 
 
GPIO.add_event_detect(ECHO, GPIO.BOTH, callback=controlar_leds) 
 
try: 
    while True: 
        time.sleep(1) 
except KeyboardInterrupt: 
    print("Programa finalitzat") 
finally: 
    GPIO.cleanup() 