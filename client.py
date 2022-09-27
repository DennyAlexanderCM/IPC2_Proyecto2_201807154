class Client:
    def __init__(self, DPI, nombre):
        self.DPI = DPI
        self.nombre = nombre
        self.lista_transacciones = None
    
    def getDPI(self):
        return self.DPI
    
    def getNombre(self):
        return self.nombre