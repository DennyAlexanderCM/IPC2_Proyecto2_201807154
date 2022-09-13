from xml.dom import minidom
from tkinter import filedialog

def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce una opción: "))
            correcto=True
        except ValueError:
            print('¡Error, introduce un numero entero!')
    return num  

def systemConfiguration():
    end = False
    selection = 0

    while not end:
        print("""
        \n---------- Configuración de empresas ----------\n 1. Limpiar sistema\n 2. Cargar archivo (Configuracion sistema)\n 3. Crear nueva empresa\n 4. Cargar archivo (Configuración inicial)\n 5. Regresar""")
        selection = pedirNumeroEntero()
        
        if selection == 1:
            pass

        elif selection == 2:
            pathSystemConfiguration = leerArchivo()
            if pathSystemConfiguration:
                XMLSystemConfiguration(pathSystemConfiguration)
            else:
                print("Sin Cambios.")

        elif selection == 3:
            pass

        elif selection == 4:
            pathInitialSetup = leerArchivo()
            if pathInitialSetup:
                print(pathInitialSetup)
            else:
                print("Sin Cambios.")
                
        elif selection == 5:
            end = True
        else:
            print("Intente de nuevo") 


def leerArchivo():
    #obtenemos la direccion local del archivo
    root = filedialog.askopenfilename(title= "Abrir Archivo", filetypes=(("Xml","*.xml"),("Todos los archivos","*.*")))
    if root != "":
        return root
    return None 

def XMLSystemConfiguration(data):
    #LISTA QUE CONTRENDRÁ CADA PACIENTE
    doc = minidom.parse(data)

    # Elemento raíz del documento
    rootNode = doc.documentElement
    # Obtenemos cada elemento con la etiqueta paciente
    empresas = rootNode.getElementsByTagName("empresa")
    
    for empresa in empresas:
        #ID DE LA EMPRESA
        id_empresa = empresa.getAttribute("id")
        # OBTENEMOS EL NOMBRE
        nombre = empresa.getElementsByTagName("nombre")[0].firstChild.data
        # OBTENEMOS EL ELEMENTO
        abreviatura = empresa.getElementsByTagName("abreviatura")[0].firstChild.data
        # OBTENEMOS EL NÚMERO DE PERIODOS
        listasPuntosAtencion = empresa.getElementsByTagName("listaPuntosAtencion")[0].firstChild.data
        print(id_empresa, nombre, abreviatura)
    
    print("Datos cargadodos...")