class Vertex:
    def __init__(self, id):
        self.id = id
        self.adj = {}
    def adiciona_vizinho(self, vertice, peso=0):
        self.adj.setdefault(vertice, []).append(peso)
        # self.adj[vertice] = peso
    def remove_vizinho(self, vertice):
        if vertice in self.adj:
            self.adj.pop(vertice)
    def getAdj(self):
        return self.adj
    def __str__(self):
        vizinhos_str = " ".join(f"{vizinho.id}:{peso}" for vizinho, peso in self.adj.items())
        return f"{self.id} conectado a: {vizinhos_str}"
    def getWeight(self,id):
        return self.adj[id]
class Graph:
    def __init__(self):
        self.vertices = {}
    def adiciona_vertice(self, key):
        self.vertices[key] = Vertex(key)
    def getVertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        return None
    def add_edges(self, src, dst, weight=0):
        if not self.getVertex(src):
            self.adiciona_vertice(src) 
        if not self.getVertex(dst):
            self.adiciona_vertice(dst) 
        vertice = self.getVertex(src)
        vertice.adiciona_vizinho(self.getVertex(dst), weight)
    def __iter__(self):
        return iter(self.vertices.values())
    
    

grafin = Graph()
grafin.adiciona_vertice("V0")
grafin.adiciona_vertice("V1")
grafin.adiciona_vertice("V2")
grafin.adiciona_vertice("V3")
grafin.adiciona_vertice("V4")
grafin.adiciona_vertice("V5")

grafin.add_edges("V0", "V1", 5)
grafin.add_edges("V0", "V5", 2)

grafin.add_edges("V1", "V2", 4)

grafin.add_edges("V2", "V3", 9)

grafin.add_edges("V3", "V4", 7)
grafin.add_edges("V3", "V5", 3)

grafin.add_edges("V4", "V0", 1)

grafin.add_edges("V5", "V2", 1)
grafin.add_edges("V5", "V4", 8)





for i in grafin:
    print(f'{i}')

