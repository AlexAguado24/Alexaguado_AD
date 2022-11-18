#!/usr/bin/env.python
# -*- coding: utf-8 -*-
import os, sys

#Declaro las variables del programa principal


#Declaro las funciones/....

def consultarContacto(file, cliente):
   try:
       f = open(file,"r")
   except FileNotFoundError:
       return "Primero debes crear el archivo"
   else:
       directorio = f.readlines()
       f.close()
       directorio = dict([tuple(line.split(",")) for line in directorio])
       if cliente in directorio:
           return ("Nombre: "+ cliente +"  Teléfono: " + directorio.get(cliente))
       else:
           return ("El contacto " + cliente + " no está en la agenda")

def telefono_nuevo(file, cliente, telefono):
    try:
        with open(file, "r+") as f:
            contenido = f.read()
            f.write(cliente + "," + telefono + "\n")
            print("Contacto añadido con éxito")
            f.close()
    except FileNotFoundError:
        return "Primero debes crear el archivo"


def crear_fichero(file):
    '''
        Funcion que crea un fichero vacio para guardar la agenda.
        parametros:
            fichero: Es un fichero.
        Devuelve:
            un mensaje informando sobre si el fichero se ha crteado correctamente o no.
            Ademas, debe comprobar si el fichero existe o no. y si existe, lo machaca
    '''
    if os.path.isfile(file):
        answer = input('El fichero'+ file+ ' ya existe. ¿Desea vaciarlo (S/N)?')
        if answer == 'N':
            return 'No se ha creado el fichero porque ya existe.\n'


    f = open(file, 'w')
    f.close()
    return "se ha creado el fichero para la agenda"


def menu():
    '''
    Funcion que presenta un menu con las opciones disponibles sobre
    una agenda y devuelbe la opcionseleccionada por el usuario.
    Devuelve:
    La opcion seleccionada por el usuadrio
    '''

    print("--------------Agenda-----------")
    print("1-------Consulta Telefonica")
    print("2-----Añadir telefono/cliente")
    print("3------------Eliminar")
    print("4----------Crear Agenda")
    print("0------------Salir")
    opcion1 = str(input("Introduce la opcion deseada\n"))
    return opcion1

def lanzarPrograma():
    '''
    Funcion que lanza las opciones del menu de la aplicacion para la gestion de
    la agenda telefonica
    '''

    fichero = 'miagenda.txt'
    while True:
        opcion=str(menu())
        print("La opcion pulsada es: ",opcion)
        if opcion == '1':
            nombre = str(input("introduce el nombre"))
            consultarContacto(fichero,nombre)
        elif opcion == '2':
            nombre = str(input("introduce el nombre"))
            telf = str(input("introduce el telefono"))
            print(telefono_nuevo(fichero,nombre,telf))
        elif opcion == '3':
            return "Primero debes crear el archivo"
        elif opcion == '4':
            print(crear_fichero(fichero))
        else:
            break
        #return



#-------------------Programa Principal--------------------
#Examen ¿Que se descarga p`rimero las lñibrerias o las variables? Respuesta: Las librerias

print("Ejecutando lanzar programa")
lanzarPrograma()