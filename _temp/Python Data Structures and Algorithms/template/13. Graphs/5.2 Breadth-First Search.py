____ ? _______ ?
_______ numpy as np


c_ Graph:
    ___ -  vertices):
        _adjMat _ np.zeros((vertices, vertices))
        _vertices _ vertices

    ___ insert_edge  u, v, w_1):
        _adjMat[u][v] _ w

    ___ delete_edge  u, v):
        _adjMat[u][v] _ 0

    ___ get_edge  u, v):
        r_ _adjMat[u][v]

    ___ vertices_count
        r_ _vertices

    ___ edge_count
        count _ 0
        for i in range(_vertices):
            for j in range(_vertices):
                __ n.. _adjMat[i][j] __ 0:
                    count +_ 1
        r_ count

    ___ indegree  u):
        count _ 0
        for i in range(_vertices):
            __ n.. _adjMat[i][u] __ 0:
                count +_ 1
        r_ count

    ___ outdegree  u):
        count _ 0 ;
        for i in range(_vertices):
            __ n.. _adjMat[u][i] __ 0:
                count +_ 1
        r_ count

    ___ display
        print(_adjMat)

    ___ BFS  source):
        i _ source
        q _ LinkedQueue()
        visited _ [0] * _vertices
        print(i, e.._' - ')
        visited[i] _ 1
        q.enqueue(i)
        _____ n.. q.is_empty():
            i _ q. dequeue()
            for j in range(_vertices):
                __ _adjMat[i][j] __ 1 and visited[j] __ 0:
                    print(j, e.._' - ')
                    visited[j] _ 1
                    q.enqueue(j)


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
G.BFS(0)