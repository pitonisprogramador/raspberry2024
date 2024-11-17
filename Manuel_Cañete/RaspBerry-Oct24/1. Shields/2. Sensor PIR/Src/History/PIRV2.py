import RPi.GPIO as GPIO
import time

pinpir = 23
pinled = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinpir, GPIO.IN)
GPIO.setup(pinled, GPIO.OUT)

def intruso_detectado(channel):
    print("Alerta Intruso")
    GPIO.output(pinled, 1)
    time.sleep(0.5)
    GPIO.output(pinled, 0)


GPIO.add_event_detect(pinpir, GPIO.RISING, callback=intruso_detectado)

try:
    
    while True:
        time.sleep(1)  

except KeyboardInterrupt:
    print("Detenido por el usuario")

finally:
    GPIO.cleanup()
'''
apt install python3-rpi-lgpio
Ha calgut aquest comandament per utilitzar aquest codi d'interrupcions
Aquest codi l'hem provat per canviar el paradigma
while True:
    if GPIO.input(pirpin) == 1:
        print("Alerta intrusos")
    time.sleep(1)        
'''     