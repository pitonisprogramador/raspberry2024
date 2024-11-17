# 13: Activació d'un buzzer segons distància amb interrupcions 
# Enunciat: Crea un sistema d'alerta amb un sensor de distància i un buzzer. Quan 
# la distància sigui menor de 15 cm, el buzzer ha de sonar, i quan la distància 
# superi aquest valor, s'ha de silenciar. Utilitza una interrupció que s'activa quan 
# hi ha un canvi de distància per controlar l'activació del buzzer de manera 
# eficient i només quan cal. 

import RPi.GPIO as GPIO 
import time 
TRIG = 23 
ECHO = 24 
BUZZER_PIN = 18 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(TRIG, GPIO.OUT) 
GPIO.setup(ECHO, GPIO.IN) 
GPIO.setup(BUZZER_PIN, GPIO.OUT) 
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
def activar_buzzer(channel): 
distancia = mesurar_distancia() 
if distancia < 15: 
GPIO.output(BUZZER_PIN, True) 
else: 
GPIO.output(BUZZER_PIN, False) 
GPIO.add_event_detect(ECHO, GPIO.BOTH, callback=activar_buzzer) 
try: 
while True: 
time.sleep(1) 
except KeyboardInterrupt: 
print("Programa finalitzat") 
finally: 
GPIO.cleanup()