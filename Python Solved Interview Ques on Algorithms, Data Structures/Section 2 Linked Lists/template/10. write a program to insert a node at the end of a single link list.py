# from pprint import pprint
#
#
# c_ Node o..
#
#     ___ -  data_N.. next_node_N..
#         ? ?
#         ? ?
#
#     ___ get_data
#         r_ ?
#
#     ___ get_next
#         r_ ?
#
#     ___ set_next new_next
#         n_n.. _ ?
#
# c_ LinkedList o..
#     ___  - head_N..
#         ? ?
#
#     ___ insert data
#         new_node _ N.. ?
#         ?.s_n.. h..
#         h.. _ ?
#
#     ___ insertatEnditem
#         current _ h..
#         __ ?:
#             w__ ?.g_n.. !_ N..
#                 ? _ ?.g_n..
#             ?.s_n.. N.. i..
#         ____
#             h.. _ N.. i..
#
#
#     ___ size
#         current _ head
#         count _ 0
#         w__ ?
#           co.. +_ 1
#           ? _ ?.g_n..
#         r_ ?
#
#
#     ___ search data
#         current _ h..
#         found _ F..
#         w__ ? an. f.. __ F..
#             __ ?.g_d.. __ d..
#                 f.. _ T..
#             ____
#                 ? _ ?.g_n..
#         __ ? __ N..
#             r_ V.. ("Data not in list")
#         r_ ?
#
#
#     ___ delete data
#         current _ h..
#         previous _ N..
#         found _ F..
#         w__ ? an. f.. __ F..
#             __ ?.g_d.. __ d..
#                 f.. _ T..
#             ____
#                 previous _ ?
#                 ? _ ?.g_n..
#         __ ? __ N..
#             r_ V.. "Data not in list"
#         __ pr.. __ N..
#             h.. _ ?.g_n..
#         ____
#             p__.s_n.. ?.g_n..
#
#     ___ -s
#         s _ ""
#         p _ h..
#         __ p !_ N..
#                 w__ p.n_n.. !_ N..
#                         s +_ p.da..
#                         p _ p.n_n..
#                 s +_ p.da..
#         r_ s
#
#
# l _ LinkedList()
#
# l.insertatEnd( 'a' )
# l.insertatEnd( 'b' )
# l.insertatEnd( 'c' )
#
#
# print l
#
# __ l.search( 'b' ):
#   print "node found"
# ____
#   print "not not found"
#
# l.delete( 'b' )
# print l
#
