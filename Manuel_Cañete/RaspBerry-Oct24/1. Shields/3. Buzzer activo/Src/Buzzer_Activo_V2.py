import RPi.GPIO as GPIO
import time

pinbuzzer = 18
lista_buzzer = [.2, .3, .5, .1, .0, .1, .9, 1.1, 0.3, .1, .2]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinbuzzer, GPIO.OUT)

try:
    i = 0
    while True:
        for i in range(1, 20, 1):
            GPIO.output(pinbuzzer, GPIO.HIGH)
            time.sleep(i/10)
            GPIO.output(pinbuzzer, GPIO.LOW)
            time.sleep(i/10)

except KeyboardInterrupt:
    GPIO.cleanup()
