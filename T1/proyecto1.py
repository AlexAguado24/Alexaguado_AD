"""
año1 = int(input("dime un año"))

año2 = int(input("dime un año"))

if año1 - año2 >= 100:
    print("si hay un siglo de diferencia")
else:
    print("no hay un siglo de diferencia")

print(año)
"""
numeros  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
"""
for num in numeros:
    if num%2 == 0:
        print(num)

print()

for num in numeros:
    if num%2 != 0:
        print(num)
"""
"""
print("1. listar pares")
print("2. listar impares")
print("3. listar todos")
opcion = int(input("Introduce una de las opciones"))


if opcion == 1:
    for num in numeros:
        if num%2 == 0:
            print(num)
if opcion == 2:
    for num in numeros:
        if num%2 != 0:
            print(num)
if opcion == 3:
    for num in numeros:
        print(num)
"""

texto = "Hola estoy programando en python"
cantidad = 0
for letra in texto:
    if letra == str('a'):
        cantidad + 1

print(cantidad)