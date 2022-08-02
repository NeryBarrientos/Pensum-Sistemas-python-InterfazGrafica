class nodo:
    def __init__(self,codigo,nombre,prerequisitos,obligatorio,semestre,creditos,estado):
        self.codigo = codigo
        self.nombre = nombre
        self.prerequisitos = prerequisitos
        self.obligatorio = obligatorio
        self.semestre =semestre
        self.creditos = creditos
        self.estado = estado
        self.siguiente = None
