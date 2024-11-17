'''
Utilizamos 2 motores con un único driver L293D
Definimos la clase MotorDC 
Añadimos PWM para control de la velocidad del motor (velocidad: -100..100)
Simplificamos la clase con un único método para arrancar, que requiere velocidad y dirección de giro
Añadimos multiprocessing para que cada motor sea gestionado por un proceso separado

&&&&&
&&&&&                NO FUNCIONA CON PROCESOS. EN CAMBIO HA FUNCIONADO CON THREADS        &&&&&
&&&&&

'''



import time
from multiprocessing import Process, Semaphore, Value
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
        self.pwm = GPIO.PWM(enable, 1000)
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
    

#sem = Semaphore(1)

def loop_motor(motor, loop):
    '''
    Ciclo principal del motor
    Entradas: 
        motor: variable tipo MotorDC
    '''
    # sem.acquire()
    for l in loop:
        print(f"\nMotor: {motor} - Loop: {l[0]}, {l[1]}")
        motor.on(l[0])
        time.sleep(l[1])
    motor.off()
    # sem.release()

       
    # for speed in range(-100, -51):
    #     motor1.on(speed)
    #     motor2.on(-speed)
    #     time.sleep(.5)

    # for speed in range(50, 101):
    #     motor1.on(speed)
    #     motor2.on(-speed)
    #     time.sleep(.5)


    # for speed in range(25, 101):
    #     motor1.on(-speed)
    #     motor2.on(speed)
    #     time.sleep(.5)
        
    # motor1.on_CW(50)
    # motor2.on_CCW(70)
    # time.sleep(6)
    # motor1.off()
    # time.sleep(3)
    # motor2.off()
    
    # motor1.on_CCW(30)
    # time.sleep(4)
    
    # motor2.on_CW(80)
    # time.sleep(8)
    
    # motor2.on_CCW(20)
    # time.sleep(4)
    # motor1.off()
    # time.sleep(3)


# Motor 1
IN1 = (26, 19)      # Board 37, 35
EN1 = 13            # Board 33 (PWM)
motor1 = MotorDC(IN1, EN1)
# motor1 = MotorDC(IN1, EN1)
loop_motor1 = [(40, 3), (60, 2), (80, 5), (95, 3)]

# Motor 2
IN2 = (24, 25)        # Board 18, 22
EN2 = 12              # Board 32
motor2 = MotorDC(IN2, EN2)
loop_motor2 = [(-40, 3), (-50, 6), (-100, 5)]


# Main function (MULTIPROCESO)
def main():
    try:
        lista_procesos = [
            Process(target=loop_motor, args=(motor1, loop_motor1)),
            # Process(target=loop_motor, args=(motor2, loop_motor2)),
        ]
        for proceso in lista_procesos:
            proceso.start()

        for proceso in lista_procesos:
            proceso.join()

    except KeyboardInterrupt:
        print("\nParando motores...")

        for proceso in lista_procesos:
            proceso.terminate()

        for proceso in lista_procesos:
            proceso.join()

    finally:
        GPIO.cleanup()
        print("\nThat's all Folks!")

''' 
def main():
    try:
        while True:
            loop_motor(motor1, loop_motor1)
            loop_motor(motor2, loop_motor2)

    except KeyboardInterrupt:
        GPIO.cleanup()
'''

# Command line execution
if __name__ == '__main__':
    main()

