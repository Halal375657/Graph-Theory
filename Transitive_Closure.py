
#
# Floyd Warshall
# Transitive Closure
# Book:- Introduction to Algorithms(Cormen). Page no:- 698
# Time:- O(n^3)
# Space:- O(n^2)

class Transitive:
    def __init__(self, n):
        self.T = [[0] * (n) for _ in range(n)]
        self.n = n

    def addEdge(self, u, v):
        self.T[u][v] = 1
        self.T[v][v] = 1
        self.T[u][u] = 1

    def transitiveClosure(self):
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    self.T[i][j] = self.T[i][j] or (self.T[i][k] and self.T[k][j])

    def print_t(self):
        for row in self.T:
            print(' '.join(str(i) for i in row))
            print()

if __name__=="__main__":
    edges = ((4, 1),
             (4, 3),
             (3, 2),
             (2, 3),
             (2, 4)
             )
    t = Transitive(4)
    for edge in edges:
        t.addEdge(edge[0]-1, edge[1]-1)

    print("=======Before========")
    t.print_t()
    t.transitiveClosure()
    print("======After==========")
    t.print_t()
