#CLASE NODO
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#CLASE DE LA LISTA ENLAZADA PARA GUARGAR LOS PATRONES DE CADA PISO
class Stack:
    def __init__(self):
        self.head = None

    # VERIFICAMOS SI LA LISTA ESTA VACÍA
    def emply(self):
        return self.head
    
    # AGREGAMOS LOS DATOS AL FINAL
    def insert(self, data):
        nodo = Node(data)
        
        if not self.emply():
            self.head = nodo
        else:
            nodo.next = self.head
            self.head = nodo
    
    # RETORNAR EL NÚMERO DE ELEMENTOS
    def length(self):
        n = 0
        i = self.head
        while i:
            i = i.next
            n+=1
        return n

    # BUSCAMOS UN DATO EN ESPECIFICO POR SU POSICION
    def searchDate(self, selection):
        n = 1
        i = self.head
        while i:
            if selection == n:
                return i.data
            else:
                n +=1 
                i = i.next  
        return False
    
    def print(self):
        aux = self.head
        while aux:
            print(aux.data)
            aux = aux.next
    
    def pop(self):
        if not self.emply():
            return None
        else:
            aux = self.head
            self.head = self.head.next
            return aux.data