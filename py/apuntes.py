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


def generateApuntes(name, path):
    crPath = str(path) + "\_" + str(name)  # Crear path ampliado

    try:
        makeDir(name, path)
    except:
        newname = input(color.RED + "Nombre en uso, introduce otro Nombre $-> " + color.END)
        while newname == name:
            newname = input(color.RED + "Nombre en uso, introduce otro Nombre $-> " + color.END)
        makeDir(newname, path)
        # Cambia el nombre original por el nuevo nombre
        name = newname
    tematic = input(color.RED + "Asignatura o Tema $-> " + color.END)
    createMD(path, name, tematic)
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


# MD apuntes
def createMD(path, name, tematic):
    crPath = str(path) + "\_" + str(name)
    file = open(crPath + "\mainApuntes.md", "w")
    file.write("# " + name + os.linesep)
    file.write("### Asignatura : " + tematic)
    destatus = input(
        color.CYAN + "Quieres añadir una descripcion de los apuntes? (y/n) \n" + color.RED + "$-> " + color.END)
    if destatus == "y":
        description = input(color.RED + "Descripción $-> " + color.END)
        file.write(description + "\n\n")
    else:
        time.sleep(0.1)

    file.write("Powered by ProyectManager")
    file.close


# Pagina final del menu
def finish(name):
    os.system("cls")
    menu()
    print("  Proyecto " + name + " creado con exito")
