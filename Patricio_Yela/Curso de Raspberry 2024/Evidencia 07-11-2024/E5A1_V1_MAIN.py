from LED_v1_classe import *            # Importa la clase para controlar los LEDs
from distancia_classe import *         # Importa la clase para medir la distancia
import time                            # Importa el modulo de tiempo

#------------------------------------------------------------------- CONFIG. RASPBERRY

LED_pins = [17, 27, 22, 5]             # Pines para cada LED
LEDs = [LED(pin) for pin in LED_pins]  # Instancia de cada LED usando la clase LED

Sensores = SensorDistancia(23, 24)     # Asignacion de pines para TRIG y ECHO del sensor de distancia

#------------------------------------------------------------------- MAIN

try:    
    while True:                         # Bucle infinito
        dist = Sensores.mesura_distancia()  # Calcula la distancia
            
        if dist < 10:                    # Si la distancia es menor a 10 cm
            for LED in LEDs:
                LED.encendre()          # Enciende el LED actual
                time.sleep(0.1)         # Tiempo que el LED permanece encendido
                LED.apagar()            # Apaga el LED actual
                

        time.sleep(0.5)                 # Tiempo de reposo entre cada ciclo de verificacion de distancia

#------------------------------------------------------------------- INTERRUPCIONES

except KeyboardInterrupt:
    for LED in LEDs:
        LED.cleanup()                   # Limpia los GPIO de la RASPBERRY
