#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

# Floyd Warshall Algorithm in python

INF _ 9999
# Printing the solution
___ printSolution(nV, distance
    ___ i __ range(nV
        ___ j __ range(nV
            __(distance[i][j] == INF
                print("INF", end_" ")
            ____
                print(distance[i][j], end_"  ")
        print(" ")


___ floydWarshall(nV, G
    distance _ G
    ___ k __ range(nV
        ___ i __ range(nV
            ___ j __ range(nV
                distance[i][j] _ min(distance[i][j], distance[i][k]+distance[k][j])
    
    printSolution(nV, distance)

G _ [[0, 8, INF,1],
    [INF, 0, 1,INF],
    [4, INF, 0,INF],
    [INF, 2, 9,1]
    ]

floydWarshall(4, G)

