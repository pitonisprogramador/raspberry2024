import RPi.GPIO as GPIO
import time

class Motor: 
    def __init__(self,ENA, IN1, IN2):       # CONSTRUCTOR
        
        self.ENA = ENA
        self.IN1 = IN1
        self.IN2 = IN2
        
        GPIO.setmode(GPIO.BCM)              # Configurar els pins GPIO
        GPIO.setup  (self.ENA,   GPIO.OUT)  # ENA: SALIDA
        GPIO.setup  (self.IN1,   GPIO.OUT)  # IN1: SALIDA
        GPIO.setup  (self.IN2,   GPIO.OUT)  # IN2: SALIDA



    def giro_derecha(self,t):               # "giro_derecha"
        GPIO.output(self.ENA,GPIO.HIGH)     # habilito Motor
        GPIO.output(self.IN1,GPIO.LOW)      # IN1 --> "0"
        GPIO.output(self.IN2,GPIO.HIGH)     # IN2 --> "1"
        time.sleep(t)                       # Retardo (Seg)


    def parate(self,t):                     # "parate"
        GPIO.output(self.ENA,GPIO.LOW)      # Deshabilito Motor
        time.sleep(t)                       # Retardo (Seg)


    def giro_izquierda(self,t):             # "giro_izquierda"
        GPIO.output(self.ENA,GPIO.HIGH)     # habilito Motor
        GPIO.output(self.IN1,GPIO.HIGH)     # IN1 --> "1"
        GPIO.output(self.IN2,GPIO.LOW)      # IN2 --> "0"
        time.sleep(t)                       # Retardo (Seg)

    def loop(self):                         # "loop"                            
        self.giro_derecha(5)                # derecha
        self.parate(2)                      # para
        self.giro_izquierda(5)              # izquierda
        self.parate(2)                      # para
    
    def cleanup(self):                      # Limpieza Conf. Pins
        GPIO.cleanup()