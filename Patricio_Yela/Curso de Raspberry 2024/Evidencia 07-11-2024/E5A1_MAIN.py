from LED_v1_classe          import *                  # CLASE
from distancia_classe       import *                  # CLASE
import RPi.GPIO as GPIO

#------------------------------------------------------------------- CONFIG. RASPBERRY

'''LED1 = LED(17)                     # Assignació Nº PIN --> LED1     (enciende, apaga)
LED2 = LED(27)                     # Assignació Nº PIN --> LED2     (enciende, apaga)
LED3 = LED(22)                     # Assignació Nº PIN --> LED3     (enciende, apaga)
LED4 = LED(5)                      # Assignació Nº PIN --> LED4     (enciende, apaga)'''

LEDs = [LED(17),LED(27),LED(22),LED(5)]
#x = len(LEDs)

Sensores = SensorDistancia(23,24)  # Assignació Nº PIN --> TRIG, ECHO

#------------------------------------------------------------------- MAIN


try:    
    while True:                                     # Bucle infinit
        
        dist = Sensores.mesura_distancia()          # Cálcula  la distància
        
        
            
        if dist < 10:                               # SI:   dist < 10 cm        ----> MIentras detectes objeto
           for led in LEDs:
            
            led.encendre()
            
            time.sleep(0.5)
            
            led.apagar()
            
        #else:                                       # SINO: dist > 10 cm
         #   LED[17,27,22,5].apagar   ()                    # Apaga LED1
             
        
        time.sleep(0.5)                                   # Tiempo reposo (1 seg)



#------------------------------------------------------------------- INTERRUPCIONES

except KeyboardInterrupt:
      
    GPIO.cleanup()                              # Limpia los GPIO de la RASPBERRY
