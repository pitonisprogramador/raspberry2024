# Exercici 4: Alarma de Proximitat amb LED i So
# Encendre un LED i activar un so d'alarma quan un objecte és a menys de 5 cm de distància.
# ==> Mantenim els 3 LEDs de l'exercici anterior i afegim el buzzer en un pin nou
# ==> Fem servir el buzzer actiu

from led_classe import *
from distancia_classe import *
from Active_Buzzer_classe import *
from multiprocessing import Process

buzzer_pin = 26
buzzer2_pin = 19

led_verde_pin = 12
led_rojo_pin = 16
led_amarillo_pin = 1

trigger_pin = 21
echo_pin = 20

distancia_minima = 5        # Distancia mínima 
distancia_maxima = 16       # Distancia máxima
histeresis = 0.5            # Histeresis de 1 cm para evitar oscilaciones

RANGO_MIN = 2               # Mínima distancia (2 cm) medible por el dispositivo
RANGO_MAX = 400             # Máxima distancia (400 cm) medible por el dispositivo

def prueba_conexiones_led():
    """
    Funcion para comprobar que los leds estan correctamente conectados a la Raspberry Pi
    """
    led_verde.encendre()
    time.sleep(1)
    led_verde.apagar()
    time.sleep(1)

    led_amarillo.encendre()
    time.sleep(1)
    led_amarillo.apagar()
    time.sleep(1)

    led_rojo.encendre()
    time.sleep(1)
    led_rojo.apagar()
    time.sleep(1)


def check_distancia():
    led_verde = LED(led_verde_pin)
    led_amarillo = LED(led_amarillo_pin)
    led_rojo  = LED(led_rojo_pin)

    sensor_distancia = SensorDistancia(trigger_pin, echo_pin)

    buzzer = Buzzer(buzzer_pin)
    buzzer2 = Buzzer(buzzer2_pin)

    # prueba_conexiones_led()

    try:
        while True:
            distancia = sensor_distancia.mesura_distancia()
            if (RANGO_MIN <= distancia <= RANGO_MAX):                   # Filtra valores fuera de rango del sensor
                if distancia < distancia_minima - histeresis:
                    """ 0 < distancia < distancia_minima """
                    buzzer.encendre()
                    buzzer2.encendre()
                    led_rojo.encendre()
                    led_amarillo.apagar()
                    led_verde.apagar()
                if distancia > distancia_maxima + histeresis:
                    """ distancia_minima < distancia < distancia_maxima """
                    buzzer.apagar()
                    buzzer2.apagar()
                    led_rojo.apagar()
                    led_amarillo.apagar()
                    led_verde.encendre()
                if (distancia > distancia_minima + histeresis) and (distancia < distancia_maxima - histeresis):
                    """ distancia > distancia_maxima """
                    buzzer.apagar()
                    buzzer2.apagar()
                    led_rojo.apagar()
                    led_amarillo.encendre()
                    led_verde.apagar()
                print(f"Distancia: {distancia:.1f} cm.")
            time.sleep(.2)
            
    except KeyboardInterrupt:
        led_verde.cleanup()
        led_rojo.cleanup()
        sensor_distancia.cleanup()
        buzzer.apagar()
        buzzer2.cleanup()
        

# if __name__ == '__main__' :
#     main()

if __name__ == '__main__' :
    p = Process(target=check_distancia)
    p.start()
    p.join()



# Ojo: No utilizar 'cleanup()' en 'finally' ya que como que se
# ejecuta siempre, borra la definicion de los pines.
