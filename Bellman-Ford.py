

#
# The Bellman-Ford Algorithm
# Book:- Introduction to Algorithms(H.Cormen)
# Time:- O(VE)
#

from sys import maxsize
from collections import defaultdict

class Graph:
    def __init__(self, v):
        self.dist = [maxsize] * v
        self.cost = [[0]*n for _ in range(n)]
        self.n = v
        self.G = defaultdict(list)

    def addEdges(self, u, v, w):
        self.cost[u][v] = w
        self.G[u].append(v)
        
    def relax(self, u, v):
        if self.dist[u] + self.cost[u][v] < self.dist[v]:
            self.dist[v] = self.dist[u] + self.cost[u][v]

    def BellmanFord(self, src):
        self.dist[src] = 0

        for u in range(self.n-1): #Alert, is this [V]-1, not [V].V is number of vertice
            for v in self.G[u]:
                self.relax(u, v)

        for u in range(self.n): # Alert, is this [V], not [V]-1, V is number of vertices.
            for v in self.G[u]:
                if self.dist[v] > self.dist[u] + self.cost[u][v]:
                    return False

        return True
    
if __name__ == "__main__":

    # Without negative cycle graph
    edges = ((1, 4, 4),
             (1, 3, 2),
             (2, 3, 10),
             (3, 4, 1),
             (4, 5, 7),
             (4, 6, 5)
             )
    # Negative cycle graph.
    edges = ((1, 2, 2),
             (2, 3, 1),
             (3, 1, -6)
             )

    n = 6
    n = 3
    g = Graph(n)
    for edge in edges:
        g.addEdges(edge[0]-1, edge[1]-1, edge[2])

    src = 1
    if g.BellmanFord(src-1):
        print("Not present negative cycle in this graph")
    else:
        print("Negative cycle detected")

