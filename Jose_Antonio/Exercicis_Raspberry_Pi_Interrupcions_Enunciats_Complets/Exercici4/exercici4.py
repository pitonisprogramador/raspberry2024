import time
import RPi.GPIO as GPIO
from sensor_pir import SensorPIR  # Asegúrate de que el archivo se llame sensor_pir.py
from buzzer import Buzzer        # Asegúrate de que el archivo se llame buzzer.py
from led import LED              # Asegúrate de que el archivo se llame led.py

# Definir los pines
PIR_PIN = 23
BUZZER_PIN = 18
LED_PIN = 17

# Crear instancias de los objetos
sensor_pir = SensorPIR(PIR_PIN)
buzzer = Buzzer(BUZZER_PIN)
led = LED(LED_PIN)

def alarma_seqüencial(channel):
    """Secuencia de alarma: Buzzer suena, LED parpadea."""
    buzzer.sonar_durant(1)  # Hace sonar el buzzer durante 1 segundo
    led.encendre()          # Enciende el LED
    time.sleep(2)           # Mantiene el LED encendido durante 2 segundos
    led.apagar()            # Apaga el LED

# Configurar GPIO
GPIO.setmode(GPIO.BCM)  # Usar numeración BCM de los pines GPIO
GPIO.setup(PIR_PIN, GPIO.IN)  # Configurar el pin PIR como entrada
GPIO.setup(BUZZER_PIN, GPIO.OUT)  # Configurar el pin del buzzer como salida
GPIO.setup(LED_PIN, GPIO.OUT)  # Configurar el pin LED como salida

# Configurar la interrupción para detectar movimiento en el PIR
GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=alarma_seqüencial, bouncetime=300)

try:
    # El programa ahora solo espera la interrupción, no necesita un bucle constante
    while True:
        time.sleep(1)  # Solo esperar, sin necesidad de comprobar constantemente el PIR

except KeyboardInterrupt:
    print("Programa finalizado")

finally:
    # Limpiar la configuración de GPIO al final
    sensor_pir.cleanup()
    buzzer.cleanup()
    led.cleanup()
    GPIO.cleanup()  # Limpiar configuración GPIO
