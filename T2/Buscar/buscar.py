
''' lista = [1, 8, 7, 2, 15, 21, 17, 4]
array = [21, 25]


for i in range(len(array)):
    for j in range(len(lista)):
        if lista[j] == array[i]:
            print(str(lista[j]))
            break
        else:
            print("numero no encontrado") '''


''' lista = [1, 2, 3, 4, 8, 100, 1200, 1201]
num = int(input("mete numero a buscar"))


def buscar(listaNumeros, numBuscar):
    mitad = len(listaNumeros)//2
    print(listaNumeros[mitad:])
    print(listaNumeros[:mitad])
    print(listaNumeros[mitad])
    if listaNumeros[mitad] == numBuscar:
        print("Encontrado")
        return numBuscar
    elif listaNumeros[mitad] > numBuscar:
        return buscar(lista[:mitad], numBuscar)
    else:
        return buscar(lista[mitad:], numBuscar)


buscar(lista, num) '''

lista = [40, 21, 4, 10, 9, 35]


def busqueda(listaNew):
    pivote = listaNew[-1]
    listaMayores = []
    listaMenores = []
    for i in listaNew:
        if i > pivote:
            listaMayores.append(i)
        else:
            listaMenores.append(i)
    listaNew += listaMenores + listaMayores
    busqueda(listaNew)


busqueda(lista)
print(lista)
