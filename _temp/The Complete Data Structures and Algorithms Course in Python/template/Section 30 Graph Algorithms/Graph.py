#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

c_ Graph:
    ___ -  gdict_None
        __ gdict __ N..:
            gdict _     # dict
        gdict _ gdict
    
    ___ addEdge vertex, edge
        gdict[vertex].a..(edge)
    
    ___ bfs vertex
        visited _ [vertex]
        queue _ [vertex]
        _____ queue:
            deVertex _ queue.p.. 0)
            print(deVertex)
            ___ adjacentVertex __ gdict[deVertex]:
                __ adjacentVertex n.. __ visited:
                    visited.a..(adjacentVertex)
                    queue.a..(adjacentVertex)
    
    ___ dfs vertex
        visited _ [vertex]
        stack _ [vertex]
        _____ stack:
            popVertex _ stack.p.. 
            print(popVertex)
            ___ adjacentVertex __ gdict[popVertex]:
                __ adjacentVertex n.. __ visited:
                    visited.a..(adjacentVertex)
                    stack.a..(adjacentVertex)
    



customDict _ { "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f", "c"],
            "f" : ["d", "e"]
               }



g _ Graph(customDict)
g.dfs("a")

