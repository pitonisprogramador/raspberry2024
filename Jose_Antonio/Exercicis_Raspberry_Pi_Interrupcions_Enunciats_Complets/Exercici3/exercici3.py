import time
import RPi.GPIO as GPIO
from distancia_classe import SensorDistancia
from led_classe import LED

# Definir pines
TRIG = 27
ECHO = 22
RED_LED_PIN = 17
YELLOW_LED_PIN = 18

# Crear instancias de los objetos
sensor = SensorDistancia(TRIG, ECHO)
led_rojo = LED(RED_LED_PIN)
led_amarillo = LED(YELLOW_LED_PIN)

distancia_medida = 0  # Variable global para guardar la distancia

def medir_distancia(channel):
    """Callback que mide la distancia cuando ocurre un evento en el pin ECHO."""
    global distancia_medida
    distancia_medida = sensor.mesura_distancia()
    print(f"Distancia medida: {distancia_medida:.2f} cm")
    
    # Controlar LEDs basado en la distancia
    if distancia_medida < 10:
        led_rojo.encendre()
        led_amarillo.apagar()
    elif 10 <= distancia_medida <= 20:
        led_rojo.apagar()
        led_amarillo.encendre()
    else:
        led_rojo.apagar()
        led_amarillo.apagar()

# Configuración de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Configurar interrupción en el pin ECHO
GPIO.add_event_detect(ECHO, GPIO.FALLING, callback=medir_distancia, bouncetime=300)

try:
    print("Programa en ejecución. Presiona Ctrl+C para salir.")
    while True:
        # Generar un pulso en TRIG periódicamente
        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.00001)  # Pulso de 10 microsegundos
        GPIO.output(TRIG, GPIO.LOW)
        time.sleep(1)  # Espera 1 segundo para la siguiente medición

except KeyboardInterrupt:
    print("Programa finalizado por el usuario")

finally:
    # Limpiar la configuración de GPIO
    sensor.cleanup()
    led_rojo.cleanup()
    led_amarillo.cleanup()
