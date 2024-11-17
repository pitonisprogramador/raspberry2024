# 11 Sistema d’Alarma Completa amb PIR, Buzzer i LEDs (Amb Threading) 
# Crear una alarma completa que inclogui el sensor PIR, el sensor ultrasònic, diversos LEDs i 
# un brunzidor per senyalitzar la proximitat i el moviment en paral·lel utilitzant *threading*. 
# Solució en codi: 
# Solució en codi Python 
import RPi.GPIO as GPIO 
import time 
import threading 
 
GPIO.setmode(GPIO.BCM) 
PIR_PIN = 4 
TRIG = 23 
ECHO = 24 
LED_PIN = 17 
BUZZER_PIN = 18 
 
GPIO.setup(TRIG, GPIO.OUT) 
GPIO.setup(ECHO, GPIO.IN) 
GPIO.setup(PIR_PIN, GPIO.IN) 
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
 
def proximity_alert(): 
    while True: 
        dist = distance() 
        if dist < 5: 
            GPIO.output(LED_PIN, True) 
            GPIO.output(BUZZER_PIN, True) 
        else: 
            GPIO.output(LED_PIN, False) 
            GPIO.output(BUZZER_PIN, False) 
        time.sleep(0.5) 
 
def movement_alert(): 
    while True: 
        if GPIO.input(PIR_PIN): 
            GPIO.output(LED_PIN, True) 
            time.sleep(1) 
        else: 
            GPIO.output(LED_PIN, False) 
        time.sleep(0.5) 
 
try: 
    proximity_thread = threading.Thread(target=proximity_alert) 
    movement_thread = threading.Thread(target=movement_alert) 
 
    proximity_thread.start() 
    movement_thread.start() 
    proximity_thread.join() 
    movement_thread.join()

except KeyboardInterrupt: 
GPIO.cleanup()