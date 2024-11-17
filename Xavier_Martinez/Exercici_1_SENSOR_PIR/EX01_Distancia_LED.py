# Exercici 1: Sistema de Distància amb Indicador LED (Sense PWM)
# Utilitzar el sensor HC-SR04 per mesurar la proximitat d'un objecte i 
# encendre un LED quan aquest es trobi a menys de 15 cm. 
# Si l'objecte és més lluny, el LED s'apaga.

from led_classe import *
from distancia_classe import *

led_pin = 12
trigger_pin = 21
echo_pin = 20

distancia_minima = 15       # Distancia mínima en cm
histeresis = 1              # Histeresis de +-1 cm para evitar oscilaciones
RANGO_MIN = 2               # Mínima distancia (cm) medible por el dispositivo
RANGO_MAX = 400             # Máxima distancia (cm) medible por el dispositivo

def main():
    led = LED(led_pin)
    sensor_distancia = SensorDistancia(trigger_pin, echo_pin)

    try:
        while True:
            distancia = sensor_distancia.mesura_distancia()
            if distancia > RANGO_MIN and distancia < RANGO_MAX:          # Filtra valores fuera de rango
                if distancia < distancia_minima - histeresis:
                    led.encendre()
                if distancia > distancia_minima + histeresis:
                    led.apagar()
                print(f"Distancia: {distancia:.1f} cm.")
            time.sleep(.05)
            
    except KeyboardInterrupt:
        led.cleanup()
        sensor_distancia.cleanup()

if __name__ == '__main__' :
    main()


# Ojo: No utilizar 'cleanup()' en 'finally' ya que como que se
# ejecuta siempre, borra la definicion de los pines.
