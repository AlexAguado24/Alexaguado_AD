class Graph():
 
    def __init__(self, vertice):
        self.v = vertice
        self.graph = [[0 for column in range(vertice)]
                      for row in range(vertice)]
 
    def pSol(self, dist):
        for node in range(self.V):
            print(node, "t", dist[node])
 

    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 

    def dijk(self, source):
 
        dist = [sys.maxsize] * self.V
        dist[source] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            u = self.minDistance(dist, sptSet)
 
            sptSet[u] = True
 

            for v in range(self.V):
                if self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
 
        self.pSol(dist)



class  