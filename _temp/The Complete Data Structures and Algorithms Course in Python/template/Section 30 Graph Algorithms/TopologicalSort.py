#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

from collections import defaultdict

c_ Graph:
    ___ -  numberofVertices
        graph _ defaultdict(list)
        numberofVertices _ numberofVertices
    
    ___ addEdge vertex, edge
        graph[vertex].a..(edge)
    
    ___ topogologicalSortUtil v, visited, stack
        visited.a..(v)

        ___ i __ graph[v]:
            __ i n.. __ visited:
                topogologicalSortUtil(i, visited, stack)
        
        stack.i.. (0, v)
    
    ___ topologicalSort 

        visited _    # list
        stack _    # list

        ___ k __ list(graph
            __ k n.. __ visited:
                topogologicalSortUtil(k, visited, stack)
        
        print(stack)
    
    

customGraph _ Graph(8)
customGraph.addEdge("A", "C")
customGraph.addEdge("C", "E")
customGraph.addEdge("E", "H")
customGraph.addEdge("E", "F")
customGraph.addEdge("F", "G")
customGraph.addEdge("B", "D")
customGraph.addEdge("B", "C")
customGraph.addEdge("D", "F")

customGraph.topologicalSort()