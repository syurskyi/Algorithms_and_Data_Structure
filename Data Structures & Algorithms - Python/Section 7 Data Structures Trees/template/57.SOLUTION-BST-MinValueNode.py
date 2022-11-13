# c_ Node
#     ___ -  v..
#         ? _ ?
#         l.. _ N..
#         r.. _ N..
#
#
# c_ BinarySearchTree
#     ___ -r.. _ N..
#         r.. _ N..
#
#     ___ insert  v..
#         n.. _ ? ?
#         __ ? __ N..
#             r.. __ ?
#             r.. T..
#         t.. _ ?
#         ____ T..
#             __ ?.v.. __ ?.v..
#                 r_ F..
#             __ ?.v.. < ?.v..
#                 __ ?.l.. __ N..
#                     ?.l.. _ ?
#                     r.. T..
#                 t.. _ ?.l..
#             ____
#                 __ ?.r.. __ N..
#                     ?.r.. _ ?
#                     r.. T..
#                 t.. _ ?.r..
#
#     ___ contains  v..
#         t.. _ ?
#         _____ ? __ n.. N..
#             __ v.. < ?.v..
#                 t.. _ ?.l..
#             ____ v.. > ?.v..
#                 t.. _ ?.r..
#             ____
#                 r.. T..
#         r_ F..
#
#     ___ min_value_node  current_node
#         _____ ?.l.. __ n.. N..
#             ? _ ?.l..
#         r_ ?
#
#
#
#
# my_tree = ?
# ?.i.. 47
# ?.i.. 21
# ?.i.. 76
# ?.i.. 18
# ?.i.. 27
# ?.i.. 52
# ?.i.. 82
#
#
# print('Minimum Value in Tree:')
# print( ?.m..(m__.r..).v.. )
#
#
#
# """
#     EXPECTED OUTPUT:
#     ----------------
#     Minimum Value in Tree:
#     18
#
# """