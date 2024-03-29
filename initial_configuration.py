from stack import Stack
class InitialConfiguration:
    def __init__(self, id, id_empresa, id_punto):
        self.id = id
        self.id_empresa = id_empresa
        self.id_punto = id_punto
        self.escritorios_activos = Stack()
        self.listado_clientes= None
    
    def getId(self):
        return self.id
    
    def getIdEmpresa(self):
        return self.id_empresa

    def getIdPunto(self):
        return self.id_punto
    
    def getEscritoriosActivos(self):
        return self.escritorios_activos
    
    def addEscritorioActivo(self, id):
        self.escritorios_activos.insert(id)

class InitTransaction:
    def __init__(self, id_transaccion, cantidad):
        self.id_transaccion = id_transaccion
        self.cantidad = cantidad
        self.time = 0