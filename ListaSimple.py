import Nodo
cn = Nodo

class LSimple(object):
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacio(self):
        if self.primero == None:
            return True
        else:
            return False

    def Agregar(self,codigo,nombre,prerequisitos,obligatorio,semestre,creditos,estado):
        nuevo = cn.nodo(codigo,nombre,prerequisitos,obligatorio,semestre,creditos,estado)
        if self.vacio():
            self.primero = self.ultimo = nuevo
            self.ultimo.siguiente = self.primero
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
            self.ultimo.siguiente = self.primero

    def printLista(self):
        if self.vacio():
            print('Lista Vacia')
        else:
            validar = True
            aux = self.primero
            n = 1
            while validar:
                print(f'Codigo: {aux.codigo} nombre: {aux.nombre} prerequisitos: {aux.prerequisitos} obligatorio:  {aux.obligatorio} semestre: {aux.semestre} creditos: {aux.creditos} estado: {aux.estado}')
                n += 1
                if aux == self.ultimo:
                    validar = False
                else:
                    aux = aux.siguiente

    def ObtenerLista(self):
        datos = []
        if self.vacio():
            print('Lista Vacia')
        else:
            validar = True
            aux = self.primero
            n = 1
            while validar:
                temporal = []
                temporal = [aux.codigo] + [aux.nombre] + [aux.prerequisitos] + [aux.obligatorio] + [aux.semestre] + [aux.creditos] + [aux.estado]
                datos.append(temporal)
                n += 1
                if aux == self.ultimo:
                    validar = False
                else:
                    aux = aux.siguiente
            return datos