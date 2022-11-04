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

lista = ["\nEscribiendo \n", "listas \n", "en ficheros"]

#lo abrimos como Reescribir (r+)
'''
with open ("ficheroenpython.txt", "r+") as f:
    #lo abrimos utilizando read y lo almacenamos en la variable
    contenido = f.read()
    #escribimos la lista en el archivo linea a linea
    f.writelines(lista)
f.close()
'''
with open ("ficheroenpython.txt", "a") as f:
    #lo abrimos utilizando read y lo almacenamos en la variable
    #contenido = f.read()
    #escribimos la lista en el archivo linea a linea
    f.writelines(lista)
f.close()


