import RPi.GPIO as GPIO
import time

IN1 = 17
IN2 = 27
ENA = 18
LEDD = 4
LEDI = 23

def gderecha(t):
   GPIO.output(ENA,GPIO.HIGH)
   GPIO.output(IN1,GPIO.LOW) 
   GPIO.output(IN2,GPIO.HIGH) 
   GPIO.output(LEDD,GPIO.HIGH)
   GPIO.output(LEDI,GPIO.LOW)
   time.sleep(t)


def parar(t):
    GPIO.output(ENA,GPIO.LOW)
    GPIO.output(LEDD,GPIO.LOW)
    GPIO.output(LEDI,GPIO.LOW)
    time.sleep(t)


def gizquierda(t):
    GPIO.output(ENA,GPIO.HIGH)
    GPIO.output(IN1,GPIO.HIGH) 
    GPIO.output(IN2,GPIO.LOW) 
    GPIO.output(LEDD,GPIO.LOW)
    GPIO.output(LEDI,GPIO.HIGH)
    
    time.sleep(t)


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([ENA,IN1,IN2,LEDD,LEDI], GPIO.OUT)


def loop():
    gderecha(5)
    parar(3)
    gizquierda(5)
    parar(3)
    
def main():
    setup()
    while True:
       loop()

try:
    main()

except KeyboardInterrupt:
    GPIO.cleanup()
