class Desktop():
    def __init__(self, id, identificacion, encargado):
        self.id = id
        self.identificacion = identificacion
        self.encargado = encargado
        self.estado = False
    
    def getId(self):
        return self.id
    
    def getIdentificacion(self):
        return self.identificacion

    def getEncargado(self):
        return self.encargado
    
    def getEstado(self):
        return self.estado
    
    def setId(self, id):
        self.id = id
    
    def setIdentificacion(self, identificacion):
        self.identificacion = identificacion
    
    def setEncargado(self, encargado):
        self.encargado = encargado
    
    def setEstado(self, estado):
        self.estado = estado
    
    def printDates(self):
        print(self.id, self.identificacion, self.encargado)
    
    