from distancia_classe import *        # CLASE
from LED_v1_classe    import *        # CLASE


#--------------------------------------------- CONFIG. RASPBERRY 

LED_PIN = LED(17)                                             # Asignación Nº PIN --> LED        (enciende, apaga)
Sensores  = SensorDistancia(trigger_pin= 23, echo_pin= 24)    # Asignación Nº PIN --> TRIG, ECHO (Activa y mide los ojitos) 



#--------------------------------------------- MAIN
try: 
    while True:                             # BUCLE INFINITO
        dist = Sensores.mesura_distancia()  #   variable "dist" == función "distance ()"
        
        if dist < 15:                       #   SI: "dist" < 15cm
            LED_PIN.encendre()              #       enciendo LED
        else:                               #   SINO:
            LED_PIN.apagar()                #       apago    LED
                                            #       
        time.sleep(1)                       # Tiempo siguiente medición.




#--------------------------------------------- INTERRUPCIONES
except KeyboardInterrupt:   
    GPIO.cleanup()                          # Limpieza Congfi. PIN's