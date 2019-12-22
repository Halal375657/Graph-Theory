# Depth-First-Search Without Recursive.
# Time is O(v + E)


from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdges(self, src, dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def DFS(self, src):
        stack, path = [src], []

        while stack:
            u = stack.pop()
            
            if u not in path:
                path.append(u)
                for neighbor in self.graph[u]:
                    stack.append(neighbor)

        return path

if __name__ == "__main__":
    Edges = [
        (1, 2),
        (1, 3),
        (2, 5),
        (2, 4),
        (4, 6),
        (6, 7),
        (5, 6),
        (3, 5),
        ]
    obj = Graph()

    for tple in Edges:
        obj.addEdges(tple[0], tple[1])
        
    path = obj.DFS(1)
    print(path)
    # Output: [1, 3, 5, 6, 7, 2, 4]

