# ____ pprint ______ pprint
#
#
# c_ Node o..
#
#     ___  -  data_N.. next_node_N..
#         ? _ ?
#         ? _ N..
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
#     ___ -s
#         s _ ""
#         p _ head
#         __ ? !_ N..
#                 w__ ?.n... !_ N..
#                         ? +_ ?.d..
#                         p _ ?.n...
#                 ? +_ ?.d..
#         r_ s
#
# ___ displayListFromTail list1
#    __ ? __ N..
#       r_
#
#    head_?
#    end_list1.n..
#    displayListFromTail(end)
#    print head.data
#
# l_ ?
#
# l.i.. ( 'a' )
# l.i.. ( 'b' )
# l.i.. ( 'c' )
# l.i.. ( 'd' )
# l.i.. ( 'e' )
# l.i.. ( 'f' )
# l.i.. ( 'g' )
# print l
# displayListFromTail(l.head)
