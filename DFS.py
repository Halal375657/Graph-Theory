# DFS Algorithm.
# Time: O(V + E), Here, V is number of vertices and E is number of Edges.


from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.time = 0
        self.d = []
        self.f = []
        self.color = []

    def addEdges(self, src, dest):
        self.graph[src].append(dest)

    def DFS_Visit(self, v):

        self.time += 1
        self.d[v] = self.time
        self.color[v] = 'Gray'

        for i in self.graph[v]:
            if self.color[i] == 'White':
                self.DFS_Visit(i)

        self.time += 1
        self.f[v] = self.time
        self.color[v] = 'Black'

        return
        

    def DFS(self):
        n = len(self.graph) + 1

        self.color = ['White'] * n
        self.d = [0] * n
        self.f = [0] * n

        for u in self.graph:
            if self.color[u] == 'White':
                self.DFS_Visit(u)


if __name__ == "__main__":
    
    g = Graph()
    edges = [
        (1, 2),
        (1, 3),
        (2, 4),
        (4, 3),
        (3, 2),
        (5, 4),
        (5, 6),
        (6, 6)
        ]
    for edge in edges: # Connection nodes.
        g.addEdges(edge[0], edge[1])
        
    g.DFS()
    print(g.color[1:])
    print("Nodes ---------",' '.join(map(str, range(1, 7))))
    print("Discovery time:",' '.join(map(str, g.d[1:])))
    print("Finishing time:",' '.join(map(str, g.f[1:])))
