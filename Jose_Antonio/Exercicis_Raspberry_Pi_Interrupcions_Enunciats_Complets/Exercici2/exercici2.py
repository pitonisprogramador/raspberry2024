import time
from Active_Buzzer_classe import Buzzer
from distancia_classe import SensorDistancia
import RPi.GPIO as GPIO

# Pines GPIO
TRIG = 27
ECHO = 22
BUZZER_PIN = 4

# Umbral de distancia en cm
DISTANCIA_UMBRAL = 15

# Inicializar las clases
buzzer = Buzzer(BUZZER_PIN)
sensor = SensorDistancia(TRIG, ECHO)

def activar_buzzer(channel):
    """Función de callback para la interrupción."""
    distancia = sensor.mesura_distancia()
    print(f"Distancia medida: {distancia:.2f} cm")

    if distancia < DISTANCIA_UMBRAL:
        print("Distancia menor al umbral. Activando el buzzer.")
        buzzer.encendre()
    else:
        print("Distancia segura. Apagando el buzzer.")
        buzzer.apagar()

# Configurar la interrupción en el pin ECHO
GPIO.add_event_detect(ECHO, GPIO.BOTH, callback=activar_buzzer)

try:
    print("Programa en ejecución. Presiona Ctrl+C para salir.")
    while True:
        # El programa principal queda en espera, la interrupción maneja el buzzer
        time.sleep(1)

except KeyboardInterrupt:
    print("Programa interrumpido. Limpiando GPIO...")

finally:
    buzzer.cleanup()
    sensor.cleanup()


