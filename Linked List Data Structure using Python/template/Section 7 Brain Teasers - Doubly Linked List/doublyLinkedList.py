# c_ Node
#     ___ - data
#         ?  ?
#         next _ N..
#         previous _ N..
#
# c_ LinkedList
#     ___ -
#         head _ N..
#
#     ___ listLength
#         # 10->20->None
#         length _ 0
#         currentNode _ h__
#         w__ ? is not N..
#             ? _ ?.next
#             l.. +_ 1
#         r_ ?
#
#     ___ insertHead newNode
#         previousHead _ h__
#         h__ _ ?
#         ?.n.. _ ?
#         ?.p.. _ h__
#
#     ___ insertAt newNode position
#         # 10->30->20 || position +> 1
#         __ p.. < 0 o. p.. > lL..
#             print("Invalid position")
#             r_
#         __ p.. __ lL..
#             iE.. ?
#             r_
#         __ p.. __ 0
#             iH.. ?
#             r_
#         currentNode _ h__
#         currentPosition _ 0
#         w__ T..
#             __ cP.. __ p..
#                 ?.p__.n.. _ newNode
#                 ?.p.. _ ?.p..
#                 ?.n.. _ ?
#                 ?.p.. _ newNode
#                 b..
#             ? _ ?.next
#             cP.. +_ 1
#
#     ___ insertEnd newNode
#         # (head_> Joe->Mary->Grace->None || head_>N.. <-Joe<-Mary<-Grace
#         __ h__ __ N..
#             h__ _ ?
#             r_
#         currentNode _ h__
#         w__ T..
#             __ ?.n.. __ N..
#                 b..
#             ? _ ?.n..
#         ?.n.. _ newNode
#         newNode.p.. _ ?
#
#     ___ deleteHead
#         h__ _ h__.n..
#         ?.p___.n.. _ N..
#         ?.p.... _ N..
#
#     ___ deleteAt position
#         currentNode _ h__
#         currentPosition _ 0
#         w__ T..
#             __ cP.. _ p..
#                 ?.p__.n.. _ ?.n..
#                 ?.n__.p.. _ ?.p..
#                 ?.n.. _ N..
#                 ?.p.. _ N..
#                 b..
#             ? _ ?.n..
#             cP.. +_ 1
#
#     ___ deleteEnd
#         currentNode _ h__
#         w__ T..
#             __ ?.n__.n.. __ N..
#                 ?.n__.p.. _ N..
#                 ?.n__.n.. _ N..
#                 ?.n.. _ N..
#                 b..
#             ? _ ?.n..
#
#     ___ printList
#         __ h__ __ N..
#             print("List is empty")
#             r_
#         currentNode _ h__
#         print("Printing from the beginning")
#         w__ T..
#             __ ? __ N..
#                 b..
#             print ?.d..
#             __ ?.n.. __ N..
#                 reverseTraversalNode _ ?
#             ? _ ?.n..
#         print("Printing form end")
#         w__ T..
#             __ r.. __ N..
#                 b..
#             print(r__.d..
#             r__ _ r__.p..
#
# # nodeOne _ Node('Joe')
# # nodeTwo _ Node('Mary')
# # nodeThree _ Node('Grace')
# # linkedList _ LinkedList()
# # linkedList.insertEnd(nodeOne)
# # linkedList.insertEnd(nodeTwo)
# # linkedList.insertHead(nodeThree)
# # linkedList.deleteAt(0)
# # linkedList.printList()
#
