from tkinter import messagebox as MessageBox
from Crypto.PublicKey import RSA
from tkinter import filedialog
import os
from pathlib import Path

def generarLLaves(llavePriv, llavePublic):
    llave = RSA.generate(2048)

    f = open(llavePriv, "wb")
    f.write(llave.exportKey('PEM'))
    f.close

    f = open(llavePublic, "wb")
    f.write(llave.public_key().export_key('PEM'))
    f.close 

    MessageBox.showinfo("Alerta!", "LLaves Generadas")

def getDireccionArchivo(direccion, extension):
    direccion[0]= filedialog.askopenfilename(title = "Open key", filetypes = [("Files "+extension, "*."+extension), ("All files", "*.*")])


def crearArchivoAgregandoCaracteres(rutaArchivo, mensaje, caracter, extension): ##Crea un archivo con el nombre del archivo que se pasa en ruta archivo y agrega caracteres
                                                                    ##Ejemplo mensje.txt ->> mensaje_C.txt

    
    rutaArchivo=os.path.split(rutaArchivo)
    nombreArchivo= rutaArchivo[1]
    nombreArchivo=nombreArchivo.split(".")
    nuevoNombre=nombreArchivo[0]+"_"+caracter+"."+extension
    nuevoArchivo= rutaArchivo[0]+"/"+nuevoNombre

    f = open(nuevoArchivo, "wb")
    
    f.write(mensaje)
    f.close()
    
    return nuevoArchivo
    

def nuevaRuta(rutaArchivo,caracter,extension):
    rutaArchivo=os.path.split(rutaArchivo)
    nombreArchivo= rutaArchivo[1]
    nombreArchivo=nombreArchivo.split(".")
    nuevoNombre=nombreArchivo[0]+"_"+caracter+"."+extension
    nuevoArchivo= rutaArchivo[0]+"/"+nuevoNombre
    return nuevoArchivo