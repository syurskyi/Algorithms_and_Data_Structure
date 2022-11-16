from collections import defaultdict


c_ Graph:
    ___ -  
        graph _ defaultdict(list)

    ___ insertEdge v1, v2
        graph[v1].a..(v2)

    ___ printGraph 
        ___ node __ graph:
            ___ v __ graph[node]:
                print(node, "->", v)


g _ Graph()

g.insertEdge(1, 2)
g.insertEdge(2, 3)
g.insertEdge(4, 5)

g.printGraph()
