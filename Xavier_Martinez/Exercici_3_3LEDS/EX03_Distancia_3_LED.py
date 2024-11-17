# Exercici 3: Indicador de Tres Zones amb Multiprocessing
# Indicar tres intervals de distància amb tres LEDs diferents, on cada LED indica una zona de proximitat.

from led_classe import *
from distancia_classe import *
from multiprocessing import Process

led_verde_pin = 12
led_rojo_pin = 16
led_amarillo_pin = 1

trigger_pin = 21
echo_pin = 20

distancia_minima = 6        # Distancia mínima 
distancia_maxima = 16       # Distancia máxima
histeresis = 1              # Histeresis de +-1 cm para evitar oscilaciones
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

    # prueba_conexiones_led()

    try:
        while True:
            distancia = sensor_distancia.mesura_distancia()
            if (RANGO_MIN <= distancia <= RANGO_MAX):                   quit# Filtra valores fuera de rango del sensor
                if distancia < distancia_minima - histeresis:
                    led_rojo.encendre()
                    led_amarillo.apagar()
                    led_verde.apagar()
                if distancia > distancia_maxima + histeresis:
                    led_rojo.apagar()
                    led_amarillo.apagar()
                    led_verde.encendre()
                if (distancia > distancia_minima + histeresis) and (distancia < distancia_maxima - histeresis):
                    led_rojo.apagar()
                    led_amarillo.encendre()
                    led_verde.apagar()
                print(f"Distancia: {distancia:.1f} cm.")
            time.sleep(.5)
            
    except KeyboardInterrupt:
        led_verde.cleanup()
        led_rojo.cleanup()
        sensor_distancia.cleanup()

# if __name__ == '__main__' :
#     main()

if __name__ == '__main__' :
    p = Process(target=check_distancia)
    p.start()
    p.join()



# Ojo: No utilizar 'cleanup()' en 'finally' ya que como que se
# ejecuta siempre, borra la definicion de los pines.
