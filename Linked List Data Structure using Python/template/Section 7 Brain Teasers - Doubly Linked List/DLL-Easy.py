# # Delete a node with the given data in a doubly linked list
#
# c_ Node
#     ___ - data
#         ? ?
#         next _ N..
#         previous _ N..
#
# c_ LinkedList
#     ___ -
#         head _ N..
#
#     ___ insertEnd newNode
#         __ h.. __ N..
#             h.. _ ?
#             r_
#         currentNode _ h..
#         w__ ?.n.. __ no. N..
#             ? _ ?.n..
#         ?.n.. _ newNode
#         ?.p.. _ ?
#
#     ___ deleteNode data
#         currentNode _ h..
#         w__ ? __ not N..
#             __ ?.d.. __ d..
#                 # h.. node deletion
#                 __ ? __ h..
#                     h.. _ ?.n..
#                     ?.n.. _ N..
#                     __ h.. __ no. N..
#                         h...p.. _ N..
#                     r_
#                 # last node deletion
#                 __ ?.n.. __ N..
#                     ?.p...n.. _ N..
#                     ?.p.. _ N..
#                     r_
#                 # node in between two nodes
#                 ?.n...p.. _ ?.p..
#                 ?.p...n.. _ ?.n..
#                 ?.n.. _ N..
#                 ?.p.. _ N..
#                 r_
#             ? _ ?.n..
#         print("Data not found")
#
#     ___ printList
#         __ h.. __ N..
#             print("Empty list")
#             r_
#         currentNode _ h..
#         w__ ? __ not N..
#             print ?.d..
#             ? _ ?.n..
#
# nodeOne _ ?(10)
# nodeTwo _ ?(30)
# nodeThree _ ?(15)
# linkedList _ ?
# ?.insertEnd(nodeOne)
# ?.insertEnd(nodeTwo)
# ?.insertEnd(nodeThree)
# ?.deleteNode(30)
# ?.printList()
