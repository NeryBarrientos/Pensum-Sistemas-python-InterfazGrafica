import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from os import system
system("cls")

def menuprincipal():
    imprimir = '*********************************************'
    imprimir1 = 'Lenguajes Formales de Programación'
    print(imprimir.center(50,' ') + '\n' + imprimir1.center(50,' ') + '\n' + imprimir.center(50,' ') + '\n')
    imprimir1 = 'Sección B+ 201807086'
    print(imprimir.center(50,' ') + '\n' + imprimir1.center(50,' ') + '\n' + imprimir.center(50,' ') + '\n')
    print("Opciones: \n1.Cargar archivo de entrada \n2.Cargar instrucciones \n3.Analizar \n4.Reportes \n5.Salir")
    print('--------------------------------------------------')
    messagebox.showinfo("Mensaje","Archivo cargado correctamente")
    #lectura = input("Escoja una opcion: ")
    #print('--------------------------------------------------')

ventana = tkinter.Tk()
ventana.geometry('1280x720')
ventana.title('Menú Principal')
miFrame = Frame()
miFrame.pack(side="top",fill="x")
miFrame.config(width="1280",height="50",bg="red",relief="solid",bd="3")
miFrame1 = Frame()
miFrame1.pack(side="bottom",fill="x")
miFrame1.config(width="1280",height="50",bg="red",relief="solid",bd="3")
#boton1 = tkinter.Button(ventana, text='Cargar', width=13, height=3 )
#boton2 = tkinter.Button(ventana, text='Analizar', width=13, height=3)
etiqueta = Label(ventana,text="Escoja una imagen a trabajar:")
etiqueta.place(x=50, y=180)
combo = ttk.Combobox(ventana,state="readonly")
combo.place(x=50, y=200)
boton3 = tkinter.Button(ventana, text='Reportes', width=13, height=3)
boton4 = tkinter.Button(ventana, text='Salir', width=13, height=3)
etiqueta = Label(ventana,text="Escoja el filtro a trabajar:")
etiqueta.place(x=50, y=230)
boton5 = tkinter.Button(ventana, text='Original', width=13, height=3)
boton6 = tkinter.Button(ventana, text='MirrorX', width=13, height=3)
boton7 = tkinter.Button(ventana, text='MirrorY', width=13, height=3)
boton8 = tkinter.Button(ventana, text='Double Mirror', width=13, height=3)
#boton1.grid(row=0, column=0)
#boton2.grid(row=0, column=1)
#boton3.grid(row=0, column=2)
#boton4.grid(row=0, column=3)
#boton5.place(x=50,y=250)
#boton6.place(x=50,y=310)
#boton7.place(x=50,y=370)
#boton8.place(x=50,y=430)
ventana.mainloop()