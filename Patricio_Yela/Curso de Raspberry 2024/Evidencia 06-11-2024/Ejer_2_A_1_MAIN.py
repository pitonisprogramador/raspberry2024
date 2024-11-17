from distancia_classe import *        # CLASE
from LED_v1_classe    import *        # CLASE


#--------------------------------------------- CONFIG. RASPBERRY 

LED1 = LED (17)                              # Asignación Nº PIN --> LED1        (enciende, apaga)
LED2 = LED (27)                              # Asignación Nº PIN --> LED2        (enciende, apaga)

Sensor = SensorDistancia(trigger_pin= 23, echo_pin= 24)# Asignación Nº PIN --> TRIG, ECHO (Activa y mide los ojitos) 



#--------------------------------------------- MAIN
try: 
    while True:                             # BUCLE INFINITO
        dist = Sensor.mesura_distancia()    #   variable "dist" == función "distance ()"
        
        if dist < 10:                       #   SI: "dist" < 10cm
            LED1.encendre()                 #       enciendo LED1
            LED2.apagar  ()                 #       apagar   LED2
        else:                               #   SINO:
            LED1.apagar  ()                 #       apago    LED1
            LED1.encendre()                 #       enciendo LED2                               #       
        
        time.sleep(1)                       # Tiempo siguiente medición.




#--------------------------------------------- INTERRUPCIONES
except KeyboardInterrupt:   
    GPIO.cleanup()                          # Limpieza Congfi. PIN's