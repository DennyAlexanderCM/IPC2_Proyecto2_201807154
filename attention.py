from linkend_list import LinkedList
class Attention():
    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.listaEscritorio = LinkedList()
        self.transaccion = 0
        self.tiempos_atencion = LinkedList()
        self.tiempos_espera = LinkedList()
    
    def getId(self):
        return self.id
    
    def getNombre(self):
        return self.nombre
    
    def getDireccion(self):
        return self.direccion
    
    def getListaEscritorio(self):
        return self.listaEscritorio
    
    def getNumeroTransacciones(self):
        return self.transaccion

    def setId(self, id):
        self.id = id
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setDireccion(self, direccion):
        self.direccion = direccion
    
    def setListaEscritorio(self, listaEscitorio):
        self.listaEscritorio = listaEscitorio   

    def addEscritorio(self, escritorio):
        self.listaEscritorio.append(escritorio)
    
    def addEscritorioActivo(self, activo):
        self.escritoriosActivos.insert(activo)
    
    def contarTransaccion(self):
        self.transaccion += 1
    
    def addTiempoEspera(self, tiempo):
        if tiempo>0:
            self.tiempos_espera.append(tiempo)

    def promedioEsperta(self):
        return self.tiempos_atencion.tiempoPromedio()
    
    def minimoEspera(self):
        return self.tiempos_espera.tiempoMenor()
    
    def maximoEspera(self):
        return self.tiempos_espera.tiempoMayor()
    
    def addTiempoAtencion(self, tiempo):
        self.tiempos_atencion.append(tiempo)
    
    def promedioAtencion(self):
        return self.tiempos_atencion.tiempoPromedio()
    
    def minimoAtencion(self):
        return self.tiempos_atencion.tiempoMenor()
    
    def maximoAtencion(self):
        return self.tiempos_atencion.tiempoMayor()