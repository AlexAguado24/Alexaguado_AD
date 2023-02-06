''' def ordenar(lista):
    for i in range(1, len(lista)):
        for j in range(0, len(lista)-i):
            if (lista[j+1] < lista[j]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    print(lista)


numeros = [40, 21, 4, 9, 10, 35]

ordenar(numeros) '''


''' def ordenar(lista):
    for i in range(0, len(lista)):
        for j in range(1, len(lista)-i):
            if (lista[j-1] > lista[j]):
                lista[j], lista[j-1] = lista[j-1], lista[j]
    print(lista)


numeros = [40, 21, 4, 9, 10, 35]

ordenar(numeros) '''


# print(mitad)
nuevaLista = []


def ordenarLista(lista1, lista2):
    if lista1[0] > lista2[0]:
        nuevaLista.append(lista2[0])
        lista2.pop(0)
    else:
        nuevaLista.append(lista1[0])
        lista1.pop(0)
    print(nuevaLista)


def partirLista(lista):
    if len(lista) < 2:
        return lista
    else:
        mitad = len(lista)//2
        partirLista(lista[:mitad])
        partirLista(lista[mitad:])
        return ordenarLista(lista[:mitad], lista[mitad:])


numeros = [40, 21, 4, 9, 10, 35]

# numUno, numDos = partirLista(numeros)

partirLista(numeros)
# print(numDos)
