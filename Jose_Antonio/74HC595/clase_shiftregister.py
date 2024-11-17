import RPi.GPIO as GPIO
import time

class ShiftRegister74HC595:
    def __init__(self, data, latch, clock):
        """
        Inicialitza els pins per controlar el 74HC595.
        :param data: Pin de dades (DS)
        :param latch: Pin de latch (RCLK)
        :param clock: Pin de rellotge (SRCLK)
        """
        self.data = data
        self.latch = latch
        self.clock = clock

        # Configurar els pins GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.data, GPIO.OUT)
        GPIO.setup(self.latch, GPIO.OUT)
        GPIO.setup(self.clock, GPIO.OUT)

    def emmagatzemar_bit(self, bit):
        """
        Desa un únic bit al registre.
        :param bit: Valor '0' o '1' com a string.
        """
        GPIO.output(self.data, int(bit))  # Assigna el valor al pin de dades
        GPIO.output(self.clock, GPIO.HIGH)  # Pols al rellotge (rising edge)
        time.sleep(0.002)  # Breu retard
        GPIO.output(self.clock, GPIO.LOW)  # Torna el rellotge a LOW
        time.sleep(0.002)  # Breu retard

    def emmagatzemar_8_bits(self, byte):
        """
        Desa 8 bits al registre.
        :param byte: Cadena de 8 bits (ex: "10101010")
        """
        for bit in byte:  # Itera sobre cada caràcter de la cadena
            self.emmagatzemar_bit(bit)

    def mostrar_output(self):
        """
        Actualitza les sortides del registre amb els bits emmagatzemats.
        """
        GPIO.output(self.latch, GPIO.HIGH)  # Pols al latch per mostrar l'estat
        time.sleep(0.002)  # Breu retard
        GPIO.output(self.latch, GPIO.LOW)  # Torna el latch a LOW
        time.sleep(0.002)  # Breu retard
