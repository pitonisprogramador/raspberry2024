import RPi.GPIO as IO
import time

pinled1 = 4
pinled2 = 17
pausa = 1

def setup_gpio():
    IO.setmode(IO.BCM)
    IO.setup(pinled1, IO.OUT)
    IO.setup(pinled2, IO.OUT)

def blink_leds():
    IO.output(pinled1, IO.HIGH)
    IO.output(pinled2, IO.LOW)
    time.sleep(pausa)
    
    IO.output(pinled1, IO.LOW)
    IO.output(pinled2, IO.HIGH)
    time.sleep(pausa)

def netejaIO():
    IO.cleanup()

setup_gpio()

try:
    while True:
        blink_leds()
        
except KeyboardInterrupt:
    netejaIO()
