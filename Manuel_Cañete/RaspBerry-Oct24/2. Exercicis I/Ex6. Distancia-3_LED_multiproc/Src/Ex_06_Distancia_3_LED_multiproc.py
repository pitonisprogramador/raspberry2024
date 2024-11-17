# Exercici 6: Indicador de Distància amb Multiprocessing (Múltiples Processos)
# Utilitzar tres processos paral·lels per controlar tres LEDs diferents, 
# cadascun associat a un interval de distància diferent (0-10 cm, 10-20 cm i més de 20 cm). 
# Cada procés controla un LED en funció d'un interval de distància específic, 
# permetent que els LEDs s'encenguin i s'apaguin independentment segons la distància de l'objecte detectat.

from led_classe import *
from distancia_classe import *
from Active_Buzzer_classe import *
from multiprocessing import Process, Semaphore
import RPi.GPIO as GPIO

buzzer_pin = 26

# led_azul_pin = 7
led_verde_pin = 12
led_rojo_pin = 16
led_amarillo_pin = 1

trigger_pin = 21
echo_pin = 20

distancia_minima = 5        # Distancia mínima 
# distancia_media = 10        # Distancia media
distancia_maxima = 15       # Distancia máxima

RANGO_MIN = 2               # Mínima distancia (2 cm) medible por el dispositivo
RANGO_MAX = 400             # Máxima distancia (400 cm) medible por el dispositivo

# Declaración de los dispositivos
led_verde = LED(led_verde_pin)
led_amarillo = LED(led_amarillo_pin)
led_rojo = LED(led_rojo_pin)
# led_azul = LED(led_azul_pin)

sensor_distancia = SensorDistancia(trigger_pin, echo_pin)

# buzzer = Buzzer(buzzer_pin)

sem = Semaphore(1)          # Semáforo para coordinar acceso al medidor

def control_led(led, dmin, dmax):
    #global sem

    while True:
        sem.acquire()       # Bloquea el semáforo
    
        try:
            distancia = sensor_distancia.mesura_distancia()

            if (dmin <= distancia < dmax):
                led.encendre()
                # print(f"Distancia: {distancia:.1f} cm. [{dmin} cm. - {dmax} cm.]")

            else:
                led.apagar()         

            # print(f"Distancia: {distancia:.1f} cm. [{dmin}-{dmax}]")
        
        finally:
            sem.release()           # Libera semáforo
        
        time.sleep(.2)              # Retardo antes de la siguiente medida

# if __name__ == '__main__' :
#     main()

if __name__ == '__main__':
    try:
        lista_procesos = [
            Process(target=control_led, args=(led_rojo, RANGO_MIN, distancia_minima)),
            Process(target=control_led, args=(led_amarillo, distancia_minima, distancia_maxima)),
            Process(target=control_led, args=(led_verde, distancia_maxima, RANGO_MAX))
        ]
        for led in lista_procesos:
            led.start()

        for led in lista_procesos:
            led.join()

    except KeyboardInterrupt:
        print("\nAturant processos...")
        for led in lista_procesos:
            led.terminate()
            led.join()
        '''for led in lista_procesos:
            led.join()'''

        '''led_rojo.cleanup()
        led_amarillo.cleanup()
        led_verde.cleanup()
        sensor_distancia.cleanup()'''
        GPIO.cleanup()
        print("\nDispositius netejats!")

