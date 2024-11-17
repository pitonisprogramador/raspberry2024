from pir_classe import *
from led_classe import *
import RPi.GPIO as GPIO
import time

def main():
    pir_pin = 23
    led_pin = 17

    # Inicializamos las clases
    sensor = SensorPIR(pir_pin)
    led = LED(led_pin)

    # Callback para manejar la detección de movimiento
    def manejar_movimiento(channel):
        print("Movimiento detectado!")
        led.encendre()
        time.sleep(2)  # LED encendido por 2 segundos
        led.apagar()

    try:
        # Configurar la interrupción para el pin del sensor PIR
        GPIO.add_event_detect(pir_pin, GPIO.RISING, callback=manejar_movimiento, bouncetime=200)

        # Mantener el programa activo
        print("Presiona Ctrl+C para finalizar.")
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("Programa finalizado")

    finally:
        sensor.cleanup()
        led.cleanup()
        GPIO.remove_event_detect(pir_pin)  # Limpiar interrupciones

if __name__ == "__main__":
    main()
