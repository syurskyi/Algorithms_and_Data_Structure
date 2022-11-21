# #   Created by Elshad Karimov on 01/05/2020.
# #   Copyright © 2020 AppMillers. All rights reserved.
#
# c_ Node:
#     ___ -  value_N..
#         ? _ ?
#         n.. _ N..
#
# c_ CircularSinglyLinkedList
#     ___ -
#         h.. _ N..
#         t.. _ N..
#
#     ___ -i..
#         node _ ?
#         _____ ?
#             y.. ?
#             node _ ?.n..
#             __ ? __ t__.n..
#                 b..
#
#
#     #  Creation of circular singly linked list
#     ___ createCSLL nodeValue
#         node _ ? ?
#         ?.n.. _ ?
#         h.. _ ?
#         t.. _ ?
#         r_ "The CSLL has been created"
#
#     #  Insertion of a node in circular singly linked list
#
#     ___ insertCSLL value, location
#         __ h.. __ N..
#             r_ "The head reference is None"
#         ____
#             newNode _ ? ?
#             __ l.. __ 0
#                 ?.n.. _ ?
#                 h.. _ ?
#                 ?.n.. _ ?
#             ____ l.. __ 1
#                 ?.n.. _ t__.n..
#                 ?.n.. _ ?
#                 t.. _ ?
#             ____
#                 tempNode _ ?
#                 ? _ 0
#                 _____ ? < l.. - 1
#                     t.. _ ?.n..
#                     ? +_
#                 nextNode _ ?.n..
#                 ?.n.. _ ?
#                 ?.n.. _ ?
#             r_ "The node has been successfully inserted"
#
#     # Traversal of a node in circular singly linked list
#     ___ traversalCSLL
#         __ h.. __ N..
#             print("There is not any element for traversal")
#         ____
#             tempNode _ ?
#             _____ ?
#                 print ?.v..
#                 t.. _ ?.n..
#                 __ ? __ ?.n..
#                     b..
#
#     # Searching for a node in circular singly linked list
#     ___ searchCSLL nodeValue
#         __ h.. __ N..
#             r_ "There is not any node in this CSLL"
#         ____
#             tempNode _ ?
#             _____ ?
#                 __ ?.v.. __ n..
#                     r_ ?.v..
#                 t.. _ ?.n..
#                 __ ? __ ?.n..
#                     r_ "The node does not exist in this CSLL"
#
#     # Delete  a node from circular singly linked list
#     ___ deleteNode location
#         __ h.. __ N..
#             print("There is not any node in CSLL")
#         ____
#             __ l.. __ 0
#                 __ ? __ t..
#                     ?.n.. _ N..
#                     h.. _ N..
#                     t.. _ N..
#                 ____
#                     h.. _ ?.n..
#                     ?.n.. _ h..
#             ____ l.. __ 1
#                 __ ? __ t..
#                     ?.n.. _ N..
#                     h.. _ N..
#                     t.. _ N..
#                 ____
#                     node _ ?
#                     _____ ? __ n.. N..
#                         __ ?.n.. __ t..
#                             b..
#                         node _ ?.n..
#                     ?.n.. _ ?
#                     t.. _ ?
#             ____
#                 tempNode _ ?
#                 ? _ 0
#                 _____ ? < l.. - 1
#                     t.. _ ?.n..
#                     ? +_
#                 nextNode _ ?.n..
#                 ?.n.. _?.n..
#
#     # Delete entire circular sinlgy linked list
#     ___ deleteEntireCSLL
#         h.. _ N..
#         ?.n.. _ N..
#         t.. _ N..
#
#
#
# circularSLL _ CircularSinglyLinkedList()
# circularSLL.createCSLL(0)
# circularSLL.insertCSLL(1,1)
# circularSLL.insertCSLL(2,1)
# circularSLL.insertCSLL(3,1)
#
# print([node.value ___ node __ circularSLL])
# circularSLL.deleteEntireCSLL()
# print([node.value ___ node __ circularSLL])
#
#
#
#
#
#
#
#
#
#
#
#
