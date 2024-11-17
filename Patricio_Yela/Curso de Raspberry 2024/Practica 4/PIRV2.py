import RPi.GPIO as GPIO
import time

pinpir = 23
pinled = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinpir, GPIO.IN)
GPIO.setup(pinled, GPIO.OUT)

def intruso_detectado(channel):
    print("Alerta Intruso")
    GPIO.output(pinled, 1)
    time.sleep(0.5)
    GPIO.output(pinled, 0)

# Configuramos el evento para detectar en modo RISING
GPIO.add_event_detect(pinpir, GPIO.RISING, callback=intruso_detectado)

try:
    # Espera indefinidamente mientras se activa el evento
    while True:
        time.sleep(1)  # Pequeña pausa para reducir carga en el CPU

except KeyboardInterrupt:
    print("Detenido por el usuario")

finally:
    GPIO.cleanup()
