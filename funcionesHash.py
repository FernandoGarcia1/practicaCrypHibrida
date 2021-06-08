from Crypto.PublicKey import RSA
from tkinter import messagebox as MessageBox
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA1
from funArchivos import *







def signature(rutaArchivo, rutaLLave,nuevoCaracter):
    f = open(rutaArchivo, "rb")
    mensajeArchivo= f.read()  
    crearArchivoAgregandoCaracteres(rutaArchivo,mensajeArchivo,nuevoCaracter,"txt")
    f.close()
    h= SHA1.new()
    h.update(mensajeArchivo)
    nuevoArchivo=nuevaRuta(rutaArchivo,nuevoCaracter,"txt")
    
    
    mensajeHash = h
    print("El mensaje Hash es: ")
    print(mensajeHash)    
    try:
        llave = RSA.importKey(open(rutaLLave , "rb").read())
        signature = pkcs1_15.new(llave).sign(mensajeHash)
    except (ValueError, TypeError):        
        MessageBox.showinfo("Alerta!", "Debe seleccionar la llave Privada")
        #print(message)
    print("La Firma  es")
    print(signature)


    #f = open(rutaArchivo, "ab")
    #f.write(b"\n--------------\n")
    
    #f.write(signature)

    f = open(nuevoArchivo, "ab")
    f.write(b"\n--------------\n")
    
    f.write(signature)
    f.close()

    
    print("se firmo")
    return signature




def vericacionFirma(rutaArchivo, rutaLLave):
    f=open(rutaArchivo,'ab')
    f.write(b'')
    f.close()
    f= open(rutaArchivo, 'rb')
    contador=0    
    signatureArchivo= b''
    mensajeArchivo= b''
    print("El archivo dice: ")

    for linea in f.readlines():
        print(linea)
        
        if contador == 1:
            signatureArchivo=signatureArchivo+linea        
        if linea == b"--------------\n":
            contador=1
            print(contador)
            
        if contador == 0:
            mensajeArchivo=mensajeArchivo+linea
    mensajeArchivo=mensajeArchivo[:-1]    

    print("EL mensaje es:")
    print(mensajeArchivo)
    print("La firma es:")
    print(signatureArchivo)
    h= SHA1.new()
    h.update(mensajeArchivo)        
    
    
    try:
        llave = RSA.import_key(open(rutaLLave).read())
    except (ValueError):
        MessageBox.showinfo("Alerta!", "La llave es Incorrecta")
    try:
        
        pkcs1_15.new(llave).verify(h, signatureArchivo)
        MessageBox.showinfo("Alerta!", "La firma es Correcta")
        
        print ("La llave es valida.")
    # print(signature.decode("utf-8"))
        
    except (ValueError, TypeError):
        print ("La llave NO es valida.")
        MessageBox.showinfo("Alerta!", "La firma No es Correcta")
        
        #print(message)
    signatureArchivo=b""
