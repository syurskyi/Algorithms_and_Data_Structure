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
#     ___ frNode  n
#         fNode_None
#         current_head
#
#         i _ 0
#         __ ? <_ 0
#            r_ N..
#
#         w__ ? !_ N..
#             __ i%n __ 0
#                 __ f.. __ N..
#                    f.. _ h..
#                 ____
#                    f.. _ ?.n..
#             i _ ? + 1
#             current_current.n..
#
#         print ?.d..
#
#
#     ___ -s
#         s _ ""
#         p _ head
#         __ ? !_ N..
#                 w__ ?.n... !_ N.. :
#                         ? +_ ?.d..
#                         p _ ?.n...
#                 ? +_ ?.d..
#         r_ s
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
# print l
# l.frNode(3)
#
#
