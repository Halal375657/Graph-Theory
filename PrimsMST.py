
#
# Prim's Algorithm
# Book:- Introduction to Algorithms
# O(E log V)
#

from heapq import heappush, heappop, heapify


class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [{} for _ in range(n)]

    def addEdges(self, u, v, w):
        self.graph[u][v] = w
        # As undirected.
        self.graph[v][u] = w

    def primMST(self, src):
        
        setMST = [False]*self.n
        Q = [(0, 0, src)]
        lookup = set()
        A = []
        
        while Q:

            w, _, u = heappop(Q)

            for v in self.graph[u]:
                if setMST[v] == False:
                    heappush(Q, (self.graph[u][v], u, v))

            if Q:
                w, u, v = Q[0][0], Q[0][1], Q[0][2]
                if v in lookup: continue
                lookup.add(v)
                setMST[u] = True
                A.append((u,v, w))
                
        return A
    
if __name__ == "__main__":


    g = Graph(5)

    edges = ((1, 2, 5),
             (1, 3, 2),
             (2, 3, 1),
             (2, 4, 2),
             (3, 4, 3)
             )
    for (u, v, w) in edges:
        g.addEdges(u, v, w)
    A = g.primMST(1)
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
