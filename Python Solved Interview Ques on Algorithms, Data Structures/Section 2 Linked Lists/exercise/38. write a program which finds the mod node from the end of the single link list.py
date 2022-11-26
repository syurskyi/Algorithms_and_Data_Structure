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
#     ___ modnodefromend  n
#             current_h..
#             modnode_N..
#
#             i_1
#             __ ? <_ 0
#                r_ N..
#
#             w__ ? !_ N..
#                   __ i%n __ 0
#                        modnode_current
#                   i_i+1
#                   current_current.n..
#
#             r_ ?
#
#
#
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
#         r_ ?
#
#
# l_ ?
#
# l.i.. ( '250' )
# l.i.. ( '200' )
# l.i.. ( '100' )
# l.i.. ( '25' )
# l.i.. ( '20' )
# l.i.. ( '10' )
# print l
# print(l.modnodefromend(3).data)
#
