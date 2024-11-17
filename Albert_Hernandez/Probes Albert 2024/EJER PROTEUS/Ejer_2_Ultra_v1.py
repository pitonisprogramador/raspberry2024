import RPi.GPIO as GPIO
import time

# GPIO modo BCM (Nomenclatura)
GPIO.setmode(GPIO.BCM)

# DEFINE PINS
TRIG_PIN = 23                           # GPIO23 Activa Detector
ECHO_PIN = 24                           # GPIO24 Objeto Detectado

# CONFIGURACIÓN PIN's (IN,OUT)
GPIO.setup(TRIG_PIN, GPIO.OUT)          # PIN 23: OUT
GPIO.setup(ECHO_PIN, GPIO.IN)           # PIN 24: IN

# Detección/Medición distancia()
def measure_distance():
    # Me aseguro TRIG_PIN a "0"
    GPIO.output(TRIG_PIN, False)        # PIN 23: Pongo a "0"
    time.sleep(0.1)                     # Espero Ojitos se estabilice

    # Pulso disparo corto TRIG_PIN
    GPIO.output(TRIG_PIN, True)         # PIN 23: Pongo a "1"
    time.sleep(0.00001)                 # 
    GPIO.output(TRIG_PIN, False)        # PIN 23: Pongo a "0"

    # Espera que ECHO_PIN detecte
    while GPIO.input(ECHO_PIN) == 0:    # Mientras ECHO_PIN = "0"
        pulse_start = time.time()       # variable "pulse_start" = tiempo actual

    # Espera que ECHO_PIN termine
    while GPIO.input(ECHO_PIN) == 1:    # Mientras ECHO_PIN = "1"
        pulse_end = time.time()         # variable "pulse_end"   = tiempo actual

    # Calcula tiempo de detección objeto
    pulse_duration = pulse_end - pulse_start

    # Calculate distance in centimeters
    distance = (pulse_duration * 34300) / 2

    return distance



# VOID MAIN

try:
    while True:                             # BUCLE: Infinito
        dist = measure_distance()           # variable "dist" = función "measure_distance()"
        print(f"Distancia: {dist:.2f} cm")  # print ("mensaje")
        time.sleep(1)                       # Espero 1Seg, siguiente medición

except KeyboardInterrupt:                   # EXCEPCIÓN: Teclado
    GPIO.cleanup()                          # Clean up GPIO on Ctrl+C
    

finally:                                    # FINALMENTE:
    GPIO.cleanup()                          # Clean up GPIO on script exit
    