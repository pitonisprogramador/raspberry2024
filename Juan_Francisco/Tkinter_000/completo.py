import tkinter as tk
import tkinter.ttk as ttk
import re

vlist = ["combo1", "Option2", "Option3", "Option4", "Option5"]
          
          
def kombo():
    print(Combo.get())
 
def normal():
     print("normal")
 
           
def regex():
    dni =e1.get()
    patro = re.compile("^[1-9]{1}[0-9]{7}[A-Z]{1}$")   
    print(patro.findall(dni))

def on_button_click():
    print("¡Botón presionado!")
    print(scale1.get())
    print(var.get())
    print(cb_var.get())
    print(entry.get())
    print(text_area.get('1.0', tk.END))
    entry.delete(0,tk.END)
    text_area.delete('1.0', tk.END)
    listbox.insert(0, "XXXXXXXX")
    listbox.insert(2, "AAAAAAAA")
    listbox.insert(10, "????????")
    label.config(text = "oooooooooooooo")
    button.config(text = "SIIIIIIIIIII")
    canvas.config(bg="yellow")
    canvas.create_rectangle(50, 20, 150, 80, fill="blue")
    frame.config(bg="black")
    root.title("MASTER")
    Label1.destroy()
def o():
    print(scale1.get())
    
def SELF(self):
    print(scale1.get())    


    
    
root = tk.Tk()
root.title("TITULO DE LA VENTANA")


amplada = root.winfo_screenwidth()
alcada = root.winfo_screenheight()
#strink = f"{amplada}x{alcada}"
#root.geometry(strink)

print(amplada, alcada)


frame = tk.Frame(root, bg="lightgray")
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="TITULO CENTRAL")
label.pack()
#-----------------------------------------------------------------------
separator = ttk.Separator(frame,orient= tk.HORIZONTAL)
separator.pack(expand = True, fill = tk.X)

sep = ttk.Separator(frame,orient= tk.VERTICAL)
sep.pack(expand = True, fill = tk.Y, side = tk.RIGHT)
#-----------------------------------------------------------------------




button = tk.Button(frame, width = 12, height = 3, text="button", command=on_button_click)

button.pack()









button1 = tk.Button(frame, text = "Button1", command = kombo,
                fg = "yellow", font = "Verdana 14 underline",
                bd = 2, bg = "light blue", relief = "groove",)
button1.pack()

#-----------------------------------------------------------------------
boton_normal = tk.Button(root, text="normal", state="normal", width=20, height=7,
                       command = normal,
                       foreground='red',
                       background='blue',
                       activeforeground='yellow',
                       activebackground='grey',
                       disabledforeground='green').pack()
#-----------------------------------------------------------------------






Combo = ttk.Combobox(frame, values = vlist)
Combo.set("Seleccione una option")
Combo.pack(padx = 5, pady = 5)

#-----------------------------------------------------------------------

entry = tk.Entry(frame)
entry.pack()

text_area = tk.Text(frame, height=3, width=25)
text_area.pack()



#-----------------------------------------------------------------------
canvas = tk.Canvas(frame, width=200, height=100, bg="white")
canvas.pack()
canvas.create_rectangle(50, 20, 150, 80, fill="red")

#-----------------------------------------------------------------------
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="  borra", command=on_button_click)
file_menu.add_separator()
file_menu.add_command(label="  Salir", command=root.destroy)

file_menu = tk.Menu(menu)
file_menu.add_separator()
menu.add_cascade(label="arxiu", menu=file_menu)
file_menu.add_command(label="esborra", command=on_button_click)
file_menu.add_command(label="surtir", command=root.destroy)

#-----------------------------------------------------------------------

listbox = tk.Listbox(frame, width=22, height=3)
listbox.pack()
listbox.insert(1, "Opción 0")
listbox.insert(2, "Opción 1")
listbox.insert(3, "Listbox")
#-----------------------------------------------------------------------

var = tk.StringVar()
rb1 = tk.Radiobutton(frame, text="Opción 1", variable=var, value="1", command=o)
rb2 = tk.Radiobutton(frame, text="Opción 2", variable=var, value="2")
rb3 = tk.Radiobutton(frame, text="Opción 3", variable=var, value="3")
rb1.pack()
rb2.pack()
rb3.pack()
#-----------------------------------------------------------------------

cb_var = tk.IntVar()
checkbutton = tk.Checkbutton(frame, text="Opción 1", variable=cb_var, command=o)
checkbutton.pack()

cb_var1 = tk.IntVar()
checkbutton1 = tk.Checkbutton(frame, text="Opción 2", variable=cb_var1)
checkbutton1.pack()
#-----------------------------------------------------------------------

v = tk.IntVar()
scale1 = tk.Scale(frame, variable=v, from_=0, to=100, command=SELF)
scale1.pack()
#-----------------------------------------------------------------------

Label1 = tk.Label(frame, text = ('TEST','MOUSE'), width = 0,
                  font = ('Arial', 50), bg = frame.cget('bg'))

Label1.bind('<Button-1>', lambda event: print("Mouse BOTON IZUIERDO"))
Label1.bind('<Button-2>', lambda event: print("Mouse BOTON RUEDA"))
Label1.bind('<Button-3>', lambda event: print("Mouse BOTON DERECHO"))
Label1.bind('<Button-4>', lambda event: print("Mouse RUEDA ARRIBA"))
Label1.bind('<Button-5>', lambda event: print("Mouse RUEDA ABAJO"))
Label1.place( x = amplada//2, y = alcada//2, anchor ="center")
Label1.pack()

#-----------------------------------------------------------------------

root.bind('A', lambda event: print("A PRESIONADA"))
root.bind('B', lambda event: print("B PRESIONADA"))
root.bind('C', lambda event: print("C PRESIONADA"))
root.bind('D', lambda event: print("D PRESIONADA"))

root.bind('1', lambda event: print("1 PRESIONADA"))
root.bind('2', lambda event: print("2 PRESIONADA"))
root.bind('3', lambda event: print("3 PRESIONADA"))
root.bind('4', lambda event: print("4 PRESIONADA"))

root.bind('<Up>', lambda event: print("SUBIR"))
root.bind('<Down>', lambda event: print("BAJAR"))
root.bind('<Right>', lambda event: print("DERECHA"))
root.bind('<Left>', lambda event: print("IZQUIERDA"))

#-----------------------------------------------------------------------

root.mainloop()

print("FIN")



