import RPi.GPIO as IO
import time

pinled1 = 4
pinled2 = 17
pausa = 1

IO.setmode(IO.BCM)
IO.setup(pinled1, IO.OUT)
IO.setup(pinled2, IO.OUT)

try:
    while True:
        IO.output(pinled1, IO.HIGH)
        IO.output(pinled2, IO.HIGH)
        time.sleep(pausa)
        
        IO.output(pinled1, IO.LOW)
        IO.output(pinled2, IO.LOW)
        time.sleep(pausa)
        
except KeyboardInterrupt:
    IO.cleanup()
