# c_ Node o..
#
#     ___ -  data
#         ? _ ?
#         leftChild _ N..
#         rightChild _ N..
#
#
# c_ BinarySearchTree o..
#
#     ___ -
#         root _ N..
#
#     ___ i..  data
#         __ n.. ?
#             ? _ ? ?
#         ____
#             ? ? ?
#
#     # O(logN)   if the tree is balanced !!!!!!!!!!!!!  --> it can reduced to O(N) --> AVL RBT are needed !!!!!
#     ___ insertNode data node
#
#         __ ? < ?.d..
#             __ ?.l..
#                 ? ? ?.l..
#             ____
#                 ?.l.. _ ? ?
#         ____
#             __ ?.r..
#                 ? ?  ?.r..
#             ____
#                 ?.r.. _ ? ?
#
#     # O(logN)
#     ___ removeNode data node
#
#         __ n.. ?
#             r_ ?
#
#         __ d.. < ?.d..
#             ?.l.. _ ? ? ?.l..
#         ____ d.. > ?.d..
#             ?.r.. _ ? ? ?.r..
#         ____
#
#             __ n.. ?.l.. ___ n.. ?.r..
#                 print("Removing a leaf node...")
#                 d.. n..
#                 r_ N..
#
#             __ n.. ?.l..  # node !!!
#                 print("Removing a node with single right child...")
#                 tempNode _ ?.r..
#                 d.. n..
#                 r_ ?
#             ____ n.. ?.r..  # node instead of self
#                 print("Removing a node with single left child...")
#                 tempNode _ ?.l..
#                 d.. n..
#                 r_ ?
#
#             print("Removing node with two children....")
#             tempNode _ g.. ?.l..  # self instead of elf  + get predecessor
#             ?.d.. _ ?.d..
#             ?.l.. _ ? ?.d.. ?.l..
#
#         r_ ?  # !!!!!!!!!!!!
#
#     ___ getPredecessor node
#
#         __ ?.r..
#             r_ ? ?.r..
#
#         r_ node
#
#     ___ remove data
#         __ root
#             r.. _ ? ? ?
#
#     # O(logN)
#     ___ getMinValue
#         __ root
#             r_ ? ?
#
#     ___ getMin node
#
#         __ ?.l..
#             r_ ? ?.l..
#
#         r_ ?.data
#
#     # O(logN)
#     ___ getMaxValue
#         __ root
#             r_ ? ?
#
#     ___ getMax node
#
#         __ ?.r..
#             r_ ? ?.r..
#
#         r_ ?.d..
#
#     ___ traverse
#         __ root
#             ? ?
#
#         # O(N)
#
#     ___ traverseInOrder node
#
#         __ ?.l..
#             ? ?.l..
#
#         print("_s " _ ?.d..
#
#         __ ?.r..
#             ? ?.r..
#
#
# bst _ BinarySearchTree()
# bst.i.. (10)
# bst.i.. (13)
# bst.i.. (5)
# bst.i.. (14)
# bst.remove(10)
#
# bst.traverse()
