#!/usr/bin/env.python
#.-*-. codigo: utf-8 -*-
'''
#Forma clásica de crear un archivo:
#creamos el archivo
with open ("archivotext.txt", "w") as f:

#Ecribimos en el
    f.write("Creando archivo de texto en python usando with as")

#Cerramos el archivo
f.close()
'''



#escribir fichero de foma clasica

'''
f = open("ficheroenpython.txt", "w")

f.write("Este es mi primer progrma de fichero y lo he escrito en python usando la \n"
        "forma clasica, que es la siguiente \n"
        "f = open() \n"
        "f.write \n"
        "f.close")
f.close()
'''

#escribiendo un fichero de con 'with as'
'''
with open("ficheroenpython.txt", "w") as f:
    f.write("Este es mi primer progrma de fichero y lo he escrito en python usando la \n"
            "forma recomendada, que es la siguiente \n"
            "with open as f \n"
            "f.write \n"
            "f.close")
f.close()
'''
'''

with open ("ficheroenpython.txt", "r") as f:
    texto=(linea for i,linea in enumerate(f) if i>=1 and i<=3)
    for linea in texto:
        print (linea)
'''
'''
f = open("ficheroenpython.txt", "w")

f.write("Este es mi primer progrma de fichero y lo he escrito en python usando la \n"
        "forma clasica, que es la siguiente \n"
        "f = open() \n"
        "f.write \n"
        "f.close")
f.close()
'''

#lista = ["\nEscribiendo \n", "listas \n", "en ficheros"]

#lo abrimos como Reescribir (r+)
'''
with open ("ficheroenpython.txt", "r+") as f:
    #lo abrimos utilizando read y lo almacenamos en la variable
    contenido = f.read()
    #escribimos la lista en el archivo linea a linea
    f.writelines(lista)
f.close()
'''
'''
with open ("ficheroenpython.txt", "a") as f:
    #lo abrimos utilizando read y lo almacenamos en la variable
    #contenido = f.read()
    #escribimos la lista en el archivo linea a linea
    f.writelines(lista)
f.close()
'''
'''
#Forma clasica de crear un archivo: #Creamos el archivo
f = open("archivotext-excepciones.txt", "w")
#Escribimos en el
f.write("Probando excepciones")
#Cerramos el archivo
f.close()
#Ahora intentamos abrirlo e imprimir su contenido:
nombre_fichero = "archivotext-excepciones.txt"
try:
    with open(nombre_fichero, "r") as f:
        print(f.read())
except FileExistsError:
    print('No existe el fichero con la tabla del')
'''
#Ejercicio 1


'''
try:
    numero = int(input("Escribe un numero positivo del 1 al 100\n"))
    f = open("ejercicio1-100.txt", "w")
    f.write(str(numero))
    f.close()
except ValueError:
    print("El dato introducido es erroneo, por favor ingresa un numero")
'''

'''
try:
    numero = int(input("Escribe un numero positivo del 1 al 100\n"))
    nombre_fichero = "ejercicio1-100.txt"
    with open(nombre_fichero, "w") as f:
        f.write(str(numero))
    f.close()
except ValueError:
    print("El dato introducido es erroneo, por favor ingresa un numero")
'''
'''
¿Por que for y no while?
Por que sabemos el numero de veces que queremos que se ejecute la accion,
si no lo supieramos usariamos while
'''
#Ejercicio 2
'''
try:
    numero = int(input("Escribe un numero positivo del 1 al 10\n"))
    fichero2 = "ejercicio2-tabla.txt"

    with open(fichero2, "w") as f:
        for i in range(1,11):
            f.write(str(i)+"x"+str(numero)+"="+str(i*numero)+"\n")
    f.close()
except ValueError:
    print("El dato introducido es erroneo, por favor ingresa un numero")
'''

#Ejercicio 3
'''
numero = int(input("Escribe un numero positivo del 1 al 10\n"))
fichero3 = "ejercicio3-tabla.txt"

with open(fichero3, "w") as f:
    for i in range(1,numero+1):
        for n in range(0,11):
            f.write(str(n)+"x"+str(i)+"="+str(n*i)+"\n")
        f.write("\n")
f.close()
'''

#Ejercicio4
'''
numero = int(input("Escribe un numero positivo del 1 al 10\n"))
fichero3 = "ejercicio3-tabla del "+str(numero)+".txt "

with open(fichero3, "w") as f:
    for i in range(1,numero+1):
        for n in range(0,11):
            f.write(str(n)+"x"+str(i)+"="+str(n*i)+"\n")
        f.write("\n")
f.close()
'''

#Ejercicio5
'''
numero = int(input("Escribe un numero positivo del 1 al 10\n"))
ficheroabrir = "fichero-tabla-del-"+str(numero)+".txt"
try:
    with open(ficheroabrir, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("fichero no encontrado")
'''

#Ejercicio6
'''
#opcion2
try:
    numero = int(input("Escribe un numero\n"))
    with open("ejercicio2-tabla.txt", "r") as f:
        texto=(linea for i,linea in enumerate(f) if i>=0 and i<=numero-1)
        for linea in texto:
            print(linea)
except FileNotFoundError:
    print("El fichero no existe")
'''
'''
#opcion1
try:
    n=int(input("dame un n de lineas:"))
    with open("ejercicio2-tabla.txt","r") as f:
        for i in range(n):
            print(f.readline())
except FileNotFoundError:
    print("El fichero no existe")
'''


















