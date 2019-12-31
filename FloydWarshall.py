


# Floyd Warshall without path contstruction.
# Time :- O(n^3)
# Space:- O(n^2)


from sys import maxsize

class Graph:
    def __init__(self, n):
        self.dist = [[maxsize]*(n+1) for _ in range(n+1)]
        self.n = n

    def addEdges(self, src, dest, w):
        self.dist[src][dest] = w


    def FloydWarshall(self, dist):
        n = self.n+1

        for v in range(n):
            dist[v][v] = 0
        
        for k in range(1, n):
            for i in range(1, n):
                for j in range(1, n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                    
if __name__=="__main__":

    g = Graph(4)
    edges = ((1, 2, 3),
             (2, 3, 2),
             (3, 2, 5),
             (2, 1, 2),
             (4, 3, 8),
             (4, 1, 20),
             )
    for tpl in edges:
        g.addEdges(tpl[0], tpl[1], tpl[2])

    g.FloydWarshall(g.dist)
    print(g.dist[1:][1:])
    
