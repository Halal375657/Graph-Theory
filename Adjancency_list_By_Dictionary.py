#A simple representation of graph using Adjacency List.Implement by dictionary.

class Graph:
    def __init__(self, vertex):
        self.graph = {i:[] for i in vertex}

    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def print_graph(self):
        keys = self.graph.keys()
        for key in keys:
            print(key, end = ": ")
            for node in self.graph[key]:
                print("%d"%(node), end=" ")
            print()

if __name__ == "__main__":
    graph = Graph([0, 3, 2, 1, 4, 9])
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
