#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

# Kruskal Algorithm  in Python
______ DisjointSet as dst

c_ Graph:
    ___ -  vertices
        V _ vertices
        graph _    # list
        nodes _    # list
        MST _    # list

    ___ addEdge s, d, w
        graph.a..([s, d, w])
    
    ___ addNode value
        nodes.a..(value)
    
    ___ printSolutions,d,w
        ___ s, d, w __ MST:
            print("%s - %s: %s" % (s, d, w))
    
    ___ kruskalAlgo 
        i, e _ 0, 0
        ds _ dst.DisjointSet(nodes)
        graph _ s..(graph, key_lambda item: item[2])
        _____ e < V - 1:
            s, d, w _ graph[i]
            i +_ 1
            x _ ds.find(s)
            y _ ds.find(d)
            __ x !_ y:
                e +_ 1
                MST.a..([s,d,w])
                ds.union(x,y)
        printSolution(s,d,w)

g _ Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "B", 5)
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)
g.addEdge("B", "A", 5)
g.addEdge("B", "C", 10)
g.addEdge("B", "D", 8)
g.addEdge("C", "A", 13)
g.addEdge("C", "B", 10)
g.addEdge("C", "E", 20)
g.addEdge("C", "D", 6)
g.addEdge("D", "B", 8)
g.addEdge("D", "C", 6)
g.addEdge("E", "A", 15)
g.addEdge("E", "C", 20)

g.kruskalAlgo()


