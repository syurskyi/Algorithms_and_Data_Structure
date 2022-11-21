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
#     ___ makeCycle
#         current _ ?
#         __ ?
#             w__ ?.g.. !_ N..
#                 c.. _ ?.g..
#             ?.next_node_head.next_node
#
#     ___ detectCycle
#          first_head
#          second_head
#
#          loopLength _ 0
#          w__(first a__ second
#            first_first.g..
#            __ (first  __ second
#               r_ first
#
#            __ first __ N..
#               r_ N..
#
#            first _ first.g..
#            __ (first __ second
#               r_ first
#
#            second _ second.g..
#
#
#     ___ findLoopLength
#           first_detectCycle()
#           print "first.data:",first.data
#           loopLength _ 0
#           second_first.next_node
#           w__(first !_ second
#             second _ second.next_node
#             loopLength _ loopLength + 1
#
#           print loopLength
#
#
#     ___ size
#         current _ ?
#         count _ 0
#         w__ ?
#           ? +_ 1
#           c.. _ ?.g..
#         r_ count
#
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
#
# print l
# l.makeCycle()
# l.findLoopLength()
