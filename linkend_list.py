#CLASE NODO
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    # VERIFICAMOS SI LA LISTA ESTA VACÍA
    def emply(self):
        return self.head
    
    # AGREGAMOS LOS DATOS AL FINAL
    def append(self, data):
        nodo = Node(data)
        if not self.emply():
            self.head = nodo
            self.last = nodo
        else:
            self.last.next = nodo
            nodo.prev = self.last
            self.last = nodo
    
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
    
    def eliminardatos(self):
        if self.length() > 0:
            self.head = None
            self.last = None
    
    def pop(self):
        if not self.emply():
            return None
        else:
            aux = self.head
            self.head = self.head.next
            return aux.data
    
    def tiempoMenor(self):
        aux = self.head
        menor = aux
        if aux:
            while aux:
                if aux.next:
                    if menor.data > aux.next.data:
                        menor = aux.next
                else:
                    return menor.data
                aux = aux.next
        else:
            return 0
    
    def tiempoMayor(self):
        aux = self.head
        menor = aux
        if aux:
            while aux:
                if aux.next:
                    if menor.data < aux.next.data:
                        menor = aux.next
                else:
                    return menor.data
                aux = aux.next
        else:
            return 0
    
    def tiempoPromedio(self):
        if not self.emply():
            return 0
        else:
            aux = self.head
            count = 0
            while aux:
                count += aux.data
                aux = aux.next

            count = count/self.length()

            return count
        
        

            
