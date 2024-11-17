import pigpio
import time

# Configuracion de pines
LED_PINS = [17, 27, 22]  # Pines de los LEDs
TRIG_PIN = 23            # Pin TRIG del sensor de distancia
ECHO_PIN = 24            # Pin ECHO del sensor de distancia

# Conecta a pigpio
pi = pigpio.pi()

# Verifica que la conexion con pigpio fue exitosa
if not pi.connected:
    print("Error al conectar con pigpio daemon")
    exit()

# Configura los pines de los LEDs como salida
for pin in LED_PINS:
    pi.set_mode(pin, pigpio.OUTPUT)

# Configura el pin TRIG como salida y el pin ECHO como entrada
pi.set_mode(TRIG_PIN, pigpio.OUTPUT)
pi.set_mode(ECHO_PIN, pigpio.INPUT)

# Define una funcion para medir la distancia
def medir_distancia():
    # Genera un pulso de 10 microsegundos en el pin TRIG
    pi.write(TRIG_PIN, 1)
    time.sleep(0.00001)  # 10 microsegundos
    pi.write(TRIG_PIN, 0)
    
    # Espera a que ECHO pase a alto
    while pi.read(ECHO_PIN) == 0:
        inicio = time.time()
    
    # Espera a que ECHO pase a bajo
    while pi.read(ECHO_PIN) == 1:
        fin = time.time()
    
    # Calcula el tiempo transcurrido y convierte a distancia
    duracion = fin - inicio
    distancia = (duracion * 34300) / 2  # 34300 cm/s es la velocidad del sonido
    return distancia

try:
    while True:
        # Mide la distancia
        distancia = medir_distancia()
        print(f"Distancia: {distancia:.2f} cm")
        
        # Si la distancia es menor a 30 cm, enciende los LEDs en secuencia
        if distancia < 30:
            for pin in LED_PINS:
                pi.write(pin, 1)  # Enciende el LED
                time.sleep(0.5)   # Espera medio segundo
                pi.write(pin, 0)  # Apaga el LED
        else:
            # Si no hay objeto cercano, apaga todos los LEDs
            for pin in LED_PINS:
                pi.write(pin, 0)

        time.sleep(0.1)  # Espera breve antes de la siguiente medicion

except KeyboardInterrupt:
    print("Nos vemos simple mortal")

finally:
    # Limpia y desconecta de pigpio
    for pin in LED_PINS:
        pi.write(pin, 0)  # Apaga cada LED
    pi.stop()
