import os
import time
import json
from plyer import notification
from deco import *
from py.adPr import *
from py.simPr import *
from py.apuntes import *
from py.pathAdd import *


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# Probamos a leer el archivo de config json, si no se crea uno.

try:
    open('py/settings.json')
except:
    print("Error to read setting.json")



# Funcion para abrir menu y escoger opciones
def selec():
    menu()
    selector()
    option = input(color.YELLOW + "$-> " + color.END)
    opt(int(option))


def opt(option):
    if option == 0:
        exit()
    elif option == 1:
        readSettings()
    elif option == 2:
        os.system("cls")
        menu()
        print("Creando un Proyecto Simple \n")
        pathsRecomendados()
        name = input(color.RED + "Nombre Proyecto $-> " + color.END)
        path = input(color.RED + "Path $-> " + color.END)
        generateProyectSim(name, path)

    elif option == 3:
        os.system("cls")
        menu()
        print("Creando un Proyecto Avanzado \n")
        pathsRecomendados()
        name = input(color.RED + "Nombre Proyecto $-> " + color.END)
        path = input(color.RED + "Path $-> " + color.END)
        generateProyect(name, path)

    elif option == 4:
        os.system("cls")
        menu()
        print("Creando unos Apuntes \n")
        pathsRecomendados()
        name = input(color.RED + "Nombre Apuntes $-> " + color.END)
        path = input(color.RED + "Path $-> " + color.END)
        generateApuntes(name, path)

    elif option == 5:
        os.system("cls")
        menu()
        print("Añadiendo nuevo Path")
        pathsRecomendados()
        path = input(color.RED + "Path $-> " + color.END)
        addPath(path)

    elif option == 6:
        os.system("cls")
        menu()
        pathsRecomendados()
        time.sleep(3)


def pathsRecomendados():  # Muestra todos los paths añadidos en la carpeta de path
    contenido = os.listdir("path/")
    num = int(len(contenido))
    print("Paths añadidos")
    for i in range(1,num+1):
        if i == 1:
            with open('path/path.json') as file:  # Leer archivo settings.json y mostrar info
                data = json.load(file)
                for client in data['settings']:
                    pathReco = str(client['path'])
                    print(pathReco)
        else:
            with open('path/path'+str(i)+'.json') as file:  # Leer archivo settings.json y mostrar info
                data = json.load(file)
                for client in data['settings']:
                    pathReco = str(client['path'])
                    print(pathReco)

    print(" ")

def readSettings(): # Lectura de la configuracion/settings.json
    try:
        with open('py/settings.json') as file:  # Leer archivo settings.json y mostrar info
            data = json.load(file)
            for client in data['info']:
                name = str(client['name'])
                version = str(client['version'])
                author = str(client['author'])
                github = str(client['git-hub'])
        os.system("cls")
        menu()
        print("Nombre del programa -> " + name)
        print("Version -> " + version)
        print("Autor -> " + author)
        print("Git Hub -> " + github)

        print("Volviendo al menu en 5s..")
        time.sleep(5)
        os.system("cls")
        selec()
    except:  # Si no es capaz de leer el archivo mandara este mensaje
        print("No se a podido leer el settings.json")
        print("Volviendso al menu en 5s..")
        time.sleep(5)
        os.system("cls")
        selec()

selec()

