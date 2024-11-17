from clase_shiftregister import *


# Define los pines GPIO
data_pin = 4
latch_pin = 6
clock_pin = 5

# Crea una instancia de la clase ShiftRegister74HC595
registro = ShiftRegister74HC595(data_pin, latch_pin, clock_pin)

# Ejecuta la secuencia de salidas utilizando un bucle `for`
try:
    while True:
        for i in range(16):
            # Genera un byte con un único bit en alto, desplazado según `i`
            byte = '0' * (15 - i) + '1' + '0' * i
            registro.emmagatzemar_8_bits(byte)
            registro.mostrar_output()
            time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()


