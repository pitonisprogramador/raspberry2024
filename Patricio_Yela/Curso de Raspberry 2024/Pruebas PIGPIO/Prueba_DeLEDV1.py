import pigpio
import time

# Configura los pines GPIO donde tienes conectados los LEDs
LED_PINS = [17, 27, 22]  # Cambia estos numeros segun los pines que uses para cada LED

# Conecta a pigpio
pi = pigpio.pi()

# Verifica que la conexion con pigpio fue exitosa
if not pi.connected:
    print("Error al conectar con pigpio daemon")
    exit()

# Configura los pines de los LEDs como salidas
for pin in LED_PINS:
    pi.set_mode(pin, pigpio.OUTPUT)

try:
    while True:
        # Enciende cada LED en secuencia
        for pin in LED_PINS:
            pi.write(pin, 1)  # Enciende el LED
            time.sleep(0.5)   # Espera medio segundo
            pi.write(pin, 0)  # Apaga el LED

except KeyboardInterrupt:
    print("Programa interrumpido")

finally:
    # Limpia y desconecta de pigpio
    for pin in LED_PINS:
        pi.write(pin, 0)  # Apaga cada LED
    pi.stop()
