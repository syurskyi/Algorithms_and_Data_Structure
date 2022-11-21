# c_ Node:
#     ___ -  data
#         ? _ ?
#         p.. _ N..
#         n.. _ N..
#
#
# c_ LinkedList
#     ___ -
#         head _ N..
#
#     ___ createList arr
#         start _ ?
#         n _ l.. ?
#
#         t.. _ ?
#         i _ 0
#
#         _____ ? < ?
#             newNode _ ? ? ?
#             __ ? __ 0
#                 s.. _ ?
#                 ? _ ?
#             ____
#                 ?.n.. _ ?
#                 ?.p.. _ ?
#                 t.. _ ?.n..
#             ? +_ 1
#         h.. _ s..
#         r_ ?
#
#     ___ printList
#         t.. _ ?
#         linked_list _ ""
#         _____ ?
#             ? +_ s.. ?.d.. + " "
#             t.. _ ?.n..
#
#         print ?
#
#     ___ countList
#         t.. _ ?
#         c.. _ 0
#         _____ ? __ n.. N..
#             t.. _ ?.n..
#             ? +_ 1
#         r_ ?
#
#     # we will consider that the index begin at 1
#     ___ insertAtLocation value, index
#         t.. _ ?
#
#         c.. _ ?
#
#         #index is 6, count is 5, valid
#         #index is 7, count is 5,
#         __ ?+1<?
#             r_ ?
#
#         newNode _ ? ?
#
#         __ ? __ 1
#             ?.n.. _ t..
#             ?.p.. _ ?
#             h.. _ ?
#             r_ ?
#
#         __ ? __ ? +1
#             _____ ?.n.. __ n.. N..
#                 t.. _ ?.n..
#
#             ?.n.. _ ?
#             ?.p.. _ ?
#             r_ ?
#
#         i _ 1
#         _____ ? < ?-1
#             t.. _ ?.n..
#             ?+_1
#
#         nodeAtTarget _ ?.n..
#
#         ?.n.. _ ?
#         ?.p.. _ ?
#
#         ?.n.. _ ?
#         ?.p.. _ ?
#
#         r_ head
#
#
# arr _ [1, 2, 3, 4, 5]
#
# llist _ LinkedList()
#
# llist.createList(arr)
#
# llist.insertAtLocation(5,6)
#
# llist.printList()
