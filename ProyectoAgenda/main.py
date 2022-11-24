#!/usr/bin/env.python
# -*- coding: utf-8 -*-
import os, sys







def consultar_Telefono(file, contacto):
    try:
        f = open(file,"r"):
    except FileNotFoundError:
        return 'Primero debes crear la genda'
    else





def contacto_nuevo(file, nombre, telefono):
    try:
        with open(file,'r+')as f:
            documento = f.read()
            f.write(nombre+","+telefono+"\n")
            print("Contacto añadido")
            f.close()
    except FileNotFoundError:
        return 'primero debes crear el fichero'



def crear_fichero(file):
    if os.path.isfile(file):
        answer = input("El fichero " + file + " ya existe, ¿Deseas vaciarlo?(S/N)")
        if answer == 'N':
            return 'No se ha creado el fichero por que ya existe'

    f = open(file, 'w')
    f.close()
    return 'El fichero se ha creado'


def menu():
    print("Bienvenido al menu de la agenda")
    print("1º- Agregar Contacto a la agenda")
    print("2º- Consultar Telefono")
    print("3º- Borrar Contacto")
    print("4º- Crear Agenda")
    print("0º- salir")
    opcion = int(input("Elige la opcion deseada\n"))

    return opcion

def programa():
    agenda = "Agenda.txt"
    while True:
        opcion = str(menu())
        print("Has elegido la opcion ", opcion)
        if opcion == '1':
            print("Has elegido agregar contacto nuevo")
            nombre = str(input("Escribe el nombre: "))
            telefono = int(input("Escribe el telefono: "))
            contacto_nuevo(agenda,nombre,telefono)
        elif opcion == '2':
            print("consultar telefono")
        elif opcion == '3':
            print("Borrar contacto")
        elif opcion == '4':
            print(crear_fichero(agenda))
        else:
            break


programa()
