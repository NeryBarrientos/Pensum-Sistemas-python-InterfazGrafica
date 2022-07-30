import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from traceback import print_tb
import easygui as eg
from os import system
system("cls")

def cargar():
    global archivoData
    extension = ["*.py","*.pyc"]
    archivo = eg.fileopenbox(msg="Abrir archivo",
                         title="Control: fileopenbox",
                         default='C:/Users/USUARIO/Desktop/*lfp',
                         filetypes=extension)                      
    eg.msgbox(archivo, "fileopenbox", ok_button="Continuar")
    f = open(archivo,'r',encoding="utf8")
    leer = f.read()
    f.close()
    archivoData = leer.replace("\n","")
    imprimir = '*********************************************'
    imprimir1 = 'Archivo Cargado exitosamente'
    eg.msgbox(msg='\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir1.center(75,' ') + '\n' + imprimir.center(75,' ') + '\n')
    print(leer)

ventana = tkinter.Tk()
ancho_ventana = 500
alto_ventana = 600
x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.title('Menú Principal')
miFrame = Frame()
miFrame.pack(side="top",fill="x")
miFrame.config(width="500",height="50",relief="solid",bd="3")
label = Label(miFrame,text="Práctica 1")
label.pack(side="left")
label = Label(ventana,text="Nombre del curso: Lenguajes Formales y de Programación")
label.place(x=50,y=50)
label1 = Label(ventana,text="Nombre del Estudiante: Nery José Barrientos Posadas")
label1.place(x=50,y=100)
label2 = Label(ventana,text="Carné del Estudiante: 201807086")
label2.place(x=50,y=150)
miFrame1 = Frame()
miFrame1.pack(side="bottom",fill="x")
miFrame1.config(width="500",height="30",relief="solid",bd="3")
boton1 = tkinter.Button(ventana, text='Cargar Archivo', width=15, height=3,bd="4",command=cargar)
boton1.place(x=200,y=200)
boton2 = tkinter.Button(ventana, text='Gestionar Cursos', width=15, height=3,bd="4")
boton2.place(x=200,y=270)
boton3 = tkinter.Button(ventana, text='Conteo de Crétditos', width=15, height=3,bd="4")
boton3.place(x=200,y=340)
boton4 = tkinter.Button(ventana, text='Salir', width=15, height=3,command=exit,bd="4")
boton4.place(x=200,y=410)
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