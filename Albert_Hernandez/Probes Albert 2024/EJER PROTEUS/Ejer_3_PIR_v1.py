import RPi.GPIO as GPIO
import time




#------------------------------------------------------------------------------ DEFINE
# DEFINE PINS
PIR_PIN = 23                           # GPIO23 Objeto Detectado
LED_PIN = 24                           # GPIO24 LED ON




#------------------------------------------------------------------------------ CONFIG
# CONFIGURACIÓN PIN's (IN,OUT)
GPIO.setmode(GPIO.BCM)                 # GPIO Modo BCM (Nomenclatura)

GPIO.setup(PIR_PIN, GPIO.IN)           # PIN 23: IN
GPIO.setup(LED_PIN, GPIO.OUT)          # PIN 24: OUT



#----------------------------------------------------------------------------- FUNCIONES
# Detección Objeto()
def detecta_objeto():
    print ("Alerta Intruso")
    
    GPIO.output (LED_PIN, True )
    time.sleep  (0.5)
    GPIO.output (LED_PIN, False)
    
    


#------------------------------------------------------------------------------ MAIN
# VOID MAIN

# Se activa detector en "Modo Rising"    # Detecta Objeto
GPIO.add_event_detect (PIR_PIN, GPIO.rising, callback = detecta_objeto)


try:
    while True:                          # BUCLE: Infinito
        time.sleep(1)                    # Espero 1Seg, pausa para reducir carga en CPU



except KeyboardInterrupt:                # EXCEPCIÓN: Teclado
    print ("Detenido por el usuario")
    GPIO.cleanup()                       # Clean up GPIO on Ctrl+C
    

finally:                                 # FINALMENTE:
    GPIO.cleanup()                       # Clean up GPIO on script exit
    