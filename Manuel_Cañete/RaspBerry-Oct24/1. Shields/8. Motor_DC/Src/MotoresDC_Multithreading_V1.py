'''
Utilizamos 2 motores con un único driver L293D
Definimos la clase MotorDC 
Añadimos PWM para control de la velocidad del motor (velocidad: -100..100)
Simplificamos la clase con un único método para arrancar, que requiere velocidad y dirección de giro
Añadimos multithreading para que cada motor sea gestionado por un thread separado
'''

import time
from threading import Thread
import RPi.GPIO as GPIO


class MotorDC():
    def __init__(self, input, enable):
        '''
        Inicializa clase MotorDC
            input: (IN1, IN2) pines de control de sentido de giro
            enable: pin de activación
        '''
        GPIO.setmode(GPIO.BCM)
        GPIO.setup([input[0], input[1], enable], GPIO.OUT)
        self.input = input
        self.enable = enable
        self.pwm = GPIO.PWM(enable, 100)            # Comprobado que funciona mejor con frecuencias bajas (aprox 100 Hz.)
        self.pwm.start(0)

           
    def on(self, speed):
        '''
        Gira motor sentido horario
            speed: (-100..100) velocidad 
        '''
        if 0 <= speed <= 100:                           # Girar derecha
            GPIO.output(self.input[0], GPIO.LOW)
            GPIO.output(self.input[1], GPIO.HIGH)
            # GPIO.output(self.enable, GPIO.HIGH)
            self.pwm.ChangeDutyCycle(speed)
        elif -100 <= speed < 0:                         # Girar izquierda
            GPIO.output(self.input[0], GPIO.HIGH)
            GPIO.output(self.input[1], GPIO.LOW)
            # GPIO.output(self.enable, GPIO.HIGH)
            self.pwm.ChangeDutyCycle(-speed)
    
    def off(self):
        '''
        Apagar motor
        '''
        GPIO.output(self.input[0], GPIO.LOW)
        GPIO.output(self.input[1], GPIO.LOW)
        # GPIO.output(self.enable, GPIO.LOW)
        self.pwm.ChangeDutyCycle(0)
    

def loop_motor(motor, loop):
    '''
    Ciclo principal del motor
    Entradas: 
        motor: variable tipo MotorDC
    '''
    for l in loop:
        motor.on(l[0])
        time.sleep(l[1])

    for l in reversed(loop):
        motor.on(l[0])
        time.sleep(l[1])

    motor.off()

       

# Motor 1
IN1 = (26, 19)      # Board 37, 35
EN1 = 13            # Board 33 (PWM)
motor1 = MotorDC(IN1, EN1)
# motor1 = MotorDC(IN1, EN1)
loop_motor1 = [(30, 5), (50, 3), (60, 2), (80, 5), (95, 3), (100, 0)]

# Motor 2
IN2 = (25, 24)        # Board 22, 18
EN2 = 12              # Board 32
motor2 = MotorDC(IN2, EN2)
loop_motor2 = [(-30, 5), (-40, 3), (-60, 6), (-100, 5)]


# Main function (MULTITHREADING)
def main():
    try:
        lista_threads = [
            Thread(target=loop_motor, args=(motor1, loop_motor1)),
            Thread(target=loop_motor, args=(motor2, loop_motor2)),
        ]
        for thread in lista_threads:
            thread.start()

        for thread in lista_threads:
            thread.join()

    except KeyboardInterrupt:
        print("\nParando motores...")

        for thread in lista_threads:
            thread.terminate()

        for thread in lista_threads:
            thread.join()

    finally:
        GPIO.cleanup()
        print("\nThat's all Folks!")



# Command line execution
if __name__ == '__main__':
    main()

