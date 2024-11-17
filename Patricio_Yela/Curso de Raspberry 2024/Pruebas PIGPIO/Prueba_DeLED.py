import pigpio
import time

# Configura el pin GPIO donde tienes el LED conectado
LED_PIN = 17  # Cambia este numero segun el pin que uses

# Conecta a pigpio
pi = pigpio.pi()

# Verifica que la conexion con pigpio fue exitosa
if not pi.connected:
    print("Error al conectar con pigpio daemon")
    exit()

# Configura el pin del LED como salida
pi.set_mode(LED_PIN, pigpio.OUTPUT)

try:
    while True:
        # Enciende el LED
        pi.write(LED_PIN, 1)
        time.sleep(1)  # Espera 1 segundo

        # Apaga el LED
        pi.write(LED_PIN, 0)
        time.sleep(1)  # Espera 1 segundo
except KeyboardInterrupt:
    print("Programa interrumpido")

finally:
    # Limpia y desconecta de pigpio
    pi.write(LED_PIN, 0)  # Asegurate de apagar el LED
    pi.stop()
