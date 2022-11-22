_______ numpy as np


c_ Graph:
    ___ -(self, vertices):
        _adjMat _ np.zeros((vertices, vertices))
        _vertices _ vertices
        _visited _ [0] * vertices

    ___ insert_edge(self, u, v, w_1):
        _adjMat[u][v] _ w

    ___ delete_edge(self, u, v):
        _adjMat[u][v] _ 0

    ___ get_edge(self, u, v):
        r_ _adjMat[u][v]

    ___ vertices_count
        r_ _vertices

    ___ edge_count
        count _ 0
        for i in range(_vertices):
            for j in range(_vertices):
                __ not _adjMat[i][j] __ 0:
                    count +_ 1
        r_ count

    ___ indegree(self, u):
        count _ 0
        for i in range(_vertices):
            __ not _adjMat[i][u] __ 0:
                count +_ 1
        r_ count

    ___ outdegree(self, u):
        count _ 0
        for i in range(_vertices):
            __ not _adjMat[u][i] __ 0:
                count +_ 1
        r_ count

    ___ display
        print(_adjMat)

    ___ DFS(self, source):
        __ _visited[source] __ 0:
            print(source, end_' - ')
            _visited[source] _ 1
            for j in range(_vertices):
                __ _adjMat[source][j] __ 1 and visited[j] __ 0:
                    DFS(j)


G _ Graph(7)
G.insert_edge(0, 1)
G.insert_edge(0, 5)
G.insert_edge(0, 6)
G.insert_edge(1, 0)
G.insert_edge(1, 2)
G.insert_edge(1, 5)
G.insert_edge(1, 6)
G.insert_edge(2, 3)
G.insert_edge(2, 4)
G.insert_edge(2, 6)
G.insert_edge(3, 4)
G.insert_edge(4, 2)
G.insert_edge(4, 5)
G.insert_edge(5, 2)
G.insert_edge(5, 3)
G.insert_edge(6, 3)
G.DFS(0)
