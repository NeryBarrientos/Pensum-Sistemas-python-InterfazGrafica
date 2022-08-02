import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from xml.dom.minidom import Element
import easygui as eg
import functools
import tkinter as tk
from os import system
system("cls")

probando = []

def cargar():
    global Usar,probando
    imprimir = '*********************************************'
    imprimir1 = 'Archivo Cargado exitosamente'
    extension = ["*.py","*.pyc"]
    archivo = eg.fileopenbox(msg="Abrir archivo",
                         title="Control: fileopenbox",
                         default='C:/Users/USUARIO/Desktop/*lfp',
                         filetypes=extension)                      
    eg.msgbox('Ruta del Archivo: ' + archivo + '\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir1.center(75,' ') + '\n' + imprimir.center(75,' ') + '\n' , "fileopenbox", ok_button="Continuar")
    f = open(archivo,'r',encoding="utf8")
    #leer = f.read()
    for linea in f:
        temporal = []
        prueba = linea.rstrip('\n')
        prueba = prueba.split(',')
        temporal = [str(prueba[0])] + [str(prueba[1])] + [str(prueba[2])] + [str(prueba[3])] + [str(prueba[4])] + [str(prueba[5])] + [str(prueba[6])]
        probando.append(temporal)
    f.close()
    for dato in probando:
        if dato[3] == "1":
            dato[3] = "Obligatorio"
        elif dato[3] == "0":
            dato[3] = "Opcional"
        if dato[6] == "0":
            dato[6] = "Aprobado"
        elif dato[6] == "1":
            dato[6] = "Cursando"
        elif dato[6] == "-1":
            dato[6] = "Pendiente"
    #print(probando)
    for element in probando:
        #print(element)
        arbol.insert("",END,text=element[0],values=(element[1],element[2],element[3],element[4],element[5],element[6]))

def ventana_secundaria(master, callback=None, args=(), kwargs={}):
    global temporal
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = tk.Frame(master)
    label = Label(main_frame,text="Gestionar Cursos")
    label.place(x=615,y=30)
    boton1 = tkinter.Button(main_frame, text='Listar Cursos', width=15, height=3,bd="4",command=mostrar_tercera)
    boton1.place(x=600,y=70)
    boton2 = tkinter.Button(main_frame, text='Agregar Curso', width=15, height=3,bd="4",command=mostrar_agregar)
    boton2.place(x=600,y=140)
    boton3 = tkinter.Button(main_frame, text='Editar curso', width=15, height=3,bd="4",command=mostrar_editar)
    boton3.place(x=600,y=210)
    boton4 = tkinter.Button(main_frame, text='Eliminar curso', width=15, height=3,bd="4",command=mostrar_eliminar)
    boton4.place(x=600,y=280)
    boton5 = tkinter.Button(main_frame, text='Regresar', width=15, height=3,command=callback,bd="4")
    boton5.place(x=600,y=350)
    return main_frame
    
def mostrar_principal():
    secundaria.pack_forget()
    tercera.pack_forget()
    eliminar.pack_forget()
    miFrameV.pack(side="top", fill="both", expand=True)

def mostrar_secundaria():
    global label
    miFrameV.pack_forget()
    tercera.pack_forget()
    agregar.pack_forget()
    editar.pack_forget()
    eliminar.pack_forget()
    secundaria.pack(side="top", fill="both", expand=True)

def mostrar_tercera():
    global label, probando
    miFrameV.pack_forget()
    secundaria.pack_forget()
    agregar.pack_forget()
    editar.pack_forget()
    eliminar.pack_forget()
    tercera.pack(side="top", fill="both", expand=True)

def mostrar_agregar():
    global label
    miFrameV.pack_forget()
    secundaria.pack_forget()
    tercera.pack_forget()
    editar.pack_forget()
    eliminar.pack_forget()
    agregar.pack(side="top", fill="both", expand=True)\

def mostrar_editar():
    global label
    miFrameV.pack_forget()
    secundaria.pack_forget()
    tercera.pack_forget()
    agregar.pack_forget()
    eliminar.pack_forget()
    editar.pack(side="top", fill="both", expand=True)

def mostrar_eliminar():
    global label
    miFrameV.pack_forget()
    secundaria.pack_forget()
    tercera.pack_forget()
    agregar.pack_forget()
    editar.pack_forget()
    eliminar.pack(side="top", fill="both", expand=True)


def ventana_tercera(master, callback=None, args=(), kwargs={}):
    global arbol
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = tk.Frame(master)
    label = Label(main_frame,text="Listar Cursos")
    label.place(x=615,y=30)
    arbol = ttk.Treeview(main_frame,columns=("Nombre","Pre-requisitos","Obligatorio","Semestre","Creditos","Estado"))
    arbol.column("#0",width=50,anchor=CENTER)
    arbol.column("Nombre",anchor=CENTER)
    arbol.column("Pre-requisitos",width=60,anchor=CENTER)
    arbol.column("Obligatorio",width=60,anchor=CENTER)
    arbol.column("Creditos",width=60,anchor=CENTER)
    arbol.column("Semestre",width=70,anchor=CENTER)
    arbol.column("Estado",width=60,anchor=CENTER)
    sb = Scrollbar(main_frame, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)
    arbol.config(yscrollcommand=sb.set)
    sb.config(command=arbol.yview)
    arbol.place(width="1280",height="500",x="0",y="60")
    arbol.heading("#0",text="Código")
    arbol.heading("Nombre",text="Nombre")
    arbol.heading("Pre-requisitos",text="Pre-requisitos")
    arbol.heading("Obligatorio",text="Obligatorio")
    arbol.heading("Semestre",text="Semestre")
    arbol.heading("Creditos",text="Creditos")
    arbol.heading("Estado",text="Estado")
    arbol.insert("",END,text="017",values=("Social Humanistica 1 Prueba","","Obligatorio","1","4","Pendiente"))
    for element in probando:
        arbol.insert("",END,text=element[0],values=(element[1],element[2],element[3],element[4],element[5],element[6]))
    boton = tkinter.Button(main_frame, text='Regresar', width=15, height=3,command=callback,bd="4")
    boton.place(x=600,y=600)
    return main_frame    
'''a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for row in a:
    for elem in row:
        print(elem, end=' ')
    print() ''' 

def ventana_agregar(master, callback=None, args=(), kwargs={}):
    global arbol
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)
    main_frame = tk.Frame(master)
    label = Label(main_frame,text="Agregar Curso")
    label.place(x=615,y=30)
    boton = tkinter.Button(main_frame, text='Regresar', width=15, height=3,command=callback,bd="4")
    boton.place(x=600,y=600)
    return main_frame    

def ventana_editar(master, callback=None, args=(), kwargs={}):
    global arbol
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)
    main_frame = tk.Frame(master)
    label = Label(main_frame,text="Editar Curso")
    label.place(x=615,y=30)
    boton = tkinter.Button(main_frame, text='Regresar', width=15, height=3,command=callback,bd="4")
    boton.place(x=600,y=600)
    return main_frame

def ventana_eliminar(master, callback=None, args=(), kwargs={}):
    global arbol
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)
    main_frame = tk.Frame(master)
    label = Label(main_frame,text="Eliminar Curso")
    label.place(x=615,y=30)
    boton = tkinter.Button(main_frame, text='Regresar', width=15, height=3,command=callback,bd="4")
    boton.place(x=600,y=600)
    return main_frame

ventana = tkinter.Tk()
#Abro venta
ancho_ventana = 1280
alto_ventana = 720
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
miFrameV.config(width=ancho_ventana,height=alto_ventana,relief="solid",bd="3")
secundaria = ventana_secundaria(ventana, mostrar_principal)
tercera = ventana_tercera(ventana, mostrar_secundaria)
agregar = ventana_agregar(ventana, mostrar_secundaria)
editar = ventana_editar(ventana, mostrar_secundaria)
eliminar = ventana_eliminar(ventana, mostrar_secundaria)
#agregando Items a frameV
label = Label(miFrameV,text="Nombre del curso: Lenguajes Formales y de Programación")
label.place(x=250,y=50)
label1 = Label(miFrameV,text="Nombre del Estudiante: Nery José Barrientos Posadas")
label1.place(x=250,y=100)
label2 = Label(miFrameV,text="Carné del Estudiante: 201807086")
label2.place(x=250,y=150)
boton1 = tkinter.Button(miFrameV, text='Cargar Archivo', width=15, height=3,bd="4",command=cargar)
boton1.place(x=600,y=200)
boton2 = tkinter.Button(miFrameV, text='Gestionar Cursos', width=15, height=3,bd="4",command=mostrar_secundaria)
boton2.place(x=600,y=270)
boton3 = tkinter.Button(miFrameV, text='Conteo de Crétditos', width=15, height=3,bd="4")
boton3.place(x=600,y=340)
boton4 = tkinter.Button(miFrameV, text='Salir', width=15, height=3,command=exit,bd="4")
boton4.place(x=600,y=410)

#frame Inferior
miFrame1 = Frame()
miFrame1.pack(side="bottom",fill="x")
miFrame1.config(width="500",height="30",relief="solid",bd="3")
ventana.mainloop()

#Lista.Agregar(150,"Física 1","103;147",1,3,6,1)
#Lista.printLista()

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