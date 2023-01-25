class Nodo:
    def __init__(self, dato):
        self.raiz = None
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

    def tieneDerecho(self):
        return self.derecho != None

    def tieneIzquierdo(self):
        return self.izquierdo != None

    def preOrden(self):
        print(self.dato)
        if self.tieneIzquierdo():
            self.izquierdo.preOrden()
        if self.tieneDerecho():
            self.derecho.preOrden()

    def inOrden(self):
        if self.tieneIzquierdo():
            self.izquierdo.preOrden()
        print(self.dato)
        if self.tieneDerecho():
            self.derecho.preOrden()

    def postOrden(self):
        if self.tieneIzquierdo():
            self.izquierdo.preOrden()
        if self.tieneDerecho():
            self.derecho.preOrden()
        print(self.dato)

    def insertar(self, nodo):
        if self.dato == nodo.dato:
            print("El elemento ya existe")
        elif nodo.dato < self.dato:
            if self.tieneIzquierdo():
                self.izquierdo.insertar(nodo)
            else:
                self.izquierdo = nodo
        else:
            if self.tieneDerecho():
                self.derecho.insertar(nodo)
            else:
                self.derecho = nodo


class Arbol:
    def __int__(self):
        self.raiz = None

    def esVacio(self):
        return self.raiz == None

    def preOrden(self):
        if not self.esVacio():
            self.raiz.preOrden()
        else:
            print("Esta vacio")

    def inOrden(self):
        if not self.esVacio():
            self.raiz.preOrden()
        else:
            print("Esta vacio")

    def postOrden(self):
        if not self.esVacio():
            self.raiz.preOrden()
        else:
            print("Esta vacio")

    def insertar(self, dato):
        nodo = Nodo(dato)
        if self.esVacio():
            self.raiz = nodo
        else:
            self.raiz.insertar(nodo)


arbol1 = Arbol()
arbol1.insertar(10)
arbol1.insertar(8)
arbol1.insertar(6)
arbol1.insertar(9)
arbol1.insertar(5)
arbol1.insertar(3)
arbol1.insertar(7)
arbol1.insertar(20)
arbol1.insertar(15)
arbol1.insertar(25)
arbol1.insertar(35)
arbol1.insertar(18)
