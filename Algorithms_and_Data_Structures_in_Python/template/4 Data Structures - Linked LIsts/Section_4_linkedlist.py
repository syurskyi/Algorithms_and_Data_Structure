# c_ Node o..
#
#     ___ -  data
#         ? _ ?
#         nextNode _ N..
#
#
# c_ LinkedList o..
#
#     ___ -
#         head _ N..
#         size _ 0
#
#     # O(1) !!!
#     ___ insertStart data
#
#         s.. _ s.. + 1
#         newNode _ ? ?
#
#         __ n.. ?
#             ? _ ?
#         ____
#             ?.n.. _ ?
#             ? _ ?
#
#     ___ remove data
#
#         __ ? __ N..
#             r_
#
#         ? _ ? - 1
#
#         currentNode _ ?
#         previousNode _ N..
#
#         _____ ?.d.. !_ d..
#             p.. _ ?
#             c.. _ ?.n..
#
#         __ p.. __ N..
#             h.. _ ?.n..
#         ____
#             p__.n.. _ ?.n..
#
#     # O(1)
#     ___ size1
#         r_ ?
#
#     # O(N) not good !!!
#     ___ size2
#
#         actualNode _ ?
#         s.. _ 0
#
#         _____ ? __ n.. N..
#             ? +_ 1
#             a.. _ ?.n..
#
#         r_ ?
#
#     # O(N)
#     ___ insertEnd data
#
#         s.. _ ? + 1
#         newNode _ ? ?
#         actualNode _ ?
#
#         _____ ?.n.. __ n.. N..
#             a.. _ ?.n..
#
#         ?.n.. _ ?
#
#     ___ traverseList
#
#         actualNode _ ?
#
#         _____ ? __ n.. N..
#             print "_d " _ ?.d..
#             a.. _ ?.n..
#
#
# linkedlist _ LinkedList()
#
# linkedlist.insertStart(12)
# linkedlist.insertStart(122)
# linkedlist.insertStart(3)
# linkedlist.insertEnd(31)
#
# linkedlist.traverseList()
#
# linkedlist.remove(3)
# linkedlist.remove(12)
# linkedlist.remove(122)
# linkedlist.remove(31)
#
# print(linkedlist.size1())
