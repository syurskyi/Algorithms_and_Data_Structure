#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

# Prims Algorithm  in Python
import sys
c_ Graph:
    ___ -  vertexNum, edges, nodes
        edges _ edges
        nodes _ nodes
        vertexNum _ vertexNum
        MST _    # list
    
    ___ printSolution 
        print("Edge : Weight")
        ___ s, d, w __ MST:
            print("%s -> %s: %s" % (s, d, w))
    
    ___ primsAlgo 
        visited _ [0]*vertexNum
        edgeNum_0
        visited[0]_True
        _____ edgeNum<vertexNum-1:
            min _ sys.maxsize
            ___ i __ range(vertexNum
                __ visited[i]:
                    ___ j __ range(vertexNum
                        __ ((n.. visited[j]) and edges[i][j]
                            __ min > edges[i][j]:
                                min _ edges[i][j]
                                s _ i
                                d _ j
            MST.a..([nodes[s], nodes[d], edges[s][d]])
            visited[d] _ True
            edgeNum +_ 1
        printSolution()



edges _ [[0, 10, 20, 0, 0],
		[10, 0, 30, 5, 0],
		[20, 30, 0, 15, 6],
		[0, 5, 15, 0, 8],
		[0, 0, 6, 8, 0]]
nodes _ ["A","B","C","D","E"]
g _ Graph(5, edges, nodes)
g.primsAlgo()
