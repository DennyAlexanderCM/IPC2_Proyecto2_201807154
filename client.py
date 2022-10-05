from platform import release


class Client:
    def __init__(self, DPI, nombre):
        self.DPI = DPI
        self.nombre = nombre
        self.lista_transacciones = None
        self.tiempoT = 0
        self.tiempo_espera_promedio = 0
        self.tiempo_atencion = 0
        self.tiempo_espera = 0
        self.tiempo_espera_total = 0
    
    def getDPI(self):
        return self.DPI
    
    def getNombre(self):
        return self.nombre
    
    def getTransacciones(self):
        return self.lista_transacciones
    
    def getTiempo(self):
        return self.tiempoT
        
    def getTiempoAtencion(self):
        return self.tiempo_atencion
    
    def getTiempoEsperaPromedio(self):
        return self.tiempo_espera_promedio
    
    def addTiempo(self, tiempo):
        self.tiempoT += tiempo
        self.tiempo_atencion += tiempo
    
    def quitarTiempo(self, tiempo):
        self.tiempoT -= tiempo
    
    def agregarTiempoEspera(self,tiempo):
        self.tiempo_espera_total += tiempo

    def setTiempoEspera(self, tiempo):
        self.tiempo_espera = tiempo
    
    def setTiempoEsperaPromedio(self, tiempo):
        self.tiempo_espera_promedio = tiempo