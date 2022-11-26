# # Create nodes
# # Create linked list
# # Add nodes to linked list
# # Print linked list
#
# c_ Node
#     ___ - data
#         ? ?
#         next _ N..
#
# c_ LinkedList:
#     ___ -
#         head _ N..
#
#     ___ isListEmpty
#         __ h.. __ N..
#             r_ T..
#         ____
#             r_ F..
#
#     ___ insertHead newNode
#         # data = > Matthew, next => None
#         temporaryNode _ h.. # John
#         head _ nN.. # Matthew
#         ?.ne.. _ tN..
#         del ?
#
#     ___ listLength
#         currentNode _ h..
#         length _ 0
#         w__ cN__ __ no. N..
#             l.. +_ 1
#             cN__ _ cN__.ne..
#         r_ ?
#
#     ___ insertAt newNode position
#         # head =>10->20->None || newNode => 15 -> None || position=>1
#         __ p.. < 0 o. p... > lL..
#             print("Invalid position")
#             r_
#         __ p.. __ 0
#             iH.. ?
#             r_
#         cN__ _ h.. # 10, 20
#         currentPosition _ 0 # 0, 1
#         w__ T..
#             __ ? __ p..
#                 pN__.ne.. _ nN..
#                 nN__.ne.. _ cN__
#                 b..
#             pN.. _ cN__
#             cN__ _ cN__.ne..
#             cP.. +_ 1
#
#
#     ___ insertEnd newNode
#         __ h.. __ N..
#             h.. _ ?
#         ____
#             lastNode _ h..
#             w__ T..
#                 __ ?.ne.. __ N..
#                     b..
#                 ? _ ?.ne..
#             ?.ne.. _ nN..
#
#     ___ deleteHead
#         __ iLE.. __ F..
#             # head => 10 -> 15 -> 20 || 15->20->10-> None
#             previousHead _ h..
#             h.. _ h__.ne..
#             pH__.ne.. _ N..
#         ____
#             print("Linked List __ empty. Delete failed")
#
#     ___ deleteAt position
#         __ p.. < 0 o. p.. > lL..
#             print("Invalid position")
#             r_
#         __ iLE.. __ F..
#             __ p.. __ 0
#                 dH..
#                 r_
#             cN__ _ h..
#             cP.. _ 0
#             w__ T..
#                 __ cP.. __ p..
#                     pN__.ne.. _ cN__.ne..
#                     cN__.ne.. _ N..
#                     b..
#                 pN.. _ cN__
#                 cN__ _ cN__.ne..
#                 cP... +_ 1
#
#
#     ___ deleteEnd
#         # head => John -> Ben -> Mattew -> None
#         __ iLE.. __ F..
#             __ h__.ne.. __ N..
#                 dH..
#                 r_
#             lastNode _ h..
#             w__ ?.ne.. __ not N..
#                 pN.. _ ?
#                 ? _ ?.ne..
#             pN__.ne.. _ N..
#         ____
#             print("Linked List is empty. Delete failed")
#
#     ___ printList
#         # head _> John -> Ben -> Matthew -> None
#         __ h.. __ N..
#             print("List is empty")
#             r_
#         cN__ _ h..
#         w__ T..
#             __ cN__ __ N..
#                 b..
#             print cN__.da..
#             cN__ _ cN__.ne..
#
# # Node => data, next
# # firstNode.data => John, firstNode.next => None
# firstNode = Node("John")
# linkedList = LinkedList()
# linkedList.insertEnd(firstNode)
# secondNode = Node("Ben")
# linkedList = LinkedList()
# linkedList.insertEnd(secondNode)
# thirdNode = Node("Matthew")
# linkedList.insertHead(thirdNode)
# linkedList.printList()
#
#
#
