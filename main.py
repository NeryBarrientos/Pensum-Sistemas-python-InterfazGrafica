import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import easygui as eg
import functools
import tkinter as tk
from os import system

from pip import main
system("cls")

def cargar():
    global archivoData
    imprimir = '*********************************************'
    imprimir1 = 'Archivo Cargado exitosamente'
    extension = ["*.py","*.pyc"]
    archivo = eg.fileopenbox(msg="Abrir archivo",
                         title="Control: fileopenbox",
                         default='C:/Users/USUARIO/Desktop/*lfp',
                         filetypes=extension)                      
    eg.msgbox('Ruta del Archivo: ' + archivo + '\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir1.center(75,' ') + '\n' + imprimir.center(75,' ') + '\n' , "fileopenbox", ok_button="Continuar")
    f = open(archivo,'r',encoding="utf8")
    leer = f.read()
    f.close()
    archivoData = leer.replace("\n","")
    print(leer)

def ventana_secundaria(master, callback=None, args=(), kwargs={}):
    global temporal
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = tk.Frame(master)
    #boton2 = tk.Button(main_frame, text="Boton 2")
    #boton2.place(x=15, y=30)
    label = Label(main_frame,text="Gestionar Cursos")
    label.place(x=215,y=30)
    boton1 = tkinter.Button(main_frame, text='Listar Cursos', width=15, height=3,bd="4",command=cargar)
    boton1.place(x=200,y=70)
    boton2 = tkinter.Button(main_frame, text='Agregar Curso', width=15, height=3,bd="4")
    boton2.place(x=200,y=140)
    boton3 = tkinter.Button(main_frame, text='Editar curso', width=15, height=3,bd="4")
    boton3.place(x=200,y=210)
    boton4 = tkinter.Button(main_frame, text='Eliminar curso', width=15, height=3,bd="4")
    boton4.place(x=200,y=280)
    boton5 = tkinter.Button(main_frame, text='Regresar', width=15, height=3,command=callback,bd="4")
    boton5.place(x=200,y=350)
    return main_frame
    
def mostrar_principal():
    secundaria.pack_forget()
    miFrameV.pack(side="top", fill="both", expand=True)

def mostrar_secundaria():
    global label
    miFrameV.pack_forget()
    secundaria.pack(side="top", fill="both", expand=True)

ventana = tkinter.Tk()
#Abro venta
ancho_ventana = 500
alto_ventana = 600
x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.title('Menú Principal')
#Frame con nombre practica
miFrame = Frame()
miFrame.pack(side="top",fill="x")
miFrame.config(width="500",height="50",relief="solid",bd="3")
label = Label(miFrame,text='Práctica 1')
label.pack(side="left")
#frame Variable
miFrameV = Frame()
miFrameV.pack(fill="x")
miFrameV.place(x=0,y=25)
miFrameV.config(width="500",height="640",relief="solid",bd="3")
secundaria = ventana_secundaria(ventana, mostrar_principal)
#agregando Items a frameV
label = Label(miFrameV,text="Nombre del curso: Lenguajes Formales y de Programación")
label.place(x=50,y=50)
label1 = Label(miFrameV,text="Nombre del Estudiante: Nery José Barrientos Posadas")
label1.place(x=50,y=100)
label2 = Label(miFrameV,text="Carné del Estudiante: 201807086")
label2.place(x=50,y=150)
boton1 = tkinter.Button(miFrameV, text='Cargar Archivo', width=15, height=3,bd="4",command=cargar)
boton1.place(x=200,y=200)
boton2 = tkinter.Button(miFrameV, text='Gestionar Cursos', width=15, height=3,bd="4",command=mostrar_secundaria)
boton2.place(x=200,y=270)
boton3 = tkinter.Button(miFrameV, text='Conteo de Crétditos', width=15, height=3,bd="4")
boton3.place(x=200,y=340)
boton4 = tkinter.Button(miFrameV, text='Salir', width=15, height=3,command=exit,bd="4")
boton4.place(x=200,y=410)

#frame Inferior
miFrame1 = Frame()
miFrame1.pack(side="bottom",fill="x")
miFrame1.config(width="500",height="30",relief="solid",bd="3")
ventana.mainloop()



#etiqueta = Label(ventana,text="Escoja una imagen a trabajar:")
#etiqueta.place(x=50, y=180)
#combo = ttk.Combobox(ventana,state="readonly")
#combo.place(x=50, y=200)
#boton3 = tkinter.Button(ventana, text='Reportes', width=13, height=3)
#boton4 = tkinter.Button(ventana, text='Salir', width=13, height=3)
#etiqueta = Label(ventana,text="Escoja el filtro a trabajar:")
#etiqueta.place(x=50, y=230)
#boton5 = tkinter.Button(ventana, text='Original', width=13, height=3)
#boton6 = tkinter.Button(ventana, text='MirrorX', width=13, height=3)
#boton7 = tkinter.Button(ventana, text='MirrorY', width=13, height=3)
#boton8 = tkinter.Button(ventana, text='Double Mirror', width=13, height=3)
#boton1.grid(row=0, column=0)
#boton2.grid(row=0, column=1)
#boton3.grid(row=0, column=2)
#boton4.grid(row=0, column=3)
#boton5.place(x=50,y=250)
#boton6.place(x=50,y=310)
#boton7.place(x=50,y=370)
#boton8.place(x=50,y=430)