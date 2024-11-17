import RPi.GPIO as IO
import time
import threading

pinled1 = 4
pinled2 = 17
interval_led1 = 1  
interval_led2 = 0.5 


def setup_gpio():
    IO.setmode(IO.BCM)
    IO.setup(pinled1, IO.OUT)
    IO.setup(pinled2, IO.OUT)


def netejaIO():
    IO.cleanup()

def blink_led1():
    led1_state = False
    while True:
        led1_state = not led1_state
        IO.output(pinled1, led1_state)
        time.sleep(interval_led1)

def blink_led2():
    led2_state = False
    while True:
        led2_state = not led2_state
        IO.output(pinled2, led2_state)
        time.sleep(interval_led2)

setup_gpio()

try:
    thread_led1 = threading.Thread(target=blink_led1)
    thread_led2 = threading.Thread(target=blink_led2)

    thread_led1.start()
    thread_led2.start()

    thread_led1.join()
    thread_led2.join()

except KeyboardInterrupt:
    netejaIO()
