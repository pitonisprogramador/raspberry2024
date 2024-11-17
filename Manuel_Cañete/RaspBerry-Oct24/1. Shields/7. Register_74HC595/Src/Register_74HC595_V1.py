import time
import RPi.GPIO as GPIO

class ShiftRegister74HC595():
    '''
    Clase para control del shift register 74HC595
           
    '''
    def __init__(self, data, clock, latch):
        ''' 
        Entrada: pines de la RB (modo BCM)
            data: pin data (modo BCM)
            clock: pin clock (modo BCM)
            latch: pin latch (modo BCM)
        Salida: -
        '''
        self.data = data 
        self.clock = clock 
        self.latch = latch 
        GPIO.setmode(GPIO.BCM)
        GPIO.setup([data, clock, latch], GPIO.OUT)

    def emmagatzemar_bit(self, bit):
        ''' 
        Almacena un bit en el registro 595
        Entrada: 
            bit: int con valores 0 o 1
        Salida: -
        '''
        GPIO.output(self.data, bit)
        time.sleep(0.01)
        GPIO.output(self.clock, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(self.clock, GPIO.LOW)
        
    def emmagatzemar_valor(self, valor):
        ''' 
        Almacena un valor en el registro 595
        Admite Daisy Chain
        Entrada: 
            valor: string con "0" y "1"
        '''
        for bit in valor:
            self.emmagatzemar_bit(int(bit))
        
    def mostrar_output(self):
        '''
        Muestra la salida del registro 595
        Entrada: -
        Salida: -
        '''
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


def peripheral_loop_8bits():
#    byte = [random.randrange(0, 2) for element in range(8)]
    valor = "10000000"
    for _ in range(len(valor)):
        # print(byte)
        registre.emmagatzemar_valor(valor)
        registre.mostrar_output()
        time.sleep(.5)
        valor = valor[-1] + valor[:-1]             # Rotación hacia derecha
    valor = "00000010"
    for _ in range(len(valor) - 2):
        # print(byte)
        registre.emmagatzemar_valor(valor)
        registre.mostrar_output()
        time.sleep(0.2)
        valor = valor[1:] + valor[0]               # Rotación hacia la izquierda


def peripheral_loop_16bits():
    valor = "1000000000000000"
    for _ in range(len(valor)):
        # print(byte)
        registre.emmagatzemar_valor(valor)
        registre.mostrar_output()
        time.sleep(.4)
        valor = valor[-1] + valor[:-1]             # Rotación hacia derecha
    valor = "0000000000000010"
    for _ in range(len(valor) - 2):
        # print(byte)
        registre.emmagatzemar_valor(valor)
        registre.mostrar_output()
        time.sleep(0.15)
        valor = valor[1:] + valor[0]               # Rotación hacia la izquierda


'''
# Main function
def main():
    # peripheral_setup()		    # Setup
    
    while True:					# Infinite loop
        peripheral_loop()
'''
def main():
    try:
        while True:
            # peripheral_loop_8bits()
            peripheral_loop_16bits()

    except KeyboardInterrupt:
        GPIO.cleanup()


# Command line execution
if __name__ == '__main__':
    main()

'''
try:
    i = 0
    while True:
        for i in range(1, 20, 1):
            GPIO.output(pinbuzzer, GPIO.HIGH)
            
            time.sleep(i/10)
            GPIO.output(pinbuzzer, GPIO.LOW)
            time.sleep(i/10)

except KeyboardInterrupt:
    GPIO.cleanup()
'''