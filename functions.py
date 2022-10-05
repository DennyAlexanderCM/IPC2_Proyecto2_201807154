from client import Client
from linkend_list import LinkedList
from business import Business
from transaction import Transaction
from desktop import Desktop
from stack import Stack
from attention import Attention
from xml.dom import minidom
from tkinter import filedialog
from initial_configuration import InitialConfiguration, InitTransaction
from graphviz import Digraph

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

def systemConfiguration(lista_empresas:LinkedList, configuracion_inicial):
    end = False
    selection = 0

    while not end:
        print("""---------- Configuración de empresas ----------\n 1. Limpiar sistema\n 2. Cargar archivo (Configuracion sistema)\n 3. Crear nueva empresa\n 4. Cargar archivo (Configuración inicial)\n 5. Regresar""")
        selection = pedirNumeroEntero()
        
        # VACIA LA LISTA DE LOS DATOS
        if selection == 1:
            lista_empresas.eliminardatos()
            configuracion_inicial.eliminardatos()
            print("¡Datos eliminados")

        elif selection == 2:
            pathSystemConfiguration = leerArchivo()
            if pathSystemConfiguration:
                XMLSystemConfiguration(pathSystemConfiguration, lista_empresas)
            else:
                print("Ningún archivo seleccionado")

        elif selection == 3:
            empresa = createNewBussines()
            lista_empresas.append(empresa)
            print("\n¡Empresa creada!")

        elif selection == 4:
            pathInitialSetup = leerArchivo()
            if pathInitialSetup:
                XMLInitialSetup(pathInitialSetup, configuracion_inicial)
            else:
                print("Ningún archivo seleccionado")
                
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
        empresa_obj = Business(id_empresa, nombre.strip(), abreviatura)

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
            punto_atencion = Attention(id_punto_atencion, nombrePuntoAtencion.strip(), direccionPuntoAtencion)
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
                punto_atencion.addEscritorio(desktop)
            # AÑADIMOS EL PUNTO DE ATENCION A LA LISTA DE PUNTOS DE ATENCION
            empresa_obj.addPuntoAtencion(punto_atencion)
        #  OBTENEMOS LA LISTA DE TRANSACCIONES
        ListaTransacciones = empresa.getElementsByTagName("transaccion")
        # RECORREMOS LA LISTA DE TRANSACCIONES
        for transaccion in ListaTransacciones:
            # OBTENEMOS EL ID DE LA TRANSACCION
            id_transaccion = transaccion.getAttribute("id")
            # OBTENEMOS EL NOMBRE DE LA TRANSACCION
            nombretransaccion = transaccion.getElementsByTagName("nombre")[0].firstChild.data
            # TIEMPO DE LA TRANSACCION
            tiempoAtencion = transaccion.getElementsByTagName("tiempoAtencion")[0].firstChild.data
            #CREAMOS EL OBJETO DE LA TRANSACCION
            transaction = Transaction(id_transaccion.strip(), nombretransaccion, float(tiempoAtencion.strip()))
            # AGREGAMOS LA TRANSACCION A LA LISTA
            empresa_obj.addTransaccion(transaction)
        # AGREGAMOS LA EMPRESA A LA LISTA QUE CONTIENE LAS EMPRESAS
        lista_empresas.append(empresa_obj)
    print("¡Datos cargados!")

def XMLInitialSetup(data, configuracion_inicial:LinkedList):
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
        #ID DEL PUNTO DE ATENCION
        id_punto = configInicial.getAttribute("idPunto")
        #CREAMOS EL OBJETO DE LA CONFIGURACIONINICIAL
        configuracion = InitialConfiguration(id_config, id_empresa, id_punto)
        #CREAMOS LA PILA QUE CONTENDRA LOS ESCRIORIOS
        lista_escritorios = Stack()
        #CREAMOS LA LISTA QUE CONTENDRA LOS CLIENTES
        lista_clientes = LinkedList()
        # ESCRITORIO ACTIVOS
        escritorioActivos = configInicial.getElementsByTagName("escritorio")
        for escritorio in escritorioActivos:
            id_escritorio = escritorio.getAttribute("idEscritorio")
            lista_escritorios.insert(id_escritorio)

        ListaClientes = configInicial.getElementsByTagName("cliente")
        for cliente in ListaClientes:
            # DPI DEL CLIENTE
            dpi = cliente.getAttribute("dpi")
            nombreCliente = cliente.getElementsByTagName("nombre")[0].firstChild.data
            # CREAMOS EL OBJETO CLIENTE
            obj_cliente = Client(dpi, nombreCliente)
            lista_transacciones = LinkedList()
            ListadoTransacciones = cliente.getElementsByTagName("transaccion")

            for transaccion in ListadoTransacciones:
                # ID DE LA TRANSACCION
                id_transaccion = transaccion.getAttribute("idTransaccion")
                # CANTIDAD
                cantidad = transaccion.getAttribute("cantidad")
                # AGREGAMOS AL LISTADO
                lista_transacciones.append(InitTransaction(id_transaccion.strip(), cantidad.strip()))
            
            obj_cliente.lista_transacciones = lista_transacciones
            lista_clientes.append(obj_cliente)
        
        configuracion.escritorios_activos = lista_escritorios
        configuracion.listado_clientes = lista_clientes
        configuracion_inicial.append(configuracion)

    print("¡Datos cargados!")

def createNewBussines():
    end = False
    id_empresa = ""
    name = ""
    abrev = ""

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
                empresa.addPuntoAtencion(punto_atencion)

                print("\n¡Punto de atención añadido!\n¿Desea agregar otro punto de atención?\n 1. Si\n 2. No")
                end_2 = False
                while(not end_2):
                    selection = pedirNumeroEntero()
        
                    if selection == 1:
                        end_2 = True

                    elif selection == 2:
                        end_1 = True
                        end_2 = True
                    else:
                        print("Intente de nuevo")
            
            end_1 = False
            while(not end_1):
                transaccion = createNewTransaction()
                empresa.addTransaccion(transaccion)

                print("\n¡Transacción creada!\n¿Desea crear una nueva transaccion?\n 1. Si\n 2. No")
                end_2 = False
                while(not end_2):
                    selection = pedirNumeroEntero()
        
                    if selection == 1:
                        end_2 = True

                    elif selection == 2:
                        end_1 = True
                        end_2 = True
                    else:
                        print("Intente de nuevo")
            return empresa

        else:
            print("\n¡Ingrese todos los datos requeridos!")

def createNewAttention():
    id_punto = ""
    name = ""
    direccion = ""
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
                punto_atencion.addEscritorio(escritorio)
                print("\n¡Escritorio de atención añadido!\n¿Desea agregar otro Escritorio de atención?\n 1. Si\n 2. No")
                
                end_2 = False
                while(not end_2):
                    selection = pedirNumeroEntero()

                    if selection == 1:
                        end_2 = True

                    elif selection == 2:
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
            name = input("Ingrese el nombre: ")
        if not(tiempoAtencion):
            tiempoAtencion = input("Ingrese el tiempo de atencion: ")
        
        if id and name and tiempoAtencion:
            transaccion = Transaction(id, name, tiempoAtencion)
            return transaccion
        else:
            print("¡Ingrese todos los datos requeridos!")

def selectBussines(lista_empresas:LinkedList):
    aux = lista_empresas.head
    if aux:
        i = 0
        print("\n---------- Seleccionar empresa ----------")
        while aux:
            i += 1
            print(str(i)+". "+aux.data.getNombre())
            aux = aux.next
        
        while True:
            num = pedirNumeroEntero()
            if num <= i and num > 0:
                empresa = lista_empresas.searchDate(num)
                return empresa
            else:
                print("¡Ingrese una opción correcta!")
    else:

        print("¡Lista vacía!")
        return None

def selectPoint(empresa:Business):
    if empresa:
        puntos_atencion:LinkedList = empresa.getPuntosAtencion()
        aux = puntos_atencion.head
        if aux:
            i = 0
            print("\n---------- Seleccionar punto de atención ----------")
            while aux:
                i += 1
                print(str(i)+". "+aux.data.getNombre())
                aux = aux.next

            while True:
                num = pedirNumeroEntero()
                if num <= i and num > 0:
                    pto_atencion = puntos_atencion.searchDate(num)
                    return pto_atencion
                else:
                    print("¡Ingrese una opción correcta!")
        else:
            print("¡Lista vacía!")
            return None
    else:
        return None

def searchConfiguration(id_emresa, id_punto, configuraciones:LinkedList):
    aux = configuraciones.head
    while aux:
        date:InitialConfiguration = aux.data
        if date.getIdEmpresa() == id_emresa and date.getIdPunto() == id_punto:
            return date
        aux = aux.next
    return None

def startTest(empresa: Business, punto_atencion:Attention, configuracion:InitialConfiguration):
    escritorios_activos:Stack = configuracion.escritorios_activos
    lista_escritorios:LinkedList = punto_atencion.getListaEscritorio()
    transacciones = empresa.getTransacciones()
    clientes:LinkedList = configuracion.listado_clientes
    end = False
    selection = 0

    estimarTiempo(clientes, transacciones)

    while not end:
        #ASIGNAR CLIENTES A LOS ESCRITORIOS
        asignarEscritorios(punto_atencion, configuracion)
        tiempoPromedioEspera(clientes, punto_atencion)
        print("""
---------- Configuración de empresas ----------
1. Ver estado de punto de atención
2. Activar escritorio
3. Desactivar escritorio
4. Atender Cliente
5. Solicitud de atención
6. Simular actividad
7. Regresar""")

        selection = pedirNumeroEntero()
        # GRÁFICA EL ESTADO ACTUAL DEL PUNTO DE ATENCION
        if selection == 1:
            graficarEstado(punto_atencion, clientes)
        # ACTIVA EL SIGUIENTE ESCRITORIO DESACTIVADO
        elif selection == 2:
            activar = True
            aux = lista_escritorios.head
            while aux and activar:
                escritorio:Desktop = aux.data
                if escritorio.getEstado() is False:
                    escritorio.activar()
                    escritorios_activos.insert(escritorio.getId())
                    activar = False
                aux= aux.next
        # DESACTIVA EL ULTIMO ESCRITORIO DESACTIVADO
        elif selection == 3:
            # ELIMINAMOS Y RETORNA EL VALOR ELIMINADO
            escritorio = escritorios_activos.pop()
            if escritorio:
                desactivar = True
                aux = lista_escritorios.head
                while aux and desactivar:
                    escritorio_1:Desktop = aux.data
                    if escritorio_1.getId() == escritorio:
                        escritorio_1.desactivar()
                        activar = False
                        print("Escritorio desactivado: "+ escritorio)
                    aux= aux.next
            else:
                print("Ningún escritorio activo")
        # ATENDER CLIENTE AL CLIENTE PROXIMO
        elif selection == 4:
            atenderCliente(punto_atencion, clientes)
        # SOLICITUD DE ATENCION --- AGREGAMOS MANUALMENTE UN CLIENTE AL SISTEMA 
        elif selection == 5:
            end_1 = False
            while(not end_1):
                cliente = crearCliente(transacciones)
                if clientes.emply():
                    tiempo_espera = clientes.last.data.getTiempoAtencion()+ clientes.last.data.getTiempoEsperaPromedio()
                    print("Tiempo promedio de espera: ", tiempo_espera)
                    end_1 = True
                else:
                    print("¡Sin tiempo de espera!")

                clientes.append(cliente)

                print("\n¡Cliente agregado!")
                
                estimarTiempo(clientes, transacciones)

        elif selection == 6:
            end_1 = False
            while(not end_1):
                end_1 = True
                atenderCliente(punto_atencion,clientes)
                asignarEscritorios(punto_atencion, configuracion)
                tiempoPromedioEspera(clientes, punto_atencion)
                graficarEstado(punto_atencion, clientes)
                aux = punto_atencion.getListaEscritorio().head
                while aux:
                    cliente:Client = aux.data.getCliente()
                    if cliente:
                        end_1 = False
                    aux = aux.next
                
            #graficarEstado(punto_atencion, clientes)
        elif selection == 7:
            end = True
        else:
            print("Intente de nuevo")

def crearCliente(lista_transacciones:LinkedList):
    end = False
    dpi = ""
    nombre = ""
    transacciones = LinkedList()
    print("\n---------- Solicitar turno ----------")
    while(not end):
        if not(dpi):
            dpi = input("Ingrese su número de DPI: ")
        if not(nombre):
            nombre = input("Ingrese el Nombre: ")

        if dpi and nombre:
            
            cliente = Client(dpi, nombre)
            
            end_1 = False
            while(not end_1):
                end_2 = False
                id_transaccion = ""
                cantidad = 0
                print("\n-------- Agregar Transacción --------")
                while(not end_2):
                    if not(id_transaccion):
                        id_transaccion = crearTransaccion(lista_transacciones)
                    if cantidad == 0:
                        print("\n>>Cantidad de transacciones")
                        cantidad = pedirNumeroEntero()
                    if id_transaccion and cantidad != 0:
                        transaccion = InitTransaction(id_transaccion, cantidad)
                        transacciones.append(transaccion)
                        id_transaccion = ""
                        cantidad = 0

                        print("\n¡Transaccion agregada!\n¿Desea agregar otra transacción?\n 1. Si\n 2. No")
                        end_3 = False
                        while(not end_3):
                            selection = pedirNumeroEntero()
                            if selection == 1:
                                end_3 = True

                            elif selection == 2:
                                cliente.lista_transacciones = transacciones
                                return cliente
                            else:
                                print("Intente de nuevo")

def crearTransaccion(listaTransacciones:LinkedList):
    aux = listaTransacciones.head
    i = 0

    print("\n>>Seleccionar transacción")
    while aux:
        i += 1
        print(str(i)+". "+aux.data.getNombre())
        aux = aux.next
    
    while True:
        num = pedirNumeroEntero()
        if num <= i and num > 0:
            empresa = listaTransacciones.searchDate(num)
            return empresa.getId()
        else:
            print("¡Ingrese una opción correcta!")
    
def estimarTiempo(clientes, transacciones):
    # ESTIMAR TIEMPO DE ATENCION CADA CLIENTE
    aux = clientes.head
    while aux:
        cliente:Client = aux.data
        time = 0
        aux_2 = cliente.lista_transacciones.head
        while aux_2:
            transaccion = aux_2.data
            aux_3 = transacciones.head
            while aux_3:
                transaccion_1 = aux_3.data
                if transaccion.id_transaccion == transaccion_1.getId():
                    tiempo = transaccion_1.getTiempo()
                    n_transaccion = int(transaccion.cantidad)
                    tiempo_tot = (tiempo*n_transaccion)
                    transaccion.time = tiempo_tot
                    time += tiempo_tot
                aux_3 = aux_3.next
            aux_2 = aux_2.next
        cliente.tiempoT = time
        cliente.tiempo_atencion = time
        aux = aux.next

def tiempoPromedioEspera(clientes:LinkedList, puntos_atencion:Attention):
    prom_tiempo = puntos_atencion.promedioAtencion()
    aux = clientes.head
    while aux:
        cliente:Client = aux.data
        cliente.setTiempoEsperaPromedio(prom_tiempo)
        prom_tiempo += cliente.tiempo_atencion
        aux = aux.next

def asignarEscritorios(punto_atencion:Attention, configuracion:InitialConfiguration):
    # ACTIVAR ESCRITORIOS
    aux = configuracion.escritorios_activos.head
    while aux:
        aux_2 = punto_atencion.getListaEscritorio().head
        while aux_2:
            escritorio = aux_2.data
            if escritorio.getId() == aux.data:
                escritorio.activar()
            aux_2 = aux_2.next
        aux=aux.next
    
    # ASIGNAR CLIENTES A ESCRITORIOS
    aux = punto_atencion.getListaEscritorio().head
    while aux :
        escritorio:Desktop = aux.data
        if escritorio.getEstado():
            if escritorio.getCliente() is None:
                cliente = configuracion.listado_clientes.pop()
                if cliente:
                    escritorio.atenderCliente(cliente)
        aux = aux.next

def atenderCliente(punto_atencion:Attention, clientes:LinkedList):
    lista_escritorios = punto_atencion.getListaEscritorio()
    tiempos = LinkedList()
    aux = lista_escritorios.head
    while aux:
        if aux.data.getCliente():
            cliente: Client = aux.data.getCliente()
            tiempos.append(cliente.getTiempo())
        aux = aux.next
            
    min = tiempos.tiempoMenor()

    if min > 0:
        aux = lista_escritorios.head
        while aux:
            cliente:Client = aux.data.getCliente()
            if cliente:
                tiempo = cliente.getTiempo()
                if tiempo == min:
                    print("Cliente: ",cliente.getNombre()," Atendido")
                    aux.data.clienteAtendido()
                    aux.data.addTiempoAtencion(cliente.getTiempoAtencion())
                    punto_atencion.contarTransaccion()
                    punto_atencion.addTiempoAtencion(cliente.getTiempoAtencion())
                    punto_atencion.addTiempoEspera(cliente.tiempo_espera_total)
                else:
                    cliente.quitarTiempo(min)
            aux = aux.next
        
        aux = clientes.head
        while aux:
            cliente:Client = aux.data
            cliente.agregarTiempoEspera(min)
            aux = aux.next
    else:
        print("Error, ningún cliente atendido")

def graficarEstado(punto_atencion:Attention, lista_clientes:LinkedList):
    s = Digraph()

    txt_escritorios = """<<table border='0' cellborder='0'><tr><td width="500">ESCRITORIOS DE ATENCION</td></tr>
    <tr><td><table color='orange' cellspacing='0' cellpadding='7'><tr><td>ESCRITORIO</td><td>CLIENTE</td></tr>"""

    #OBTENER DATOS DE ESCRITORIOS DE ATENCION
    activos_n = 0
    desactivados_n = 0
    aux = punto_atencion.getListaEscritorio().head
    while aux:
        escritorio:Desktop = aux.data
        if escritorio.getEstado() or escritorio.getCliente():
            activos_n += 1

            if escritorio.getCliente():
                cliente:Client = escritorio.getCliente()
                txt_escritorios += "<tr><td><table border='0' cellborder='0'><tr><td>ID: "+escritorio.getId()+"</td></tr><tr><td>Encargado: "+escritorio.getEncargado()+"</td></tr><tr><td>Clientes atendidos: "+str(escritorio.getAtendidos())+"</td></tr><tr><td>Promedio de atención: "+str(escritorio.promedioAtencion())+"</td></tr><tr><td>Tiempo máximo de atención: "+str(escritorio.maximoAtencion())+"</td></tr><tr><td>Tiempo mínimo de atención: "+str(escritorio.minimoAtencion())+"</td></tr></table></td>"
                txt_escritorios += "<td><table border='0' cellborder='0'><tr><td>Nombre: "+cliente.getNombre()+"</td></tr><tr><td>Tiempo restante de atención: "+str(cliente.getTiempo())+"</td></tr><tr><td>Tiempo de espera: "+str(cliente.tiempo_espera_total)+"</td></tr></table></td></tr>"
            else:
                txt_escritorios += "<tr><td><table border='0' cellborder='0'><tr><td>ID: "+escritorio.getId()+"</td></tr><tr><td>Encargado: "+escritorio.getEncargado()+"</td></tr><tr><td>Clientes atendidos: "+str(escritorio.getAtendidos())+"</td></tr><tr><td>Promedio de atención: "+str(escritorio.promedioAtencion())+"</td></tr><tr><td>Tiempo máximo de atención: "+str(escritorio.maximoAtencion())+"</td></tr><tr><td>Tiempo mínimo de atención: "+str(escritorio.minimoAtencion())+"</td></tr></table></td>"
                txt_escritorios += "<td></td></tr>"
        else:
            desactivados_n += 1
            txt_escritorios += "<tr><td bgcolor='#b8c0ff'><table border='0' cellborder='0'><tr><td>ID: "+escritorio.getId()+"</td></tr><tr><td>Encargado: "+escritorio.getEncargado()+"</td></tr><tr><td>Clientes atendidos: "+str(escritorio.getAtendidos())+"</td></tr><tr><td>Promedio de atención: "+str(escritorio.promedioAtencion())+"</td></tr><tr><td>Tiempo máximo de atención: "+str(escritorio.maximoAtencion())+"</td></tr><tr><td>Tiempo mínimo de atención: "+str(escritorio.minimoAtencion())+"</td></tr></table></td>"
            txt_escritorios += "<td></td></tr>"
        aux = aux.next

    txt_escritorios += "</table></td></tr></table>>"
    s.node('tab', label=txt_escritorios, shape='none')
    
    #OBTENER DATOS DE LA LISTA DE CLIENTES EN ESPERA
    clientes_espera = 0
    txt_clientes = """<<table border='0' cellborder='0'><tr><td width="450">CLIENTES EN ESPERA</td></tr><tr><td>
    <table color='orange' cellspacing='0' cellpadding='7'><tr><td>No.</td><td>CLIENTES</td></tr>"""

    aux = lista_clientes.head
    while aux:
        clientes_espera +=1
        cliente:Client = aux.data
        txt_clientes += "<tr><td>"+str(clientes_espera)+"</td><td><table border='0' cellborder='0'><tr><td>Nombre: "+cliente.getNombre()+"</td></tr><tr><td>Tiempo de atención: "+str(cliente.getTiempo())+"</td></tr><tr><td>Tiempo promedio de espera: "+str(cliente.getTiempoEsperaPromedio())+"</td></tr></table></td></tr>"
        aux = aux.next

    txt_clientes +="</table></td></tr></table>>"
    s.node('clientes', label=txt_clientes, shape='none')
    s.attr(label = "\nEscritorios activos: "+str(activos_n)+"\nEscritorios Inactivos: "+str(desactivados_n)+"\nClientes en espera: "+str(clientes_espera)+"\nTiempo promedio de atención: "+str(punto_atencion.promedioAtencion())+"\nTiempo máximo de atención: "+str(punto_atencion.maximoAtencion())+"\nTiempo mínimo de atención: "+str(punto_atencion.minimoAtencion())+"\nTiempo promedio de espera: "+str(punto_atencion.promedioEsperta())+"\nTiempo máximo de espera: "+str(punto_atencion.maximoEspera())+"\nTiempo mínimo de espera: "+str(punto_atencion.minimoEspera()), fontsize='25', pad="2", bgcolor="white")
    
    s.render('Datos/'+punto_atencion.getNombre()+'/'+str(punto_atencion.getNumeroTransacciones()),format='jpg')