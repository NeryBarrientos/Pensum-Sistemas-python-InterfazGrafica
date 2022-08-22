from tkinter import messagebox
from ttkthemes import ThemedTk
import tkinter
from tkinter import *
from tkinter import ttk
import easygui as eg
import functools
import tkinter as tk
from os import system
system("cls")

probando = []
nombreCurso = []
agredados = []
codigoCurso = []
codigos = []
codigosBien = []

def cargar():
    global probando,codigos,codigosBien
    imprimir = '*********************************************'
    imprimir1 = 'Archivo Cargado exitosamente'
    imprimir2 = 'Archivo no seleccionado, vuelva a intentarlo'
    extension = ["*.py","*.pyc"]
    archivo = eg.fileopenbox(msg="Abrir archivo",
                         title="Control: fileopenbox",
                         default='C:/Users/neri_/OneDrive/Escritorio/*lfp',
                         filetypes=extension)
    mensaje = 'Ruta del Archivo: ' + str(archivo) + '\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir1.center(75,' ') + '\n' + imprimir.center(75,' ') + '\n'
    messagebox.showinfo(message=mensaje,title="Mensaje")
    f = open(archivo,'r',encoding="utf8")
    for linea in f:
        temporal = []
        prueba = linea.rstrip('\n')
        prueba = prueba.split(',')
        temporal = [str(prueba[0])] + [str(prueba[1])] + [str(prueba[2])] + [str(prueba[3])] + [str(prueba[4])] + [str(prueba[5])] + [str(prueba[6])]
        if len(probando) == 0:
            probando.append(temporal)
            codigos.append(str(prueba[0]))
        else:
            try:
                if str(prueba[0]) in codigos:
                    probando.pop(codigos.index(str(prueba[0])))
                    codigos.remove(str(prueba[0]))
                    probando.append(temporal)
                else:
                    probando.append(temporal)
                    codigos.append(str(prueba[0]))
            except ValueError:
                probando.append(temporal)
                codigos.append(str(prueba[0]))
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
    #editar
    if len(agredados) == 0:
        #print("Vacia")
        for element in probando:
            agredados.append(element)
            arbol.insert("",END,text=element[0],values=(element[1],element[2],element[3],element[4],element[5],element[6]),iid=element[0])
    else:
        #print("Con datos")
        for element in probando:
            if element in agredados:
                continue
            else:
                codigos.append(str(element[0]))
                arbol.insert("",END,text=element[0],values=(element[1],element[2],element[3],element[4],element[5],element[6]),iid=element[0])
    for element in probando:
        codigosBien.append(element[0])

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
    boton.place(x=600,y=580)
    return main_frame    

def ObtenerEntry():
    global probando, arbol,codigos,codigosBien
    #print(codigosBien)
    imprimir = '*********************************************'
    imprimir1 = 'Dato Opcionalidad fuera de rango'
    imprimir2 = 'Dato estado fuera de rango'
    imprimir3 = 'Curso Agregado Correctamente'
    imprimir4 = 'Dato semestre fuera de rango'
    imprimir5 = 'Curso ya existente, eliminado anterior y sustituio por el actual'
    correcto = True
    if opcionalidad.get() == 1:
        temporal = "Obligatorio"
    elif opcionalidad.get() == 0:
        temporal = "Opcional"
    else:
        messagebox.showerror(message='\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir1.center(75,' ')+ '\n' + imprimir.center(75,' '),title="Error")
        correcto = False        
    if estado.get() == 0:
        temporal1 = "Aprobado"
    elif estado.get() == 1:
        temporal1 = "Cursando"
    elif estado.get() == -1:
        temporal1 = "Pendiente"
    else:
        messagebox.showerror(message='\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir2.center(75,' ')+ '\n' + imprimir.center(75,' '),title="Error")
        correcto = False
    if semestre.get() >=1 and semestre.get() <=10:
        prueba = ''
    else:
        correcto = False
        messagebox.showerror(message='\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir4.center(75,' ')+ '\n' + imprimir.center(75,' '),title="Error")
    temp = [codigo.get()] + [nombre.get()] + [requisito.get()] + [semestre.get()] + [temporal] + [creditos.get()] + [temporal1]
    if correcto == True:
        if len(probando) == 0:
            probando.append(temp)
            codigosBien.append(str(codigo.get()))
        else:
            try:
                if str(codigo.get()) in codigosBien:
                    probando.pop(codigosBien.index(str(codigo.get())))
                    codigosBien.remove(str(codigo.get()))
                    arbol.delete(str(codigo.get()))
                    probando.append(temp)
                    arbol.insert("",END,text=codigo.get(),values=(nombre.get(),requisito.get(),temporal,semestre.get(),creditos.get(),temporal1),iid=codigo.get())
                    messagebox.showwarning(message='\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir5.center(75,' ') + '\n' + imprimir.center(75,' '),title="Advertencia")
                else:
                    probando.append(temp)
                    codigosBien.append(str(codigo.get()))
                    arbol.insert("",END,text=codigo.get(),values=(nombre.get(),requisito.get(),temporal,semestre.get(),creditos.get(),temporal1),iid=codigo.get())
                    messagebox.showinfo(message='\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir3.center(75,' ') + '\n' + imprimir.center(75,' '),title="Mensaje")
            except ValueError:
                probando.append(temp)
                codigosBien.append(str(codigo.get()))
                arbol.insert("",END,text=codigo.get(),values=(nombre.get(),requisito.get(),temporal,semestre.get(),creditos.get(),temporal1),iid=codigo.get())
                messagebox.showinfo(message='\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir3.center(75,' ') + '\n' + imprimir.center(75,' '),title="Mensaje")

def ventana_agregar(master, callback=None, args=(), kwargs={}):
    global arbol,codigo,nombre,requisito,semestre,opcionalidad,creditos,estado
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)
    main_frame = tk.Frame(master)
    label = Label(main_frame,text="Agregar Curso")
    label.place(x=615,y=30)
    #saveEntry
    codigo = tk.StringVar()
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
    boton1.place(x=520,y=580)
    boton = tkinter.Button(main_frame, text='Regresar', width=15, height=3,command=callback,bd="4")
    boton.place(x=680,y=580)
    return main_frame    

def mostrarCursos():
    global combo,nombreCurso
    temporal = []
    for valor in probando:
        temporal.append(valor[0])
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
    imprimir3 = 'Curso editado Correctamente'
    imprimir4 = 'Dato semestre fuera de rango'
    correcto = True
    comboSeleccionado = combo.get()
    if opcionalidadEditar.get() == 1:
        temporal = "Obligatorio"
    elif opcionalidadEditar.get() == 0:
        temporal = "Opcional"
    else:
        messagebox.showerror(message='\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir1.center(75,' ')+ '\n' + imprimir.center(75,' '),title="Error")
        correcto = False        
    if estadoEditar.get() == 0:
        temporal1 = "Aprobado"
    elif estadoEditar.get() == 1:
        temporal1 = "Cursando"
    elif estadoEditar.get() == -1:
        temporal1 = "Pendiente"
    else:
        messagebox.showerror(message='\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir2.center(75,' ')+ '\n' + imprimir.center(75,' '),title="Error")
        correcto = False
    if semestreEditar.get() >=1 and semestreEditar.get() <=10:
        prueba = ''
    else:
        correcto = False
        messagebox.showerror(message='\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir4.center(75,' ')+ '\n' + imprimir.center(75,' '),title="Error")
    temp = [codigoeditar.get()] + [nombreEditar.get()] + [requisitoEditar.get()] + [semestreEditar.get()] + [temporal] + [creditosEditar.get()] + [temporal1]
    if correcto == True:
        if len(probando) == 0:
            probando.append(temp)
            codigosBien.append(str(codigoeditar.get()))
        else:
            try:
                if str(comboSeleccionado) in codigosBien:
                    #print(f"Lo encontre {comboSeleccionado}")
                    #print(codigosBien)
                    poscodigo = codigosBien.index(str(comboSeleccionado))
                    #print(poscodigo)
                    probando[poscodigo][0] = codigoeditar.get()
                    probando[poscodigo][1] = nombreEditar.get()
                    probando[poscodigo][2] = requisitoEditar.get()
                    probando[poscodigo][3] = temporal
                    probando[poscodigo][4] = semestreEditar.get()
                    probando[poscodigo][5] = creditosEditar.get()
                    probando[poscodigo][6] = temporal1
                    codigosBien[poscodigo] = codigoeditar.get()
                    arbol.insert("",END,text=codigoeditar.get(),values=(nombreEditar.get(),requisitoEditar.get(),temporal,semestreEditar.get(),creditosEditar.get(),temporal1),iid=codigoeditar.get())
                    indexanterior = arbol.index(comboSeleccionado)
                    indexactual = arbol.index(codigoeditar.get())
                    arbol.move(comboSeleccionado,"",index=indexactual)
                    arbol.move(codigoeditar.get(),"",indexanterior)
                    arbol.delete(comboSeleccionado)
                    messagebox.showinfo(message='\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir3.center(75,' ') + '\n' + imprimir.center(75,' '),title="Mensaje")
                else:
                    messagebox.showinfo(message='\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir3.center(75,' ') + '\n' + imprimir.center(75,' '),title="Mensaje")
            except ValueError:
                messagebox.showinfo(message='\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir3.center(75,' ') + '\n' + imprimir.center(75,' '),title="Mensaje")

def eliminarCurso():
    global probando,arbol
    imprimir = '*********************************************'
    imprimir1 = 'Curso Eliminado Correctamente'
    comboSeleccionado = comboEliminar.get()
    for elemento in range(len(probando)):
        if probando[elemento][1] == comboSeleccionado:
            #print(f"Lo encontre: {probando[elemento]}")
            arbol.delete(probando[elemento][0])
            probando.pop(elemento)
            break
    messagebox.showinfo(message='\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir1.center(75,' ') + '\n' + imprimir.center(75,' '),title="Mensaje")

def mostrarCursoBoton():
    global probando,arbol
    imprimir = '*********************************************'
    imprimir1 = 'Curso mostrado Correctamente'
    comboSeleccionado = comboEliminar1.get()
    #Entry box
    campoCodigo = Entry(frameMostrarCurso,font=('Arial',12),justify=CENTER)
    campoCodigo.place(x=600,y=80,width=200,height=50)
    campoCodigo.insert("0",comboSeleccionado)
    campoCodigo.config(state="readonly")

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
            #print(dato[0])
            campoNombre.insert("0",dato[1])
            campoRequisito.insert("0",dato[2])
            campoSemestre.insert("0",dato[4])
            campoOpcionalidad.insert("0",dato[3])
            campoCreditos.insert("0",dato[5])
            campoEstado.insert("0",dato[6])
    campoNombre.config(state="readonly")
    campoRequisito.config(state="readonly")
    campoSemestre.config(state="readonly")
    campoOpcionalidad.config(state="readonly")
    campoCreditos.config(state="readonly")
    campoEstado.config(state="readonly")
    #Mensaje curso mostrado
    messagebox.showinfo(message='\n\n\n\n\n' + imprimir.center(75,' ') + '\n' + imprimir1.center(75,' ') + '\n' + imprimir.center(75,' '),title="Mensaje")

def ventana_editar(master, callback=None, args=(), kwargs={}):
    global arbol,probando,prueba,nombreEditar,requisitoEditar,semestreEditar,opcionalidadEditar,creditosEditar,estadoEditar,codigoeditar
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)
    prueba = tk.Frame(master)
    label = Label(prueba,text="Editar Curso")
    label.place(x=630,y=10)
    #saveEntry
    codigoeditar = tk.StringVar()
    nombreEditar = tk.StringVar()
    requisitoEditar = tk.StringVar()
    semestreEditar = tk.IntVar()
    opcionalidadEditar = tk.IntVar()
    creditosEditar = tk.IntVar()
    estadoEditar = tk.IntVar()
    #Entry box
    campoCodigo = ttk.Entry(prueba,font=('Arial',12),textvariable=codigoeditar).place(x=600,y=80,width=200,height=50)
    campoNombre = ttk.Entry(prueba,font=('Arial',12),textvariable=nombreEditar).place(x=600,y=150,width=200,height=50)
    campoRequisito = ttk.Entry(prueba,font=('Arial',12),textvariable=requisitoEditar).place(x=600,y=220,width=200,height=50)
    campoSemestre = ttk.Entry(prueba,font=('Arial',12),textvariable=semestreEditar).place(x=600,y=290,width=200,height=50)
    campoOpcionalidad = ttk.Entry(prueba,font=('Arial',12),textvariable=opcionalidadEditar).place(x=600,y=360,width=200,height=50)
    campoCreditos = ttk.Entry(prueba,font=('Arial',12),textvariable=creditosEditar).place(x=600,y=430,width=200,height=50)
    campoEstado = ttk.Entry(prueba,font=('Arial',12),textvariable=estadoEditar).place(x=600,y=500,width=200,height=50)
    #labels
    labelCursoEditar = Label(prueba,text="Curso a Editar",font=('Arial',11)).place(x=500,y=30,height=30)
    labelEditar = Label(prueba,text="Codigo",font=('Arial',12)).place(x=500,y=80,height=50)
    labelNombre = Label(prueba,text="Nombre",font=('Arial',12)).place(x=500,y=150,height=50)
    labelRequisito = Label(prueba,text="Pre requisito",font=('Arial',12)).place(x=500,y=220,height=50)
    labelSemestre = Label(prueba,text="Semestre",font=('Arial',12)).place(x=500,y=290,height=50)
    labelOpcionalidad = Label(prueba,text="Opcionalidad",font=('Arial',12)).place(x=500,y=360,height=50)
    labelCreditos = Label(prueba,text="Créditos",font=('Arial',12)).place(x=500,y=420,height=50)
    labelEstado = Label(prueba,text="Estado",font=('Arial',12)).place(x=500,y=500,height=50)
    boton1 = tkinter.Button(prueba, text='Editar', width=15, height=3,bd="4",command=editarCurso)
    boton1.place(x=520,y=580)
    boton = tkinter.Button(prueba, text='Regresar', width=15, height=3,command=callback,bd="4")
    boton.place(x=680,y=580)
    boton2 = tkinter.Button(prueba, text='Mostrar Cursos', width=15, height=3,bd="4",command=mostrarCursos)
    boton2.place(x=820,y=30,width=150,height=30)
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
    boton2.place(x=820,y=250,width=150,height=30)
    boton1 = tkinter.Button(frameEliminar, text='Eliminar', width=15, height=3,bd="4",command=eliminarCurso)
    boton1.place(x=520,y=580)
    boton = tkinter.Button(frameEliminar, text='Regresar', width=15, height=3,command=callback,bd="4")
    boton.place(x=680,y=580)
    return frameEliminar

def creditosAprobados():
    suma = 0
    for dato in probando:
        if dato[6] == "Aprobado":
            suma += int(dato[5])
    campoCreditosA = ttk.Entry(frameConteo,font=('Arial',12),justify=CENTER)
    campoCreditosA.place(x=600,y=50,width=100,height=20)
    campoCreditosA.insert("0",suma)
    campoCreditosA.config(state="readonly")

def creditosCursando():
    suma = 0
    for dato in probando:
        if dato[6] == "Cursando":
            suma += int(dato[5])
    campoCreditosC = ttk.Entry(frameConteo,font=('Arial',12),justify=CENTER)
    campoCreditosC.place(x=600,y=80,width=100,height=20)
    campoCreditosC.insert("0",suma)
    campoCreditosC.config(state="readonly")

def creditosPendiente():
    suma = 0
    for dato in probando:
        if dato[6] == "Pendiente":
            suma += int(dato[5])
    campoCreditosP = ttk.Entry(frameConteo,font=('Arial',12),justify=CENTER)
    campoCreditosP.place(x=600,y=110,width=100,height=20)
    campoCreditosP.insert("0",suma)
    campoCreditosP.config(state="readonly")

def creditosobligatorios():
    suma = 0
    opcionseleccionada = comboO.get()
    for dato in probando:
        if int(dato[4]) <= int(opcionseleccionada) and dato[3] == "Obligatorio":
            suma += int(dato[5])
    campoCreditosO = ttk.Entry(frameConteo,font=('Arial',12),justify=CENTER)
    campoCreditosO.place(x=700,y=140,width=100,height=20)
    campoCreditosO.insert("0",suma)
    campoCreditosO.config(state="readonly")

def creditosSemestre():
    suma = 0
    opcionseleccionada = combo1.get()
    for dato in probando:
        if int(dato[4]) == int(opcionseleccionada):
            suma += int(dato[5])
    campoCreditosS = ttk.Entry(frameConteo,font=('Arial',12),justify=CENTER)
    campoCreditosS.place(x=580,y=210,width=100,height=20)
    campoCreditosS.insert("0",suma)
    campoCreditosS.config(state="readonly")

def ventana_Conteo(master, callback=None, args=(), kwargs={}):
    global arbol,frameConteo,campoCreditosA,campoCreditosC,campoCreditosP,comboO,combo1,campoCreditosO,campoCreditosS
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)
    frameConteo = tk.Frame(master)
    #labels
    label = Label(frameConteo,text="Conteo de Creditos")
    label.place(x=630,y=10)
    labelcreditosAprobados = Label(frameConteo,text="Créditos Aprobados:",font=('Arial',12)).place(x=400,y=50,height=20)
    labelcreditosCursando = Label(frameConteo,text="Créditos Cursando:",font=('Arial',12)).place(x=400,y=80,height=20)
    labelcreditosPendientes = Label(frameConteo,text="Créditos Pendientes:",font=('Arial',12)).place(x=400,y=110,height=20)
    labelcreditosObligatorios = Label(frameConteo,text="Creditos obligatorios hasta semestre N:",font=('Arial',12)).place(x=400,y=140,height=20)
    labelcreditosSemestre = Label(frameConteo,text="Creditos del semestre:",font=('Arial',12)).place(x=400,y=210,height=20)
    #Entry
    campoCreditosA = ttk.Entry(frameConteo,font=('Arial',12),justify=CENTER,state="readonly")
    campoCreditosA.place(x=600,y=50,width=100,height=20)
    campoCreditosC = ttk.Entry(frameConteo,font=('Arial',12),justify=CENTER,state="readonly")
    campoCreditosC.place(x=600,y=80,width=100,height=20)
    campoCreditosP = ttk.Entry(frameConteo,font=('Arial',12),justify=CENTER,state="readonly")
    campoCreditosP.place(x=600,y=110,width=100,height=20)
    campoCreditosO = ttk.Entry(frameConteo,font=('Arial',12),justify=CENTER,state="readonly")
    campoCreditosO.place(x=700,y=140,width=100,height=20)
    campoCreditosS = ttk.Entry(frameConteo,font=('Arial',12),justify=CENTER,state="readonly")
    campoCreditosS.place(x=580,y=210,width=100,height=20)
    #botones
    boton = tkinter.Button(frameConteo, text='Regresar', width=15, height=3,command=callback,bd="4")
    boton.place(x=600,y=580)
    botonAprobados = tkinter.Button(frameConteo, text='Mostrar', width=15, height=3,bd="4",command=creditosAprobados)
    botonAprobados.place(x=710,y=50,width=100,height=20)
    botonCursando = tkinter.Button(frameConteo, text='Mostrar', width=15, height=3,bd="4",command=creditosCursando)
    botonCursando.place(x=710,y=80,width=100,height=20)
    botonPendiente = tkinter.Button(frameConteo, text='Mostrar', width=15, height=3,bd="4",command=creditosPendiente)
    botonPendiente.place(x=710,y=110,width=100,height=20)
    botonCreditosO = tkinter.Button(frameConteo, text='Contar', width=15, height=3,bd="4",command=creditosobligatorios)
    botonCreditosO.place(x=600,y=175,width=100,height=20)
    botonCreditosS = tkinter.Button(frameConteo, text='Contar', width=15, height=3,bd="4",command=creditosSemestre)
    botonCreditosS.place(x=600,y=255,width=100,height=20)
    #combo
    numeros = ["1","2","3","4","5","6","7","8","9","10"]
    comboO = ttk.Combobox(frameConteo,font=('Arial',10),state="readonly",values=numeros)
    comboO.place(x=550,y=170,width=50,height=30)
    combo1 = ttk.Combobox(frameConteo,font=('Arial',10),state="readonly",values=numeros)
    combo1.place(x=550,y=250,width=50,height=30)
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
    boton.place(x=680,y=580)
    boton2 = tkinter.Button(frameMostrarCurso, text='Mostrar Cursos', width=15, height=3,bd="4",command=mostrarCodigoCursos)
    boton2.place(x=820,y=50,width=150,height=30)
    boton1 = tkinter.Button(frameMostrarCurso, text='Mostrar', width=15, height=3,bd="4",command=mostrarCursoBoton)
    boton1.place(x=520,y=580)
    return frameMostrarCurso

def salir():
    exit()

#ventana = tkinter.Tk()
#Abro venta
ventana = ThemedTk(theme="ubuntu")
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
boton4 = tkinter.Button(miFrameV, text='Salir', width=15, height=3,command=salir,bd="4")
boton4.place(x=600,y=410)

#frame Inferior
miFrame1 = Frame()
miFrame1.pack(side="bottom",fill="x")
miFrame1.config(width="500",height="30",relief="solid",bd="3")
ventana.mainloop()