#!/usr/bin/env.python
# .-*-. codigo: utf-8 -*-

'''
with open("ficheroenpython.txt", "w") as f:
    f.write("with open () as f\n"
            "f.write \n"
            "f.close")
f.close()
'''
import Diccionarios

'''
numero = int(input("Escribe un numero positivo del 1 al 100\n"))
ficheroNumero = "ejercicio1-100.txt"
with open(ficheroNumero, "w") as f:
    if numero >= 1 and numero <=100:
        f.write(str(numero))
    else:
        print("El numero introducido es incorrecto")
f.close()
'''
'''
numero = int(input("Escribe un numero entre el 1 y el 10\n"))
ficheroTablaNumero = "ejercicio2-tabla.txt"
with open(ficheroTablaNumero, "w") as f:
    for i in range(1,11):
        f.write(str(i)+" * "+str(numero)+" = "+ str(i*numero)+"\n")
f.close()
'''
'''
numero = int(input("Escribe un numero del 1 al 10"))
ficheroNumero = "ejercicio2-tabla del "+str(numero)+".txt"
with open(ficheroNumero,"w") as f:
    f.close()
'''
'''
n = int(input("Escribe un numero positivo del 1 al 10\n"))
ficheroLeer = "ejercicio2-tabla del "+str(n)+".txt"
try:
    with open(ficheroLeer,"r") as f:
        print(f.read())
    f.close()
except FileNotFoundError:
    print("Fichero no encontrado")
'''
'''
Ejercicio de leer las lineas que le indico con nro
primera forma-
try:
    nro = int(input("escribe un numero positivo\n"))
    with open("ejercicio2-tabla.txt","r")as f:
        for i in range(nro):
            print(f.readline())
except FileNotFoundError:
    print("Fichero ausente")
    
opcion 2
try:
    numero = int(input("Escribe un numero\n"))
    with open("ejercicio2-tabla.txt", "r") as f:
        texto=(linea for i,linea in enumerate(f) if i>=0 and i<=numero-1) #Enumerate cuenta lineas
        for linea in texto:
            print(linea)
except FileNotFoundError:
    print("El fichero no existe")
'''

