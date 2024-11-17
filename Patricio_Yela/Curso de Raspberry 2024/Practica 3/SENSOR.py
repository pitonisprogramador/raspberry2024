import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)


TRIG_PIN = 23  
ECHO_PIN = 24  


GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)


def measure_distance():
   
    GPIO.output(TRIG_PIN, False)
    time.sleep(0.1)  

   
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

   
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    
    pulse_duration = pulse_end - pulse_start

    
    distance = (pulse_duration * 34300) / 2

    return distance

try:
    while True:
        dist = measure_distance()
        print(f"Distance: {dist:.2f} cm")
        time.sleep(1)  

except KeyboardInterrupt:
    
    GPIO.cleanup()

finally:
    
    GPIO.cleanup()