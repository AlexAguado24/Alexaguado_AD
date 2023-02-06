def ordenar(lista):
    for i in range(1, len(lista)):
        for j in range(0, len(lista)-i):
            if (lista[j+1] < lista[j]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    print(lista)


numeros = [40, 21, 4, 9, 10, 35]

ordenar(numeros)
