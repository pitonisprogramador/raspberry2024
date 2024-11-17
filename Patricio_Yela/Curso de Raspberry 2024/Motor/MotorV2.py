import RPi.GPIO as GPIO
import time

class MotorControl:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup([ENA, IN1, IN2, LEDD, LEDI], GPIO.OUT)

    def gderecha(self, t):
        GPIO.output(ENA, GPIO.HIGH)
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(LEDD, GPIO.HIGH)
        GPIO.output(LEDI, GPIO.LOW)
        time.sleep(t)

    def parar(self, t):
        GPIO.output(ENA, GPIO.LOW)
        GPIO.output(LEDD, GPIO.LOW)
        GPIO.output(LEDI, GPIO.LOW)
        time.sleep(t)

    def gizquierda(self, t):
        GPIO.output(ENA, GPIO.HIGH)
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(LEDD, GPIO.LOW)
        GPIO.output(LEDI, GPIO.HIGH)
        time.sleep(t)

    def loop(self):
        self.gderecha(5)
        self.parar(3)
        self.gizquierda(5)
        self.parar(3)

IN1 = 17
IN2 = 27
ENA = 18
LEDD = 4
LEDI = 23

    
def main():
    motor = MotorControl()
    while True:
       motor.loop()

try:
    main()

except KeyboardInterrupt:
    GPIO.cleanup()
