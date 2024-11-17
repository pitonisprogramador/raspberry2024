import RPi.GPIO as IO
import time
import multiprocessing

pinled1 = 4
pinled2 = 17
interval_led1 = 1  # Interval per al LED 1
interval_led2 = 0.5  # Interval per al LED 2

# Configura els pins GPIO
def setup_gpio(pin):
    IO.setmode(IO.BCM)
    IO.setup(pin, IO.OUT)

# Neteja la configuració GPIO
def netejaIO():
    IO.cleanup()

# Funció per al parpelleig del LED 1
def blink_led1():
    setup_gpio(pinled1)  # Configura el GPIO del LED 1 en el procés
    led1_state = False
    while True:
        led1_state = not led1_state
        IO.output(pinled1, led1_state)
        time.sleep(interval_led1)

# Funció per al parpelleig del LED 2
def blink_led2():
    setup_gpio(pinled2)  # Configura el GPIO del LED 2 en el procés
    led2_state = False
    while True:
        led2_state = not led2_state
        IO.output(pinled2, led2_state)
        time.sleep(interval_led2)

# Configuració dels processos
if __name__ == "__main__":
    try:
        # Creem els processos per cada LED
        process_led1 = multiprocessing.Process(target=blink_led1)
        process_led2 = multiprocessing.Process(target=blink_led2)

        # Iniciem els processos
        process_led1.start()
        process_led2.start()

        # Mantenim els processos actius
        process_led1.join()
        process_led2.join()

    except KeyboardInterrupt:
        # Neteja dels GPIO al final
        netejaIO()
        IO.cleanup()