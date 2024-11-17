import time
import RPi.GPIO as GPIO

class ShiftRegister74HC595():
    '''
    Clase para control del shift register 74HC595
           
    '''
    __init__(self, data, clock, latch):
        ''' 
        Entrada: pines de la RB (modo BCM)
        '''
        self.data = data 
        self.clock = clock 
        self.latch = latch 
        GPIO.setmode(GPIO.BCM)
        GPIO.setup([data, clock, latch], GPIO.OUT)

    emmagatzemar_bit(self, bit):
        ''' 
        Almacena un bit
        Entrada: bit (valores "0" o "1")
        '''
        GPIO.output(self.data, int(bit))
        time.sleep(0.01)
        GPIO.output(self.clock, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(self.clock, GPIO.LOW)
        
    emmagatzemar_byte(self, byte):
        ''' 
        Almacena un byte
        Entrada: byte (string con "0" y "1")
        '''
        for bit in byte():
            self.emmagatzemar(int(bit))
        
    mostrar_output(self):
        GPIO.output(self.latch, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(self.latch, GPIO.LOW) 



DATA = 17
CLOCK = 4
LATCH = 18
registre = ShiftRegister74HC595(DATA, CLOCK, LATCH)


#byte = [1,0,0,0,0,0,0,0]



# Peripheral Configuration 
# def peripheral_setup():
#     DATA = 17
#     CLOCK = 4
#     LATCH = 18
#     registre = ShiftRegister74HC595(DATA, CLOCK, LATCH)

# Peripheral Constructors
# Install interrupt handlers
#    GPIO.setmode(GPIO.BCM)
#    GPIO.setup([DATA, CLOCK, LATCH], GPIO.OUT)

def peripheral_loop():
#    byte = [random.randrange(0, 2) for element in range(8)]
    byte = "10000000"
    registre.emmagatzemar(byte)
    registre.mostrar_output()
    time.sleep(1)
    byte = byte[-1] + byte[:-1]
 
    # for bit in byte:
    #     GPIO.output(DATA, int(bit))
    #     time.sleep(0.01)
    #     GPIO.output(CLOCK, GPIO.HIGH)
    #     time.sleep(0.01)
    #     GPIO.output(CLOCK, GPIO.LOW)
    # GPIO.output(LATCH, GPIO.HIGH)
    # time.sleep(0.01)
    # GPIO.output(LATCH, GPIO.LOW) 
    # byte = byte[-1] + byte[:-1]
    # time.sleep(1)

# Main function
def main():
    # peripheral_setup()		    # Setup
    while True:					# Infinite loop
        peripheral_loop()

# Command line execution
if __name__ == '__main__':
    main()

'''
