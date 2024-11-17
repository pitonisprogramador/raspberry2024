# 9: Indicador de Moviment amb PIR, Buzzer Passiu i LED (Time Slicing) 
# Utilitzar un brunzidor passiu i un LED per alertar de moviments detectats pel sensor PIR, 
# amb *time slicing* per alternar el so i la llum. 
# Solució en codi: 
# Solució en codi Python 
import RPi.GPIO as GPIO 
import time 
 
GPIO.setmode(GPIO.BCM) 
PIR_PIN = 4 
LED_PIN = 17 
BUZZER_PIN = 18 
 
GPIO.setup(PIR_PIN, GPIO.IN) 
GPIO.setup(LED_PIN, GPIO.OUT) 
GPIO.setup(BUZZER_PIN, GPIO.OUT) 
 
def alert_with_time_slicing(): 
    while True: 
        if GPIO.input(PIR_PIN): 
            GPIO.output(LED_PIN, True) 
            GPIO.output(BUZZER_PIN, True) 
            time.sleep(0.5) 
            GPIO.output(LED_PIN, False) 
            GPIO.output(BUZZER_PIN, False) 
            time.sleep(0.5) 
        else: 
            GPIO.output(LED_PIN, False) 
            GPIO.output(BUZZER_PIN, False) 
            time.sleep(0.5) 
 
try: 
	alert_with_time_slicing() 
	except KeyboardInterrupt: 
	GPIO.cleanup()