#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

from collections import defaultdict

c_ Graph:
    ___ -  
        nodes _ s..
        edges _ defaultdict(list)
        distances _     # dict
    
    ___ addNodevalue
        nodes.add(value)
    
    ___ addEdge fromNode, toNode, distance
        edges[fromNode].a..(toNode)
        distances[(fromNode, toNode)] _ distance


___ dijkstra(graph, initial
    visited _ {initial : 0}
    path _ defaultdict(list)

    nodes _ s..(graph.nodes)

    _____ nodes:
        minNode _ N..
        ___ node __ nodes:
            __ node __ visited:
                __ minNode __ N..
                    minNode _ node
                ____ visited[node] < visited[minNode]:
                    minNode _ node
        __ minNode __ N..
            b..

        nodes.remove(minNode)
        currentWeight _ visited[minNode]

        ___ edge __ graph.edges[minNode]:
            weight _ currentWeight + graph.distances[(minNode, edge)]
            __ edge n.. __ visited __ weight < visited[edge]:
                visited[edge] _ weight
                path[edge].a..(minNode)
    
    r_ visited, path

customGraph _ Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addNode("F")
customGraph.addNode("G")
customGraph.addEdge("A", "B", 2)
customGraph.addEdge("A", "C", 5)
customGraph.addEdge("B", "C", 6)
customGraph.addEdge("B", "D", 1)
customGraph.addEdge("B", "E", 3)
customGraph.addEdge("C", "F", 8)
customGraph.addEdge("D", "E", 4)
customGraph.addEdge("E", "G", 9)
customGraph.addEdge("F", "G", 7)

print(dijkstra(customGraph, "A"))


