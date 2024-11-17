import RPi.GPIO as GPIO
import time

from Motor_Clase import *        # Clase Motor (importar todas funciones)

ENA = 4
IN1 = 17
IN2 = 18

Motor1 = Motor(ENA,IN1,IN2)

try:
    while True:
        Motor1.loop()

#-------------------  INTERRUPCCIONES

except KeyboardInterrupt:
    Motor1.cleanup()      # Limpieza Config. PIN's 
