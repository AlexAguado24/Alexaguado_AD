#!/usr/bin/env.python
#.-*-. codigo: utf-8 -*-

import os, sys

#Declaracion de variables




#Declaracion de funciones

def consultar_numero(file, cliente):
    try:
        f = open(file, "r")
    except FileNotFoundError:
        return 'Antes debes crear el fichero'
    else:
        contenido = f.readlines()
        f.close()
        contenido=dict([tuple(line.split(","))for line in contenido])
        if cliente in contenido:
            return ("Nombre: "+cliente+" Telefono " + contenido.get(cliente))
        else:
            return ("El contacto "+cliente+" no est en la agenda")





def aniadir_contacto(file, nombre, numero):
    try:
        with open(file, "r+")as f:
            contenido = f.read()
            f.write(nombre+","+numero + "\n")
            print("Añadido con exito")
            f.close()
    except FileNotFoundError:
        return 'Fichero o encontrado, crealo antes de seguir'



def crear_agenda(file):
    if os.path.isfile(file):
        respuesta = input(file + " ya existe, ¿Deseas sobreescribirlo?(S/N)")
        if respuesta == 'n':
            return 'El fichero no se creo por que ya eiste'
    f = open(file, "w")
    f.close()
    return 'Agenda creada conexito'


def menu():
    print("-----------Agenda---------------")
    print("1º------Añadir contacto---------")
    print("2º------consultar telefono------")
    print("3º-------Borrar contacto-------")
    print("4º--------Crear Agenda-----------")
    print("0º-----------Salir---------------")
    opcion=str(input("Elige una de las opciones\n"))
    return opcion


def ejecutar_menu():
    agenda = "miagenda.txt"
    while True:
        opcion=str(menu())
        print("La opcion elegida es ",opcion)
        if opcion == '1':
            print("Has elegido añadir contacto")
            nombre = str(input("indica el nobre"))
            numero = int(input("indica el nobre"))
            aniadir_contacto(agenda,nombre,numero)
        elif opcion == '2':
            print("Has elegido consultar telefono")
            cliente = input("Escribe el nombre")
            consultar_numero(agenda,cliente)
        elif opcion == '3':
            print("Has elegido borrar un contacto")
        elif opcion == '4':
            print("Creando la agenda")
            crear_agenda(agenda)
        else:
            return 'Hasta pronto'

ejecutar_menu()