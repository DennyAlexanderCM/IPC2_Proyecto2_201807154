class Business:
    def __init__(self, id_empresa, nombre, abreviatura):
        self.id_empresa = id_empresa
        self.nombre = nombre
        self.abreviatura = abreviatura
    
    def getId(self):
        return self.id_empresa
    
    def getNombre(self):
        return self.nombre
    
    def getAbreviatura(self):
        return self.abreviatura
    
    def setId(self, id_empresa):
        self.id_empresa = id_empresa
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setAbreviatura(self, abreviatura):
        self.abreviatura = abreviatura
    
    