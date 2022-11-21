# #   Created by Elshad Karimov on 12/05/2020.
# #   Copyright © 2020 AppMillers. All rights reserved.
#
# c_ Node
#     ___ -  value_N..
#         ? _ ?
#         n.. _ N..
#         p.. _ N..
#
# c_ CircularDoublyLinkedList
#     ___ -
#         h.. _ N..
#         t.. _ N..
#
#
#     ___ -i..
#         node _ ?
#         _____ ?
#             y.. ?
#             node _ ?.n..
#             __ ? __ t__.n..
#                 b..
#
#     #  Creation of Circular Doubly Linked List
#     ___ createCDLL nodeValue
#         newNode _ ? ?
#         h.. _ ?
#         t.. _ ?
#         ?.p.. _ ?
#         ?.n.. _ ?
#         r_ "The CDLL is created successfully"
#
#
#     # Insertion Method in Circular Doubly Linked List
#     ___ insertCDLL value location
#         __ h.. __ N..
#             r_ "The CDLL does not exist"
#         ____
#             newNode _ ? ?
#             __ l.. __ 0
#                 ?.n.. _ ?
#                 ?.p.. _ t..
#                 ?.p.. _ ?
#                 h.. _ ?
#                 ?.n.. _ ?
#             ____ l.. __ 1
#                 ?.n.. _ ?
#                 ?.p.. _ t..
#                 ?.p.. _ ?
#                 ?.n.. _ ?
#                 t.. _ ?
#             ____
#                 tempNode _ ?
#                 ? _ 0
#                 _____ ? < l.. - 1
#                     t.. _ ?.n..
#                     ? +_
#                 ?.n.. _ ?.n..
#                 ?.p.. _ t..
#                 ?.n...p.. _ ?
#                 ?.n.. _ ?
#             r_ "The node has been successfully inserted"
#
#     # Traversal of Circular Doubly Linked List
#     ___ traversalCDLL
#         __ h.. __ N..
#             print("There is not any node for traversal")
#         ____
#             tempNode _ ?
#             _____ ?
#                 print ?.v..
#                 __ ? __ t..
#                     b..
#                 t.. _ ?.n..
#
#     # Reverse traversal of Circular Doubly Linked List
#     ___ reverseTraversalCDLL
#         __ h.. __ N..
#             print("There is not any node for reverse traversal")
#         ____
#             tempNode _ t..
#             _____ ?
#                 print ?.v..
#                 __ ? __ h..
#                     b..
#                 t.. _ ?.p..
#
#     # Search Circular Doubly Linked List
#     ___ searchCDLL nodeValue
#         __ h.. __ N..
#             r_ "There is not any node in CDLL"
#         ____
#             tempNode _ ?
#             _____ ?
#                 __ ?.v.. __ n..
#                     r_ ?.v..
#                 __ ? __ t..
#                     r_ "The value does not exist in CDLL"
#                 t.. _ ?.n..
#
#     # Delete a node from Circular Doubly Linked List
#     ___ deleteNode location
#         __ h.. __ N..
#             print("There is not any node to delete")
#         ____
#             __ l.. __ 0
#                 __ ? __ t..
#                     ?.p.. _ N..
#                     ?.n.. _ N..
#                     h.. _ N..
#                     t.. _ N..
#                 ____
#                     h.. _ ?.n..
#                     ?.p.. _ t..
#                     ?.n.. _ h..
#             ____ l.. __ 1
#                 __ ? __ t..
#                     ?.p.. _ N..
#                     ?.n.. _ N..
#                     h.. _ N..
#                     t.. _ N..
#                 ____
#                     t.. _ ?.p..
#                     ?.n.. _ h..
#                     ?.p.. _ t..
#             ____
#                 curNode _ ?
#                 ? _ 0
#                 _____ ? < l.. - 1
#                     c.. _ ?.n..
#                     ? +_
#                 ?.n.. _ ?.n...n..
#                 ?.n...p.. _ c..
#             print("The node has been successfully deleted")
#
#     # Delete entire Circular Doubly Linked List
#     ___ deleteCDLL
#         __ h.. __ N..
#             print("There is not any element to delete")
#         ____
#             ?.n.. _ N..
#             tempNode _ ?
#             _____ ?
#                 ?.p.. _ N..
#                 t.. _ ?.n..
#             h.. _ N..
#             t.. _ N..
#             print("The CDLL has been successfully deleted")
#
#
#
# circularDLL _ CircularDoublyLinkedList()
# circularDLL.createCDLL(5)
# circularDLL.insertCDLL(0,0)
# circularDLL.insertCDLL(1,1)
# circularDLL.insertCDLL(2,2)
# print([node.value ___ node __ circularDLL])
# circularDLL.deleteCDLL()
# print([node.value ___ node __ circularDLL])
#
#
#
#
#
