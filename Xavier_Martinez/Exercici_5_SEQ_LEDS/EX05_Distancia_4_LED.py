# Exercici 5: Patró de Senyalització Seqüencial amb LEDs
# Crear un patró seqüencial d'encesa de quatre LEDs en funció de la proximitat de l'objecte detectat.
# ==> Mantenim els 3 LEDs de l'exercici anterior i el buzzer actiu, i afegim el quart LED
# ==> Incorporamos un semáforo para acceder correctamente al GPIO de la RBPi


from led_classe import *
from distancia_classe import *
from Active_Buzzer_classe import *
from multiprocessing import Process, Semaphore

buzzer_pin = 26

led_azul_pin = 7
led_verde_pin = 12
led_rojo_pin = 16
led_amarillo_pin = 1

trigger_pin = 21
echo_pin = 20

distancia_minima = 5        # Distancia mínima 
distancia_media = 10        # Distancia media
distancia_maxima = 16       # Distancia máxima

RANGO_MIN = 2               # Mínima distancia (2 cm) medible por el dispositivo
RANGO_MAX = 400             # Máxima distancia (400 cm) medible por el dispositivo

# Declaración de los dispositivos
led_verde = LED(led_verde_pin)
led_amarillo = LED(led_amarillo_pin)
led_rojo = LED(led_rojo_pin)
led_azul = LED(led_azul_pin)

sensor_distancia = SensorDistancia(trigger_pin, echo_pin)

buzzer = Buzzer(buzzer_pin)

sem = Semaphore(1)          # Semaforo para coordinar acceso al GPIO

def check_distancia():
    while True:
        sem.acquire()       # Bloquea el semáforo
    
        try:
            distancia = sensor_distancia.mesura_distancia()

            if (RANGO_MIN <= distancia <= distancia_minima):
                """ 0 < distancia <= distancia_minima: ROJO + BUZZER """
                buzzer.encendre()           # BUZZER
                led_rojo.encendre()         # ROJO
                led_amarillo.apagar()
                led_verde.apagar()
                led_azul.apagar()

            elif (distancia_minima < distancia <= distancia_media):
                """ distancia_minima < distancia < distancia_media: AMARILLO """
                buzzer.apagar()
                led_rojo.apagar()
                led_amarillo.encendre()     # AMARILLO
                led_verde.apagar()
                led_azul.apagar()

            elif (distancia_media < distancia <= distancia_maxima):
                """ distancia_media < distancia < distancia_maxima: VERDE """
                buzzer.apagar()
                led_rojo.apagar()
                led_amarillo.apagar()
                led_verde.encendre()        # VERDE
                led_azul.apagar()

            elif (distancia_maxima < distancia <= RANGO_MAX):
                """ distancia_maxima < distancia: AZUL """
                buzzer.apagar()
                led_rojo.apagar()
                led_amarillo.apagar()
                led_verde.apagar()
                led_azul.encendre()         # AZUL

            else:
                """ Fuera del rango del medidor de distancia """
                buzzer.apagar()
                led_rojo.apagar()
                led_amarillo.apagar()
                led_verde.apagar()
                led_azul.apagar()         

            print(f"Distancia: {distancia:.1f} cm.")
        
        finally:
            sem.release()           # Libera semáforo
        
        time.sleep(.2)              # Retardo antes de la siguiente medida

# if __name__ == '__main__' :
#     main()

if __name__ == '__main__' :
    try:
        p = Process(target=check_distancia)
        p.start()
        p.join()

    except KeyboardInterrupt:
        print("\nAturant processos...")
        p.terminate()
        p.join()
        led_verde.cleanup()
        led_rojo.cleanup()
        led_amarillo.cleanup()
        led_azul.cleanup()
        sensor_distancia.cleanup()
        print("\nDispositius netejats!")

