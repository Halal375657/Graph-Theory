

#
# Problem Link:-https://www.hackerrank.com/challenges/kruskalmstrsub/problem
# Time:- O(E log V)
#

from operator import itemgetter

class Disjoin:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.v = n+1

    def find(self, r):
        if self.par[r] != r:
            self.par[r] = self.find(self.par[r])
        return self.par[r]

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u != v:
            self.par[v] = u

class Graph(Disjoin):
    def __init__(self, n):
        super().__init__(n)

    def kruskals(self, graph):

        MST_cost = 0

        for (u, v, w) in sorted(graph, key = itemgetter(2)):
            if self.find(u) != self.find(v):
                self.union(u, v)
                MST_cost += w

        return MST_cost

if __name__=="__main__":
    nodes, edges = map(int, input().split())
    graph = []
    for _ in range(edges):
        graph.append(tuple(map(int, input().split())))

    g = Graph(nodes)
    pathMST = g.kruskals(graph)
    print(pathMST)
