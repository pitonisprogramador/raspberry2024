# Puesta en marcha del sensor PIR (V1)
import RPi.GPIO as GPIO
import time

pinpir = 23

GPIO.setmode(GPIO.BCM)				# Selecciona modo BCM
GPIO.setup(pinpir, GPIO.IN)			# Programa como entrada

while True:
	if GPIO.input(pinpir) == 1:
		pass						# Enviar alerta
	time.sleep(1)

