import time
import RPi.GPIO as GPIO
import lcd_lib as lcd

RS = 4
E = 18
D4 = 27
D5 = 22
D6 = 23
D7 = 24
PAUSA = 0.03

lcd.inicialitza_pins(RS, E, D4, D5, D6, D7, PAUSA)

FRASE = "LA PERSEVERANCIA ES SIN DUDA VITAL PARA PODER LLEGAR A ALCANZAR NUESTROS OBJETIVOS SIN ELLA NUNCA PODREMOS \
ALCANZAR LAS METAS QUE ANTERIORMENTE NOS HAYAMOS PROPUESTO. Recuerda que la gente sufre del sindrome \
de la iditez, pero depende de cada uno como sacarlo."


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

    try:
        while True:
            peripheral_loop()
    except KeyboardInterrupt:
       
        lcd.esborra_la_pantalla()
        lcd.escriu_a_fila_u()
        despedida = "Hasta pronto"
        for char in despedida:
            lcd.envia_dades_al_display(lcd.char2bin(char))
        time.sleep(2)  # Espera 2 segundos para que el usuario lea el mensaje
        lcd.esborra_la_pantalla()
        lcd.detencio_pantalla()
        GPIO.cleanup()  

if __name__ == '__main__':
    main()
