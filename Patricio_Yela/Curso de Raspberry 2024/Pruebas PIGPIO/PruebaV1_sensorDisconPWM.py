import pigpio
import time
import threading

# Configuracion de pines
LED_PINS = [17, 27, 22]                  # Pines de los LEDs
TRIG_PIN = 23                             # Pin TRIG del sensor de distancia
ECHO_PIN = 24                             # Pin ECHO del sensor de distancia

# Conecta a pigpio
pi = pigpio.pi()

# Verifica que la conexion con pigpio fue exitosa
if not pi.connected:
    print("Error al conectar con pigpio daemon")
    exit()

# Configura el pin TRIG como salida y el pin ECHO como entrada
pi.set_mode(TRIG_PIN, pigpio.OUTPUT)
pi.set_mode(ECHO_PIN, pigpio.INPUT)

# Variable global para almacenar la distancia
distancia = 100                           # Inicializamos con un valor alto para que los LEDs inicien apagados
DISTANCIA_ACTIVACION = 30                 # Distancia limite para activar los LEDs
medicion_activa = True                    # Controla el ciclo de medicion

# Funcion para medir distancia continuamente en un hilo separado
def hilo_medicion_distancia():
    global distancia, medicion_activa
    while medicion_activa:
        try:
            # Genera un pulso de 10 microsegundos en el pin TRIG
            pi.write(TRIG_PIN, 1)
            time.sleep(0.00001)               # 10 microsegundos
            pi.write(TRIG_PIN, 0)
            
            # Temporizador para evitar que el bucle se bloquee
            inicio = time.time()
            timeout = inicio + 0.05           # Timeout de 50ms para evitar bloqueos
            
            # Espera a que ECHO pase a alto, con timeout
            while pi.read(ECHO_PIN) == 0 and time.time() < timeout:
                inicio = time.time()
            
            # Espera a que ECHO pase a bajo, con timeout
            timeout = inicio + 0.05           # Otro timeout de 50ms
            while pi.read(ECHO_PIN) == 1 and time.time() < timeout:
                fin = time.time()
            
            # Calcula el tiempo transcurrido y convierte a distancia
            duracion = fin - inicio
            distancia = (duracion * 34300) / 2  # 34300 cm/s es la velocidad del sonido
            print(f"Distancia: {distancia:.2f} cm")
            
            # Espera breve antes de la siguiente medicion
            time.sleep(0.1)

        except Exception as e:
            print(f"Error al medir distancia: {e}")
            distancia = 100  # Reinicia distancia a un valor seguro en caso de error

# Inicia el hilo para la medicion de distancia
hilo_distancia = threading.Thread(target=hilo_medicion_distancia)
hilo_distancia.start()

try:
    while True:
        # Si la distancia es menor a DISTANCIA_ACTIVACION, enciende los LEDs con PWM en secuencia
        if distancia < DISTANCIA_ACTIVACION:
            for pin in LED_PINS:
                for brillo in range(0, 256, 25):        # Aumenta el brillo de 0 a 255
                    pi.set_PWM_dutycycle(pin, brillo)
                    time.sleep(0.05)
                for brillo in range(255, -1, -25):      # Reduce el brillo de 255 a 0
                    pi.set_PWM_dutycycle(pin, brillo)
                    time.sleep(0.05)
        else:
            # Si no hay objeto cercano, apaga todos los LEDs
            for pin in LED_PINS:
                pi.set_PWM_dutycycle(pin, 0)           # Asegura que los LEDs esten apagados

except KeyboardInterrupt:
    print("Programa interrumpido")
    medicion_activa = False  # Detenemos el ciclo de medicion

finally:
    # Espera a que el hilo de medicion termine
    hilo_distancia.join()
    # Limpia y desconecta de pigpio
    for pin in LED_PINS:
        pi.set_PWM_dutycycle(pin, 0)                   # Apaga cada LED
    pi.stop()
