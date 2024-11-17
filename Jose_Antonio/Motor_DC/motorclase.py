from motorcc_clase import *

def loop(motor_control):
    motor_control.motor_izquierda()
    time.sleep(5)
    motor_control.motor_paro()
    time.sleep(2)
    motor_control.motor_derecha()
    time.sleep(5)
    motor_control.motor_paro()
    time.sleep(2)

def main():
    motor_control = MotorControl(4, 17, 18)
    try:
        while True:
            loop(motor_control)
    except KeyboardInterrupt:
        pass

main()
