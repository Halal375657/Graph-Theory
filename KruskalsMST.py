
#
# The algorithm of Kruskal's.
# Book:- Introduction ot Algorithoms(H.Cormen)
# O(E log V)
#

from operator import itemgetter


class Disjoin:
    def __init__(self, vertices):
        self.v =  vertices
        self.par = [v for v in range(vertices)] # Make-Set().

    # Path Compression.
    def find_par(self, r):
        if self.par[r] != r:
            self.par[r] = self.find_par(self.par[r])
        return self.par[r]

    def union(self, u, v):
        u = self.find_par(u)
        v = self.find_par(v)

        if u != v:
            self.par[v] = u


# Inherite Disjoin in Graph.
class Graph(Disjoin):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.graph = [{} for v in range(vertices)]

    def addEdges(self, u, v, w):
        self.graph[u][v] = w
        # As Undirected.
        self.graph[v][u] = w


    # MST-Kruskal's
    def Kruskals(self, edges):

        A = []

        for (u, v, w) in sorted(edges, key=itemgetter(2)):
            if self.find_par(u) != self.find_par(v):
                A.append((u, v, w))
                self.union(u, v)

        return A


if __name__=="__main__":

    v = 5
    edges = ((1, 2, 5),
             (1, 3, 2),
             (2, 3, 1),
             (2, 4, 2),
             (3, 4, 3)
             )
    g = Graph(v)
    A = g.Kruskals(edges)
    print("============Before prim's MST============")
    print("u - v -> Weight")
    totalCost = 0
    for (u, v, w) in edges:
        totalCost += w
        print(u,"-",v,"->",w)
    print("Total Cost is:", totalCost)
    print("\n\n============After prim's MST============")
    print("u - v -> Weight")
    totalCost = 0
    for (u, v, w) in A:
        totalCost += w
        print(u,"-",v,"->",w)
    print("Total Cost is:", totalCost)
