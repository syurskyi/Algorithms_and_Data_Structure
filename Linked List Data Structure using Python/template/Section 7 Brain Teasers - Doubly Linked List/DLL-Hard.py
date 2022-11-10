# # Merge two unsorted list into a sorted list such that final list has no duplicate values
#
# c_ Node
#     ___ - data
#         ? ?
#         next _ N...
#         previous _ N...
#
# c_ LinkedList
#     ___ -
#         head _ N...
#
#     ___ insertEnd newNode
#         __ h.. __ N...
#             h.. _ ?
#             r_
#         currentNode _ h..
#         w___ ?.n.. __ no. N...
#             ? _ ?.n..
#         ?.n.. _ newNode
#         ?.p.. _ ?
#
#     ___ printList
#         __ h.. __ N...
#             print("Empty list")
#             r_
#         currentNode _ h..
#         w___ T..
#             print ?.d..
#             __ ?.n.. __ N...
#                 b..
#             ? _ ?.n..
#
# ___ isDuplicate currentNode mergedList
#     currentMerge _ m__.h..
#     # Check __ data already exists in list
#     w___ ? __ no. N...
#         __ ?.d.. __ ?.d..
#             r_ T..
#         ? _ ?.n..
#     r_ F..
#
# ___ sortNodeOrder currentNode mergedList
#     currentMerge _ m__.h..
#     w___ T..
#         # Insert in sorted order
#         __ ?.d.. < ?.d..
#             # Check __ ? __ to be made the new h.. node
#             __ ? __ m__.h..
#                 ?.n.. _ ?
#                 ?.p.. _ ?
#                 m__.h.. _ ?
#             ____
#                 ?.p.. _ ?.p..
#                 ?.n.. _ ?
#                 ?.p...n.. _ ?
#                 ?.p.. _ ?
#             r_
#         ____
#             __ ?.n.. __ N...
#                 ?.n.. _ ?
#                 ?.p.. _ ?
#                 r_
#             ? _ ?.n..
#
# ___ mergeList linkedListOne linkedListTwo mergedList
#     currentFirst _ __O__.h..
#     currentSecond _ __T__.h..
#     # Insert list one into merged list
#     w___ T..
#         __ _F.. __ N...
#             b..
#         currentFirstNext _ _F__.n..
#         _F__.n.. _ N...
#         _F__.p.. _ N...
#         __ m__.h.. __ N...
#             m__.h.. _ _F___
#             __F__ _ cFN..
#             c....
#         # Check __ node already exists
#         __ isDuplicate _F_ m__ __ F..
#             # Place the node in sorted order
#             sortNodeOrder(_F_, m__)
#         _F_ _ cFN..
#     # Insert list two into merged list
#     w___ T..
#         __ __S.. __ N...
#             b..
#         __SN__ _ __S__.n..
#         __S__.n.. _ N...
#         __S___.p.. _ N...
#         __ m__.h.. __ N...:
#             m__.h.. _ __S__
#             __S__ _ __SN__
#             c...
#         # Check __ node already exists
#         __ isDuplicate __S__ m__ __ F..
#             # Place the node in sorted order
#             sortNodeOrder __S__ m__
#         __S__ _ __SN__
#
#
#
# linkedListOne _ LinkedList()
# nodeOne _ Node(5)
# nodeTwo _ Node(10)
# nodeThree _ Node(7)
# nodeFour _ Node(5)
# linkedListOne.insertEnd(nodeOne)
# linkedListOne.insertEnd(nodeTwo)
# linkedListOne.insertEnd(nodeThree)
# linkedListOne.insertEnd(nodeFour)
#
# linkedListTwo _ LinkedList()
# nodeFive _ Node(23)
# nodeSix _ Node(7)
# nodeSeven _ Node(1)
# nodeEight _ Node(7)
# linkedListTwo.insertEnd(nodeFive)
# linkedListTwo.insertEnd(nodeSix)
# linkedListTwo.insertEnd(nodeSeven)
# linkedListTwo.insertEnd(nodeEight)
#
#
# print("Printing List 1")
# linkedListOne.printList()
# print("Printing List 2")
# linkedListTwo.printList()
# print("Done")
# mergedList _ LinkedList()
# mergeList(linkedListOne, linkedListTwo, mergedList)
#
# print("Printing Merged List")
# mergedList.printList()
