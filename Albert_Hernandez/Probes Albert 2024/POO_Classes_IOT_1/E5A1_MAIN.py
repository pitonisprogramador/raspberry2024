from LED_v1_classe          import *                  # CLASE
from distancia_classe       import *                  # CLASE

import RPi.GPIO as GPIO

#------------------------------------------------------------------- CONFIG. RASPBERRY

LEDs = [LED(17),LED(27),LED(22),LED(5)]     # craci´pon de objetos LED

Sensores = SensorDistancia(23,24)           # Assignació Nº PIN --> TRIG, ECHO

#------------------------------------------------------------------- MAIN


try:    
    while True:                                     # Bucle infinit
        
        dist = Sensores.mesura_distancia()          # Cálcula  la distància
        
        if dist < 10:               # SI:   dist < 10 cm        
           for led in LEDs:         #   FOR "Objeto" in "cantidad de objetos"
            
            led.encendre()          #       Enciende LEDx
            
            time.sleep(0.5)         # Tiempo reposo (1 seg)
            
            led.apagar()            #       Apaga LEDx
            
                
        time.sleep(0.5)             # Tiempo reposo (1 seg)



#------------------------------------------------------------------- INTERRUPCIONES

except KeyboardInterrupt:
      
    GPIO.cleanup()                              # Limpia los GPIO de la RASPBERRY
