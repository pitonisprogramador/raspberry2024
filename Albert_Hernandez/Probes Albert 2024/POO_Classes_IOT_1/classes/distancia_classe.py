import RPi.GPIO as GPIO                         # LIBRERIAS
import time

class SensorDistancia:                          # CONSTRUCTOR()
    def __init__(self, trigger_pin, echo_pin):  
        self.trigger_pin = trigger_pin          # traspaso valor de variables         
        self.echo_pin    = echo_pin             # traspaso valor de variables
        
        GPIO.setmode(GPIO.BCM)                  # Conf. de numeració de pins
        
        GPIO.setup(self.trigger_pin, GPIO.OUT)  # Configura el pin trigger  com a OUT
        GPIO.setup(self.echo_pin,    GPIO.IN)   # Configura el pin echo     com a IN

    def mesura_distancia(self):                 # MIDE DISTANCIA()
        """Mesura la distància en centímetres."""
                                                # Envia un pols de 10 µs pel pin trigger per iniciar la mesura
        GPIO.output(self.trigger_pin, GPIO.HIGH)# Config. Trigger_pin --> "1"
        time.sleep(0.00001)                     # Pols de 10 microsegons
        GPIO.output(self.trigger_pin, GPIO.LOW) # Config. Trigger_pin --> "0"

                                                
        while GPIO.input(self.echo_pin) == 0:   # MIENTRAS: NO detecta objeto
            start_time = time.time()            #       variable "start_time" == tiempo.actual
        
        while GPIO.input(self.echo_pin) == 1:   # MIENTRAS: SI detecta objeto
            stop_time = time.time()             #       variable "stop_time" == tiempo.actual

                                                
        elapsed_time = stop_time - start_time   # Calcula el temps de vol del pols
                                                 
        distancia = (elapsed_time * 34300) / 2  # Calcula la distància (en centímetres),velocitat del so en cm/s
        
        return distancia                        # devuelve el valor a quien lo ha llamado

    def cleanup(self):                          # CLEANUP()
        """Neteja la configuració de GPIO."""
        GPIO.cleanup()                          # Limpieza Config. PIN's
