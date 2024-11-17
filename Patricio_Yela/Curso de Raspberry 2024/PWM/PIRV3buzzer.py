import RPi.GPIO as GPIO
import time

pinpir = 23
pinled = 24
pinled2 = 25
pinled3 = 17
pinbuzzer = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinpir, GPIO.IN)
GPIO.setup(pinled, GPIO.OUT)
GPIO.setup(pinled2, GPIO.OUT)
GPIO.setup(pinled3, GPIO.OUT)
GPIO.setup(pinbuzzer, GPIO.OUT)


GPIO.output(pinled,0)
GPIO.output(pinled2,0)
GPIO.output(pinled3,0)


pwm = GPIO.PWM(pinbuzzer, 440) 
pwm.start(50) 


def intruso_detectado(channel):
    print("Alerta Intruso")
    GPIO.output(pinled, 1)
    GPIO.output(pinled2, 0)
    GPIO.output(pinled3, 1)
    time.sleep(1)
    GPIO.output(pinled, 0)
    GPIO.output(pinled2, 1)
    GPIO.output(pinled3, 0)
    
    pwm.ChangeFrequency(523) # Nota Do
    time.sleep(2)
    pwm.ChangeFrequency(587) # Nota Re  
    time.sleep(1)
    pwm.ChangeFrequency(659) # Nota Mi
    time.sleep(0.5)
    pwm.ChangeFrequency(698) # Nota Fa
    time.sleep(0.25)
    pwm.stop()



GPIO.add_event_detect(pinpir, GPIO.RISING, callback=intruso_detectado)

try:
    
    while True:
        time.sleep(1) 

except KeyboardInterrupt:
    print("Gracias por venir PY")

finally:
    GPIO.cleanup()
