# from pprint import pprint
#
#
# c_ Node o..
#
#     ___ -  data_None next_node_N..
#         ? ?
#         ? ?
#
#     ___ getData
#         r_ ?
#
#     ___ getNext
#         r_ ?
#
#     ___ setNext new_next
#         ?  ?
#
# c_ LinkedList o..
#     ___ -  head_N..
#         ? ?
#
#     ___ insert data
#         new_node _ N.. ?
#         ?.sN.. h..
#         h.. _ ?
#
#     ___ insertatEnditem
#         current _ h..
#         __ ?
#             w___ ?.gN.. !_ N..
#                 ? _ ?.gN..
#             ?.sN.. N.. i..
#         ____
#             h.. _ N.. i..
#
#
#     ___ size
#         current _ h..
#         count _ 0
#         w___ cu..
#           co.. +_ 1
#           cu.. _ cu__.gN..
#         r_ co..
#
#
#     ___ search data
#         current _ h..
#         found _ F..
#         w__ cu__ an. fo__ __ F..
#             __ cu__.gD.. __ d..
#                 f... _ T..
#             ____
#                 cu__ _ c__.gN..
#         __ cu__ __ N..
#             r_ V..("Data not in list")
#         r_ ?
#
#
#     ___ delete data
#         current _ h..
#         previous _ N..
#         found _ F..
#         w__ c.. and f.. __ F..
#             __ c__.gD.. __ d..
#                 found _ True
#             ____
#                 pr.. _ c..
#                 c.. _ c__.gN..
#         __ c__ __ N..
#             r_ V.. "Data not in list"
#         __ p.. __ N..
#             h.. _ c__.gN..
#         ____
#             p__.sN.. c__.gN..
#
#     ___ -s
#         s _ ""
#         p _ h..
#         __ ? !_ N..
#                 w___ ?.n_n.. !_ N..
#                         s +_ ?.data
#                         p _ ?.n_n..
#                 s +_ ?.data
#         r_ s
#
#
# l _ ?
# l.insert( 'a' )
# l.insert( 'b' )
# l.insert( 'c' )
#
#
# print(l)
#
# #__ l.search( 'b' ):
# #  print "node found"
# #____
# #  print "not not found"
# #
# #l.delete( 'b' )
# #print l
#
