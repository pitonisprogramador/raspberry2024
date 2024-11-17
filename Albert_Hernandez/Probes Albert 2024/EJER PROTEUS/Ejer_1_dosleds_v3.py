import RPi.GPIO as IO
import time

pinled1 = 4
pinled2 = 17
pausa = 1

def setup_gpio():
    IO.setmode(IO.BCM)
    IO.setup(pinled1, IO.OUT)
    IO.setup(pinled2, IO.OUT)

def blink_led(pin):
    IO.output(pin, IO.HIGH)
    time.sleep(pausa)
    IO.output(pin, IO.LOW)
    time.sleep(pausa)

def netejaIO():
    IO.cleanup()

setup_gpio()

try:
    while True:
        blink_led(pinled1)
        blink_led(pinled2)
        
except KeyboardInterrupt:
    netejaIO()

