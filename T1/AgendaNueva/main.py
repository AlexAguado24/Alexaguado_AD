#!/usr/bin/env.python
# -*- coding: utf-8 -*-
import os, sys

#Declaro las variables del programa principal


#Declaro las funciones/....

def telefono_nuevo(file, cliente, telefono):



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
            print('menu 1')
        elif opcion == '2':
            print(telefono_nuevo(fichero,nombre,telf))
        elif opcion == '3':
            print('menu 3')
        elif opcion == '4':
            print(crear_fichero(fichero))
        else:
            break
        #return



#-------------------Programa Principal--------------------
#Examen ¿Que se descarga p`rimero las lñibrerias o las variables? Respuesta: Las librerias

print("Ejecutando lanzar programa")
lanzarPrograma()