import RPi.GPIO as IO
import time
import multiprocessing

pinled1 = 4
pinled2 = 17
interval_led1 = 1
interval_led2 = 0.5

def setup_gpio(pin):
    IO.setmode(IO.BCM)
    IO.setup(pin, IO.OUT)

def netejaIO():
    IO.cleanup()

def blink_led1():
    setup_gpio(pinled1)
    led1_state = False
    while True:
        led1_state = not led1_state
        IO.output(pinled1, led1_state)
        time.sleep(interval_led1)

def blink_led2():
    setup_gpio(pinled2)
    led2_state = False
    while True:
        led2_state = not led2_state
        IO.output(pinled2, led2_state)
        time.sleep(interval_led2)

if __name__ == "__main__":
    try:
       
        process_led1 = multiprocessing.Process(target=blink_led1)
        process_led2 = multiprocessing.Process(target=blink_led2)

       
        process_led1.start()
        process_led2.start()

        process_led1.join()
        process_led2.join()

    except KeyboardInterrupt:
        netejaIO()
