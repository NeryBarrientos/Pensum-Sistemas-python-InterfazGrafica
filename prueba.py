import tkinter as tk
from tkinter import ttk



v = ["Enero", "Febrero", "Marzo", "Abril"]
c = ["Lunes", "Martes", "Miercoles", "Jueves"]
m = ["1", "2", "3", "4"]

def sel():
    r = str(var.get())
    selection = "Tu estas selecionando: " + r
    label.config(text=selection)

    if r == "1" :
        combo_box['values'] = v
    elif r == "2" :
        combo_box['values'] = c
    elif r == "3" :
        combo_box['values'] = m

root = tk.Tk()  

var  = tk.IntVar()
r1 = tk.Radiobutton(root, text="Opcion 1", variable=var, value=1, command=sel)
r1.pack(anchor=tk.W )

r2 = tk.Radiobutton(root, text="Opcion 2", variable=var, value=2, command=sel)
r2.pack(anchor=tk.W)

r3 = tk.Radiobutton(root, text="Opcion 3", variable=var, value=3, command=sel)
r3.pack(anchor=tk.W)

label = tk.Label(root)
label.pack()

combo_box = ttk.Combobox(root, values=v)
combo_box.pack()

root.mainloop()