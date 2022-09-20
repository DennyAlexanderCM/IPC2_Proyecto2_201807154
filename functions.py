from linkend_list import LinkedList
from business import Business
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

def systemConfiguration(lista_empresas):
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
                XMLSystemConfiguration(pathSystemConfiguration, lista_empresas)
            else:
                print("Sin Cambios.")

        elif selection == 3:
            pass

        elif selection == 4:
            pathInitialSetup = leerArchivo()
            if pathInitialSetup:
                XMLInitialSetup(pathInitialSetup)
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

def XMLSystemConfiguration(data, lista_empresas:LinkedList):
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
        listasPuntosAtencion = empresa.getElementsByTagName("puntoAtencion")
        # CREAMOS EL OBJETO EMPRESA
        print("Empresa: ", id_empresa, nombre, abreviatura)

        for puntoAtencion in listasPuntosAtencion:
            nombrePuntoAtencion = puntoAtencion.getElementsByTagName("nombre")[0].firstChild.data
            direccionPuntoAtencion = puntoAtencion.getElementsByTagName("direccion")[0].firstChild.data
            listaEscritorio = puntoAtencion.getElementsByTagName("escritorio")
            print("Punto atención: ",nombrePuntoAtencion, direccionPuntoAtencion)
            for escritorio in listaEscritorio:
                id_escritorio = escritorio.getAttribute("id")
                identificacion = escritorio.getElementsByTagName("identificacion")[0].firstChild.data
                encargado = escritorio.getElementsByTagName("encargado")[0].firstChild.data
                print("Escritorio: ", id_escritorio, identificacion, encargado)
        
        ListaTransacciones = empresa.getElementsByTagName("transaccion")
        for transaccion in ListaTransacciones:
            nombretransaccion = transaccion.getElementsByTagName("nombre")[0].firstChild.data
            tiempoAtencion = transaccion.getElementsByTagName("tiempoAtencion")[0].firstChild.data
            
            print("Transaccion: ", nombretransaccion, tiempoAtencion)
    
    print("Datos cargadodos...")

def XMLInitialSetup(data):
    #LISTA QUE CONTRENDRÁ CADA PACIENTE
    doc = minidom.parse(data)
    # Elemento raíz del documento
    rootNode = doc.documentElement
    # Obtenemos cada elemento con la etiqueta paciente
    listadoInicial = rootNode.getElementsByTagName("configInicial")
    
    for configInicial in listadoInicial:
        #ID DE LA CONFIG
        id_config = configInicial.getAttribute("id")
        #ID DE LA EMPRESA
        id_empresa = configInicial.getAttribute("idEmpresa")
        #ID DEL PUNTO
        id_punto = configInicial.getAttribute("idPunto")
        # ESCRITORIO ACTIVOS
        escritorioActivos = configInicial.getElementsByTagName("escritorio")
        print("Config Inicial: ", id_config, id_empresa, id_punto)
        for escritorio in escritorioActivos:
            idEscritorio = escritorio.getAttribute("idEscritorio")
            print("Escritorio: ",idEscritorio)

        ListaClientes = configInicial.getElementsByTagName("cliente")
        for cliente in ListaClientes:
            # DPI DEL CLIENTE
            dpi = cliente.getAttribute("dpi")
            nombreCliente = cliente.getElementsByTagName("nombre")[0].firstChild.data
            ListadoTransacciones = cliente.getElementsByTagName("transaccion")
            print("Cliente: ",dpi, nombreCliente)

            for transaccion in ListadoTransacciones:
                # ID DE LA TRANSACCION
                id_transaccion = transaccion.getAttribute("idTransaccion")
                # CANTIDAD
                cantidad = transaccion.getAttribute("cantidad")
                print("Transacción: ", id_transaccion, cantidad)
    
    print("Datos cargadodos...")