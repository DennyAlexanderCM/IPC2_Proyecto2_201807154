class Desktop():
    def __init__(self, id, identificacion, encargado):
        self.id = id
        self.identificacion = identificacion
        self.encargado = encargado
        self.estado = False
        self.cliente = None
    
    def getId(self):
        return self.id
    
    def getIdentificacion(self):
        return self.identificacion

    def getEncargado(self):
        return self.encargado
    
    def getEstado(self):
        return self.estado
    
    def getCliente(self):
        return self.cliente
    
    def setId(self, id):
        self.id = id
    
    def setIdentificacion(self, identificacion):
        self.identificacion = identificacion
    
    def setEncargado(self, encargado):
        self.encargado = encargado
    
    def activar(self):
        self.estado = True
    
    def desactivar(self):
        self.estado = False
    
    def atenderCliente(self, cliente):
        self.cliente = cliente
    
    def clienteAtendido(self):
        self.cliente = None
    
    