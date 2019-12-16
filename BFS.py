#Time O(V+E), Where V is number of vertices and E is number of edges in the graph.
#Representation by Adjacency List.

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Function to add an edge to graph.
    def addEdge(self, u, v):
        self.graph[u].append(v)
        #For undirected graph.
        self.graph[v].append(u)

    # Functin to print a BFS of graph.
    def BFS(self, source):

        # Marked all the verteces as not visited.
        visited = [False] * (len(self.graph)+1)

        # Create a queue for BFS
        queue = []

        #Mark the source node as visited and enqueue it.
        queue.append(source)
        visited[source] = True

        while queue:

            # Dequeue a vertex from queue and print it.
            source = queue.pop(0)
            print(source, end = " ")

            # Get all adjacent vertices of the dequeued vertex source.
            # If a adjacent has not been visited, then mark it visited and enqueue it.
            for i in self.graph[source]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

if __name__ == "__main__":
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 5)
    g.addEdge(4, 5)
    g.addEdge(4, 6)
    g.addEdge(5, 2)
    g.addEdge(5, 4)
    g.addEdge(5, 6)
    g.addEdge(6, 4)
    g.addEdge(6, 5)

    print ("Following is Breadth First Traversal(starting from vertex 1)")
    g.BFS(1)
