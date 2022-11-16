# c_ Node
#     ___ -   data
#         ? _ ?
#         n.. _ N..
#         p.. _ N
#
# c_ LinkedList
#     ___ -
#         h.. _ N..
#
#     ___ listLength
#         # 10->20->None
#         length _ 0
#         currentNode _ ?
#         w_ ? __ not N..
#             ? _ ?.n..
#             ? +_ 1
#         r_ ?
#
#     ___ insertHead  newNode
#         previousHead _ h..
#         h.. _ ?
#         ?.n.. _ ?
#         ?.p.. _ h..
#
#     ___ insertAt  newNode,position
#         # 10->30->20 || position +> 1
#         __ ? < 0 __ ? > l..
#             print("Invalid position")
#         __ ? __ l..
#             i.. ?
#             r_
#         __ ? __ 0
#             i.. ?
#             r_
#         currentNode _ h..
#         currentPosition _ 0
#         w_ T..
#             __ currentPosition __ ?
#                 ?.p...n.. _ n..
#                 ?.p.. _ c__.p..
#                 n__.n.. _ c..
#                 ?.p.. _ n..
#                 ______
#             c.. _ ?.n..
#             c..+_ 1
#
#     ___ insertEnd  newNode
#         # (head=> Joe->Mary->Grace->None || head=>None <-Joe<-Mary<-Grace
#         __ h.. __ N..
#             ? _ ?
#             r_
#         currentNode _ ?
#         w_ T..
#             __ ?.n.. __ N..
#                 ______
#             c.. _ ?.n..
#         ?.n.. _ ?
#         ?.p.. _ c..
#
#     ___ printList
#         __ head __ N..
#             print("List is empty")
#             r_
#         currentNode _ ?
#         print("Printing from the beginning")
#         w_ T..
#             __ ? __ N..
#                 ______
#             print ?. data
#             __ ?.n.. __ N..
#                 r.. _ c..
#             c.. _ ?.n..
#         print("Printing form end")
#         w_ T..
#             __ r.. __ N..
#                 ______
#             print ?. data
#             ? _ ?.p..
#
# nodeOne _ ? 10
# nodeTwo _ ? 20
# nodeThree _ ? 30
# linkedList _ ?
# ?.i.. ?
# ?.i.. ?
# ?.i.. ? 2
# ?.p..
#
