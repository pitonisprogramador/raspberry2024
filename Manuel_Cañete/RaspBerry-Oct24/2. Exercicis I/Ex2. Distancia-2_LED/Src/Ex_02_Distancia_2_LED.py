# Exercici 2: Sistema Bicolor amb LEDs per a Dues Distàncies
# Utilitzar dos LEDs (vermell i verd) per indicar si un objecte és a prop (menys de 10 cm) o lluny (més de 10 cm).

from led_classe import *
from distancia_classe import *

led_verde_pin = 12
led_rojo_pin = 16
trigger_pin = 21
echo_pin = 20

distancia_minima = 10       # Distancia de cambio de estado
histeresis = 1              # Histeresis de +-1 cm para evitar oscilaciones
RANGO_MIN = 2               # Mínima distancia (cm) medible por el dispositivo
RANGO_MAX = 400             # Máxima distancia (cm) medible por el dispositivo

def main():
    led_verde = LED(led_verde_pin)
    led_rojo  = LED(led_rojo_pin)
    sensor_distancia = SensorDistancia(trigger_pin, echo_pin)

    try:
        while True:
            distancia = sensor_distancia.mesura_distancia()
            if distancia > RANGO_MIN and distancia < RANGO_MAX:          # Filtra valores fuera de rango del sensor
                if distancia < distancia_minima - histeresis:
                    led_rojo.encendre()
                    led_verde.apagar()
                if distancia > distancia_minima + histeresis:
                    led_rojo.apagar()
                    led_verde.encendre()
                print(f"Distancia: {distancia:.1f} cm.")
            time.sleep(.05)
            
    except KeyboardInterrupt:
        led_verde.cleanup()
        led_rojo.cleanup()
        sensor_distancia.cleanup()

if __name__ == '__main__' :
    main()


# Ojo: No utilizar 'cleanup()' en 'finally' ya que como que se
# ejecuta siempre, borra la definicion de los pines.
