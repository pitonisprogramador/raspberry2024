
import time
import RPi.GPIO as GPIO



IN1 = (26, 19)      
EN1 = 13           

IN2 = (24, 25)       
EN2 = 12  
            


class MotorDC():
    def __init__(self, input, enable):
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup([input[0], input[1], enable], GPIO.OUT)
        self.input = input
        self.enable = enable
        self.speed = GPIO.PWM(enable, 1000)
        self.speed.start(0)
           
    def on(self, speed):
       
        if 0 <= speed <= 100:                          
            GPIO.output(self.input[0], GPIO.LOW)
            GPIO.output(self.input[1], GPIO.HIGH)
            self.speed.ChangeDutyCycle(speed)
            
        elif -100 <= speed < 0:                        
            GPIO.output(self.input[0], GPIO.HIGH)
            GPIO.output(self.input[1], GPIO.LOW)
            self.speed.ChangeDutyCycle(-speed)
            
    
    
    
    def off(self):
        
        GPIO.output(self.input[0], GPIO.LOW)
        GPIO.output(self.input[1], GPIO.LOW)
        # GPIO.output(self.enable, GPIO.LOW)
        self.speed.ChangeDutyCycle(0)
    
motor1 = MotorDC(IN1, EN1)
motor2 = MotorDC(IN2, EN2)
        

def peripheral_loop():
    for speed in range(-100, -51):
        motor1.on(speed)
        motor2.on(-speed)
        time.sleep(.5)
    motor1.off()
    motor2.off()
    time.sleep(5)
    for speed in range(50, 101):
        motor1.on(speed)
        motor2.on(-speed)
        time.sleep(.5)
    motor1.off()
    motor2.off()
    time.sleep(5)

def main():
    try:
        while True:
            peripheral_loop()

    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == '__main__':
    main()

