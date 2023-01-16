numUno = int(input("Ingresa un numero con el que quieres trabajar\n"))
numDos = int(input("Ingresa otro numero con el que quieres trabajar\n"))

def resta(A,B):
    if B == 0:
        return A
    else:
        return  resta(A,B-1)-1
    

def exponente(exponenteUno, exponenteDos):
    if exponenteDos == 1:
        return exponenteUno
    else:
        return exponenteUno * exponente(exponenteUno,exponenteDos-1)


def maximoComunDivisor(comunUno, comunDos):
    if comunDos == 0:
        return comunUno
    else:
        return maximoComunDivisor(comunDos,comunUno%comunDos)
    
    

def multiplicacion(A,B):
    if B == 1:
        return A
    else:
        return A + multiplicacion(A,B-1)

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
    
def factorialIterativo(valor1):
    print("--Iterativo--")
    for i in range(1,valor1):
        resultado = i*valor1
        valor1 = resultado
    return resultado


def menu():
    print("1. Calcular factorial")
    print("2. Multiplicacion de 2 números")
    print("3. Maximo comun divisor")
    print("4. Exponente")
    print("5. Resta")
    opcion = input("Introduce la opcion deseada\n")
    return opcion

def lanzar_programa():
    while True:
        opcion = str(menu())
        if opcion == str("1"):
            print("--Recursivo--")
            print(factorial(numUno))
            print()
            print(factorialIterativo(numUno))
            print()
        elif opcion == str("2"):
            print("--Recursivo--")
            print(multiplicacion(numUno,numDos))
            print()
            print("--Iterativo--\n"+str(numUno*numDos))
        elif opcion == str("3"):
            print("--Recursivo--")
            print(maximoComunDivisor(numUno,numDos))
            print()
            print("--Iterativo--\n")
        elif opcion == str("4"):
            print("--Recursivo--")
            print(exponente(numUno,numDos))
            print()
            print("--Iterativo--\n"+str(numUno**numDos))
        elif opcion == str("5"):
            print("--Recursivo--")
            print(resta(numUno,numDos))
            print()
            print("--Iterativo--\n"+str(numUno-numDos))
        else:
            break
        
lanzar_programa()
