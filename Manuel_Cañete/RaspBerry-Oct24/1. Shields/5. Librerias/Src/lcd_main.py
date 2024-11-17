import time
import RPi.GPIO as GPIO
import lcd_lib as lcd

RS = 4
E = 18
D4 = 27
D5 = 22
D6 = 23
D7 = 24
PAUSA = 0.02

lcd.inicialitza_pins(RS, E, D4, D5, D6, D7, PAUSA)

FRASE = "TENGO UN DEFECTO EN LA NARIZ QUE ES MUY MOLESTO QUE ME SUCEDE IGUAL EN VIGO QUE EN MADRID NO SE POR QUE CUANDO ME PONGO MUY NERVIOSO \
ME DA UN PICOR IRRESISTIBLE EN LA NARIZ. SI EN EL COLEGIO HAY UN EXAMEN IMPORTANTE O POR LAS NOTAS ME REGANA MI PAPA ME DA ENSEGUIDA ESE PICOR TAN EXCITANTE \
QUE POR DESGRACIA SIEMPRE ME HACE ESTORNUDAR AH  AH ACHIS COMO ME PICA LA NARIZ COMO ME PICA LA NARIZ YA NO LO PUEDO RESISTIR COMO ME PICA LA NARIZ"


def peripheral_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup([RS, E, D4, D5, D6, D7], GPIO.OUT)
    GPIO.output([RS, E, D4, D5, D6, D7], 0)

def peripheral_loop():
    comptador = 0
    for index in range(len(FRASE)):
        if index % 16 == 0:
            if comptador % 2 == 0:
                lcd.esborra_la_pantalla()
                lcd.escriu_a_fila_u()
            else:
                lcd.escriu_a_fila_dos()
            comptador += 1
        lcd.envia_dades_al_display(lcd.char2bin(FRASE[index]))
    lcd.esborra_la_pantalla()

def main():
    peripheral_setup()
    lcd.inicia_pantalla()

    while True:
        try:
            peripheral_loop()
        except KeyboardInterrupt:
            lcd.esborra_la_pantalla()
            lcd.detencio_pantalla()
            break

if __name__ == '__main__':
    main()
