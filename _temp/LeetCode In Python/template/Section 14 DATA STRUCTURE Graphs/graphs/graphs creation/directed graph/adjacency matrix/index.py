____ collections ______ defaultdict


c_ Graph:
    ___ -  numberOfNodes
        numberOfNodes _ numberOfNodes+1
        graph _ [[0 ___ x __ r..(numberOfNodes+1)]
                      ___ y __ r..(numberOfNodes+1)]

    ___ withInBounds v1, v2
        r_ (v1 >_ 0 ___ v1 <_ numberOfNodes) ___ (v2 >_ 0 ___ v2 <_ numberOfNodes)

    ___ insertEdge v1, v2
        __(withInBounds(v1, v2
            graph[v1][v2] _ 1

    ___ printGraph
        ___ i __ r..(numberOfNodes
            ___ j __ r..(l..(graph[i]
                __(graph[i][j]
                    print(i, "->", j)


g _ Graph(5)

g.insertEdge(1, 2)
g.insertEdge(2, 3)
g.insertEdge(4, 5)

g.printGraph()
