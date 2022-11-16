# c_ Graph
#     ___  -
#         adj_list _  # dict
#
#     ___ print_graph
#         ___ v.. __ ?
#             print ? ':' ? ?
#
#     ___ add_vertex v..
#         __ ? n.. __ ?.k..
#             ? ?_  # lsit
#             r_ T..
#         r_ F..
#
#     ___ add_edge  v1, v2
#         __ ? __ ?.k.. ___ ? __ ?.k..
#             ? ?.a.. ?
#             ? ?.a.. ?
#             r_ T..
#         r_ F..
#
#     ___ remove_edge  v1, v2
#         __ ? __ ?.k.. ___ ? __ ?.k..
#             ___
#                 ? ?.r.. ?
#                 ? ?.r.. ?
#             e.. V..
#                 p..
#             r_ T..
#         r_ F..
#
#     ___ remove_vertex ? v..
#         __ v.. __ ?.k..
#             ___ ? __ ? ?
#                 ? ?.r.. ?
#             d__ ? ?
#             r_ T..
#         r_ F..
#
#
#
#
# my_graph = ?
# ?.a..'A'
# ?.a..'B'
# ?.a..'C'
# ?.a..'D'
#
# ?.a..'A','B'
# ?.a..'A','C'
# ?.a..'A','D'
# ?.a..'B','D'
# ?.a..'C','D'
#
#
# print('Graph before remove_vertex():')
# ?.p..
#
#
# ?.r.. 'D'
#
#
# print('\nGraph after remove_vertex():')
# ?.p..
#
#
#
# """
# EXPECTED OUTPUT:
# ----------------
#     Graph before remove_vertex():
#     A : ['B', 'C', 'D']
#     B : ['A', 'D']
#     C : ['A', 'D']
#     D : ['A', 'B', 'C']
#
#     Graph after remove_vertex():
#     A : ['B', 'C']
#     B : ['A']
#     C : ['A']
#
# """