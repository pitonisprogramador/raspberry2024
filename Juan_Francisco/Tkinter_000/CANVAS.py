import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, width= root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack()

#########################################  CIRCULOS  ########################################
def circulo(x,y,ancho, grueso, corte):
    x1=x+ancho
    y1=y+ancho
    canvas.create_oval(x, y, x1, y1, width=grueso, dash = corte, fill='blue')

circulo(700,850,20,20,1) # CIRCULO
circulo(100,100,100,10,1) # ARO
circulo(100,700,100,10,25) # ARO CORTADO
circulo(1000,100,4,100,1) # ESTRELLA
circulo(1000, 550,25,100,1)# DENTADO
circulo(600, 350,33,1,1)# ANILLA

izq = 250
abajo = 350
coordinates = 53+izq, 53+abajo, 140+izq, 140+abajo 
arc = canvas.create_arc(coordinates, start=0, extent=120, fill="red")
arc = canvas.create_arc(coordinates, start=120, extent=120, fill="blue")
arc = canvas.create_arc(coordinates, start=240, extent=120, fill="yellow")

#########################################  CUADRADOS  #######################################
def cuadrado(x,y,lado,color):
    x1=x+lado
    y1=y+lado    
    canvas.create_rectangle(x, y, x1, y1, fill=color)

cuadrado(1000,500,50,'orange')
cuadrado(500,500,100,'red')
cuadrado(450,100,75,'yellow')

def rectangulo_horizontal(x,y,lado,color):
    pass

def rectangulo_vertical(x,y,lado,color):
    pass

##########################################  LINEAS  #########################################
grosor = 5 
coordinates = 50, 50, 250, 250,
canvas.create_line(coordinates, fill="blue", width=grosor)

coordinates = 250, 50, 50, 250, 
canvas.create_line(coordinates, fill="red", dash = 10, width=grosor)

coordinates = 0, 10, 100, 10, 
arc = canvas.create_line(coordinates, fill="grey",dash = 10, width=grosor)

coordinates = 10, 0, 10, 150, 
arc = canvas.create_line(coordinates, fill="yellow", width=grosor)

arc = canvas.create_line(1100,200,1100,450, fill="green", width=grosor+100)

arc = canvas.create_line(400,700,900,400, fill="grey",dash = 10, width=grosor)



canvas.create_polygon(100, 10, 100, 60, 50, 35, fill='blue', outline='white')

canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85, width=5)

canvas.create_text(1000, 100, text="¡Hola, Canvas!", fill="white")

canvas.config(bg = 'cyan')

root.mainloop()
