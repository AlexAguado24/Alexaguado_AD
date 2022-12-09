'''import os'''
'''
Ejercicio 1:
Programa que suma dos numeros enteros y muestra el resultado correcto
suma=int()
suma = 2 + 3
if suma == 2:
	print ("El resultado es:",2)
elif suma == 5:
	print ("El resultado es:",5)
elif suma == 6:
	print ("El resultado es:",6)
else:
	print ("El resultado no se puede calcular:")

Respuesta correcta: D
'''

'''
Ejercicio 2:
Programa que ejecuta un metodo para sumar 2 numeros
def suma(A,B):
	return A+B
#------- Programa principal—--
N1=int(7)
N2=int(7)
print(suma(N1,N1))
Respuesta correcta: B
'''

'''
Ejercicio 3
Programa que crea una lista
MiLista = ["Esto","es",1,"Examen"]
Respuesta correcta: C
'''

'''
Ejercicio 4:
Programa que ejecuta de forma continua un bucle hasta que se le añade un numero mayor que 3
while True:
    opcion = int(input("Introduce una opción del 1 al 3:"))
    if opcion == 1:
        print("opción 1")
    elif opcion == 2:
        print("opción 2")
    elif opcion == 3:
        print("opcion 3")
    else:
        break
Respuesta correcta: D

'''

'''
Ejercicio 5:
Programa que ejecuta de forma continua un bucle hasta que se le añade un numero mayor que 3
El programa usa try, except en caso de introducir una letra o un numero con decimal
Respuesta:
while True:
    try:
        opcion = int(input("Introduce una opción del 1 al 3:"))
        if opcion == 1:
            print("opción 1")
        elif opcion == 2:
            print("opción 2")
        elif opcion == 3:
            print("opcion 3")
        else:
            break
    except ValueError:
        print("Ha pulsado una tecla, por favor introduzca un número")
'''

'''
Ejercicio 6:
Programa para crear un diccionario e insertar elementos introducidos por teclado

nombre=str(input("Escribe un nombre"))
apellido=str(input("Escribe un apellido"))
edad=str(input("Escribe un edad"))
telefono=str(input("Escribe un teléfono"))
MiDiccionario = {
    'Nombre':"",
    'Apellido':"",
    'Edad':"",
    'Teléfono':""
}

MiDiccionario['Nombre']=nombre
MiDiccionario['Apellido']=apellido
MiDiccionario['Edad']=edad
MiDiccionario['Teléfono']=telefono

'''

'''
#Ejercicio 7:
Programa que pide por pantalla un numero y escribe en un fichero creado 
los numeros desde el 0 hasta el numero introducido, en el a sobreescribe y en el
b añade al final del fichero otra lista de numeros hasta el numero nuevo
#7.a):
fichero = "ficheroexam1.txt"
numero = int(input("Escribe un numero mayor que 0\n"))

with open(fichero, "w")as f:
    for i in range(numero+1):
        f.write("El numero es:"+str(i)+"\n")
    f.write("---------------\n")
    f.close()

#7.b):
#fichero = "ficheroexam1.txt"
numero = int(input("Escribe un numero mayor que 0\n"))

with open(fichero, "r+")as f:
    contenido = f.read()
    with open(fichero, "w") as f:
        f.write(str(contenido))
        for i in range(numero + 1):
            f.write("El numero es:" + str(i) + "\n")
        f.write("------------------\n")
        f.close()
'''

'''
Ejercicio 8:
8.a):
Programa que pide 3 numero y los opera, despues escribe el resultado y tantas lineas cono 
el resultado indique en un fichero 
def operacion(A, B, C):
    resultado = (A + B) * C
    return resultado


num1 = int(input("Escribe un numero entero\n"))
num2 = int(input("Escribe un numero entero\n"))
num3 = int(input("Escribe un numero entero\n"))
print(operacion(num1, num2, num3))
numero = str(operacion(num1, num2, num3))

fichero = "ficheroexam2.txt"

with open(fichero, "w") as f:
    for i in range(operacion(num1, num2, num3)+1):
        f.write("El calculo es:" + str(numero) + " y esta en la linea:" + str(i) + "\n")
    f.close()
    
--> correccion de examen    
with open () as f:
    for i in range(1, c+1):
        f.write()

8.b):
Programa que ejecuta el programa anterior pero esta vez escribe por teclado el numero 
de lineas del fichero resultantes de la suma de los 2 primeros numeros
def operacion(A, B, C):
    suma = (A + B)
    resultado = suma * C
    return resultado


num1 = int(input("Escribe un numero entero\n"))
num2 = int(input("Escribe un numero entero\n"))
num3 = int(input("Escribe un numero entero\n"))
print(operacion(num1, num2, num3))
numero = str(operacion(num1, num2, num3))
suma = num1+num2
fichero = "ficheroexam2.txt"

with open(fichero, "r") as f:
    contenido = f.readlines()
    f.close()

linea = ([tuple(line.split("\n"))for line in contenido])
print("Ahora se mostrara el contenido de calcular a+b="+str(suma)+"\n")
for i in range(suma+1):
    print(linea[i])
    

-->Correccion de examen

a = input(numero 1)
b = input(numero 2)
c = input(numero 3)
    
a=a+b  #en la propia variable que inicialmente leo un numero añado el resultado de ese numero mas b
c=a+b

nombre_fichero=''

with open (,''w) as f:
    for i in range(1, c+1):
        f.write()
    f.close()
    
print

with open(,'r')as f:
    for contador  in range(a):
        print(f.readlines(a))



    
    
8.c)
El programa trata la lectura del fichero con un try except por si el fichero no existe
def operacion(A, B, C):
    suma = (A + B)
    resultado = suma * C
    return resultado


num1 = int(input("Escribe un numero entero\n"))
num2 = int(input("Escribe un numero entero\n"))
num3 = int(input("Escribe un numero entero\n"))
print(operacion(num1, num2, num3))
numero = str(operacion(num1, num2, num3))
suma = num1+num2
fichero = "ficheroexam2.txt"

try:
    with open(fichero, "r") as f:
        contenido = f.readlines()
        f.close()

    linea = ([tuple(line.split("\n")) for line in contenido])
    print("Ahora se mostrara el contenido de calcular a+b=" + str(suma) + "\n")
    for i in range(suma + 1):
        print(linea[i])
except FileNotFoundError:
    print("el fichero no existe")

'''

'''Ejercicio 9'''

def consulta_errores(fichero2):
    try:
        f = open(fichero2,"r")
        directorio = f.readlines()
        f.close()
        for i in range(len(directorio)):
            print(directorio[i])
    
        print("Comprobando tamaño")
        f = open(fichero2,"r")
        directorio = f.readlines()
        print("El fichero con datos de desvio contiene ",len(directorio)," posibles errores de trayectoria")
        
    except FileNotFoundError:
        print("\n El fichero "+fichero2+" no existe!\n")



def inicio():
    file = 'ficheroexam3.txt'
    file2 = 'ficheroexam4.txt'
    while True:
        opcion = menu()
        if opcion == '1':
            consulta_errores(file2)
        elif opcion == '2':
            if existe_error(file,file2):
                print("Se encontraron todos los errores")
            else:
                print("no se encontraron todos los errores")
        elif opcion == '3':
            borrar_errores(file,file2)
        else:
            print("Desconectado")
            print("....")
            break
        



inicio()




