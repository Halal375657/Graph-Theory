

# Problem Link: https://www.hackerrank.com/challenges/floyd-city-of-blinding-lights/problem
# Passed all test for PyPy3 but not able in Python3.
# Time :- O(n^3)
# Space:- O(n^2)


from sys import maxsize


class Graph:
    def __init__(self, n):
        self.dist = [[maxsize] * (n) for _ in range(n)]
        self.n = n

    def addEdges(self, u, v, w):
        self.dist[v][u] = w

        self.dist[v][v] = 0
        self.dist[u][u] = 0

    def floydWarshall(self):
        n = self.n
        dist = self.dist

        for k in range(n):
            for i in range(n):
                if dist[i][k] == maxsize: continue
                for j in range(n):
                    if dist[k][j] == maxsize: continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    def query(self, u, v):
        if self.dist[v][u] == maxsize:
            print(-1)
        else:
            print(self.dist[v][u])


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = Graph(n)
    for _ in range(m):
        u, v, w = map(int, input().split())
        g.addEdges(u-1, v-1, w)

    g.floydWarshall()
    q = int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        g.query(u-1, v-1)
