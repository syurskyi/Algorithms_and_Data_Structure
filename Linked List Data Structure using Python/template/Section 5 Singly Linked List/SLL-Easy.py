# # Print the middle node of a Singly Linked List
#
# c_ Node
#     ___ - data
#         ? ?
#         next _ N..
#
# c_ LinkedList
#     ___ -
#         head _ N..
#
#     ___ insertEnd newNode
#         __ h.. __ N..
#             h.. _ ?
#             r_
#         lastNode _ h..
#         w__ ?.ne.. __ no. N..
#             ? _ ?.ne..
#         ?.ne.. _ ?
#
#     ___ listLength
#         length _ 0
#         currentNode _ h..
#         w__ cN.. __ no. N..
#             l.. +_ 1
#             cN__ _ cN__.ne..
#         r_ ?
#
#     ___ printMiddle
#         length _ lL..
#         __ ? !_ 0
#             if ? __ 1
#                 print("Middle Node: ",head.data)
#                 r_
#             middlePosition _ ? // 2
#             middleNode _ h..
#             w__ mP.. !_ 0:
#                 mN.. _ mN__.ne..
#                 mP.. -_ 1
#             print("Middle Node: " mN__.d..
#
# nodeOne = Node(1)
# nodeTwo = Node(5)
# nodeThree = Node(3)
# nodeFour = Node(10)
# nodeFive = Node(6)
# linkedList = LinkedList()
# linkedList.insertEnd(nodeOne)
# linkedList.insertEnd(nodeTwo)
# linkedList.insertEnd(nodeThree)
# linkedList.insertEnd(nodeFour)
# linkedList.insertEnd(nodeFive)
# linkedList.printMiddle()
