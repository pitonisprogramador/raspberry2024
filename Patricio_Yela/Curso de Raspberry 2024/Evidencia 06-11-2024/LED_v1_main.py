#import LED_v1_classe        # Librerias

from LED_v1_classe import *  # Librerias

led1 = LED(23)      # Creación Objeto (Led1)
led2 = LED(24)      # Creación Objeto (Led2) 


#-------------------  MAIN 
 
try: 
    while True:        # Bucle Infinito
     
        time.sleep(1)  # Retardo Tiempo (1Seg)
        led1.alternar()# Alternar encendido Led1 (ON/OFF)
     
        time.sleep(1)  # Retardo Tiempo (1Seg)
        led2.alternar()# Alternar encendido Led2 (ON/OFF)
        


#-------------------  INTERRUPCCIONES

except KeyboardInterrupt:
    led1.cleanup()         # Limpieza Config. PIN's / con este comando se limpia en general

