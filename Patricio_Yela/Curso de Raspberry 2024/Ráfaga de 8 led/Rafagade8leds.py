from Rafagade8leds_clase import *
import time


# ----------------------------------------------------------------------------------------------Creación de pines 
registro = RegistroDesplazamiento(data_pin=17, clock_pin=4, latch_pin=18)
    
try:
     while True:
# ---------------------------------------------------------------------------------------------Genera una secuencia aleatoria de 8 bits y envíala al registro
         bits = registro.generar_bits_aleatorios()
         registro.enviar_bits(bits)
         time.sleep(1)                                                                                      # Espera 1 segundo antes de la siguiente secuencia
         registro.mostrar()
            

except KeyboardInterrupt:
     print("Nos vemos")
     registro.limpiar()
     print("GPIO limpiado y programa finalizado")

