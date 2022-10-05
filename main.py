from functions import *

def run():
    lista_empresas = LinkedList()
    configuracion_inicial = LinkedList()
    
    end = False
    selection = 0

    # VARIABLES
    empresa = None
    pto_atencion = None

    while not end:
        print("\n------------------ Menú ------------------\n  1. Configuración de empresas\n  2. Seleccionar Empresa y puntos de atención\n  3. Manejo de puntos de atención\n  4. Salir")

        selection = pedirNumeroEntero()
        
        if selection == 1:
            systemConfiguration(lista_empresas, configuracion_inicial)

        elif selection == 2:
            empresa = selectBussines(lista_empresas)
            if empresa:
                pto_atencion = selectPoint(empresa)
            else:
                print("Seleccione la empresa")

        elif selection == 3:
            if empresa !=None and pto_atencion != None:
                configuraciones = searchConfiguration(empresa.getId(), pto_atencion.getId(), configuracion_inicial)
                if configuraciones:
                   startTest(empresa, pto_atencion, configuraciones)
                else:
                    print("Sin configuraciones encontradas")
            else:
                print("Datos incorrectos")
                
        elif selection == 4:
            print("Finalizando programa...")
            end = True
        else:
            print("Intente de nuevo") 

#Método incial
if __name__ == '__main__':
    run()