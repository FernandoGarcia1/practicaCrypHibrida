# -*- coding: utf-8 -*-
import os
import random
import string



def abrirArchivo(archivo):   ##Tamaño
    f = open(archivo, "ab")
    f.write(b"---#&+") #inserta identificador al final del archivo
    f.close()
    f = open(archivo, "rb")
    arc = f.read()   
    mensajeArchivo= arc

    sizefile = os.stat(archivo).st_size    
    residuo = 16- (sizefile%16)

    x = range(residuo)

    
    for n in x:
        arc = arc + b' '

    f.close()
    pos = mensajeArchivo.find(b"---#&+")
    mensajeArchivo= mensajeArchivo[0:pos]
    f= open(archivo,"wb")
    f.write(mensajeArchivo)#regresa el archivo al texto original
    f.close()
    
    return arc


def crearArchivo(mensaje, archivo):
    f =open (archivo, "wb")

    f.write(mensaje)


def cadenaAleatoria(tam):
    S=""
    for x in range(1):
       S=  (''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(tam)))
    
    return S
    


