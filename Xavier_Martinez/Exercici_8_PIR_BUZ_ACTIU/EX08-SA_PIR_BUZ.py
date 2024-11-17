# 8: Sistema d'Alerta amb PIR i Buzzer Actiu (Amb Threading) 
# Activar un brunzidor actiu com a alarma quan el sensor PIR detecti moviment
# a menys de 5 cm del sensor HC-SR04, gestionat amb *threading*. 
# Solució en codi: 
# Solució en codi Python 
import RPi.GPIO as GPIO 
import time 
import threading 
 
GPIO.setmode(GPIO.BCM) 
PIR_PIN = 4 
BUZZER_PIN = 18 
TRIG = 23 
ECHO = 24 
 
GPIO.setup(TRIG, GPIO.OUT) 
GPIO.setup(ECHO, GPIO.IN) 
GPIO.setup(PIR_PIN, GPIO.IN) 
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
 
def pir_alarm(): 
    while True: 
        if GPIO.input(PIR_PIN): 
            dist = distance() 
            if dist < 5: 
                GPIO.output(BUZZER_PIN, True) 
                time.sleep(1) 
            else: 
                GPIO.output(BUZZER_PIN, False) 
            time.sleep(0.1) 
 
try: 
    alarm_thread = threading.Thread(target=pir_alarm) 
    alarm_thread.start() 
    alarm_thread.join() 
 
except KeyboardInterrupt: 
    GPIO.cleanup()