# ____ pprint ______ pprint
#
#
# c_ Node o..
#
#     ___  -  data_N.. next_node_N..
#         ? _ ?
#         ? _ N..
#
#     ___ getData
#         r_  ?
#
#     ___ getNext
#         r_ ?
#
#     ___ setNext new_next
#         next_node _ ?
#
# c_ LinkedList o..
#     ___  -  head_N...
#         ? _ ?
#
#     ___ i..  data
#         new_node _ ? ?
#         ?.s.. ?
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
# l_ ?
#
# l.i.. ( 'a' )
# l.i.. ( 'b' )
# l.i.. ( 'c' )
#
#
# print l
# print(l.size())
#
