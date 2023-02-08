arbol = []

dato = int(input("Introduce un numero mayor que 0"))

nodo = {}

def esVacio(arbol, nodo):
    for i in range(len(arbol)):
        if nodo.raiz == None:
            return true
        else:
            return false

def crear_arbol(valor_nuevo):
    nodo = {
        'raiz': valor_nuevo,
        'valor': None
        'izquierdo': None
        'derecho': None}
    return nodo

def valorIzquierda(nodo):
    return nodo.izquierdo != None

def valorDerecha(nodo):
    return nodo.derecho != None

def insertarValor(nodo, dato,arbol):
    if nodo.valor != 0:
        if len(arbol) == 0:
            nodo = crear_arbol(dato)
            arbol.append(nodo)
    elif nodo.dato > valor:
        if valorIzquierda():
            nodo.izquierdo.insertarValor()
        else:
            nodo.izquierdo = dato
    else:
        if valorDerecha():
            nodo.derecho.insertarValor()
        else:
            nodo.derecho = dato


def insertarValorDos(nodo, sitio,arbol):
    if nodo.valor != 0:
        if len(arbol) == 0:
            nodo = crear_arbol(nodo)
            arbol.append(nodo)
        else:
            if nodo < arbol[sitio]['valor']:
                if esVacio(arbol, != arbol.valorIzquierda(nodo)) == True:
                    nodo = crear_arbol(nodo)
                    arbol.append(nodo)
                    arbol[sitio]['izquierdo'] = nodo['valor']
                    arbol[-1]['raiz'] = arbol[sitio]['valor']
                else:
                    for i in range(len(arbol)):
                        if arbol[i]['valor'] == arbol[sitio]['izquierdo']:
                            meter = i
                        insertarValor(arbol, meter, nodo)
            elif nodo > arbol[sitio]['valor']:
                if esVacio(arbol, != arbol.valorDerecha(nodo)) == True:
                    nodo = crear_arbol(nodo)
                    arbol.append(nodo)
                    arbol[sitio]['derecho'] = nodo['valor']
                    arbol[-1]['raiz'] = arbol[sitio]['valor']
                else:
                    for i in range(len(arbol)):
                        if arbol[i]['valor'] == arbol[sitio]['derecho']:
                            meter = i
                    insertarValor(arbol, meter, nodo)

def buscarDato(nodo,dato):
    if nodo.valor == dato:
        return dato
    elif valorIzquierda():
        if nodo.izquierdo == dato:
            return dato
        else:
            nodo.izquierdo.buscarDato()
    elif valorDerecha():
        if nodo.derecho == dato:
            return dato
        else:
            nodo.derecho.buscarDato()


def buscarDatoDos(arbol, dato):
    buscado = False
    for i in range(len(arbol)):
        if arbol[i]['valor'] == dato:
            buscado = True
    if buscado == True:
        print('Dato encontrado')
        for i in range(len(arbol)):
            if arbol[i]['valor'] == dato:
                print('raiz: ' + str(arbol[i]['raiz']) + 'izquierdo:' + str(arbol[i]['izquierdo']) + 'derecho:' + str(arbol[i]['derecho']))
        for i in range(len(arbol)):
            if arbol[i]['valor'] == dato:
                if arbol[i]['raiz'] != 0:
                    for j in range(len(arbol)):
                        if arbol[j]['valor'] == arbol[i]['raiz']:
                            if arbol[j]['izquierdo'] != buscado:
                                print(
                                    'izquierdo: ' + str(arbol[j]['izquierdo']))
                            else:
                                print(
                                    'derecho:' + str(arbol[j]['derecho']))
    else:
        print('Dato encontrado: '+str(buscado))



def eliminarDato(nodo, dato):
    if nodo.valor == dato:
        nodo.valor = None
    elif valorIzquierda():
        if nodo.izquierdo == dato:
            nodo.izquierdo = None
        else:
            nodo.izquierdo.eliminarDato()
    elif valorDerecha():
        if nodo.derecho == dato:
            nodo.derecho = None
        else:
            nodo.derecho.eliminarDato()


def eliminar(arbol):
    if len(arbol) > 0:
        arbol.clear()
        return arbol
    else:
        print('Aun no hay ningun árbol')