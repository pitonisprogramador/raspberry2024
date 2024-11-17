from LED_v1_classe          import *                  # CLASE
from distancia_classe       import *                  # CLASE
from Activar_Buzzer_classe  import *                  # CLASE



#------------------------------------------------------------------- CONFIG. RASPBERRY

LED1 = LED(17)                                           # Assignació Nº PIN --> LED1     (enciende, apaga)

Sensores = SensorDistancia(23,24)                        # Assignació Nº PIN --> TRIG, ECHO

BUZZER1 = Buzzer(18)                                     # Assignació Nº PIN --> BUZZER1  (enciende, apaga)



#------------------------------------------------------------------- MAIN


try:    
    while True:                                     # Bucle infinit
        
        dist = Sensores.mesura_distancia()          # Cálcula  la distància
            
        if dist < 10:                               # SI:   dist < 10 cm
            LED1.encendre   ()                          # Enciende LED1
            BUZZER1.encendre()                          # Enciende BUZZER1
        else:                                       # SINO: dist > 10 cm
            LED1.apagar   ()                            # Apaga LED1
            BUZZER1.apagar()                            # Apaga BUZZER1    
        
        time.sleep(1)                                   # Tiempo reposo (1 seg)



#------------------------------------------------------------------- INTERRUPCIONES

    except KeyboardInterrupt:
      
        LED1.cleanup()
