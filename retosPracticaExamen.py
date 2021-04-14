#Elaborado por  Andres Quesada Artavia 
#Fecha de creación 09/04/2021 Hora: 8:18 a.m.
#Fecha de última modificación 09/04/2021 9;28 p.m.
#Versión 3.9.2

#Importación de librería
from funciones import *
import time
from datetime import date

#Declaracion de variables
def validarBinario(numBin):
    try:
        numBin=int(numBin)
        if numBin>=0:
            while numBin>0:
                if numBin%10!=1 and numBin%10!=0:
                    print ("Debe digitar un número binario.")
                    return obtenerNumeroBinario()
                numBin=numBin//10
            return True
        else:
            print ("Debe digitar un número mayor a 0.")
            return obtenerNumeroBinario()
    except ValueError:
        print ("Debe digitar un valor númerico entero.")
        return obtenerNumeroBinario()

def obtenerNumeroBinario():
    numBin=input("Digite un número binario para que sea convertido a decimal: ")
    if validarBinario(numBin)==True:
        suma=convertirBinario(numBin)
        print ("El número "+numBin+" equivale al número ",suma, "decimal")

#Ejercicio 2
def obtenerFechaActual():
    hoy=date.today()
    return str(hoy)

def validarFecha(fecha):
    if len (fecha)==10:
        if fecha[0:4].isdigit()==True and fecha[5:7].isdigit()==True and fecha[8:10].isdigit()==True:
            if int(fecha[5:7])<13 and int(fecha[5:7])>0 and int(fecha[8:10])<32 and int(fecha[8:10])>0:
                if fecha[4]=="-" and fecha[7]=="-":
                    return True
                else:
                    print ("La fecha debe estar dividida por guiones.")
                    return obtenerFecha()
            else:
                print ("Error en el formato de la fecha, intentelo nuevamente.")
                return obtenerFecha()
        else:
            print ("Ha ocurrido un error, intentelo nuevamente.\nRecuerde colocar la fecha con números.")
            return obtenerFecha()
    else:
        print ("Error en el formato de la fecha, intentelo nuevamente.")
        return obtenerFecha()
def obtenerFecha():
    fecha=input("Digite su fecha de nacimiento en formato aaaa-mm-dd:")
    if validarFecha(fecha)==True:
        fechaActual=obtenerFechaActual()
        if calcularEdad(fecha, fechaActual)==False:
            print ("La fecha de nacimiento es incorrecta.")

def validarPalabra(palabra):
    vocal="aeiouAEIOU"
    if palabra.isalpha()==True:
        if palabra[-1] in vocal:
            return True
    else:
        print ("Debe digitar unicamente una palabra.")
        return obtenerPalabra()

def opcionUsuario():
    opcion=input("Desea continuar: responda si o no\n")
    opcion=opcion.lower()
    if opcion.isalpha()==True:
        if opcion=="si" or opcion=="sí" or opcion=="sì" :
            return True
        return False
    return False
        

def obtenerPalabra():
    palabra=input("Digite una palabra: ")
    if validarPalabra(palabra)==True:
        print (invertirPalabra(palabra))
    if opcionUsuario()==True:
        return obtenerPalabra()
    else:
        return ""

def obtenerDatosPersonales(fecha):
    if esBisiesto(fecha)==True:
        año="bisiesto"
    else:
        año="No bisiesto"
    if esPar (fecha)==True:
        dia="par"
    else:
        dia="impar"
    mes=nombreMes(fecha)
    signoZ= descubrirSigno(mes=int(fecha[3:5]), numdia=int(fecha[0:2]))
    personalidad= personalidadSigno(signoZ)
    return (dia,mes,año,signoZ,personalidad)

def validarFechaNacimiento(fecha):
    if len (fecha)==10:
        if fecha[0:2].isdigit()==True and fecha[3:5].isdigit()==True and fecha[6:10].isdigit()==True:
            if int(fecha[0:2])<32 and int(fecha[0:2])>0 and int(fecha[3:5])<13 and int(fecha[3:5])>0:
                if fecha[2]=="-" and fecha[5]=="-":
                    return True
                else:
                    print ("La fecha debe estar dividida por guiones.")
                    return obtenerFechaNacimiento()
            else:
                print ("Error en el formato de la fecha, intentelo nuevamente.")
                return obtenerFechaNacimiento()
        else:
            print ("Ha ocurrido un error, intentelo nuevamente.\nRecuerde colocar la fecha con números.")
            return obtenerFechaNacimiento()
    else:
        print ("Error en el formato de la fecha, intentelo nuevamente.")
        return obtenerFechaNacimiento()

def obtenerFechaNacimiento():
    fecha=input("Digite su fecha de nacimiento en formato dd-mm-aaaa: ")
    if validarFechaNacimiento(fecha)==True:
        resultados=obtenerDatosPersonales(fecha)
        print ("Usted nació un dia "+str(resultados[0])+" en el mes "+str(resultados[1])+", en un año "+str(resultados[2])+"."
            "\nUsted es de signo: "+str(resultados[3])+", por ende su personalidad es: "+str(resultados[4]))

def validarNumTelefono(numero):
    if len(numero)==9:
        if numero[0:4].isdigit()==True and numero[5:9].isdigit()==True:
            if numero[0] in "23678":
                return True
            else:
                print("El primer carácter debe ser únicamente: 2,5,6,7,8")
                return obtenerNumeroTelefonico()
        else:
            print ("Error en el formato del número, intentelo nuevamente.")
            return obtenerNumeroTelefonico()
    else:
        print ("Error en el formato del número, intentelo nuevamente.")
        return obtenerNumeroTelefonico()

def obtenerNumeroTelefonico():
    numero=input("Digite su número de telefono: ")
    if validarNumTelefono(numero)==True:
        if numero[0]==2:
            print ("Es un número fijo, de la provincia de "+proveedorTelefonico(numero))
        else:
            print ("Es un número celular, su proveedor es el "+proveedorTelefonico(numero))
           
obtenerFechaNacimiento()
