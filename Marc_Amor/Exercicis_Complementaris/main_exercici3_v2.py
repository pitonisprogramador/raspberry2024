from distancia_classe import *
from led_classe import *
from multiprocessing import Process

def check_distance():
    while True:
        dist = distancia.mesura_distancia()
        if dist < 10:
            led1.encendre()
            led2.apagar()
            led3.apagar()
        elif 10 <= dist < 20:
            led1.apagar()
            led2.encendre()
            led3.apagar()
        else:
            led1.apagar()
            led2.apagar()
            led3.encendre()
        time.sleep(0.5)

if __name__ == '__main__':
    try:
        distancia = SensorDistancia(trigger_pin = 23, echo_pin = 24)
        led1 = LED(pin = 17)
        led2 = LED(pin = 27)
        led3 = LED(pin = 22)
        p = Process(target=check_distance)
        p.start()
        p.join()
    except KeyboardInterrupt:
        p.terminate()
        p.join()
        GPIO.cleanup()