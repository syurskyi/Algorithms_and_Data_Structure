# ____ pprint ______ pprint
#
#
# c_ Node o..
#
#     ___  -  data_N.. next_node_N..
#         ? _ ?
#         next_node _ N..
#
#     ___ get_data
#         r_  ?
#
#     ___ get_next
#         r_ ?
#
#     ___ set_next new_next
#         next_node _ ?
#
# c_ LinkedList o..
#     ___  -  head_N...
#         ? _ ?
#
#     ___ i..  data
#         new_node _ ? ?
#         ?.s.. h..
#         h.. _ ?
#
#     ___ insertatEnd item
#         current _ ?
#         __ ?
#             w__ ?.g.. !_ N..
#                 c.. _ ?.g..
#             ?.s.. ? ?
#         ____
#             h.. _ ? ?
#
#
#     ___ size
#         current _ ?
#         count _ 0
#         w__ ?
#           ? +_ 1
#           c.. _ ?.g..
#         r_ ?
#
#
#     ___ search data
#         current _ ?
#         found _ F...
#         w__ ? a__ ? __ F...
#             __ ?.g.. __ ?
#                 f.. _ T..
#             ____
#                 c.. _ ?.g..
#         __ c.. __ N..
#             r_ V..("Data not in list")
#         r_ ?
#
#
#     ___ delete data
#         current _ ?
#         previous _ N..
#         found _ F...
#         w__ ? a__ ? __ F...
#             __ ?.g.. __ ?
#                 f.. _ T..
#             ____
#                 p.. _ ?
#                 c.. _ ?.g..
#         __ c.. __ N..
#             r_ V..("Data not in list")
#         __ ? __ N..
#             h.. _ ?.g..
#         ____
#             p__.s.. ?.g..
#
#
#
#     ___ deleteNode  position
#
#              # If linked list is empty
#              __ head __ N..
#                  r_
#
#              # Store head node
#              t.. _ ?
#
#              # If head needs to be removed
#              __ ? __ 0
#                  head _ ?.n...
#                  t.. _ N..
#                  r_
#
#              # Find previous node of the node to be deleted
#              ___ i __ r.. ? -1
#                  t.. _ ?.n...
#                  __ ? __ N..
#                      b..
#
#              # If position is more than number of nodes
#              __ ? __ N..
#                  r_
#              __ ?.n... __ N..
#                  r_
#
#              # Node temp.next is the node to be deleted
#              # store pointer to the next of node to be deleted
#              next _ ?.n....n...
#
#              # Unlink the node from linked list
#              ?.n... _ N..
#
#              ?.n... _ ?
#
#     ___ -s
#         s _ ""
#         p _ head
#         __ ? !_ N..
#                 w__ ?.n... !_ N..
#                         s +_ ?.d..
#                         p _ ?.n...
#                 ? +_ ?.d..
#         r_ ?
#
#
# l_ ?
#
# l.i.. ( 'a' )
# l.i.. ( 'b' )
# l.i.. ( 'c' )
#
# print l
#
# l.deleteNode(2)
# print l
# l.deleteNode(1)
# print l
# l.deleteNode(0)
# print l
