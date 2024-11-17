from distancia_classe import *
from led_classe import *
from multiprocessing import Process, Lock

def control_led(led_pin, min_dist, max_dist, sensor, lock):
    while True:
        # Bloqueamos el acceso al sensor para que solo un proceso lo lea a la vez
        with lock:
            dist = sensor.mesura_distancia()
        
        if min_dist <= dist < max_dist:
            led_pin.encendre()
        else:
            led_pin.apagar()
        time.sleep(0.5)

if __name__ == '__main__':
    try:
        # Crear el sensor de distancia
        distancia = SensorDistancia(trigger_pin = 23, echo_pin = 24)
        leds = [LED(pin = 17), LED(pin = 27), LED(pin = 22)]

        # Crear un Lock para asegurar que solo un proceso lea el sensor a la vez
        lock = Lock()

        # Creación de tres procesos, uno para cada LED
        processes = [
            Process(target=control_led, args=(leds[0], 0, 10, distancia, lock)),
            Process(target=control_led, args=(leds[1], 10, 20, distancia, lock)),
            Process(target=control_led, args=(leds[2], 20, 100, distancia, lock)),
        ]

        # Iniciar todos los procesos
        for p in processes:
            p.start()

        # Esperar a que todos los procesos terminen (aunque en este caso nunca lo harán)
        for p in processes:
            p.join()

    except KeyboardInterrupt:
        for p in processes:
            p.terminate()
            
        for p in processes:
            p.join()
        GPIO.cleanup()
