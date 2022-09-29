from platform import release


class Client:
    def __init__(self, DPI, nombre):
        self.DPI = DPI
        self.nombre = nombre
        self.lista_transacciones = None
        self.tiempoT = 0
    
    def getDPI(self):
        return self.DPI
    
    def getNombre(self):
        return self.nombre
    
    def getTransacciones(self):
        return self.lista_transacciones
    
    def getTiempo(self):
        return self.tiempoT
    
    def addTiempo(self, tiempo):
        self.tiempoT += tiempo
    
    def quitarTiempo(self, tiempo):
        self.tiempoT -= tiempo