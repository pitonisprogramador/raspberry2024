import RPi.GPIO as GPIO
import time

IN1 = 17
IN2 = 27
ENA1 = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup([IN1, IN2, ENA1], GPIO.OUT)


try:
    while True:
        GPIO.output(ENA1, GPIO.HIGH)
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)

        time.sleep(5)

        GPIO.output(ENA1, GPIO.LOW)
        GPIO.output(IN1, GPIO.LOW)
        
        time.sleep(5)
        
        GPIO.output(ENA1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN1, GPIO.LOW)
        
        time.sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()
