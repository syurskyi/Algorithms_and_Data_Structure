#
#
# # Node class
#
#
# c_ Node:
#
#     ___ -  data
#         ? _ ?
#         p.. _ N..
#         n.. _ N..
#
#
# # Linked List class
# c_ LinkedList
#
#     ___ -
#         head _ N..
#
#     ___ createList arr
#         start _ ?
#         n _ l.. ?
#         # Declare newNode and temporary pointer
#         t.. _ ?
#         i _ 0
#
#         # Iterate the loop until array length
#         _____ ? < ?
#
#             # Create new node
#             newNode _ ? ? ?
#
#             __ ? __ 0
#                 s.. _ ?
#                 ?.p.. _ s..
#                 ? _ ?
#
#             ____
#                 ?.n.. _ ?
#                 ?.p.. _ ?
#                 ? _ ?.n..
#             i _ ? + 1
#         ? _ ?
#         r_ ?
#
#     ___ printList
#         t.. _ ?
#         linked_list _ ""
#         _____ ?
#             ? +_ s.. ?.d.. + " "
#             t.. _ ?.n..
#         print ?
#
#     # Function to count nunmber of
#     # elements in the list
#
#     ___ countList
#
#         # Declare temp pointer to
#         # traverse the list
#         t.. _ ?
#
#         # Variable to store the count
#         c.. _ 0
#
#         # Iterate the list and increment the count
#         _____ ? __ n.. N..
#             t.. _ ?.n..
#             c.. _ ? + 1
#
#         r_ ?
#
#     # we will consider that the index begin at 1
#     ___ deleteAtLocation index
#       t.. _ ?
#
#       c.. _ ?
#
#       __ ? < ?
#         r_ ?
#
#       __ ? __ 1
#         t.. _ ?.n..
#         h.. _ ?
#         r_ ?
#
#       __ ? __ ?
#         _____ ?.n.. __ n.. N.. ___ ?.n...n.. __ n.. N..
#           t.. _ ?.n..
#          # 1 => 2 => 3 => 4
#         ?.n.. _ N..
#         r_ ?
#
#
#       i _ 1
#       _____ ?<?-1
#         t.. _ ?.n..
#         ?+_1
#
#
#       prevNode _ t..
#       nodeAtTarget _ ?.n..
#       nextNode _ ?.n..
#
#       # 1 => 2 => 3 => 4
#
#       ?.p.. _ ?
#       ?.n.. _ ?
#
#       r_ ?
#
#
# # create an empty list
#
# arr _ [1, 2, 3, 4, 5]
# llist _ LinkedList()
#
# llist.createList(arr)
#
#
# llist.deleteAtLocation(2)
#
# # print(llist.head)
# llist.printList()
