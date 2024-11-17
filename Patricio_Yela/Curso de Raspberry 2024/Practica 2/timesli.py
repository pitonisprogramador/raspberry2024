import RPi.GPIO as IO
import time

pinled1 = 4
pinled2 = 17
interval_led1 = 3 
interval_led2 = 1  


def setup_gpio():
    IO.setmode(IO.BCM)
    IO.setup(pinled1, IO.OUT)
    IO.setup(pinled2, IO.OUT)

def netejaIO():
    IO.cleanup()


setup_gpio()


last_time_led1 = time.time()
last_time_led2 = time.time()
led1_state = False
led2_state = False

try:
    
    while True:
        current_time = time.time()
        
        
        if current_time - last_time_led1 >= interval_led1:
            led1_state = not led1_state  
            IO.output(pinled1, led1_state)  
            last_time_led1 = current_time  
        
        #
        if current_time - last_time_led2 >= interval_led2:
            led2_state = not led2_state 
            IO.output(pinled2, led2_state)  
            last_time_led2 = current_time  

        
        time.sleep(0.01)

except KeyboardInterrupt:
    netejaIO()
