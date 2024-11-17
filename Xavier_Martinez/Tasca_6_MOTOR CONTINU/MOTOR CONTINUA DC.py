import RPi.GPIO as GPIO
import time

ENA = 4

IN1 = 17

IN2 = 18

def giro_derecha(t):
   GPIO.output(ENA,GPIO.HIGH)
   GPIO.output(IN1,GPIO.LOW) 
   GPIO.output(IN2,GPIO.HIGH) 
   time.sleep(t)


def parate(t):
    GPIO.output(ENA,GPIO.LOW)
    time.sleep(t)


def giro_izquierda(t):
    GPIO.output(ENA,GPIO.HIGH)
    GPIO.output(IN1,GPIO.HIGH) 
    GPIO.output(IN2,GPIO.LOW) 
    time.sleep(t)


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([ENA,IN1,IN2], GPIO.OUT)


def loop():
    giro_derecha(5)
    parate(2)
    giro_izquierda(5)
    parate(2)
    
def main():
    setup()
    while True:
       loop()

main()

