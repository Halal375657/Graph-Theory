


# Floyd Warshall with path reconstruction.
# Time :- O(n^3)
# Space:- O(n^2)


from sys import maxsize

class Graph:
    def __init__(self, n):
        self.dist = [[maxsize]*(n+1) for _ in range(n+1)]
        self.next = [[None]*(n+1) for _ in range(n+1)]
        self.n = n

    def addEdges(self, u, v, w):
        self.dist[u][v] = w
        self.next[u][v] = v

    def Floyd_Warshall(self):
        n = self.n+1
        dist = self.dist

        for v in range(n):
            dist[v][v] = 0
            self.next[v][v] = v
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        self.next[i][j] = self.next[i][k]

    def path(self, u, v):
        if self.next[u][v] == None:
            return []
        
        path = [u]
        while u != v:
            u = self.next[u][v]
            path.append(u)
        return path
        

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

    g.Floyd_Warshall()

    # Test
    u, v = map(int, input().split())
    path = g.path(u, v)
    if path == []:
        print("path is not available!")
    else:
        print('Path: ', ' -> '.join(map(str, path)))
        print('Path Distance: ', g.dist[u][v])
