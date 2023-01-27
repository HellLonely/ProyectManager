import os
import json
import time

from deco import *


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

def generateProyectSim(name, path):
    crPath = str(path) + "\_" + str(name) # Crear path ampliado

    # Comprueba que el nombre del proyecto no se repita
    try:
        makeDir(name, path)
    except:
        newname = input(color.RED + "Nombre en uso, introduce otro Nombre $-> " + color.END)
        while newname == name:
            newname = input(color.RED + "Nombre en uso, introduce otro Nombre $-> " + color.END)
        makeDir(newname, path)
        # Cambia el nombre original por el nuevo nombre
        name = newname
    author = input(color.RED + "Autor $-> " + color.END)
    dataJson(name, author, path)
    finish(name)


# Crear la carpeta
def makeDir(name, path):
    if path == "":
        while path == "":
            path = input(color.RED + "Require Path $-> " + color.END)
            crPath = str(path) + "\_" + str(name)
            os.mkdir(crPath)
    else:
        crPath = str(path) + "\_" + str(name)
        os.mkdir(crPath)

# Crear archivo de información Json
def dataJson(name, author, path):
    crPath = str(path) + "\_" + str(name)
    data = {
        'info': [
            {
                'name': name,
                'author': author,
                'verison': 0.1,
            }
        ]
    }
    with open(crPath + "\proyect_info.json", 'w') as f:  # Crear JSON con datos del usuario
        json.dump(data, f, indent=4)

# Pagina final del menu
def finish(name):
    os.system("cls")
    menu()
    print("  Proyecto "+name+" creado con exito")