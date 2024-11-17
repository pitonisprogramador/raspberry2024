import RPi.GPIO as GPIO
import time
IN1 = 4
IN2 = 17
EN1 = 18
PAUSA = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup([IN1,IN2,EN1], GPIO.OUT)
forward=GPIO.PWM(IN1,100) # configuring IN1 for PWM freq 100 Hz
reverse=GPIO.PWM(IN2,100) # configuring IN2 for PWM  freq 100 Hz
forward.start(0) 
reverse.start(0)

def antihorari():
    ''' EN1 empieza a HIGH el IN2 permanece low y IN1 pasa de duty 0% a 100%'''
    GPIO.output(EN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    for duty in range(0,101,1):  
        forward.ChangeDutyCycle(duty)
        time.sleep(0.1)
    GPIO.output(EN1,GPIO.LOW)

def horari():
    ''' EN1 empieza a HIGH el IN1 permanece low y IN2 pasa de duty 0% a 100%'''
    GPIO.output(EN1,GPIO.HIGH)
    GPIO.output(IN1,GPIO.LOW)
    for duty in range(0,101,1):
        reverse.ChangeDutyCycle(duty)
        time.sleep(0.1)
    GPIO.output(EN1,GPIO.LOW)

def peripheral_setup () :
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup([IN1, IN2, EN1], GPIO.OUT)

def peripheral_loop () :
    antihorari()
    time.sleep(PAUSA)
    horari()
    time.sleep(PAUSA)

def main () :
    peripheral_setup()
    while 1 :
        peripheral_loop()
if __name__ == '__main__' :
    main()