#A simple representation of graph using Adjacency Matrix implement by python 3.
#Space O(V^2)
#Removing an edge taken O(1) time and also adding a vertex is O(V^2) time.

class Graph:
    def __init__(self, numvertex):
        self.adjMatrix = [[-1]*numvertex for _ in range(numvertex)]
        self.numvertex = numvertex
        self.vertices = {}
        self.verticeslist = [0]*numvertex

    def set_vertex(self, vtx, id):
        if 0 <= vtx <= self.numvertex:
            self.vertices[id] = vtx
            self.verticeslist[vtx] = id

    def set_edge(self, _from, to, cost=0):
        _from = self.vertices[_from]
        to = self.vertices[to]
        self.adjMatrix[_from][to] = cost
        # Add this line only for underected graph.
        self.adjMatrix[to][_from] = cost

    def get_vertex(self):
        return self.verticeslist

    def get_edges(self):
        edges = []
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                if (self.adjMatrix[i][j] != -1):
                    edges.append((self.verticeslist[i], self.verticeslist[j], self.adjMatrix[i][j]))
        return edges

    def get_matrix(self):
        return self.adjMatrix
    
if __name__ == "__main__":
    G = Graph(6)
    G.set_vertex(0, 'a')
    G.set_vertex(1, 'b')
    G.set_vertex(2, 'c')
    G.set_vertex(3, 'd')
    G.set_vertex(4, 'e')
    G.set_vertex(5, 'f')
    print("Vertices of Graph")
    print(G.get_vertex())
    G.set_edge('a', 'e', 10)
    G.set_edge('a', 'c', 20)
    G.set_edge('c', 'b', 30)
    G.set_edge('b', 'e', 40)
    G.set_edge('e', 'd', 50)
    G.set_edge('f', 'e', 60)
    print("Edges of Graph")
    print(G.get_edges())
