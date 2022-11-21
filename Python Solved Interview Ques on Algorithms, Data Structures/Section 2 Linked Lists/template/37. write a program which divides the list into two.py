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
#
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
#     ___ size
#         current _ ?
#         count _ 0
#         w__ ?
#           ? +_ 1
#           c.. _ ?.g..
#         r_ ?
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
#
# ___ divideListInto2 list1
#   first_?
#   second_?
#   w__ ? !_ N.. a__ ?.n.. !_ N..
#     second_second.n..
#     first_first.n..
#     first_first.n..
#
#   third _second.n..
#   ?.next_node_N..
#   r_ ? ?
#
# ___ displayList list1
#   temp_?
#   w__ ?
#     print ?.d..
#     temp_temp.n..
#
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
# l1,l2_divideListInto2(l.head)
# print "List1:"
# displayList(l1)
# print "List2:"
# displayList(l2)
# print "#####"
