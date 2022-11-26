# _______ numpy as np
#
#
# c_ Graph
#     ___ -  vertices
#         _adjMat _ ?.z.. ? ?
#         _? _ ?
#
#     ___ insert_edge  u v w_1
#         ? ? ? _ ?
#
#     ___ delete_edge  u v
#         ? ? ? _ 0
#
#     ___ get_edge  u v
#         r_ ? ? ?
#
#     ___ vertices_count
#         r_ ?
#
#     ___ edge_count
#         count _ 0
#         ___ i __ r.. ?
#             ___ j __ r.. ?
#                 __ n.. ? ? ? __ 0
#                     ? +_ 1
#         r_ ?
#
#     ___ indegree  u
#         count _ 0
#         ___ i __ r.. ?
#             __ n.. ? ? ? __ 0
#                 ? +_ 1
#         r_ ?
#
#     ___ outdegree  u
#         count _ 0
#         ___ i __ r.. ?
#             __ n.. ? ? ? __ 0
#                 ? +_ 1
#         r_ ?
#
#     ___ display
#         print ?
#
#
# G _ Graph(7)
# print('Graph Adjacency Matrix')
# G.display()
# G.insert_edge(0, 1)
# G.insert_edge(0, 5)
# G.insert_edge(0, 6)
# G.insert_edge(1, 0)
# G.insert_edge(1, 2)
# G.insert_edge(1, 5)
# G.insert_edge(1, 6)
# G.insert_edge(2, 3)
# G.insert_edge(2, 4)
# G.insert_edge(2, 6)
# G.insert_edge(3, 4)
# G.insert_edge(4, 2)
# G.insert_edge(4, 5)
# G.insert_edge(5, 2)
# G.insert_edge(5, 3)
# G.insert_edge(6, 3)
# print('Graph Adjacency Matrix')
# G.display()
# print('Number of Vertices:', G.vertices_count())
# print('Number of Edges: ',  G.edge_count())
# print('Outdegree of Vertex 2: ', G.outdegree(2))
