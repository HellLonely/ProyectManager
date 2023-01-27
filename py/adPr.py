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


def generateProyect(name, path):
    crPath = str(path) + "\_" + str(name)

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
    language = input(color.RED + "Lenguaje $-> " + color.END)
    crPath = str(path) + "\_" + str(name)
    dataJson(name, author, language, path)
    dirs = input(color.CYAN + "Quieres crear algun directorio (y/n) \n" + color.RED + "$-> " + color.END)
    if dirs == "y":
        cont = int(input(color.RED + "Cuantos? $-> " + color.END))
        for i in range(cont):
            conter = str(i + 1)
            name2 = input(color.RED + "Nombre Directorio " + conter + " $-> " + color.END)
            crPath2 = str(path) + "\_" + name + "\_" + str(name2)
            os.mkdir(crPath2)
    else:
        time.sleep(0.1)
    print(" ")
    status = input(color.CYAN + "Quieres crear archivos " + language + " (y/n) \n" + color.RED + "$-> " + color.END)
    if status == "y":
        create(language, path, name)
    else:
        time.sleep(0.1)

    readstatus = input(color.CYAN + "Quieres crear README.md " + language + " (y/n) \n" + color.RED + "$-> " + color.END)
    if readstatus == "y":
        createReadme(path,name,author)
    else:
        time.sleep(0.1)
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
def dataJson(name, author, language, path):
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


# Crear archivos propios del lenguaje.
def create(language, path, name):
    language = str(language)
    crPath = str(path) + "\_" + str(name)
    if language == "Java" or "java":
        file = open(crPath + "\main.java", 'w')
        file.close
    elif language == "Python" or "python" or "py":
        file = open(crPath + "\main.py", 'w')
        file.close

# Crear readme
def createReadme(path, name,author):
    crPath = str(path) + "\_" + str(name)
    file = open(crPath + "\README.md","w")
    file.write("# "+ name + os.linesep)
    destatus = input(color.CYAN + "Quieres añadir una descripcion? (y/n) \n" + color.RED + "$-> " + color.END)
    if destatus == "y":
        description = input(color.RED + "Descripción $-> " + color.END)
        file.write(description+"\n\n")
    else:
        time.sleep(0.1)

    file.write("@author "+author +"\n\n" + "### Version 0.1\n\n")
    file.write("Powered by ProyectManager")
    file.close


def finish(name):
    os.system("cls")
    menu()
    print("  Proyecto "+name+" creado con exito")