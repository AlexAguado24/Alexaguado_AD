#!/usr/bin/env.python
# .-*-. codigo: utf-8 -*-


MiDiccionario = {
    'Nombre': "Harry",
    'Apellido': "Potter",
    'Edad': "18",
    'Genero': "Chico",
    'Padres': [
        'James', 'Lili'
    ]
}
'''

print(MiDiccionario)
'''

# print(MiDiccionario['Padres'][0:2])
# Dime el valor del segundo elemento de mi diccionario del campo PAdres
print(MiDiccionario['Padres'][0])

# Cambiar la edad a 22

MiDiccionario['Edad'] = 22
print(MiDiccionario['Edad'])

# Añadir el campo grupo

MiDiccionario['Grupo'] = ""

# Cambiar el nombre de una clave por otro

MiDiccionario["Casa"] = MiDiccionario.pop("Grupo")

# Borrar un par clave-valor
# asi -> del MiDiccionario['Edad']
# o asi -> del (MiDiccionario["Edad"])

# dos formas de obtener el valor de una clave
print(MiDiccionario['Apellido'], "\n\n")  # forma 1
print(MiDiccionario.get('Apellido'))  # forma 2: dicc.get

# 10 Añadir a una variable el valor de una clave
valoravariable = MiDiccionario.get('Apellido')

# Imprimir las claves del diccionario: .keys()
print(MiDiccionario.keys())

# Imprimir todos los valores: .claves()
print(MiDiccionario.values())

# crear una tupla -> Con (parentesis), Las listas se crean con [corchetes]
Cosas = ("casa", "puerta", "reloj", "mesa", "silla", "banco", "cuadro", "alfombra")

Numeros = (1, 2, 3, 4, 5)

# como ver el par (clave valor) de un diccionario
# importante: Lo que devuelve es una.... TUPLA
print("\n\n ---------")
print(MiDiccionario.items())

# Crear un tupla:
Numeros2 = (111, 222, 333, 444, 555, 666)

# 15 Slice: vamos a importar partes (rebanadas) de una tupla
# Vamos a seleccionar (imprimir) los 3 primeros elementos de la tupla
print(Numeros2[0:3])
print(Numeros2[1:3])
print(Numeros2[:-2])
print(Numeros2[-2:])

# como saber la longitud de un diccionario
print(len(MiDiccionario))

# como saber la longitud de una clave de un diccionario
# quiero saber la longitud de la clave padres, es decir cuantos elementos tiene la clave
print(len(MiDiccionario['Padres']))

texto = "Python es un lenguaje de programacion que permite tipar pero no permite compilar, " \
        "ya que es un lenguaje interpretado"
print(texto)
print(texto.split())
print(texto.split(","))

'''
20 Crea un programa que a partir del fichero de texto:"prueba1.txt", el cual contiene excatamente esto
a,1
b,2
c,3
d,4
abra el fichero en modo lectura y para cada linea del fichero, imprima:
20.a: el contenido de la linea
20.b: el contenido de cada linea desglosadao por caracteres:
    -> ('A',',',',','1'\n)
20.c: el contenidode cada linea en formato 'primer 
elemento','segundo elemento' (o lo que es lo mismo clave,
valor):
'A','1'\n
'''
ficheroPrueba = "prueba1.txt"
with open(ficheroPrueba, "w") as f:
    f.write("A,1\n"
            "B,2\n"
            "C,3\n"
            "D,4\n")
f.close()

# pista
mitupla = tuple([1, 4, 6])
print(mitupla)

mitupla2 = tuple({4: 'one', 6: 'two'})
print(mitupla2)

mitupla3 = ({4: 'one', 6: 'two'})
print(mitupla3)
# print(mitupla3[0])

# como crear un diccionario directamente: dic
midic2 = {'nombre': "lm", 'altura': 195, 'ojos': 'azules'}
print(midic2)

'''Pasos a seguir para el eje-20
abrir el fichero en modo lectura
guardar el contenido en una variable
cerar el fichero 
iterar sobre el contenido cada linea
imprimir lo que se pide:
    a: cada linea
    b:tuplear
    c: tuplear'''
'''
file="prueba1.txt"
f=open(file,'r')
directorio = f.readlines()
f.close()
line=str()

for line in directorio:
    print("el contenido de cada linea es:",line)
    print(tuple(line))
    print(tuple(line.split(",")))
'''
'''abra el fichero en modo lectura e indique si una letra introducida 
por teclado esta dentro del fichero y de estarlo que valor tiene asociado
en caso de no estar la letra introducida mostrada un mensaje indicando 
"la letra leida: " letra leida "no se encuentra en el fichero"'''

# letra = str(input("introduce la letra a buscar\n"))

file = "prueba1.txt"
f = open(file, 'r')
contenido = f.readlines()
line = str()
'''
for line in contenido:
    linea = tuple(line.split(","))
    if linea[0] == letra:
        print("El valor de la letra "+letra+" es "+linea[1])
    else:
        print("la letra introducida "+letra+" no esta en el fichero")
'''
letra = str(input("dame una letra"))
contenido = dict([tuple(line.split(',')) for line in contenido])
# la linea anterior recorre el contenido del fichero que esta almacenado en "contenido"
# el for recorre el contenido y en cada iteracion guarda el par clave-valor en line
# crea una tupla que la parte (split) por las comas
# genera un diccionario (dict) con la tupla
# el diccionario lo guardo en content
if letra in contenido:
    print("esta")
else:
    print("la letra " + letra + " no esta")
