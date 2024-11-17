import time
import RPi.GPIO as GPIO


IN1 = 26            # Board 37
IN2 = 19            # Board 35
# IN1 = 5            # Board 29
# IN2 = 6            # Board 31
EN1 = 13            # Board 33


def motor_setup():
    '''
    Configuracion de los pines de control del motor
    '''
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([IN1, IN2, EN1], GPIO.OUT)

def motor_on_CW():
    '''
    Activa motor a derechas
    '''
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(EN1, GPIO.HIGH)

def motor_on_CCW():
    '''
    Activa motor a izquierdas
    '''
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(EN1, GPIO.HIGH)
	
def motor_off():
    '''
    Apaga y vamonos
    '''
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(EN1, GPIO.LOW)


def peripheral_loop():
    motor_on_CW()
    time.sleep(8)
    motor_off()
    time.sleep(3)
    
    motor_on_CCW()
    time.sleep(4)
    motor_off()
    time.sleep(3)


# Main function
def main():
    motor_setup()
    
    try:
        while True:
            peripheral_loop()

    except KeyboardInterrupt:
        GPIO.cleanup()


# Command line execution
if __name__ == '__main__':
    main()


