
class Dato:
    def __init__(self, i):
        self.id = i
        self.vecinos = []
        self.visitado = False
        self.padre = None
        self.costo = float('inf')

    def addDato(self, vertice, valor):
        if v not in self.datos:
            self.datos.append([vertice, valor])


class Grafica:
    def __init__(self):
        self.datos = {}

    def addDato(self, id):
        if id not in self.datos:
            self.datos[id] = Dato(id)

    def addArista(self, arista, visitado, valor):
        if arista in self.datos and visitado in self.datos:
            self.datos[arista].addDato(visitado, valor)
            self.datos[visitado].addDato(arista, valor)

    def imprimir(self):
        for vertice in self.datos:
            print(str(self.datos[vertice].id) + str(self.datos[vertice].padre))

    def camino(self, arista, visitado):
        camino = []
        actual = visitado
        while actual != None:
            camino.insert(0, actual)
            actual = self.datos[actual].padre
        return [camino, self.vertices[visitado]]


    def dijkstra(self, a):
        if a in self.datos:
            self.datos[a].costo = 0
            actual = a
            noVisitados = []

            for v in self.datos:
                if v != a:
                    self.datos[v].costo = float('inf')
                self.datos[v].padre = None
                noVisitados.append(v)

            while len(noVisitados) > 0:
                for vec in self.datos[actual].vecinos:
                    if self.datos[vec[0]].visitado == False:
                        if self.datos[actual].costo + vec[1] < self.datos[vec[0]].costo:
                            self.datos[vec[0]].costo = self.datos[actual].costo + vec[1]
                            self.datos[vec[0]].padre = actual
                self.datos[actual].visitado = True
                noVisitados.remove(actual)
                actual = self.minimo(noVisitados)
        else:
            return False


