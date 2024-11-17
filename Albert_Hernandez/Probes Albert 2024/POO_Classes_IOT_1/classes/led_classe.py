import RPi.GPIO as GPIO                     # Librerias
import time                                 

class LED:
    def __init__(self, pin):                # CONSTRUCTOR
        """Constructor del Objeto"""
        self.pin = pin                      
        GPIO.setmode(GPIO.BCM)              # Config. LLama PIN (Base)
        GPIO.setup(self.pin, GPIO.OUT)      # Config. PIN ---> OUT
        self.state = False                  # Defecto PIN ---> "0"
    
    def encendre(self):                     # LED --> "1" (Enciende LED)
        """Encén el LED."""
        GPIO.output(self.pin, GPIO.HIGH)    # Config. PIN_OUT  
        self.state = True                   # PIN ---> "1"
        
    
    def apagar(self):                       # LED --> "0" (Apaga LED)
        """Apaga el LED."""
        GPIO.output(self.pin, GPIO.LOW)     # Config. PIN_OUT
        self.state = False                  # PIN ---> "0"
       
       
    def alternar(self):                     # LED --> "0","1" (Alterna Encendido LED)
        """Canvia l'estat del LED."""
        if self.state:                      # SI: LED Encendido
            self.apagar()                   #   Apago LED
        else:                               # SINO:
            self.encendre()                 #   Enciendo LED
    
    def cleanup(self):                      # Limpieza Config. PIN's
        """Neteja la configuració de GPIO."""
        GPIO.cleanup()                      # Limpieza Congfi. PIN's