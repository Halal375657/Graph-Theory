# DFS Traversal.



from collections import defaultdict



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

        self.DFS_Visit(u, visited)


            
if __name__ == "__main__":
    g = Graph(5+1)
    g.addEdges(1, 2)
    g.addEdges(1, 5)
    g.addEdges(2, 4)
    g.addEdges(5, 4)
    g.DFS(1) 
