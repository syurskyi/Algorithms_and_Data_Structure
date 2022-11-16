#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

# Disjoint Set in Python

c_ DisjointSet:
    ___ -  vertices
        vertices _ vertices
        parent _ {}
        ___ v __ vertices:
            parent[v] _ v
        rank _ dict.fromkeys(vertices, 0)
    
    ___ find item
        __ parent[item] __ item:
            r_ item
        ____
            r_ find(parent[item])
    
    ___ union x, y
        xroot _ find(x)
        yroot _ find(y)
        __ rank[xroot] < rank[yroot]:
            parent[xroot] _ yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] _ xroot
        ____
            parent[yroot] _ xroot
            rank[xroot] +_ 1

# vertices = ["A", "B", "C", "D", "E"]

# ds = DisjointSet(vertices)
# ds.union("A", "B")
# ds.union("A", "C")
# print(ds.find("A"))