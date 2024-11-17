# 12: Control d'un LED amb un sensor PIR usant interrupcions 
# Enunciat: Configura un sistema on un LED s'encengui cada vegada que es 
# detecti moviment amb un sensor PIR. Quan el PIR detecti moviment, el LED 
# s'activarà automàticament durant uns segons i després s'apagarà. Utilitza una 
# interrupció configurada per una pujada de senyal que permeti controlar 
# l'activació del LED en funció del senyal del PIR. 

import RPi.GPIO as GPIO 
import time 
PIR_PIN = 23 
LED_PIN = 17 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(PIR_PIN, GPIO.IN) 
GPIO.setup(LED_PIN, GPIO.OUT) 
def encendre_led(channel): 
GPIO.output(LED_PIN, True) 
time.sleep(2)  # LED encès per 2 segons 
GPIO.output(LED_PIN, False) 
GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=encendre_led) 
try: 
while True: 
time.sleep(1)  # Manté el programa actiu 
except KeyboardInterrupt: 
print("Programa finalitzat") 
finally: 
GPIO.cleanup()