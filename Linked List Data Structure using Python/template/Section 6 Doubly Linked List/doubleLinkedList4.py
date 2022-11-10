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
#     ___ listLength
#         # 10->20->None
#         length _ 0
#         currentNode _ ?
#         w_ ? __ n.. N..
#             ? _ ?.n..
#             ? +_ 1
#         r_ ?
#
#     ___ insertHead  newNode
#         previousHead _ ?
#         head _ ?
#         ?.n.. _ ?
#         ?.p.. _ ?
#
#     ___ insertAt  newNode position
#         # 10->30->20 || position +> 1
#         __ ? < 0 __ ? > l..
#             print("Invalid position")
#         __ ? __ l..
#             i.. ?
#             r_
#         __ ? __ 0
#             i.. ?
#             r_
#         currentNode _ head
#         currentPosition _ 0
#         w_ T..
#             __ currentPosition __ ?
#                 ?.p...n.. _ n..
#                 ?.p.. _ ?.p..
#                 ?.n.. _ c..
#                 ?.p.. _ ?
#                 ______
#             c.. _ ?.n..
#             c.. +_ 1
#
#     ___ insertEnd  newNode
#         # (head=> Joe->Mary->Grace->None || head=>None <-Joe<-Mary<-Grace
#         __ h.. __ N..
#             ? _ ?
#             r_
#         c.. _ ?
#         w_ T..
#             __ ?.n.. __ N..
#                 ______
#             c.. _ ?.n..
#         ?.n.. _ ?
#         ?.p.. _ c..
#
#     ___ deleteHead
#         head _ ?.n..
#         ?.p...n.. _ N..
#         ?.p.. _ N
#
#     ___ deleteAt  position
#         currentNode _ head
#         currentPosition _ 0
#         w_ T..
#             __ c.. __ ?
#                 ?.p...n.. _ ?.n..
#                 ?.n...p.. _ ?.p..
#                 ?.n.. _ N..
#                 ?.p.. _ N
#                 ______
#             c.. _ ?.n..
#             c.. +_ 1
#
#     ___ deleteEnd
#         currentNode _ h..
#         w_ T..
#             __ ?.n...n.. __ N..
#                 ?.n...p.. _ N
#                 ?.n...n.. _ N..
#                 ?.n.. _ N..
#                 ______
#             c.. _ ?.n..
#
#     ___ printList
#         __ h.. __ N..
#             print("List is empty")
#             r_
#         c.. _ h..
#         print("Printing from the beginning")
#         w_ T..
#             __ c.. __ N..
#                 ______
#             print c.. data
#             __ ?.n.. __ N..
#                 reverseTraversalNode _ c..
#             c.._ ?.n..
#         print("Printing form end")
#         w_ T..
#             __ r..__ N..
#                 ______
#             print r... data
#             r.. _ r__.p..
#
# nodeOne _ ? 'Joe'
# nodeTwo _ ? 'Mary'
# nodeThree _ ? 'Grace'
# linkedList _ ?
# ?.i.. ?
# ?.i.. ?
# ?.i.. ?
# ?.d.. 0
# ?.p..
#
