import RPi.GPIO as GPIO
import time
import random
DATA = 17

CLOCK = 4

LATCH = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup([DATA,LATCH,CLOCK ] , GPIO.OUT)
while True:
    bits = [random.randrange(0,2) for element in range(8)]
    for bit in bits:
        GPIO.output(DATA,bit)
        time.sleep(0.01)
        GPIO.output(CLOCK,1)
        time.sleep(0.01)
        GPIO.output(CLOCK,0)
    GPIO.output(LATCH,1)
    time.sleep(0.01)
    GPIO.output(LATCH,0) 
    time.sleep(1)