# DFS Traversal.

<<<<<<< HEAD
from collections import defaultdict


=======


from collections import defaultdict



>>>>>>> bca4ebc3caeaccd9145c9c8a5f35645e1bcd3b4e
class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)

    # Directed graph.
    def addEdges(self, src, dest):
        self.graph[src].append(dest)

    def DFS_Visit(self, v, visited):

        visited[v] = True
        print(v, end=' ')

        for i in self.graph[v]:
            if not visited[i]:
                self.DFS_Visit(i, visited)
        

    def DFS(self, u):

        visited = [False] * self.n

<<<<<<< HEAD
        # Traverse only reachable vertices.
        # self.DFS_Visit(u, visited)

        # Traverses reachable and unreachable vertices.
        for i in range(self.n):
            if not visited[i]:
                self.DFS_Visit(i, visited)
=======
        self.DFS_Visit(u, visited)
>>>>>>> bca4ebc3caeaccd9145c9c8a5f35645e1bcd3b4e


            
if __name__ == "__main__":
    g = Graph(5+1)
    g.addEdges(1, 2)
    g.addEdges(1, 5)
    g.addEdges(2, 4)
    g.addEdges(5, 4)
    g.DFS(1) 
