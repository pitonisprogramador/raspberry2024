import RPi.GPIO as GPIO
import time

class SensorPIR:
    def __init__(self, pir_pin):
        self.pir_pin = pir_pin
        #GPIO.setmode(GPIO.BCM)  # Mode de numeració de pins
        GPIO.setup(self.pir_pin, GPIO.IN)  # Configura el pin PIR com a entrada

    def detecta_moviment(self):
        """Retorna True si detecta moviment, False en cas contrari."""
        if GPIO.input(self.pir_pin) == GPIO.HIGH:
            return True
        else:
            return False

    # def cleanup(self):
        # """Neteja la configuració de GPIO."""
        # GPIO.cleanup()