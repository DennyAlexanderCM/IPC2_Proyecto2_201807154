from cmath import nan
from mimetypes import add_type
from linkend_list import LinkedList
from business import Business
from transaction import Transaction
from desktop import Desktop
from stack import Stack
from attention import Attention
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

def systemConfiguration(lista_empresas:LinkedList):
    end = False
    selection = 0

    while not end:
        print("""
        \n---------- Configuración de empresas ----------\n 1. Limpiar sistema\n 2. Cargar archivo (Configuracion sistema)\n 3. Crear nueva empresa\n 4. Cargar archivo (Configuración inicial)\n 5. Regresar""")
        selection = pedirNumeroEntero()
        
        if selection == 1:
            lista_empresas.head = None
            lista_empresas.last = None

        elif selection == 2:
            pathSystemConfiguration = leerArchivo()
            if pathSystemConfiguration:
                XMLSystemConfiguration(pathSystemConfiguration, lista_empresas)
            else:
                print("Sin Cambios.")

        elif selection == 3:
            end_1 = False

            while(not end_1):
                correct = False
                empresa = createNewBussines()
                lista_empresas.append(empresa)

                print("\n¡Empresa creada!\n¿Desea agregar otra empresa?\n 1. Si\n 2. No")
                
                while(not correct):
                    selection = pedirNumeroEntero()
        
                    if selection == 1:
                        correct = True

                    elif selection == 2:
                        correct = True
                        end_1 = True
                    else:
                        print("Intente de nuevo") 

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
        empresa_obj = Business(id_empresa, nombre, abreviatura)
        # CREAMOS LA LISTA QUE CONTENDRA LOS PUNTOS DE ATENCION
        lista_punto_atencion = LinkedList()

        for puntoAtencion in listasPuntosAtencion:
            #ID DEL PUNTO DE ATENCION
            id_punto_atencion = puntoAtencion.getAttribute("id")
            # OBTENEMOS EL PUNTO DE ATENCION
            nombrePuntoAtencion = puntoAtencion.getElementsByTagName("nombre")[0].firstChild.data
            # DIRECCION DEL PUNTO DE ATENCION
            direccionPuntoAtencion = puntoAtencion.getElementsByTagName("direccion")[0].firstChild.data
            # OBTENEMOS LA LISTA DE ESCRITORIOS
            listaEscritorio = puntoAtencion.getElementsByTagName("escritorio")
            # CREAMOS EL OBJETO ATTENTION
            punto_atencion = Attention(id_punto_atencion, nombrePuntoAtencion, direccionPuntoAtencion)
            # CREAMOS LA LISTA QUE CONTENDRA LOS ESCRITORIOS
            lista_escritorios = LinkedList()
            # RECORREMOS LA LISTA DE ESCRITORIOS
            for escritorio in listaEscritorio:
                # OBTENEMOS EL ID DEL ESCRITORIO
                id_escritorio = escritorio.getAttribute("id")
                # ONTENEMOS LA IDENTIFICACION
                identificacion = escritorio.getElementsByTagName("identificacion")[0].firstChild.data
                # OBTENEMOS EL ENCARGADO DEL ESCRITORIO
                encargado = escritorio.getElementsByTagName("encargado")[0].firstChild.data
                # CREAMOS EL OBJETO DESKTOP
                desktop = Desktop(id_escritorio, identificacion, encargado)
                # AÑADIMOS EL OBJETO ESCRITORIO A LA LISTA
                lista_escritorios.append(desktop)
            
            # AÑADIMOS LA LISTA DE ESCRITORIOS AL OBJETO PUNTO DE ATENCION
            punto_atencion.setListaEscritorio(lista_escritorios)
            # AÑADIMOS EL PUNTO DE ATENCION A LA LISTA DE PUNTOS DE ATENCION
            lista_punto_atencion.append(punto_atencion)
        # AÑADIMOS LA LISTA DE PUNTOS DE ATENCION A LA EMPRESA
        empresa_obj.puntosAtencion = lista_punto_atencion
        #  OBTENEMOS LA LISTA DE TRANSACCIONES
        ListaTransacciones = empresa.getElementsByTagName("transaccion")
        # CREAMOS LA LISTA QUE CONTENDRA LAS TRANSACCIONES
        lista_transacciones = LinkedList()
        # RECORREMOS LA LISTA DE TRANSACCIONES
        for transaccion in ListaTransacciones:
            # OBTENEMOS EL ID DE LA TRANSACCION
            id_transaccion = transaccion.getAttribute("id")
            # OBTENEMOS EL NOMBRE DE LA TRANSACCION
            nombretransaccion = transaccion.getElementsByTagName("nombre")[0].firstChild.data
            # TIEMPO DE LA TRANSACCION
            tiempoAtencion = transaccion.getElementsByTagName("tiempoAtencion")[0].firstChild.data
            #CREAMOS EL OBJETO DE LA TRANSACCION
            transaction = Transaction(id_transaccion, nombretransaccion, tiempoAtencion)
            # AGREGAMOS LA TRANSACCION A LA LISTA
            lista_transacciones.append(transaction)
        
        # AGREGAMOS LA LISTA DE TRANSACCIONES A LA EMPRESA
        empresa_obj.transacciones = lista_transacciones
        # AGREGAMOS LA EMPRESA A LA LISTA QUE CONTIENE LAS EMPRESAS
        lista_empresas.append(empresa_obj)
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

def imprimirDatos(lista:LinkedList):
    aux = lista.head

    while aux:
        empresa:Business = aux.data
        empresa.printDates()
        aux_2 = empresa.getPuntosAtencion().head
        while aux_2:
            puntoAten = aux_2.data
            puntoAten.printDates()
            aux_3 = puntoAten.listaEscritorio.head
            while aux_3:
                aux_3.data.printDates()
                aux_3 = aux_3.next
            aux_2 = aux_2.next

        aux_2 = empresa.transacciones.head
        while aux_2:
            puntoAten = aux_2.data
            puntoAten.printDates()
            aux_2 = aux_2.next

        aux = aux.next

def createNewBussines():
    end = False
    id_empresa = ""
    name = ""
    abrev = ""
    lista_puntos_atencion = LinkedList()
    lista_transacciones = LinkedList()
    print("\n---------- Crear nueva empresas ----------")
    while(not end):
        
        if not(id_empresa):
            id_empresa = input("Ingrese el ID: ")
        if not(name):
            name = input("Ingrese el Nombre: ")
        if not(abrev):
            abrev = input("Ingrese abreviatura: ")
        
        if id_empresa and name and abrev:
            
            empresa = Business(id_empresa, name, abrev)
            
            end_1 = False
            while(not end_1):
                punto_atencion = createNewAttention()
                lista_puntos_atencion.append(punto_atencion)

                print("\n¡Punto de atención añadido!\n¿Desea agregar otro punto de atención?\n 1. Si\n 2. No")
                end_2 = False
                while(not end_2):
                    selection = pedirNumeroEntero()
        
                    if selection == 1:
                        end_2 = True

                    elif selection == 2:
                        empresa.setPuntosAtencion(lista_puntos_atencion)
                        end_1 = True
                        end_2 = True
                    else:
                        print("Intente de nuevo")
            
            end_1 = False
            while(not end_1):
                transaccion = createNewTransaction()
                lista_transacciones.append(transaccion)

                print("\n¡Transacción creada!\n¿Desea crear una nueva transaccion?\n 1. Si\n 2. No")
                end_2 = False
                while(not end_2):
                    selection = pedirNumeroEntero()
        
                    if selection == 1:
                        end_2 = True

                    elif selection == 2:
                        empresa.setTransacciones(lista_transacciones)
                        end_1 = True
                        end_2 = True
                    else:
                        print("Intente de nuevo")
            return empresa

        else:
            print("\n¡Ingrese todos los datos requeridos!")
        
        """
            print("\n---------- Agregar escritorios ----------")
            id_escrirorio = input("Ingrese el ID: ")
            identificacion = input("Ingrese la identifiacion: ")
            encargado = input("Ingrese el nombre del encargado: ")"""

def createNewAttention():
    id_punto = ""
    name = ""
    direccion = ""
    lista_escritorio = LinkedList()
    print("\n---------- Crear Punto de atención ----------")
    while True:
        if not(id_punto):
            id_punto = input("Ingrese el ID: ")
        if not(name):
            name = input("Ingrese el Nombre: ")
        if not(direccion):
            direccion = input("Ingrese direccion: ")
        
        if id_punto and name and direccion:
            punto_atencion = Attention(id_punto, name, direccion)

            while True:
                escritorio = createNewDesktop()
                lista_escritorio.append(escritorio)
                print("\n¡Escritorio de atención añadido!\n¿Desea agregar otro Escritorio de atención?\n 1. Si\n 2. No")
                
                end_2 = False
                while(not end_2):
                    selection = pedirNumeroEntero()

                    if selection == 1:
                        end_2 = True

                    elif selection == 2:
                        punto_atencion.setListaEscritorio(lista_escritorio)
                        return punto_atencion
                    else:
                        print("Intente de nuevo")
                

        else:
            print("¡Ingrese todos los datos requeridos!")

def createNewDesktop():
    id = ""
    identificacion = ""
    encargado = ""
    print("\n---------- Crear escritorio de servicio ----------")
    while True:
        if not(id):
            id = input("Ingrese el ID: ")
        if not(identificacion):
            identificacion = input("Ingrese la identificación: ")
        if not(encargado):
            encargado = input("Ingrese el nombre del encargado: ")
        
        if id and identificacion and encargado:
            escritorio = Desktop(id, identificacion, encargado)
            return escritorio
        else:
            print("¡Ingrese todos los datos requeridos!")

def createNewTransaction():
    id = ""
    name = ""
    tiempoAtencion = ""
    print("\n---------- Crear nueva transaccion ----------")
    while True:
        if not(id):
            id = input("Ingrese el ID: ")
        if not(name):
            name = input("Ingrese la identificación: ")
        if not(tiempoAtencion):
            tiempoAtencion = input("Ingrese el nombre del encargado: ")
        
        if id and name and tiempoAtencion:
            transaccion = Transaction(id, name, tiempoAtencion)
            return transaccion
        else:
            print("¡Ingrese todos los datos requeridos!")