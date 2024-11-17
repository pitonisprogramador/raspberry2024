'''
Definimos la clase `MotorDC`.
Utilizamos 2 motores con un único driver L293D.
'''

import time
import RPi.GPIO as GPIO
from multiprocessing import Process

# Motor 1
IN1 = (26, 19)      # Board 37, 35
EN1 = 13            # Board 33 (Enable)

# Motor 2
IN2 = (24, 25)      # Board 18, 22
EN2 = 12            # Board 32 (Enable)

class MotorDC():
    def __init__(self, input, enable):
        '''
        input: (IN1, IN2) pines de control de sentido de giro.
        enable: pin de activación.
        '''
        GPIO.setmode(GPIO.BCM)
        GPIO.setup([input[0], input[1], enable], GPIO.OUT)
        self.input = input
        self.enable = enable
        # Por defecto, el motor está apagado
        GPIO.output(self.enable, GPIO.LOW)
           
    def forward(self):
        '''
        Gira el motor en sentido horario.
        '''
        GPIO.output(self.input[0], GPIO.LOW)
        GPIO.output(self.input[1], GPIO.HIGH)
        GPIO.output(self.enable, GPIO.HIGH)
    
    def backward(self):
        '''
        Gira el motor en sentido antihorario.
        '''
        GPIO.output(self.input[0], GPIO.HIGH)
        GPIO.output(self.input[1], GPIO.LOW)
        GPIO.output(self.enable, GPIO.HIGH)
    
    def stop(self):
        '''
        Detiene el motor.
        '''
        GPIO.output(self.enable, GPIO.LOW)

motor1 = MotorDC(IN1, EN1)
motor2 = MotorDC(IN2, EN2)

def peripheral_loop(motor):
    while True:
        print("Motor girando hacia adelante.")
        motor.forward()
        time.sleep(3)
        
        print("Deteniendo motor.")
        motor.stop()
        time.sleep(2)
        
        print("Motor girando hacia atrás.")
        motor.backward()
        time.sleep(3)
        
        print("Deteniendo motor.")
        motor.stop()
        time.sleep(2)

def main():
    try:
        processes = [
            Process(target=peripheral_loop, args=(motor1,)),
            Process(target=peripheral_loop, args=(motor2,))
        ]
        for p in processes:
            p.start()
        for p in processes:
            p.join()
    except KeyboardInterrupt:
        print("Saliendo...")
        for p in processes:
            p.terminate()
        for p in processes:
            p.join()
        GPIO.cleanup()

# Command line execution
if __name__ == '__main__':
    main()

'''
Definimos la clase `MotorDC`.
Utilizamos 2 motores con un único driver L293D.


import time
import RPi.GPIO as GPIO
from multiprocessing import Process

# Motor 1
IN1 = (26, 19)      # Board 37, 35
EN1 = 13            # Board 33 (PWM)

# Motor 2
IN2 = (24, 25)        # Board 18, 22
EN2 = 12              # Board 32

class MotorDC():
    def __init__(self, input, enable):
        
        input: (IN1, IN2) pines de control de sentido de giro.
        enable: pin de activación.
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup([input[0], input[1], enable], GPIO.OUT)
        self.input = input
        self.enable = enable
        self.speed = GPIO.PWM(enable, 1000)
        self.speed.start(0)
           
    def on(self, speed):
        
        Gira el motor en sentido horario.
        speed: (-100..100) velocidad.
        
        if 0 <= speed <= 100:                           # Girar derecha
            GPIO.output(self.input[0], GPIO.LOW)
            GPIO.output(self.input[1], GPIO.HIGH)
            # GPIO.output(self.enable, GPIO.HIGH)
            self.speed.ChangeDutyCycle(speed)
        elif -100 <= speed < 0:                         # Girar izquierda
            GPIO.output(self.input[0], GPIO.HIGH)
            GPIO.output(self.input[1], GPIO.LOW)
            # GPIO.output(self.enable, GPIO.HIGH)
            self.speed.ChangeDutyCycle(-speed)
    
    def off(self):
        
        Apaga el motor.
        
        GPIO.output(self.input[0], GPIO.LOW)
        GPIO.output(self.input[1], GPIO.LOW)
        # GPIO.output(self.enable, GPIO.LOW)
        self.speed.ChangeDutyCycle(0)
    
motor1 = MotorDC(IN1, EN1)
motor2 = MotorDC(IN2, EN2)

def peripheral_loop(motor):
    while True:
        for speed in range(-100, -51):
            motor.on(speed)
            time.sleep(.5)
        motor.off()
        time.sleep(5)
        for speed in range(50, 101):
            motor.on(-speed)
            time.sleep(.5)
        motor.off()
        time.sleep(5)

def main():
    try:
        processes = [
            Process(target=peripheral_loop, args=(motor1,)),
            Process(target=peripheral_loop, args=(motor2,))
        ]
        for p in processes:
            p.start()
        for p in processes:
            p.join()
    except KeyboardInterrupt:
        for p in processes:
            p.terminate()
        for p in processes:
            p.join()
        GPIO.cleanup()

# Command line execution
if __name__ == '__main__':
    main()
'''