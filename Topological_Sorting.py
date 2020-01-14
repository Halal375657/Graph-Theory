


#
# Topological Sorting Algorithm.
#
# O(V + E)
#


from collections import defaultdict


graph = {}
Graph = defaultdict(list)

# Add edge of directed graph.
def addEdges(u, v):
    Graph[u].append(v)

# Adding in-degree.
def addDegree(u, v):
    try:
        graph[v] += 1
    except KeyError:
        graph[v] = 1

    try:
        if graph[u]:
            pass
    except KeyError:
        graph[u] = 0

# Topological Sorting.
def topsort():

    L = []
    nodeList = [node for node in graph]
    check = {}
    for node in nodeList:
        check[node] = False    

    while nodeList:
        
        u = nodeList.pop()
        
        if graph[u] == 0:
            if check[u] == False: #if check[u] is True that meaning is already Sort listed this node.
                L.append(u)
                check[u] = True
                
                for v in Graph[u]:
                    graph[v] -= 1
                    if graph[v] == 0: # It's meaning this node is now availabe for sorting
                        nodeList.append(v)
    return L


if __name__=="__main__":

    edges = (
        ("Breakfast", "Office"),
        ("Dress up", "Office"),
        ("Office", "Dinner"),
        ("Office", "Sports"),
        ("Office", "Email"),
        ("Email", "Sports"),
        ("Email", "Dinner"),
        ("Dinner", "Sports")
        )
    for (u, v) in edges:
        addDegree(u, v)
        addEdges(u, v)
    res = topsort()
    print(' -> '.join(map(str, res)))
