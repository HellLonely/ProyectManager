import os
import json
import time

from deco import *

def addPath(path):
    str(path)

    data = {
        'settings': [
            {
                "path":path
            }
        ]
    }
    contenido = os.listdir("path/")
    num = int(len(contenido))
    num = num +1

    with open("path/path"+str(num)+".json", 'w') as f:  # Crear JSON con datos del usuario
        json.dump(data, f, indent=4)
