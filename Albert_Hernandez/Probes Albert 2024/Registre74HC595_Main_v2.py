import RPi.GPIO as GPIO     
import time
import random
import Registre74HC595_Clase         # Classes

DATA  = 17  # GPIO
CLOCK = 4   # GPIO
LATCH = 18  # GPIO

registre = Registre74HC595_Clase.ShiftRegister74HC595(DATA,LATCH,CLOCK)  # Creo objeto


while True:

    bits =''.join([str(random.randrange(0, 2)) for _ in range(16)])       # Creo palabra aleatoria de bits

    

    for bit in bits:                            # 

         registre.emmagatzemar_bit(int(bit))    # Creo y guardo los 8 bits --> Byte
        
    registre.mostrar_output()                   # Muestro Byte --> 8 bits 

    time.sleep(1)                               # me espero 1 Seg.
