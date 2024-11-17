from distancia_classe import *
from pir_classe import *
from led_classe import *
from multiprocessing import Process, Lock

lock = Lock()

def control_leds_by_distance(led_pin, min_dist, max_dist):
    while True:
        with lock:
            dist = distancia.mesura_distancia()
        
        if min_dist <= dist < max_dist:
            led_pin.encendre()
        else:
            led_pin.apagar()
        time.sleep(0.5)

def control_leds_by_pir():
    while True:
        with lock:
            if pir.detecta_moviment():
                for pin in range(len(leds)):
                    leds[pin].encendre()
                time.sleep(1)
                for pin in range(len(leds)):
                    leds[pin].apagar()
                time.sleep(1)

if __name__ == '__main__':
    pir = SensorPIR(pir_pin = 4)
    distancia = SensorDistancia(trigger_pin = 23, echo_pin = 24)
    leds = [LED(pin = 17), LED(pin = 27), LED(pin = 22)]

    processes = [
        Process(target=control_leds_by_distance, args=(leds[0], 0, 10)),
        Process(target=control_leds_by_distance, args=(leds[1], 10, 20)),
        Process(target=control_leds_by_distance, args=(leds[2], 20, 100)),
        Process(target=control_leds_by_pir)
    ]

    for p in processes:
        p.start()
    for p in processes:
        p.join()