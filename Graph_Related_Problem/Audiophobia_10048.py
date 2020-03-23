
#
# Online Judges: UVA
# Problem Link:- https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=989
# Floyd Warshall algorithm
# 

from sys import maxsize

class Graph:
    def __init__(self, vertices):
        self.graph = [[maxsize]*vertices for _ in range(vertices)]
        self.vertices = vertices

    def addEdges(self, u, v, w):
        self.graph[u-1][v-1] = w
        self.graph[v-1][u-1] = w

    def flowd(self):

        n = self.vertices
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    self.graph[i][j] = min(self.graph[i][j], max(self.graph[i][k], self.graph[k][j]))

    def query(self, u, v):
        if self.graph[u-1][v-1] != maxsize:
            print(self.graph[u-1][v-1])
        else:
            print("no path")
        

if __name__ == "__main__":
    test = 0
    while True:
        C, S, Q = map(int, input().split())
        zero = 0
        terminate = C == S == Q == zero
        if terminate:
            break
        else:
            if test != 0:
                print()
        #  Make Nodes
        g = Graph(C)

        # insert Edges
        for _ in range(S):
            u, v, w = map(int, input().split())
            g.addEdges(u-1, v-1, w)

        # Manipulate
        g.flowd()
        # Query
        test += 1
        print("Case #{}".format(test))
        for _ in range(Q):
            u, v = map(int, input().split())
            g.query(u-1, v-1)
