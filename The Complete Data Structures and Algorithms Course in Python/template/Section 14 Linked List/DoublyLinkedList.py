# #   Created by Elshad Karimov on 05/05/2020.
# #   Copyright © 2020 AppMillers. All rights reserved.
#
# c_ Node
#     ___ -  value_N..
#         ? _ ?
#         n.. _ N..
#         p.. _ N..
#
# c_ DoublyLinkedList
#     ___ -
#         h.. _ N..
#         t.. _ N..
#
#
#     ___ -i..
#         node _ ?
#         _____ ?
#             y.. ?
#             n.. _ ?.n..
#
#     #  Creation of Doubly Linked List
#     ___ createDLL nodeValue
#         node _ ? ?
#         ?.p.. _ N..
#         ?.n.. _ N..
#         h.. _ ?
#         t.. _ ?
#         r_ "The DLL is created Successfully"
#
#
#
#     #  Insertion Method in Doubly Linked List
#     ___ insertNode nodeValue, location
#         __ h.. __ N..
#             print("The node cannot be inserted")
#         ____
#             newNode _ ? ?
#             __ l.. __ 0
#                 ?.p.. _ N..
#                 ?.n.. _ ?
#                 ?.p.. _ ?
#                 h.. _ ?
#             ____ l.. __ 1
#                 ?.n.. _ N..
#                 ?.p.. _ t..
#                 ?.n.. _ ?
#                 t.. _ ?
#             ____
#                 tempNode _ ?
#                 ? _ 0
#                 _____ ? < l.. - 1
#                     t.. _ ?.n..
#                     ? +_
#                 ?.n.. _ ?.n..
#                 ?.p.. _ ?
#                 ?.n...p.. _ ?
#                 ?.n.. _ ?
#
#     #  Traversal Method in Doubly Linked List
#     ___ traverseDLL
#         __ h.. __ N..
#             print("There is not any element to traverse")
#         ____
#             tempNode _ ?
#             _____ ?
#                 print ?.v..
#                 t.. _ ?.n..
#
#     #  Reverse Traversal Method in Doubly Linked List
#     ___ reverseTraversalDLL
#         __ h.. __ N..
#             print("There is not any element to traverse")
#         ____
#             tempNode _ t..
#             _____ ?
#                 print ?.v..
#                 t.. _ ?.p..
#
#     # Search Method in Doubly Linked List
#     ___ searchDLL nodeValue
#         __ h.. __ N..
#             r_ "There is not any element in the list"
#         ____
#             tempNode _ ?
#             _____ ?
#                 __ ?.v.. __ n..
#                     r_ ?.v..
#                 t.. _ ?.n..
#             r_ "The node does not exist in this list"
#
#     # Delete a node from Doubly Linked List
#     ___ deleteNodelocation
#         __ h.. __ N..
#             print("There is not any element in DLL")
#         ____
#             __ l.. __ 0
#                 __ ? __ t..
#                     h.. _ N..
#                     t.. _ N..
#                 ____
#                     h.. _ ?.n..
#                     ?.p.. _ N..
#             ____ l.. __ 1
#                 __ ? __ t..
#                     h.. _ N..
#                     t.. _ N..
#                 ____
#                     t.. _ ?.p..
#                     ?.n.. _ N..
#             ____
#                 curNode _ ?
#                 ? _ 0
#                 _____ ? < l.. - 1
#                     c.. _ ?.n..
#                     ? +_
#                 ?.n.. _ ?.n...n..
#                 ?.n...p.. _ ?
#             print("The node has been successfully deleted")
#
#     # Delete entire Doubly Linked List
#     ___ deleteDLL
#         __ h.. __ N..
#             print("There is not any node in DLL")
#         ____
#             tempNode _ ?
#             _____ ?
#                 ?.p.. _ N..
#                 t.. _ ?.n..
#             h.. _ N..
#             t.. _ N..
#             print("The DLL has been successfully deleted")
#
#
#
# doubyLL _ DoublyLinkedList()
# doubyLL.createDLL(5)
# doubyLL.insertNode(0,0)
# doubyLL.insertNode(2,1)
# doubyLL.insertNode(6,2)
# print([node.value ___ node __ doubyLL])
# doubyLL.deleteDLL()
# print([node.value ___ node __ doubyLL])
#
#
#
