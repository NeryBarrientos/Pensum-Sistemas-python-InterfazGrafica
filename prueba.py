import easygui as eg
probando = []
agregados = []
codigos = []
def cargar():
    global probando,agregados,codigos
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
        if len(probando) == 0:
            probando.append(temporal)
            codigos.append(str(prueba[0]))
        else:
            try:
                if str(prueba[0]) in codigos:
                    print("Valor repetido: " + str(prueba[0]))
                    print(codigos.index(str(prueba[0])))
                    print("Valor eliminado: " + str(probando[codigos.index(str(prueba[0]))]))
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
    for element in probando:
        print(element)
cargar()