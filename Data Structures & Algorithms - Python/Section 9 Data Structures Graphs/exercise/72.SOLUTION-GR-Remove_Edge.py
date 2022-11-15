# c_ Graph:
#     ___  -
#         adj_list _  # dict
#
#     ___ print_graph
#         ___ v.. __ ?
#             print ? ':' ? ?
#
#     ___ add_vertex ? v..
#         __ ? n.. __ ?.k..
#             ? ?_  # list
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
#
#
#
# my_graph = ?
# ?.a..'A'
# ?.a..'B'
# ?.a..'C'
#
# ?.a..'A','B'
# ?.a..'B','C'
# ?.a..'C','A'
#
# print('Graph before remove_edge():')
# ?.p..
#
#
# ?.r.. 'A','C'
#
#
# print('\nGraph after remove_edge():')
# ?.p..
#
#
#
# """
#     EXPECTED OUTPUT:
#     ----------------
#     Graph before remove_edge():
#     A : ['B', 'C']
#     B : ['A', 'C']
#     C : ['B', 'A']
#
#     Graph after remove_edge():
#     A : ['B']
#     B : ['A', 'C']
#     C : ['B']
#
# """