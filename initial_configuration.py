class InitialConfiguration:
    def __init__(self, id, id_empresa, id_punto):
        self.id = id
        self.id_empresa = id_empresa
        self.id_punto = id_punto
        self.escritorios_activos = None
        self.listado_clientes= None
    
    def getId(self):
        return self.id
    
    def getIdEmpresa(self):
        return self.id_empresa

    def getIdPunto(self):
        return self.id_punto