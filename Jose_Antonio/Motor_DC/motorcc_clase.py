import RPi.GPIO as GPIO
import time

class MotorControl:
    def __init__(self, in1, in2, en1):
        self.IN1 = in1
        self.IN2 = in2
        self.EN1 = en1

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.EN1, GPIO.OUT)

    def motor_izquierda(self):
        GPIO.output(self.EN1, GPIO.HIGH)
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)

    def motor_derecha(self):
        GPIO.output(self.EN1, GPIO.HIGH)
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)

    def motor_paro(self):
        GPIO.output(self.EN1, GPIO.LOW)
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)

