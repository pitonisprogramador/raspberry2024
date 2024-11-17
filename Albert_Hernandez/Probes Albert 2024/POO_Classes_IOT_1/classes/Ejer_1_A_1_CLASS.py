import RPi.GPIO as GPIO                 # LIBRERIAS            
import time 


#--------------------------------------------- CONFIG. RASPBERRY 
'''
GPIO.setmode(GPIO.BCM)                  # Config. LLama PIN's (Base)

LED_PIN = 17                            # Asignación Nº PIN --> LED  (enciende, apaga)
TRIG    = 23                            # Asignación Nº PIN --> TRIG (Activa los ojitos) 
ECHO    = 24                            # Asignación Nº PIN --> ECHO (Calibrar distancia detección ojitos)

GPIO.setup  (LED_PIN, GPIO.OUT)         # Conf. PIN --> OUT
GPIO.setup  (TRIG,    GPIO.OUT)         # Conf. PIN --> OUT 
GPIO.setup  (ECHO,    GPIO.IN )         # Conf. PIN --> IN
'''
 

class LED:
#--------------------------------------------- FUNCIONES 
        
    def __init__(self, pin):                # CONSTRUCTOR
        """Constructor del Objeto"""
        self.pin = pin                      
        GPIO.setmode(GPIO.BCM)              # Config. LLama PIN (Base)
        GPIO.setup(self.pin, GPIO.OUT)      # Config. PIN ---> OUT
        self.state = False                  # Defecto PIN ---> "0"        
        
        
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
            
            
    def cleanup(self):                          # Limpieza Config. PIN's
        """Neteja la configuració de GPIO."""
        GPIO.cleanup()                          # Limpieza Congfi. PIN's

