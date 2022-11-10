# c_ Node
#     ___ -   data
#         ? _ ?
#         n.. _ N..
#         p.. _ N
#
# c_ LinkedList
#     ___ -
#         head _ N..
#
#     ___ insertEnd  newNode
#         # (head=> Joe->Mary->Grace->None || head=>None <-Joe<-Mary<-Grace
#         __ ? __ N..
#             h.. _ ?
#             r_
#         currentNode _ h..
#         w_ T..
#             __ ?.n.. __ N..
#                 ______
#             c.. _ ?.n..
#         ?.n.. _ n..
#         ?.p.. _ ?
#
#     ___ printList
#         __ h.. __ N..
#             print("List is empty")
#             r_
#         currentNode _ h..
#         print("Printing from the beginning")
#         w_ T..
#             __ > __ N..
#                 ______
#             print ?. data
#             __ ?.n.. __ N..
#                 reverseTraversalNode _ c..
#             ? _ ?.n..
#         print("Printing form end")
#         w_ T..
#             __ r.. __ N..
#                 ______
#             print ?. data
#             r.. _ ?.p..
#
# nodeOne _ ? 'Joe'
# nodeTwo _ ? 'Mary'
# nodeThree _ ? 'Grace'
# linkedList _ ?
# ?.i.. ?
# ?.i.. ?
# ?.i.. ?
# ?.p..
