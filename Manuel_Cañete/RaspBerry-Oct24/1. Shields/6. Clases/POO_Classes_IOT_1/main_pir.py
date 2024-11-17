from pir_classe import *

pinpir = 23

pir1 = SensorPIR(pinpir)

try:
    while True:
    
        if pir1.detecta_moviment():
        
            print("Alerta, Pirates !!!")
        
        time.sleep(1)
        
except KeyboardInterrupt:
    
    pir1.cleanup()
    


       