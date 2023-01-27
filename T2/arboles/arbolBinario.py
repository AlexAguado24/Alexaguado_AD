arbol = {}

dato = int(input("Introduce un numero mayor que 0"))

nodo = {
    'raiz': None,
    'valor': None,
    'izquierdo': None,
    'derecho': None
}


def esVacio(nodo):
    if nodo.raiz == None:
        return true
    else:
        return false


def valorIzquierda(nodo):
    return nodo.izquierdo != None


def valorDerecha(nodo):
    return nodo.derecho != None


def insertarValor(nodo, dato):
    if nodo.valor == dato:
        print("Este numero ya esta en el arbol")
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


def buscarDato(nodo, dato):
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
