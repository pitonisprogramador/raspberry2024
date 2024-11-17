# 7: Sistema d'Alertes amb Threading (Múltiples Fils) 
# Crear un sistema d'alerta on es monitoritzen dos intervals de distància amb dos fils.
# Cada interval actua com una alerta independent: el primer fil activa un LED vermell per 
# proximitats extremes, i el segon fil activa un LED groc per distàncies moderades. 
# Solució en codi: 
# Solució en codi Python 
import RPi.GPIO as GPIO 
import time 
import threading 
 
# Configuració de GPIO 
GPIO.setmode(GPIO.BCM) 
RED_LED_PIN = 17 
YELLOW_LED_PIN = 27 
TRIG = 23 
ECHO = 24 
 
GPIO.setup(TRIG, GPIO.OUT) 
GPIO.setup(ECHO, GPIO.IN) 
GPIO.setup(RED_LED_PIN, GPIO.OUT) 
GPIO.setup(YELLOW_LED_PIN, GPIO.OUT) 
 
def distance(): 
    GPIO.output(TRIG, True) 
    time.sleep(0.00001) 
    GPIO.output(TRIG, False) 
    start, stop = time.time(), time.time() 
 
    while GPIO.input(ECHO) == 0: 
        start = time.time() 
    while GPIO.input(ECHO) == 1: 
        stop = time.time() 
 
    return (stop - start) * 34300 / 2  # Distància en cm 
 
def red_alert(): 
    while True: 
        dist = distance() 
        GPIO.output(RED_LED_PIN, dist < 5)  # Activa el LED vermell si està a menys de 5 cm 
        time.sleep(0.5) 
 
def yellow_alert(): 
    while True: 
        dist = distance() 
        GPIO.output(YELLOW_LED_PIN, 5 <= dist < 15)  # Activa el LED groc si està entre 5 i 15 cm 
        time.sleep(0.5) 
 
try: 
    # Creació de dos fils per a les alertes 
    red_thread = threading.Thread(target=red_alert) 
    yellow_thread = threading.Thread(target=yellow_alert) 
 
    red_thread.start() 
    yellow_thread.start() 
 
    red_thread.join() 
    yellow_thread.join() 
 
except KeyboardInterrupt: 
    GPIO.cleanup()