from cifrar_descifrar import cifrar, cifrarECB, descifrar, descifrarECBa, rsaCifrar
from archivos import cadenaAleatoria
from funcionesHash import signature
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox as MessageBox
from tkinter import filedialog
from tkinter.ttk import *
from functools import partial

from funArchivos import *
from funcionesHash import *
##Variables de Hash


direccionArchivoTxtHash=[''] ##Almacena la direccion der archivo Txt
direccionArchivoPemHash=['']##Almacena la direccion der archivo Pem
direccionArchivoTxtVer=[''] ##Almacena la direccion der archivo Txt
direccionArchivoPemVer=['']##Almacena la direccion der archivo Pem
#________________________________________________________________
direccionArchivoTxtCifrar=[''] ##Almacena la direccion der archivo Txt
direccionArchivoPemPublicaCifrar=['']##Almacena la direccion der archivo Pem
direccionArchivoTxtDescifrar=[''] ##Almacena la direccion der archivo Txt
direccionArchivoPemPrivadaDescifrar=['']##Almacena la direccion der archivo Pem
#-----------------------------------------------------

def funGenerarLLaves(TextKeys):    
    PrivKey= "LLavePrivada_"+TextKeys+".pem"
    PublicKey= "LLavePublica_"+TextKeys+".pem"
    print(TextKeys )
    print(PrivKey)
    print(PublicKey)
    generarLLaves(PrivKey,PublicKey)

def funFirmar():
    if direccionArchivoTxtHash[0] == "" :
        MessageBox.showinfo("Alerta!", "Debe seleccionar un archivo a cifrar")
    elif direccionArchivoPemHash[0] == "" :
        MessageBox.showinfo("Alerta!", "Debe seleccionar una llave para cifrar")
    else:
        signature(direccionArchivoTxtHash[0],direccionArchivoPemHash[0],'f')
        print(direccionArchivoPemHash[0])
        print(direccionArchivoTxtHash[0])
        MessageBox.showinfo("Alerta!", "El archivo: "+direccionArchivoTxtHash[0] +" Se firmo")
    
def funVerificarFirma():
    if direccionArchivoTxtVer[0] == "" :
        MessageBox.showinfo("Alerta!", "Debe seleccionar un archivo a verificar")
    elif direccionArchivoPemVer[0] == "" :
        MessageBox.showinfo("Alerta!", "Debe seleccionar una llave para verificar")
    else:
        vericacionFirma(direccionArchivoTxtVer[0] , direccionArchivoPemVer[0])
        print(direccionArchivoTxtVer[0])
        print(direccionArchivoPemVer[0])        
#___________________________________________________________________________________________-
def funCifrar():
    #98n3LgYk5aNw18jY
    #key= cadenaAleatoria(16)
    #print(key)
    if direccionArchivoTxtCifrar[0] == "" :
        MessageBox.showinfo("Alerta!", "Debe seleccionar un archivo a cifrar")
    elif direccionArchivoPemPublicaCifrar[0] == "" :
        MessageBox.showinfo("Alerta!", "Debe seleccionar una llave para cifrar")
    else:
        cifrar(direccionArchivoTxtCifrar[0],direccionArchivoPemPublicaCifrar[0])
        #cifrarECB(direccionArchivoTxtCifrar[0],key)
        #print(rsaCifrar(direccionArchivoPemPublicaCifrar[0],key))
        #print(direccionArchivoPemPublicaCifrar[0])
        #print(direccionArchivoTxtCifrar[0])
        MessageBox.showinfo("Alerta!", "El archivo: "+direccionArchivoTxtCifrar[0] +" Se cifro")

def funDescifrar():
    if direccionArchivoTxtDescifrar[0] == "" :
        MessageBox.showinfo("Alerta!", "Debe seleccionar un archivo a cifrar")
    elif direccionArchivoPemPrivadaDescifrar[0] == "" :
        MessageBox.showinfo("Alerta!", "Debe seleccionar una llave para cifrar")
    else:
        #print("Hola")
        descifrar(direccionArchivoTxtDescifrar[0],direccionArchivoPemPrivadaDescifrar[0])
        MessageBox.showinfo("Alerta!", "El archivo se Descifro")
        #descifrarECBa(direccionArchivoTxtDescifrar[0],"98n3LgYk5aNw18jY")
#-----------------------------------------------------

def menu(ventana):
    menubarra = Menu(ventana)
    # Crea un menu desplegable y lo agrega al menu barra
    menuarchivo = Menu(menubarra, tearoff=0)
    ##menuarchivo.add_command(label="Abrir", command=hola)
    menuarchivo.add_command(label="Guardar", )
    menuarchivo.add_separator()
    menuarchivo.add_command(label="Salir", command=root.quit)
    menubarra.add_cascade(label="Archivo", menu=menuarchivo)

    # Crea dos menus desplegables mas
    menueditar = Menu(menubarra, tearoff=0)
    menueditar.add_command(label="Cortar", )
    menueditar.add_command(label="Copiar", )
    menueditar.add_command(label="Pegar", )
    menubarra.add_cascade(label="Editar", menu=menueditar)
    menuayuda = Menu(menubarra, tearoff=0)
    menuayuda.add_command(label="Acerca de...", )
    menubarra.add_cascade(label="Ayuda", menu=menuayuda)

    # Mostrar el menu
    root.config(menu=menubarra)


   
root = Tk()

root.state('normal') 




root.title("Practica Criptografia Hibrida")

tab_control = ttk.Notebook(root)

pestañaFirma = ttk.Frame(tab_control)
pestañaCifrar = ttk.Frame(tab_control)

tab_control.add(pestañaFirma, text='Firma Digital')
tab_control.add(pestañaCifrar, text='Cifrar/Descifrar')





#####Definir Atributos de Ventana Algoritmos




#####Definir Atributos de Firma Digital

titleHash = Label(pestañaFirma,text="Firma Digital", font=("Arial Bold", 50), padding=20)
titleHash.grid(row=1,column=1,columnspan=4)



#### Linea 2
labelHash = Label(pestañaFirma,text="Nombre:", padding="10 10")
labelHash.grid(row=2,column=1)

entryLLave = Entry(pestañaFirma)
entryLLave.grid(row=2,column=2, padx=10)
botonGenerarLlaves = Button(pestañaFirma, text='Generar LLaves', command=lambda: funGenerarLLaves (str(entryLLave.get())), width=20)
botonGenerarLlaves.grid(row=2, column=3)

#### Linea 3

labelFirma = Label(pestañaFirma,text="Firmar archivo:", padding="10 10")
labelFirma.grid(row=3,column=1)

btnArchivoTxt = Button(pestañaFirma, text='Cargar Archivo(Txt)', command=lambda: getDireccionArchivo (direccionArchivoTxtHash,"txt"), width=20)
btnArchivoTxt.grid(row=3, column=2)

btnArchivoPem = Button(pestañaFirma, text='Cargar Archivo(Pem)', command=lambda: getDireccionArchivo (direccionArchivoPemHash,"pem"), width=20)
btnArchivoPem.grid(row=3, column=3)

btnFirma = Button(pestañaFirma, text='Firmar Archivo', command=lambda: funFirmar (), width=20)
btnFirma.grid(row=3, column=4)

#### Linea 4

labelVerificar = Label(pestañaFirma,text="Descifrar:", padding="10 10")
labelVerificar.grid(row=4,column=1)

btnArchivoTxt = Button(pestañaFirma, text='Cargar Archivo (Txt)', command=lambda: getDireccionArchivo (direccionArchivoTxtDescifrar,"txt"), width=20)
btnArchivoTxt.grid(row=4, column=2)

btnArchivoPem = Button(pestañaFirma, text='Cargar Archivo(Pem)', command=lambda: getDireccionArchivo (dir,"pem"), width=20)
btnArchivoPem.grid(row=4, column=3)

btnVerificar = Button(pestañaFirma, text='Verificar Firmar', command=lambda: funVerificarFirma(), width=20)
btnVerificar.grid(row=4, column=4)

#######




### Linea 4




#####Definir Atributos de Ventana Cifrar



titleHash = Label(pestañaCifrar,text="Cifrar/Descifrar", font=("Arial Bold", 50), padding=20)
titleHash.grid(row=1,column=1,columnspan=4)



#### Linea 2

labelLlave = Label(pestañaCifrar,text="La llave es:", padding="10 10")
labelLlave.grid(row=2,column=1)
labelMostrarLlave = Label(pestañaCifrar,text="Mostrar Llave", padding="10 10")
labelMostrarLlave.grid(row=2,column=2)
#### Linea 3

labelCifrar = Label(pestañaCifrar,text="Cifrar:", padding="10 10")
labelCifrar.grid(row=3,column=1)

btnArchivoTxt = Button(pestañaCifrar, text='Cifrar Archivo(Txt)', command=lambda: getDireccionArchivo (direccionArchivoTxtCifrar,"txt"), width=20)
btnArchivoTxt.grid(row=3, column=2)

btnArchivoPem = Button(pestañaCifrar, text='Cargar Archivo(Pem)', command=lambda: getDireccionArchivo (direccionArchivoPemPublicaCifrar,"pem"), width=20)
btnArchivoPem.grid(row=3, column=3)

btnCifrar = Button(pestañaCifrar, text='Cifrar Archivo', command=lambda: funCifrar (), width=20)
btnCifrar.grid(row=3, column=4)

#### Linea 4

labelVerificar = Label(pestañaCifrar,text="Verificar Firma:", padding="10 10")
labelVerificar.grid(row=4,column=1)

btnArchivoTxt = Button(pestañaCifrar, text='Cargar Archivo (Txt)', command=lambda: getDireccionArchivo (direccionArchivoTxtDescifrar,"txt"), width=20)
btnArchivoTxt.grid(row=4, column=2)

btnArchivoPem = Button(pestañaCifrar, text='Cargar Archivo(Pem)', command=lambda: getDireccionArchivo (direccionArchivoPemPrivadaDescifrar,"pem"), width=20)
btnArchivoPem.grid(row=4, column=3)

btnVerificar = Button(pestañaCifrar, text='Descifrar Firmar', command=lambda: funDescifrar(), width=20)
btnVerificar.grid(row=4, column=4)


############


tab_control.pack(expand=1, fill='both')

menu(root)

root.mainloop()