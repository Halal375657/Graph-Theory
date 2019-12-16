# Time: O(V log V + E), here V is number of nodes and E is number edges.

from heapq import heappush, heappop, heapify
import sys

class Graph(object):

    def __init__(self, vertices):
        self.v = vertices
        self.cost = []

    def dijkstra(self, source):
        
        Q = [source]
        distance = [sys.maxsize] * self.v
        heapify(Q)
        distance[source] = 0

        while Q:

            # nodes in Q with minimum distance[] remove u from the Q.
            u = heappop(Q)
            
            for v in range(self.v):
                if self.cost[u][v] and distance[u] + self.cost[u][v] < distance[v]:
                    distance[v] = distance[u] + self.cost[u][v]
                    # v enqueue in Q.
                    heappush(Q, v)

        return distance



if __name__ == "__main__":
    g = Graph(4)
    g.cost = [[0, 2, 5, 0],
               [2, 0, 1, 0],
               [5, 1, 0, 3],
               [0, 0, 3, 0]
               ]
    shortest_distance = g.dijkstra(0)
    print(' -> '.join(str(distance), for distance in shortest_distance)
