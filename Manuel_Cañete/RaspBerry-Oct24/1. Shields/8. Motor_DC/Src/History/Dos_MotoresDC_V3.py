import time
import RPi.GPIO as GPIO
from multiprocessing import Process

# Pines del motor 1
IN1 = (26, 19)  # Pines de direcció
EN1 = 13        # Pin de PWM

# Pines del motor 2
IN2 = (24, 25)
EN2 = 12

def motor_loop(input_pins, enable_pin):
    '''
    Bucle de control del motor amb PWM.
    Configura GPIO i PWM dins del procés.
    '''
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([input_pins[0], input_pins[1], enable_pin], GPIO.OUT)
    pwm = GPIO.PWM(enable_pin, 1000)
    pwm.start(0)
    
    try:
        while True:
            # Gira cap a un costat
            for speed in range(-100, -51):
                if speed > 0:
                    GPIO.output(input_pins[0], GPIO.LOW)
                    GPIO.output(input_pins[1], GPIO.HIGH)
                else:
                    GPIO.output(input_pins[0], GPIO.HIGH)
                    GPIO.output(input_pins[1], GPIO.LOW)
                pwm.ChangeDutyCycle(abs(speed))
                time.sleep(0.5)
            
            # Atura el motor
            GPIO.output(input_pins[0], GPIO.LOW)
            GPIO.output(input_pins[1], GPIO.LOW)
            pwm.ChangeDutyCycle(0)
            time.sleep(5)
            
            # Gira cap a l'altre costat
            for speed in range(50, 101):
                if speed > 0:
                    GPIO.output(input_pins[0], GPIO.LOW)
                    GPIO.output(input_pins[1], GPIO.HIGH)
                else:
                    GPIO.output(input_pins[0], GPIO.HIGH)
                    GPIO.output(input_pins[1], GPIO.LOW)
                pwm.ChangeDutyCycle(abs(speed))
                time.sleep(0.5)
            
            # Atura el motor
            GPIO.output(input_pins[0], GPIO.LOW)
            GPIO.output(input_pins[1], GPIO.LOW)
            pwm.ChangeDutyCycle(0)
            time.sleep(5)

    except KeyboardInterrupt:
        print("Parant el procés del motor.")
    finally:
        pwm.stop()
        GPIO.cleanup()

def main():
    try:
        # Crea processos per als motors
        motor1_process = Process(target=motor_loop, args=(IN1, EN1))
        motor2_process = Process(target=motor_loop, args=(IN2, EN2))
        
        # Inicia els processos
        motor1_process.start()
        motor2_process.start()
        
        # Espera que els processos acabin
        motor1_process.join()
        motor2_process.join()

    except KeyboardInterrupt:
        print("Parant motors.")
        motor1_process.terminate()
        motor2_process.terminate()

if __name__ == '__main__':
    main()
