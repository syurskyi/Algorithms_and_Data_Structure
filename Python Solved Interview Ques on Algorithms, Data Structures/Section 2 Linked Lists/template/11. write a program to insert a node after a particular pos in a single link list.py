# from pprint import pprint
#
#
# c_ Node o..
#
#     ___ -  data_N.. next_node_N..
#         ? _ ?
#         ? _ N..
#
#     ___ get_data
#         r_  ?
#
#     ___ set_data data
#         ? _ ?
#
#     ___ get_next
#         r_ next_node
#
#     ___ set_next new_next
#         next_node _ ?
#
# c_ LinkedList o..
#     ___  -  head_None
#         ? _ ?
#
#     ___ insert data
#         new_node _ ? ?
#         ?.s.. h..
#         head _ ?
#
#     ___ insertatEnd item
#         current _ h..
#         __ ?
#             w__ ?.g.. !_ N..
#                 c.. _ ?.g..
#             ?.s.. ? ?
#         ____
#             head _ ? ?
#
#     ___ insertAtPos  pos item
#         __ ? > s.. __ ? < 0
#             r_ N..
#         __ p.. __ 0
#             i.. ?
#         ____
#             __ p.. __ s..
#                 i.. ?
#             ____
#                 newNode _ ? ?
#                 ?.s.. ?
#                 current _ h..
#                 count _ 0
#                 w__ ? < ? - 1:=
#                     ? +_ 1
#                     c.. _ ?.g..
#                 ?.s.. ?.g..
#                 ?.s.. ?
#
#     ___ size
#         current _ h..
#         count _ 0
#         w__ ?
#           c.. +_ 1
#           c.._ ?.g..
#         r_ ?
#
#
#     ___ search data
#         current _ h..
#         found _ F...
#         w__ ? a__ ? __ F...
#             __ ?.g.. __ ?
#                 found _ T..
#             ____
#                 c.. _ ?.g..
#         __ c.. __ N..
#             r_ V..("Data not in list")
#         r_ ?
#
#
#     ___ delete data
#         current _ h..
#         previous _ N..
#         found _ F...
#         w__ ? a__ ? __ F...
#             __ ?.g.. __ ?
#                 f.. _ T..
#             ____
#                 p.. _ c..
#                 c.. _ ?.g..
#         __ ? __ N..
#             r_ V..("Data not in list")
#         __ p.. __ N..
#             h.. _ ?.g..
#         ____
#             ?.s.. ?.g..
#
#     ___ -s
#         s _ ""
#         p _ h..
#         __ p !_ N..
#                 w__ ?.n.. !_ N..
#                         s +_ ?.d..
#                         ? _ ?.n..
#                 s +_ ?.d..
#         r_ ?
#
#
# l_ ?
#
# ?.i.. 'a'
# ?.i.. 'b'
# ?.i.. 'c'
#
# print l
#
# l.i.. 1,'ZZZZZ'
#
# print l
#
# #if l.search( 'b' ):
# #  print "node found"
# #else:
# #  print "not not found"
# #
# #l.delete( 'b' )
# #print l
# #
