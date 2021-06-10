#importamos libreria para crear directorios
import os
NOMBRE_CARPETA = 'Directorio/'
FORMATO_ARCHIVO = '.json'

def ejecutarApp():
    crearDirectorio()
    mostrarMenu()
    ejecutarDesicion()


def crearDirectorio():
    if not os.path.exists(NOMBRE_CARPETA):
        os.makedirs(NOMBRE_CARPETA)

def mostrarMenu():
    print("--------MENU DE CONTACTOS--------")
    print('1. Buscar contacto')
    print('2. Agregar contacto')
    print('3. Ver contactos')
    print('4. Editar contacto')
    print('5. Eliminar contacto')
    print('6. Salir del programa')

def ejecutarDesicion():
    ejecucion=True
    while ejecucion:
        desicion = int(input('Seleccione una accion!..   '))
        if desicion == 1:
            buscarContacto()
            ejecucion=False
        elif desicion == 2:
            agregarContacto()
            ejecucion=False
        elif desicion == 3:
            mostrarContactos()
            ejecucion=False
        elif desicion == 4:
            editarContacto()
            ejecucion=False
        elif desicion == 5:
            eliminarContacto()
            ejecucion=False
        elif desicion == 6:
            break;
        else:
            print('Accion no valida, vuelva a ingresar!')

class Contacto:
    def __init__(self,nombre,telefono,categoria):
        self._nombre=nombre
        self._telefono=telefono
        self._categoria=categoria
    
    def getNombre(self):
        return self._nombre
    def getTelefono(self):
        return self._telefono
    def getCategoria(self):
        return self._categoria

def agregarContacto():
    print('---AGREGANDO CONTACTO---')
    nombre_contacto = input("Nombre: ")
    telefono_contacto = input("Telefono: ")
    categoria_contacto = input("Categoria: ")
    EXISTE_CONTACTO = existeContacto(nombre_contacto)

    if not EXISTE_CONTACTO:
        contacto1 = Contacto(nombre_contacto,telefono_contacto,categoria_contacto)

        with open(NOMBRE_CARPETA+nombre_contacto+FORMATO_ARCHIVO,'w') as nuevo_contacto:
            nuevo_contacto.write(f'Nombre: {contacto1._nombre}\r\n')
            nuevo_contacto.write(f'Telefono: {contacto1._telefono}\r\n')
            nuevo_contacto.write(f'Categoria: {contacto1._categoria}\r\n')
        print('\nContacto registrado!.')
    else:
        print('El contacto ya existe!')
        ejecutarDesicion()

def editarContacto():
    print("---EDITANDO CONTACTO---")
    nombre_contacto = input("Escriba el nombre del contacto: ")
    EXISTE_CONTACTO = existeContacto(nombre_contacto)

    if EXISTE_CONTACTO:
        print('Contacto encontrado!!')
        nombre_nuevo=input("Nuevo nombre: ")
        contacto_nuevo=input("Nuevo telefono: ")
        categoria_nueva=input("Nueva categoria: ")
        contacto = Contacto(nombre_nuevo,contacto_nuevo,categoria_nueva)
        with open(NOMBRE_CARPETA+nombre_contacto+FORMATO_ARCHIVO,'w') as actualizar_contacto:
            actualizar_contacto.write(f'Nombre: {contacto._nombre}\r\n')
            actualizar_contacto.write(f'Telefono: {contacto._telefono}\r\n')
            actualizar_contacto.write(f'Categoria: {contacto._categoria}\r\n')
            os.rename(NOMBRE_CARPETA+nombre_contacto+FORMATO_ARCHIVO,NOMBRE_CARPETA+nombre_nuevo+FORMATO_ARCHIVO)
        print("Contacto Actualizado!!")
    else:
        print('el contacto no existe')
    ejecutarDesicion()

def existeContacto(nombre_contacto):
    return os.path.isfile(NOMBRE_CARPETA+nombre_contacto+FORMATO_ARCHIVO)

def mostrarContactos():
    print('---MOSTRANDO CONTACTO---')
    contacto=os.listdir(NOMBRE_CARPETA)
    LISTA_CONTACTO=[i for i in contacto if i.endswith(FORMATO_ARCHIVO)]
    for cada_contacto in LISTA_CONTACTO:
        with open(NOMBRE_CARPETA+cada_contacto) as archivo:
            for cada_linea in archivo:
                print(cada_linea.strip())
            print('\r\n')

def buscarContacto():
    print('---BUSCAR CONTACTO---')
    nombre_contacto=input('Nombre del contacto: ')
    try:
        with open(NOMBRE_CARPETA+nombre_contacto+FORMATO_ARCHIVO) as archivo:
            for cada_linea in archivo:
                print(cada_linea.rstrip())
            print('\r\n')
    except os.error:
        print(f'El contacto no existe, {os.error}')
        ejecutarDesicion()

def eliminarContacto():
    print('---ELIMINANDO CONTACTO---')
    nombre_contacto=input('Nombre del contacto: ')
    try:
        os.remove(NOMBRE_CARPETA+nombre_contacto+FORMATO_ARCHIVO)
        print('Contacto eliminado!!')
    except os.error:
        print(f'No se econtró el contacto: {os.error}')
    ejecutarDesicion()

ejecutarApp()