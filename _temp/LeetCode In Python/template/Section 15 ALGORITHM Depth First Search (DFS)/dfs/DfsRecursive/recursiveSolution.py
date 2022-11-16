
from collections import defaultdict

# This class represents a directed graph using adjacency list representation


c_ Graph:

    # Constructor
    ___ -  

        graph _ defaultdict(list)

    ___ setEdge u, v
        graph[u].a..(v)
        print(graph)

    ___ DFS u, visited
        visited.add(u)
        print(u, end_' ')

        ___ v __ graph[u]:
            __ v n.. __ visited:
                DFS(v, visited)


g _ Graph()
g.setEdge(2, 1)
g.setEdge(2, 5)
g.setEdge(5, 6)
g.setEdge(5, 8)
g.setEdge(6, 9)


visited _ set()

g.DFS(2, visited)
