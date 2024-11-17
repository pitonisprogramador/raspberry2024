import RPi.GPIO as GPIO
import time

class SensorDistancia:
    def __init__(self, data_pin, latch_pin, clock_pin):
        self.data_pin = data_pin
        self.latch_pin = latch_pin
        self.clock_pin = clock_pin

        GPIO.setup([data_pin, latch_pin, clock_pin], GPIO.OUT)

    def mesura_distancia(self):
        """Mesura la distància en centímetres."""
        # Envia un pols de 10 µs pel pin trigger per iniciar la mesura
        GPIO.output(self.trigger_pin, GPIO.HIGH)
        time.sleep(0.00001)  # Pols de 10 microsegons
        GPIO.output(self.trigger_pin, GPIO.LOW)

        # Mesura el temps que tarda el senyal d’echo en tornar
        while GPIO.input(self.echo_pin) == 0:
            start_time = time.time()
        
        while GPIO.input(self.echo_pin) == 1:
            stop_time = time.time()

        # Calcula el temps de vol del pols
        elapsed_time = stop_time - start_time
        # Calcula la distància (en centímetres)
        distancia = (elapsed_time * 34300) / 2  # velocitat del so en cm/s
        return distancia

    # def cleanup(self):
        # """Neteja la configuració de GPIO."""
        # GPIO.cleanup()




while True:
    bits = tuple([random.randrange(0, 2) for element in range(8)])  # Genera una secuencia aleatoria de 8 bits
    for bit in bits:
        GPIO.output(DATA, bit)
        time.sleep(0.01)
        GPIO.output(CLOCK, 1)
        time.sleep(0.01)
        GPIO.output(CLOCK, 0)
    GPIO.output(LATCH, 1)
    time.sleep(0.01)
    GPIO.output(LATCH, 0)
    time.sleep(1)
