from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

from archivos import*
from funArchivos import*






def cifrarECB(archivo,key): #Cifrado aes, reciba archivo(ruta absoluta del archivo a cifrar) y key

    mensaje = abrirArchivo(archivo)		
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    mensajeCifrado = cipher.encrypt(mensaje)  ##Multiplo del tamaño del bloque (16 en este caso)
    
    #crearArchivo(mensajeCifrado,"mensajeCifrado.txt")
    return mensajeCifrado
    
    


def descifrarECBa(archivo, key):	#descifrado aes, reciba archivo(ruta absoluta del archivo a cifrar) y key
    mensajeCifrado = abrirArchivo(archivo)	
    decipher = AES.new(key.encode(), AES.MODE_ECB)
    mensajeDescifrado = decipher.decrypt(mensajeCifrado)	
    
    pos=mensajeDescifrado.find(b"---#&+")
    
    mensajeDescifrado=mensajeDescifrado[0:pos]
    #crearArchivo(mensajeDescifrado, "mensajeDescifrado.txt")
    crearArchivoAgregandoCaracteres(archivo,mensajeDescifrado,"De","txt")

def rsaCifrar(llavePublica, mensaje):  #Cifrado con rsa, se recibe la llavePublica(rutaAbsoluta de la llave) y el mensaje a Cifrar (la llave de 16 bytes en este caso)    
    
    llave = RSA.importKey(open(llavePublica , "rb").read())
    cifrado = PKCS1_OAEP.new(llave)
    mensajeCifrado = cifrado.encrypt(mensaje.encode())

    #print(mensajeCifrado)

    return mensajeCifrado
    

def rsaDesicifrar(llavePrivada,mensaje):#Descifrado con rsa, se recibe la llavePublica(rutaAbsoluta de la llave) y el mensaje a Descifrar (la llave de 16 bytes cifrada en este caso)    
    llave = RSA.importKey(open(llavePrivada , "r").read())
    cifrado = PKCS1_OAEP.new(llave)
    mensajeDescifrado=b""
    try:
        mensajeDescifrado = cifrado.decrypt(mensaje)
        #print ("El mensaje es: " + mensajeDescifrado.decode("utf-8"))
        
    
        
    except ValueError :
        #print("La llave es Erronea")
        MessageBox.showinfo("Alerta!", "La llave es Incorecta")
    
    except TypeError :
        print("La llave es Erronea")
        MessageBox.showinfo("Alerta!", "La llave es Incorecta")
    print('Decrypted:', mensajeDescifrado)
    return mensajeDescifrado.decode()



key= cadenaAleatoria(16) 
key2=cadenaAleatoria(16)



def cifrar(rutaTxt,llavePublica):
    key= cadenaAleatoria(16)
    print(key)
    keyCifrada=rsaCifrar(llavePublica,key)
    mensajeCifrado=cifrarECB(rutaTxt, key)
    rutaNueva=crearArchivoAgregandoCaracteres(rutaTxt,mensajeCifrado,"CI","txt")
    f = open(rutaNueva, "ab")
    f.write(b"--separador--")
    f.write(keyCifrada)
    f.close()
    
def descifrar(rutaTxt,llavePrivada):
    f=open(rutaTxt,"rb")
    mensajeArchivo=f.read()
    tamTotal=len(mensajeArchivo)
    f.close()
    pos = mensajeArchivo.find(b"--separador--")
    #print(pos)
    mensajeCifrado=mensajeArchivo[0:pos]
    keyCifrada=mensajeArchivo[pos+13:tamTotal]
    #print(mensajeArchivo)
    #print("-------------------------------------------------")
    #print(keyCifrada)
    keyDescifrada=rsaDesicifrar(llavePrivada,keyCifrada)
    #print(keyDescifrada)
    descifrarECBa(rutaTxt,keyDescifrada)

#llavePrivada= r"C:\Users\LENOVO\Desktop\Trabajos escuela\Trabajos ESCOM\Escom 6° Semestre\Crypto\Parcial 2\Practicas\Final\LLavePrivada_Fer.pem"
#llavePublica= r"C:\Users\LENOVO\Desktop\Trabajos escuela\Trabajos ESCOM\Escom 6° Semestre\Crypto\Parcial 2\Practicas\Final\LLavePublica_Juan.pem"
#rutaArchivo=r"C:\Users\LENOVO\Desktop\Trabajos escuela\Trabajos ESCOM\Escom 6° Semestre\Crypto\Parcial 2\Practicas\Final\strawberry.txt"
#rutaArchivoCifrado=r"C:\Users\LENOVO\Desktop\Trabajos escuela\Trabajos ESCOM\Escom 6° Semestre\Crypto\Parcial 2\Practicas\Final\strawberry_CI.txt"

#cifrarECB(r"C:\Users\LENOVO\Desktop\Trabajos escuela\Trabajos ESCOM\Escom 6° Semestre\Crypto\Parcial 2\Practicas\Final\strawberry.txt", key)
#keyCifrado=rsaCifrar(llavePublica,key)
#keyDescifrado=rsaDesicifrar(llavePrivada,keyCifrado)
#descifrarECBa(r"C:\Users\LENOVO\Desktop\Trabajos escuela\Trabajos ESCOM\Escom 6° Semestre\Crypto\Parcial 2\Practicas\Final\mensajeCifrado.txt", keyDescifrado)

#cifrar(rutaArchivo,llavePublica)
#descifrar(rutaArchivoCifrado,llavePrivada)


#xvxMi8RWepNht9mq

#crearArchivoAgregandoCaracteres()