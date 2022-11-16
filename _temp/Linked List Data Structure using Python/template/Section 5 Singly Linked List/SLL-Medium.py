# # In an integer linked list, count the number of nodes that are even and the number of nodes that are odd
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
#     ___ insertEnd newNode
#         __ h.. __ N..
#             h.. _ ?
#             r_
#         lastNode _ h..
#         w__ ?.n.. __ no. N..
#             ? _ ?.n..
#         ?.n.. _ nN..
#
#     ___ countNodes
#         currentNode _ h..
#         evenCount _ 0
#         oddCount _ 0
#         w__ cN__ __ no. N..
#             __ cN__.d.. % 2 is 0:
#                 eC.. +_ 1
#             ____
#                 oC.. +_ 1
#             cN__ _ cN__.n..
#         print("Even Nodes: " eC..
#         print("Odd Nodes: "  oC..
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
# linkedList.countNodes()
