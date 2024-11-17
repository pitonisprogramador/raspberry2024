import time

# Funció per mostrar hola1 cada 5 segons
def hola1():
    print("hola1")

# Funció per mostrar hola2 cada 1 segon
def hola2():
    print("hola2")

# Configuració dels intervals per a cada missatge
interval_hola1 = 5
interval_hola2 = 1

# Temps inicials per a cada missatge
last_time_hola1 = time.time()
last_time_hola2 = time.time()

# Bucle principal per gestionar els intervals
while True:
    current_time = time.time()
    
    # Comprova si ha passat l'interval per a hola1
    if current_time - last_time_hola1 >= interval_hola1:
        hola1()
        last_time_hola1 = current_time  # Actualitza el temps de l'últim missatge
    
    # Comprova si ha passat l'interval per a hola2
    if current_time - last_time_hola2 >= interval_hola2:
        hola2()
        last_time_hola2 = current_time  # Actualitza el temps de l'últim missatge
    
    # Petit retard per no sobrecarregar la CPU
    time.sleep(0.01)
