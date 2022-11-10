# # Swap the first node and last node of a doubly linked list
#
# c_ Node
#     ___ - data
#         ? ?
#         next _ N...
#         previous _ N...
#
# c_ LinkedList
#     ___ -
#         head _ N...
#
#     ___ insertEnd newNode
#         __ head __ N...
#             h__ _ newNode
#             r_
#         currentNode _ h__
#         w__ ?.n.. __ no. N...
#             ? _ ?.n..
#         ?.n.. _ newNode
#         ?.p.. _ ?
#
#     ___ swapHead
#         __ h__ __ N...
#             print("Empty list")
#             r_
#         # List has just 1 Node
#         __ h__.n.. __ N...
#             r_
#         lastNode _ h__
#         w__ ?.n.. __ no. N...
#             ? _ ?.n..
#         currentHead _ h__
#         # Change previous pointer of head
#         h__.p.. _ ?.p..
#         # Change previous pointer of next node of head
#         h__.n__.p.. _ l..
#         # Change next pointer of last node
#         ?.n.. _ h__.n..
#         # Change next pointer of previous node of last node
#         ?.p__.n.. _ h__
#         # Change next pointer of head
#         h__.n.. _ N...
#         # Change previous pointer of last node
#         l___.p.. _ N...
#         # Make last node as head node
#         h__ _ l..
#
#
#     ___ printList
#         __ h__ __ N...
#             print("Empty list")
#             r_
#         currentNode _ h__
#         print("Printing from beginning")
#         w__ T..
#             print ?.d..
#             __ ?.n.. __ N...
#                 b..
#             ? _ ?.n..
#         print("Printing from end")
#         w__ T..
#             print ?.d..
#             __ ?.p.. __ N...
#                 b...
#             ? _ ?.p..
#
#
# nodeOne _ ?(10)
# nodeTwo _ ?(30)
# nodeThree _ ?(15)
# linkedList _ ?
# ?.insertEnd(nodeOne)
# ?.insertEnd(nodeTwo)
# ?.insertEnd(nodeThree)
# ?.swapHead()
# ?.printList()
