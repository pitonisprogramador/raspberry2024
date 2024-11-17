import time
import RPi.GPIO as GPIO
from sensor_distancia import SensorDistancia  # Asegúrate de que este archivo se llama sensor_distancia.py
from buzzer import Buzzer                    # Asegúrate de que este archivo se llama buzzer.py
from led import LED                          # Asegúrate de que este archivo se llama led.py

# Definir los pines
TRIG_PIN = 23
ECHO_PIN = 24
BUZZER_PIN = 18
GREEN_LED_PIN = 17
BLUE_LED_PIN = 27

# Crear instancias de los objetos
sensor_distancia = SensorDistancia(TRIG_PIN, ECHO_PIN)
buzzer = Buzzer(BUZZER_PIN)
green_led = LED(GREEN_LED_PIN)
blue_led = LED(BLUE_LED_PIN)

def alerta_buzzer_leds(channel):
    """Gestiona la alarma y los LEDs según la distancia medida cuando se activa la interrupción."""
    distancia = sensor_distancia.mesura_distancia()  # Medir la distancia
    
    if distancia < 10:
        # Si la distancia es menor de 10 cm, activar buzzer y LED verde
        buzzer.sonar_durant(1)  # Hace sonar el buzzer durante 1 segundo
        green_led.encendre()     # Enciende el LED verde
        blue_led.apagar()       # Apaga el LED azul
    elif distancia > 20:
        # Si la distancia es mayor de 20 cm, desactivar buzzer y activar LED azul
        buzzer.apagar()          # Apaga el buzzer
        green_led.apagar()       # Apaga el LED verde
        blue_led.encendre()     # Enciende el LED azul
    else:
        # Si la distancia está entre 10 y 20 cm, desactivar todos los componentes
        buzzer.apagar()          # Apaga el buzzer
        green_led.apagar()       # Apaga el LED verde
        blue_led.apagar()       # Apaga el LED azul

# Configuración de las interrupciones
GPIO.setmode(GPIO.BCM)
GPIO.setup(ECHO_PIN, GPIO.IN)  # Configurar el pin ECHO como entrada
GPIO.setup(TRIG_PIN, GPIO.OUT)  # Configurar el pin TRIG como salida
GPIO.setup(BUZZER_PIN, GPIO.OUT)  # Configurar el pin del buzzer
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)  # Configurar el pin LED verde
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)  # Configurar el pin LED azul

# Configurar la interrupción
GPIO.add_event_detect(ECHO_PIN, GPIO.BOTH, callback=alerta_buzzer_leds)

try:
    # El programa principal sigue corriendo y espera a las interrupciones
    while True:
        time.sleep(1)  # Puede hacer otras tareas si es necesario

except KeyboardInterrupt:
    print("Programa finalizado")

finally:
    # Limpiar configuraciones de GPIO al finalizar
    sensor_distancia.cleanup()
    buzzer.cleanup()
    green_led.cleanup()
    blue_led.cleanup()
    GPIO.cleanup()
