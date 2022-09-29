from linkend_list import LinkedList
class Business:
    def __init__(self, id_empresa, nombre, abreviatura):
        self.id_empresa = id_empresa
        self.nombre = nombre
        self.abreviatura = abreviatura
        self.puntosAtencion = LinkedList()
        self.transacciones = LinkedList()
    
    def getId(self):
        return self.id_empresa
    
    def getNombre(self):
        return self.nombre
    
    def getAbreviatura(self):
        return self.abreviatura

    def getPuntosAtencion(self):
        return self.puntosAtencion
    
    def getTransacciones(self):
        return self.transacciones

    def setId(self, id_empresa):
        self.id_empresa = id_empresa
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setAbreviatura(self, abreviatura):
        self.abreviatura = abreviatura
    
    def setPuntosAtencion(self, puntosAtencion):
        self.puntosAtencion = puntosAtencion
    
    def setTransacciones(self, transacciones):
        self.transacciones = transacciones
    
    def addPuntoAtencion(self, punto):
        self.puntosAtencion.append(punto)
    
    def addTransaccion(self, transaccion):
        self.transacciones.append(transaccion)
    