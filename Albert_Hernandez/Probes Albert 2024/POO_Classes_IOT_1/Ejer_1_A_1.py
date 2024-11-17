import RPi.GPIO as GPIO                 # LIBRERIAS            
import time 


#--------------------------------------------- CONFIG. RASPBERRY 

GPIO.setmode(GPIO.BCM)                  # Config. LLama PIN's (Base)

LED_PIN = 17                            # Asignación Nº PIN --> LED  (enciende, apaga)
TRIG    = 23                            # Asignación Nº PIN --> TRIG (Activa los ojitos) 
ECHO    = 24                            # Asignación Nº PIN --> ECHO (Calibrar distancia detección ojitos)

GPIO.setup  (LED_PIN, GPIO.OUT)         # Conf. PIN --> OUT
GPIO.setup  (TRIG,    GPIO.OUT)         # Conf. PIN --> OUT 
GPIO.setup  (ECHO,    GPIO.IN )         # Conf. PIN --> IN

 
#--------------------------------------------- FUNCIONES 
def distance():                             
                                            # INICIALIZAR VARIABLES:
    GPIO.output(TRIG, True)                 # Activa    ojitos TRIG --> "1"
    time.sleep(0.00001)                     # Retardo de estabilización ojitos
    GPIO.output(TRIG, False)                # Desactiva ojitos TRIG --> "0" 
    
    start, stop = time.time(), time.time()  # Variables: "start", "stop"  == tiempo.actual


                                            # Activa y mide distancia objeto 
    while GPIO.input(ECHO) == 0:            # MIENTRAS: NO detecto objeto
            start = time.time()             #   "start" = tiempo.actual

    while GPIO.input(ECHO) == 1:            # MIENTRAS: SI detecto objeto
            stop = time.time()              #   "stop" = tiempo.actual

    return (stop - start) * 34300 / 2       # Devuelve la que distancia esta el objeto

#--------------------------------------------- MAIN
try: 
    while True:                             # BUCLE INFINITO
        dist = distance()                   #   variable "dist" <-- función "distance ()"
        
        if dist < 15:                       #   SI: "dist" menor 15cm
        GPIO.output(LED_PIN, True)          #       enciendo LED
    else:                                   #   SINO:
        GPIO.output(LED_PIN, False)         #       apago    LED
        time.sleep(0.5)                     #       espero (0.5 Seg)



#--------------------------------------------- INTERRUPCIONES
except KeyboardInterrupt:   
    GPIO.cleanup()                          # Limpieza Congfi. PIN's