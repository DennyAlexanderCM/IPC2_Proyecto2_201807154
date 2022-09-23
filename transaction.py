class Transaction():
    def __init__(self, id, nombre, tiempoAtencion):
        self.id = id
        self.nombre = nombre
        self.tiempoAtencion = tiempoAtencion
    
    def getId(self):
        return self.id
    def getNombre(self):
        return self.nombre

    def getTiempo(self):
        return self.tiempoAtencion

    def setId(self, id):
        self.id = id
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setTiempo(self, tiempoAtencion):
        self.tiempoAtencion = tiempoAtencion
    
    def printDates(self):
        print(self.id, self.nombre, self.tiempoAtencion)