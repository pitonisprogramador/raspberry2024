import RPi.GPIO as GPIO
import time
import random

class RegistroDesplazamiento:
    def __init__(self, data_pin, clock_pin, latch_pin):
        '''Asigna los pines para inicializar'''
        self.data_pin = data_pin
        self.clock_pin = clock_pin
        self.latch_pin = latch_pin

        # Configuración de los pines
        GPIO.setmode(GPIO.BCM)
        GPIO.setup([self.data_pin, self.clock_pin, self.latch_pin], GPIO.OUT)

    def enviar_bits(self, bits):
        '''Envía una lista de bits al registro de desplazamiento.'''
        for bit in bits:
            GPIO.output(self.data_pin, bit)
            time.sleep(0.01)
            GPIO.output(self.clock_pin, 1)
            time.sleep(0.01)
            GPIO.output(self.clock_pin, 0)
    def mostrar(self):
        # Actualiza las salidas del latch
        GPIO.output(self.latch_pin, 1)
        time.sleep(0.01)
        GPIO.output(self.latch_pin, 0)
    

    def generar_bits_aleatorios(self):
        '''Genera una lista de 8 bits aleatorios (0 o 1).'''
        return [random.randrange(0, 2) for _ in range(8)]

    def limpiar(self):
        '''Limpia la configuración de GPIO.'''
        GPIO.cleanup()

