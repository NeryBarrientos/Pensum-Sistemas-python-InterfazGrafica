import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import easygui as eg
import functools
import tkinter as tk
from os import system
system("cls")

probando = []
nombreCurso = []
agredados = []
codigoCurso = []

def cargar():
    global probando,agredados
    repetidos = []
    archivos = []
    imprimir = '*********************************************'
    imprimir1 = 'Archivo Cargado exitosamente'
    extension = ["*.py","*.pyc"]
    archivo = eg.fileopenbox(msg="Abrir archivo",
                         title="Control: fileopenbox",
                         default='C:/Users/USUARIO/Desktop/*lfp',
                         filetypes=extension)                      
    eg.msgbox('Ruta del Archivo: ' + archivo + '\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir1.center(75,' ') + '\n' + imprimir.center(75,' ') + '\n' , "fileopenbox", ok_button="Continuar")
    f = open(archivo,'r',encoding="utf8")
    for linea in f:
        temporal = []
        prueba = linea.rstrip('\n')
        prueba = prueba.split(',')
        temporal = [str(prueba[0])] + [str(prueba[1])] + [str(prueba[2])] + [str(prueba[3])] + [str(prueba[4])] + [str(prueba[5])] + [str(prueba[6])]
        probando.append(temporal)
#Parte copiada pueba
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
    if len(agredados) == 0:
        print("Vacia")
        for element in probando:
            agredados.append(element)
            arbol.insert("",END,text=element[0],values=(element[1],element[2],element[3],element[4],element[5],element[6]),iid=element[0])
    else:
        print("Con datos")
        for element in probando:
            if element in agredados:
                print("este elemento ya ha sido agregado" , element)
            else:
                arbol.insert("",END,text=element[0],values=(element[1],element[2],element[3],element[4],element[5],element[6]),iid=element[0])

def ventana_secundaria(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)
        
    main_frame = tk.Frame(master)
    label = Label(main_frame,text="Gestionar Cursos")
    label.place(x=615,y=30)
    boton1 = tkinter.Button(main_frame, text='Listar Cursos', width=15, height=3,bd="4",command=mostrar_tercera)
    boton1.place(x=600,y=70)
    boton2 = tkinter.Button(main_frame, text='Mostrar Curso', width=15, height=3,bd="4",command=mostrar_curso)
    boton2.place(x=600,y=140)
    boton3 = tkinter.Button(main_frame, text='Agregar Curso', width=15, height=3,bd="4",command=mostrar_agregar)
    boton3.place(x=600,y=210)
    boton4 = tkinter.Button(main_frame, text='Editar Curso', width=15, height=3,bd="4",command=mostrar_editar)
    boton4.place(x=600,y=280)
    boton5 = tkinter.Button(main_frame, text='Eliminar curso', width=15, height=3,bd="4",command=mostrar_eliminar)
    boton5.place(x=600,y=350)
    boton5 = tkinter.Button(main_frame, text='Regresar', width=15, height=3,command=callback,bd="4")
    boton5.place(x=600,y=420)
    return main_frame
    
def mostrar_principal():
    secundaria.pack_forget()
    tercera.pack_forget()
    eliminar.pack_forget()
    conteo.pack_forget()
    miFrameV.pack(side="top", fill="both", expand=True)

def mostrar_secundaria():
    global label
    miFrameV.pack_forget()
    tercera.pack_forget()
    agregar.pack_forget()
    editar.pack_forget()
    eliminar.pack_forget()
    conteo.pack_forget()
    mostrarCurso.pack_forget()
    secundaria.pack(side="top", fill="both", expand=True)

def mostrar_tercera():
    global label, probando
    miFrameV.pack_forget()
    secundaria.pack_forget()
    agregar.pack_forget()
    editar.pack_forget()
    eliminar.pack_forget()
    conteo.pack_forget()
    mostrarCurso.pack_forget()
    tercera.pack(side="top", fill="both", expand=True)

def mostrar_curso():
    global label
    miFrameV.pack_forget()
    secundaria.pack_forget()
    tercera.pack_forget()
    editar.pack_forget()
    eliminar.pack_forget()
    conteo.pack_forget()
    agregar.pack_forget()
    mostrarCurso.pack(side="top", fill="both", expand=True)

def mostrar_agregar():
    global label
    miFrameV.pack_forget()
    secundaria.pack_forget()
    tercera.pack_forget()
    editar.pack_forget()
    eliminar.pack_forget()
    mostrarCurso.pack_forget()
    conteo.pack_forget()
    agregar.pack(side="top", fill="both", expand=True)

def mostrar_editar():
    global label,probando
    miFrameV.pack_forget()
    secundaria.pack_forget()
    tercera.pack_forget()
    agregar.pack_forget()
    eliminar.pack_forget()
    conteo.pack_forget()
    mostrarCurso.pack_forget()
    editar.pack(side="top", fill="both", expand=True)

def mostrar_eliminar():
    global label
    miFrameV.pack_forget()
    secundaria.pack_forget()
    tercera.pack_forget()
    agregar.pack_forget()
    editar.pack_forget()
    conteo.pack_forget()
    mostrarCurso.pack_forget()
    eliminar.pack(side="top", fill="both", expand=True)

def mostrar_Conteo():
    global label
    miFrameV.pack_forget()
    secundaria.pack_forget()
    tercera.pack_forget()
    agregar.pack_forget()
    editar.pack_forget()
    eliminar.pack_forget()
    mostrarCurso.pack_forget()
    conteo.pack(side="top", fill="both", expand=True)


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
    '''for element in probando:
        arbol.insert("",END,text=element[0],values=(element[1],element[2],element[3],element[4],element[5],element[6]))'''
    boton = tkinter.Button(main_frame, text='Regresar', width=15, height=3,command=callback,bd="4")
    boton.place(x=600,y=600)
    return main_frame    

def ObtenerEntry():
    global probando, arbol
    imprimir = '*********************************************'
    imprimir1 = 'Dato Opcionalidad fuera de rango'
    imprimir2 = 'Dato estado fuera de rango'
    imprimir3 = 'Curso Agregado Correctamente'
    if opcionalidad.get() < 0 or opcionalidad.get() > 1:
        eg.msgbox('\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir1.center(75,' ')+ '\n' + imprimir.center(75,' '))
    if opcionalidad.get() == 1:
        temporal = "Obligatorio"
    elif opcionalidad.get() == 0:
        temporal = "Opcional"
    if estado.get() < -1 or estado.get() > 1:
        eg.msgbox('\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir2.center(75,' ')+ '\n' + imprimir.center(75,' '))
    if estado.get() == 0:
        temporal1 = "Aprobado"
    elif estado.get() == 1:
        temporal1 = "Cursando"
    elif estado.get() == -1:
        temporal1 = "Pendiente"
    temp = [codigo.get()] + [nombre.get()] + [requisito.get()] + [semestre.get()] + [temporal] + [creditos.get()] + [temporal1]
    #No permitir agregar curso ya existente
    probando.append(temp)
    agredados.append(temp)
    arbol.insert("",END,text=codigo.get(),values=(nombre.get(),requisito.get(),temporal,semestre.get(),creditos.get(),temporal1),iid=codigo.get())
    eg.msgbox('\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir3.center(75,' ') + '\n' + imprimir.center(75,' ') + '\n' , "fileopenbox", ok_button="Continuar")

def ventana_agregar(master, callback=None, args=(), kwargs={}):
    global arbol,codigo,nombre,requisito,semestre,opcionalidad,creditos,estado
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)
    main_frame = tk.Frame(master)
    label = Label(main_frame,text="Agregar Curso")
    label.place(x=615,y=30)
    #saveEntry
    codigo = tk.IntVar()
    nombre = tk.StringVar()
    requisito = tk.StringVar()
    semestre = tk.IntVar()
    opcionalidad = tk.IntVar()
    creditos = tk.IntVar()
    estado = tk.IntVar()
    #Entry box
    campoCodigo = ttk.Entry(main_frame,font=('Arial',12),textvariable=codigo).place(x=600,y=60,width=200,height=50)
    campoNombre = ttk.Entry(main_frame,font=('Arial',12),textvariable=nombre).place(x=600,y=130,width=200,height=50)
    campoRequisito = ttk.Entry(main_frame,font=('Arial',12),textvariable=requisito).place(x=600,y=200,width=200,height=50)
    campoSemestre = ttk.Entry(main_frame,font=('Arial',12),textvariable=semestre).place(x=600,y=270,width=200,height=50)
    campoOpcionalidad = ttk.Entry(main_frame,font=('Arial',12),textvariable=opcionalidad).place(x=600,y=340,width=200,height=50)
    campoCreditos = ttk.Entry(main_frame,font=('Arial',12),textvariable=creditos).place(x=600,y=410,width=200,height=50)
    campoEstado = ttk.Entry(main_frame,font=('Arial',12),textvariable=estado).place(x=600,y=480,width=200,height=50)
    #labels
    labelCodigo = Label(main_frame,text="Codigo",font=('Arial',12)).place(x=500,y=60,height=50)
    labelNombre = Label(main_frame,text="Nombre",font=('Arial',12)).place(x=500,y=130,height=50)
    labelRequisito = Label(main_frame,text="Pre requisito",font=('Arial',12)).place(x=500,y=200,height=50)
    labelSemestre = Label(main_frame,text="Semestre",font=('Arial',12)).place(x=500,y=270,height=50)
    labelOpcionalidad = Label(main_frame,text="Opcionalidad",font=('Arial',12)).place(x=500,y=340,height=50)
    labelCreditos = Label(main_frame,text="Créditos",font=('Arial',12)).place(x=500,y=410,height=50)
    labelEstado = Label(main_frame,text="Estado",font=('Arial',12)).place(x=500,y=480,height=50)
    boton1 = tkinter.Button(main_frame, text='Agregar', width=15, height=3,command=ObtenerEntry,bd="4")
    boton1.place(x=530,y=600)
    boton = tkinter.Button(main_frame, text='Regresar', width=15, height=3,command=callback,bd="4")
    boton.place(x=670,y=600)
    return main_frame    

def mostrarCursos():
    global combo,nombreCurso
    temporal = []
    for valor in probando:
        temporal.append(valor[1])
    nombreCurso = temporal
    combo = ttk.Combobox(prueba,font=('Arial',10),state="readonly",values=nombreCurso)
    combo.place(x=600,y=30,width=200,height=30)

def mostrarCursosEliminar():
    global comboEliminar,nombreCurso
    temporal = []
    for valor in probando:
        temporal.append(valor[1])
    nombreCurso = temporal
    comboEliminar = ttk.Combobox(frameEliminar,font=('Arial',10),state="readonly",values=nombreCurso)
    comboEliminar.place(x=600,y=250,width=200,height=30)

def mostrarCodigoCursos():
    global comboEliminar1,codigoCurso,campoCodigoMostrar
    temporal = []
    for valor in probando:
        temporal.append(valor[0])
    nombreCurso = temporal
    comboEliminar1 = ttk.Combobox(frameMostrarCurso,font=('Arial',10),state="readonly",values=nombreCurso)
    comboEliminar1.place(x=600,y=50,width=200,height=30)
    #saveEntry
    codigoEditar = tk.IntVar()
    nombreEditar = tk.StringVar()
    requisitoEditar = tk.StringVar()
    semestreEditar = tk.IntVar()
    opcionalidadEditar = tk.IntVar()
    creditosEditar = tk.IntVar()
    estadoEditar = tk.IntVar()
    #labels
    labelCodigo = Label(frameMostrarCurso,text="Codigo",font=('Arial',12)).place(x=500,y=80,height=50)
    labelNombre = Label(frameMostrarCurso,text="Nombre",font=('Arial',12)).place(x=500,y=150,height=50)
    labelRequisito = Label(frameMostrarCurso,text="Pre requisito",font=('Arial',12)).place(x=500,y=220,height=50)
    labelSemestre = Label(frameMostrarCurso,text="Semestre",font=('Arial',12)).place(x=500,y=290,height=50)
    labelOpcionalidad = Label(frameMostrarCurso,text="Opcionalidad",font=('Arial',12)).place(x=500,y=360,height=50)
    labelCreditos = Label(frameMostrarCurso,text="Créditos",font=('Arial',12)).place(x=500,y=420,height=50)
    labelEstado = Label(frameMostrarCurso,text="Estado",font=('Arial',12)).place(x=500,y=500,height=50)

def editarCurso():
    global probando,arbol
    imprimir = '*********************************************'
    imprimir1 = 'Dato Opcionalidad fuera de rango'
    imprimir2 = 'Dato estado fuera de rango'
    imprimir3 = 'Curso Editado Correctamente'
    if opcionalidadEditar.get() < 0 or opcionalidadEditar.get() > 1:
        eg.msgbox('\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir1.center(75,' ')+ '\n' + imprimir.center(75,' '))
    if opcionalidadEditar.get() == 1:
        temporal = "Obligatorio"
    elif opcionalidadEditar.get() == 0:
        temporal = "Opcional"
    if estadoEditar.get() < -1 or estadoEditar.get() > 1:
        eg.msgbox('\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir2.center(75,' ')+ '\n' + imprimir.center(75,' '))
    if estadoEditar.get() == 0:
        temporal1 = "Aprobado"
    elif estadoEditar.get() == 1:
        temporal1 = "Cursando"
    elif estadoEditar.get() == -1:
        temporal1 = "Pendiente"
    comboSeleccionado = combo.get()
    for elemento in probando:
        if elemento[1] == comboSeleccionado:
            print(f"Lo encontre: {elemento}")
            print(arbol.item(elemento[0]))
            arbol.item(elemento[0],text=codigoEditar.get(),values=(nombreEditar.get(),requisitoEditar.get(),temporal,semestreEditar.get(),creditosEditar.get(),temporal1))
            print(codigoEditar.get())
            #elemento[0] = codigoEditar.get()
            elemento[1] = nombreEditar.get()
            elemento[2] = requisitoEditar.get()
            elemento[3] = temporal
            elemento[4] = semestreEditar.get()
            elemento[5] = creditosEditar.get()
            elemento[6] = temporal1
    eg.msgbox('\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir3.center(75,' ')+ '\n' + imprimir.center(75,' '))

def eliminarCurso():
    global probando,arbol
    imprimir = '*********************************************'
    imprimir1 = 'Curso Eliminado Correctamente'
    comboSeleccionado = comboEliminar.get()
    for elemento in range(len(probando)):
        if probando[elemento][1] == comboSeleccionado:
            print(f"Lo encontre: {probando[elemento]}")
            arbol.delete(probando[elemento][0])
            probando.pop(elemento)
    eg.msgbox('\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir1.center(75,' ')+ '\n' + imprimir.center(75,' '))

def mostrarCursoBoton():
    global probando,arbol
    imprimir = '*********************************************'
    imprimir1 = 'Curso mostrado Correctamente'
    comboSeleccionado = comboEliminar1.get()
    #Entry box
    campoCodigo = Entry(frameMostrarCurso,font=('Arial',12),justify=CENTER)
    campoCodigo.place(x=600,y=80,width=200,height=50)
    campoCodigo.insert(END,comboSeleccionado)

    campoNombre = ttk.Entry(frameMostrarCurso,font=('Arial',12),justify=CENTER)
    campoNombre.place(x=600,y=150,width=200,height=50)

    campoRequisito = ttk.Entry(frameMostrarCurso,font=('Arial',12),justify=CENTER)
    campoRequisito.place(x=600,y=220,width=200,height=50)

    campoSemestre = ttk.Entry(frameMostrarCurso,font=('Arial',12),justify=CENTER)
    campoSemestre.place(x=600,y=290,width=200,height=50)

    campoOpcionalidad = ttk.Entry(frameMostrarCurso,font=('Arial',12),justify=CENTER)
    campoOpcionalidad.place(x=600,y=360,width=200,height=50)

    campoCreditos = ttk.Entry(frameMostrarCurso,font=('Arial',12),justify=CENTER)
    campoCreditos.place(x=600,y=430,width=200,height=50)

    campoEstado = ttk.Entry(frameMostrarCurso,font=('Arial',12),justify=CENTER)
    campoEstado.place(x=600,y=500,width=200,height=50)
    #Dar valores a los entry
    for dato in probando:
        if dato[0] == comboSeleccionado:
            print(dato[0])
            campoNombre.insert(END,dato[1])
            campoRequisito.insert(END,dato[2])
            campoSemestre.insert(END,dato[4])
            campoOpcionalidad.insert(END,dato[3])
            campoCreditos.insert(END,dato[5])
            campoEstado.insert(END,dato[6])
    #Mensaje curso mostrado
    eg.msgbox('\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir1.center(75,' ')+ '\n' + imprimir.center(75,' '))

def ventana_editar(master, callback=None, args=(), kwargs={}):
    global arbol,probando,prueba,codigoEditar,nombreEditar,requisitoEditar,semestreEditar,opcionalidadEditar,creditosEditar,estadoEditar
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)
    prueba = tk.Frame(master)
    label = Label(prueba,text="Editar Curso")
    label.place(x=630,y=10)
    #saveEntry
    codigoEditar = tk.IntVar()
    nombreEditar = tk.StringVar()
    requisitoEditar = tk.StringVar()
    semestreEditar = tk.IntVar()
    opcionalidadEditar = tk.IntVar()
    creditosEditar = tk.IntVar()
    estadoEditar = tk.IntVar()
    #Entry box
    campoCodigo = ttk.Entry(prueba,font=('Arial',12),textvariable=codigoEditar).place(x=600,y=80,width=200,height=50)
    campoNombre = ttk.Entry(prueba,font=('Arial',12),textvariable=nombreEditar).place(x=600,y=150,width=200,height=50)
    campoRequisito = ttk.Entry(prueba,font=('Arial',12),textvariable=requisitoEditar).place(x=600,y=220,width=200,height=50)
    campoSemestre = ttk.Entry(prueba,font=('Arial',12),textvariable=semestreEditar).place(x=600,y=290,width=200,height=50)
    campoOpcionalidad = ttk.Entry(prueba,font=('Arial',12),textvariable=opcionalidadEditar).place(x=600,y=360,width=200,height=50)
    campoCreditos = ttk.Entry(prueba,font=('Arial',12),textvariable=creditosEditar).place(x=600,y=430,width=200,height=50)
    campoEstado = ttk.Entry(prueba,font=('Arial',12),textvariable=estadoEditar).place(x=600,y=500,width=200,height=50)
    #labels
    labelCursoEditar = Label(prueba,text="Curso a Editar",font=('Arial',11)).place(x=500,y=30,height=30)
    labelCodigo = Label(prueba,text="Codigo",font=('Arial',12)).place(x=500,y=80,height=50)
    labelNombre = Label(prueba,text="Nombre",font=('Arial',12)).place(x=500,y=150,height=50)
    labelRequisito = Label(prueba,text="Pre requisito",font=('Arial',12)).place(x=500,y=220,height=50)
    labelSemestre = Label(prueba,text="Semestre",font=('Arial',12)).place(x=500,y=290,height=50)
    labelOpcionalidad = Label(prueba,text="Opcionalidad",font=('Arial',12)).place(x=500,y=360,height=50)
    labelCreditos = Label(prueba,text="Créditos",font=('Arial',12)).place(x=500,y=420,height=50)
    labelEstado = Label(prueba,text="Estado",font=('Arial',12)).place(x=500,y=500,height=50)
    boton1 = tkinter.Button(prueba, text='Editar', width=15, height=3,bd="4",command=editarCurso)
    boton1.place(x=530,y=600)
    boton = tkinter.Button(prueba, text='Regresar', width=15, height=3,command=callback,bd="4")
    boton.place(x=670,y=600)
    boton2 = tkinter.Button(prueba, text='Mostrar Cursos', width=15, height=3,bd="4",command=mostrarCursos)
    boton2.place(x=820,y=30,width=100,height=30)
    return prueba

def ventana_eliminar(master, callback=None, args=(), kwargs={}):
    global arbol,frameEliminar
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)
    frameEliminar = tk.Frame(master)
    #labels
    labelCursoEditar = Label(frameEliminar,text="Curso a Eliminar",font=('Arial',14)).place(x=400,y=250,height=30)
    label = Label(frameEliminar,text="Eliminar Curso")
    label.place(x=630,y=10)
    boton2 = tkinter.Button(frameEliminar, text='Mostrar Cursos', width=15, height=3,bd="4",command=mostrarCursosEliminar)
    boton2.place(x=820,y=250,width=100,height=30)
    boton1 = tkinter.Button(frameEliminar, text='Eliminar', width=15, height=3,bd="4",command=eliminarCurso)
    boton1.place(x=530,y=600)
    boton = tkinter.Button(frameEliminar, text='Regresar', width=15, height=3,command=callback,bd="4")
    boton.place(x=670,y=600)
    return frameEliminar

def ventana_Conteo(master, callback=None, args=(), kwargs={}):
    global arbol,frameConteo
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)
    frameConteo = tk.Frame(master)
    #labels
    label = Label(frameConteo,text="Conteo de Creditos")
    label.place(x=630,y=10)
    creditosAprobados = Label(frameConteo,text="Créditos Aprobados:",font=('Arial',12)).place(x=400,y=50,height=20)
    creditosCursando = Label(frameConteo,text="Créditos Cursando:",font=('Arial',12)).place(x=400,y=80,height=20)
    creditosPendientes = Label(frameConteo,text="Créditos Pendientes:",font=('Arial',12)).place(x=400,y=110,height=20)
    #Entry
    campoCreditosA = ttk.Entry(frameConteo,font=('Arial',12),justify=CENTER)
    campoCreditosA.place(x=600,y=50,width=100,height=20)
    campoCreditosC = ttk.Entry(frameConteo,font=('Arial',12),justify=CENTER)
    campoCreditosC.place(x=600,y=80,width=100,height=20)
    campoCreditosP = ttk.Entry(frameConteo,font=('Arial',12),justify=CENTER)
    campoCreditosP.place(x=600,y=110,width=100,height=20)
    
    boton = tkinter.Button(frameConteo, text='Regresar', width=15, height=3,command=callback,bd="4")
    boton.place(x=600,y=600)
    return frameConteo

def ventana_mostrarCurso(master, callback=None, args=(), kwargs={}):
    global arbol,frameMostrarCurso
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)
    frameMostrarCurso = tk.Frame(master)
    #labels
    labelCursoEditar = Label(frameMostrarCurso,text="Curso a Mostrar",font=('Arial',14)).place(x=400,y=50,height=30)
    label = Label(frameMostrarCurso,text="Mostrar Curso")
    label.place(x=630,y=10)
    boton = tkinter.Button(frameMostrarCurso, text='Regresar', width=15, height=3,command=callback,bd="4")
    boton.place(x=670,y=600)
    boton2 = tkinter.Button(frameMostrarCurso, text='Mostrar Cursos', width=15, height=3,bd="4",command=mostrarCodigoCursos)
    boton2.place(x=820,y=50,width=100,height=30)
    boton1 = tkinter.Button(frameMostrarCurso, text='Mostrar', width=15, height=3,bd="4",command=mostrarCursoBoton)
    boton1.place(x=530,y=600)
    return frameMostrarCurso

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
mostrarCurso = ventana_mostrarCurso(ventana, mostrar_secundaria)
conteo = ventana_Conteo(ventana, mostrar_principal)

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
boton3 = tkinter.Button(miFrameV, text='Conteo de Crétditos', width=15, height=3,bd="4",command=mostrar_Conteo)
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