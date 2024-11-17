import RPi.GPIO as IO
import time
import threading

pinled1 = 4
pinled2 = 17
interval_led1 = 1  # Interval per al LED 1
interval_led2 = 0.5  # Interval per al LED 2

# Configura els pins GPIO
def setup_gpio():
    IO.setmode(IO.BCM)
    IO.setup(pinled1, IO.OUT)
    IO.setup(pinled2, IO.OUT)

# Neteja la configuració GPIO
def netejaIO():
    IO.cleanup()

# Funció per al parpelleig del LED 1
def blink_led1():
    led1_state = False
    while True:
        led1_state = not led1_state
        IO.output(pinled1, led1_state)
        time.sleep(interval_led1)

# Funció per al parpelleig del LED 2
def blink_led2():
    led2_state = False
    while True:
        led2_state = not led2_state
        IO.output(pinled2, led2_state)
        time.sleep(interval_led2)

# Configuració GPIO
setup_gpio()

try:
    # Creació i inici dels fils
    thread_led1 = threading.Thread(target=blink_led1)
    thread_led2 = threading.Thread(target=blink_led2)

    thread_led1.start()
    thread_led2.start()

    # Espera infinita perquè els fils segueixin executant-se
    thread_led1.join()
    thread_led2.join()

except KeyboardInterrupt:
    netejaIO()


'''
Explicació:
    blink_led1() i blink_led2(): Cada funció controla el parpelleig d'un LED de manera independent, alternant el seu estat segons l'interval específic.
    thread_led1 i thread_led2: Es creen dos fils, un per a cada funció de parpelleig.
    thread.start(): Inicia el fil d'execució per al LED corresponent.
    thread.join(): Manté el programa en execució perquè els fils es mantinguin actius.
Aquest enfocament permet que els dos LEDs parpellegin de forma totalment independent gràcies a l'ús dels fils d'execució (threads).
'''