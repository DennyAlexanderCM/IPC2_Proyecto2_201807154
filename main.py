from functions import *

def run():
    lista_empresas = LinkedList()
    end = False
    selection = 0

    while not end:
        print("\n------------------ Menú ------------------\n  1. Configuración de empresas\n  2. Seleccionar Empresa y puntos de atención\n  3. Manejo de puntos de atención\n  4. Salir")

        selection = pedirNumeroEntero()
        
        if selection == 1:
            systemConfiguration(lista_empresas)

        elif selection == 2:
            imprimirDatos(lista_empresas)

        elif selection == 3:
            pass
                
        elif selection == 4:
            print("Finalizando programa...")
            end = True
        else:
            print("Intente de nuevo") 

#Método incial
if __name__ == '__main__':
    run()