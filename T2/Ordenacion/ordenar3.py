numeros3 = [1, 40, 21, 4, 9, 10, 35]


def ordenarLista(listaUno, listaDos):
    lista = []
    for i in range(0, len(listaUno)):
        for j in range(0, len(listaDos)):
            if (listaUno[i] > listaDos[j]):
                lista.append(listaDos[j])
            else:
                lista.append(listaUno[i])
    print(lista)


def partirLista(lista):
    if len(lista) < 2:
        return lista
    else:
        mitad = len(lista)//2
        partirLista(lista[:mitad])
        partirLista(lista[mitad:])
        return ordenarLista(lista[:mitad], lista[mitad:])


partirLista(numeros3)
