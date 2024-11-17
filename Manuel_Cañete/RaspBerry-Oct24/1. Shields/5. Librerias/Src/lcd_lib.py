import RPi.GPIO as GPIO
import time

# Funció d'inicialització per establir els valors dels pins des del codi principal
def inicialitza_pins(rs, e, d4, d5, d6, d7, pausa):
    global RS, E, D4, D5, D6, D7, PAUSA
    RS, E, D4, D5, D6, D7, PAUSA = rs, e, d4, d5, d6, d7, pausa

def char2bin(char):
    """Converteix un caràcter en una representació binària de 8 bits en ordre específic i la retorna com una tupla d'enters."""
    strink = bin(ord(char))[2:]
    strink = '0' * (8 - len(strink)) + strink  
    resultat = ''
    for bit in strink:
        resultat = bit + resultat  
    res = resultat[4:] + resultat[:4]
    tupla = tuple([int(element) for element in res])
    return tupla

def modecomandament(valor):
    """Configura el mode de comandament del display, ajustant el pin RS segons si s’està enviant una instrucció (False) o dades (True)."""
    if valor == False:
        GPIO.output(RS, 1)  
    else:
        GPIO.output(RS,0)
    GPIO.output(E, 0)  

def escriu_a_fila_u():
    """Mou el cursor a l'inici de la primera fila del display."""
    modecomandament(True) 
    escriu4bits(0,0,0,0)  
    escriu4bits(0,0,0,0)
  
def escriu_a_fila_dos():
    """Mou el cursor a l'inici de la segona fila del display."""
    modecomandament(True) 
    escriu4bits(0,0,1,1)  
    escriu4bits(0,0,0,0)

def escriu4bits(b1, b2, b3, b4):
    """Envia 4 bits al display a través dels pins D4-D7."""
    GPIO.output(D4, b1)
    GPIO.output(D5, b2)
    GPIO.output(D6, b3)
    GPIO.output(D7, b4)  
    time.sleep(PAUSA)
    GPIO.output(E, 1) 
    GPIO.output(E, 0)       
    time.sleep(PAUSA)

def esborra_la_pantalla():
    """Envia la instrucció per esborrar tot el display."""
    modecomandament(True)
    time.sleep(PAUSA)
    escriu4bits(0,0,0,0) 
    escriu4bits(1,0,0,0) 

def envia_dades_al_display(dada):
    """Envia un caràcter (en forma de tupla de 8 bits) al display per a ser mostrat."""
    modecomandament(False) 
    escriu4bits(dada[0],dada[1],dada[2], dada[3]) 
    escriu4bits(dada[4],dada[5], dada[6], dada[7])

def detencio_pantalla():
    """Posa el display en mode de detenció o pausa."""
    modecomandament(True) 
    escriu4bits(0,0,0,0) 
    escriu4bits(0,0,1,1) 
   
def inicia_pantalla():
    """Configura el display per iniciar-lo, establint-lo amb dues files i esborrant-lo."""
    modecomandament(True)
    for index in range(3):
        escriu4bits(1,1,0,0)
    for index in range(2):
        escriu4bits(0,1,0,0)
    escriu4bits(1,0,1,1)   
    escriu4bits(0,0,0,0)
    escriu4bits(1,1,1,1)
    esborra_la_pantalla()
