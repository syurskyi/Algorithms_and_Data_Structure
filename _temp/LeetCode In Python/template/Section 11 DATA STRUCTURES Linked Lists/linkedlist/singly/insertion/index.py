# c_ Node:
#
#     ___ -  data
#         ? _ ?
#         n.. _ N..
#
#
# c_ LinkedList
#
#     ___ -
#         head _ N..
#
#     ___ printList
#         t.. _ ?
#         linked_list _ ""
#         _____ ?
#             ? +_ s.. ?.d.. + " "
#             t.. _ ?.n..
#         print ?
#
#     # list start at 0
#     ___ insertNode val, pos
#         target _ ? ?
#         __ ? __ 0
#             ?.n.. _ ?
#             ? _ ?
#             r_
#
#         ___ getPrev pos
#             t.. _ ?
#             c.. _ 1
#             _____ ? < ?
#                 t.. _ ?.n..
#                 ? +_ 1
#             r_ ?
#
#         prev _ ? ?
#         nextNode _ ?.n..
#
#         ?.n.. _ ?
#         ?.n.. _ ?
#
#
# # List Structure : 5 => 1 => 3 => 7
# linked_list _ LinkedList()
# linked_list.head _ Node(5)
#
# second_node _ Node(1)
# third_node _ Node(3)
# fourth_node _ Node(7)
#
# linked_list.head.n.. _ second_node
# second_node.n.. _ third_node
# third_node.n.. _ fourth_node
#
# linked_list.insertNode(2, 2)
# linked_list.printList()
