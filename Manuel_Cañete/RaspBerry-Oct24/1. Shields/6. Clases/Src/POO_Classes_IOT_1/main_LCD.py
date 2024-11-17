from LCD_classe import *

if __name__ == "__main__":
    display = LCD(rs=4, e=18, d4=27, d5=22, d6=23, d7=24, pausa=0.02)
    
    try:
        display.inicia_pantalla()
        display.escriu_a_fila_u()
        display.envia_dades_al_display(display.char2bin('H'))
        display.envia_dades_al_display(display.char2bin('o'))
        display.envia_dades_al_display(display.char2bin('l'))
        display.envia_dades_al_display(display.char2bin('a'))
    except KeyboardInterrupt:
        pass
    finally:
        display.cleanup()
