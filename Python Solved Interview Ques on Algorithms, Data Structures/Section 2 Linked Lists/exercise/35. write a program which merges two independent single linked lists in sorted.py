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
# ___ joinListsInSortedOrder l1, l2
#   thirdList_Node()
#   parse_thirdList
#   tempo_thirdList
#
#   w__ l1 !_ N.. a__ l2 !_ N..
#     __ ?.d.. < ?.d..
#       tempo.next_node_l1
#       l1_l1.next_node
#     ____
#       tempo.next_node_l2
#       l2_l2.next_node
#     tempo_tempo.next_node
#
#   __ l1 __ N..
#      tempo.next_node_l2
#
#   __ l2 __ N..
#      tempo.next_node_l1
#
#   w__ thirdList:
#      __ thirdList.data:
#        print thirdList.data
#      thirdList_thirdList.next_node
#
#
# l1 _ LinkedList()
# l2 _ LinkedList()
#
# ?.i.. ( '3' )
# ?.i.. ( '2' )
# ?.i.. ( '1' )
# print "list1:", l1
# ?.i.. ( '6' )
# ?.i.. ( '5' )
# ?.i.. ( '4' )
# print "list2:", l2
#
# joinListsInSortedOrder(?.head, ?.head)
#
