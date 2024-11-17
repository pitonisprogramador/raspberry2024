# Puesta en marcha del sensor PIR (V2)
# Se añade detección de eventos y encendido de un led
import RPi.GPIO as GPIO
import time

def intruso_detectado(channel):
	print("Intruso")
	GPIO.output(pinled, GPIO.HIGH)		# Activa LED
	time.sleep(0.5)
	GPIO.output(pinled, GPIO.LOW)		# Desactiva LED
	
#	GPIO.remove_event_detect(pinpir)
#	GPIO.add_event_detect(pinpir, GPIO.RISING, callback=intruso_detectado, bouncetime=300) 


pinpir = 23
pinled = 24

GPIO.setmode(GPIO.BCM)			# Selecciona modo BCM (Funcionalidad)
GPIO.setup(pinpir, GPIO.IN)		# Programa como entrada
GPIO.setup(pinled, GPIO.OUT)    # Programa como PIN salida


#GPIO.setup(pinpir, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)		# Programa como entrada
#GPIO.setup(pinled, GPIO.OUT, initial=GPIO.LOW)				# Programa como PIN salida y inicialmente apagado

#GPIO.add_event_detect(pinpir, GPIO.RISING, callback=detect_intrusos, bouncetime=300)
 
GPIO.add_event_detect(pinpir, GPIO.RISING, callback=intruso_detectado) 


try:
	while True:
#		print("\nWorking...", 'H' if GPIO.input(pinpir)==GPIO.HIGH else 'L')
		time.sleep(1)

except KeyboardInterrupt:
	print("Programa finalizado por el usuario")

finally:
    GPIO.cleanup()

'''
apt install python3-rpi-lgpio
Ha calgut aquest comandament per utilitzar aquest codi d'interrupcions
Aquest codi l'hem provat per canviar el paradigma
while True:
    if GPIO.input(pirpin) == 1:
        print("Alerta intrusos")
    time.sleep(1)   
'''