#A simple representation of graph using Adjacency List.
#Space: O(V+E),there, E is number of edge and V is number of Verteces.

class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [None] * self.v

    # Function to add an edge in an undirected graph.
    def add_edge(self, source, destination):
        # Adding the node to the source node.
        node = AdjNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node

        # Adding the source node to the destination as it is the undirected graph.
        node = AdjNode(source)
        node.next = self.graph[destination]
        self.graph[destination] = node

    def print_graph(self):
        for i in range(self.v):
            print("Adjacency list of vertex {}\n head".format(i), end=" ")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end=" ")
                temp = temp.next
            print(" \n")


if __name__ == "__main__":
    v = 5
    graph = Graph(v)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
    print(graph.graph)
