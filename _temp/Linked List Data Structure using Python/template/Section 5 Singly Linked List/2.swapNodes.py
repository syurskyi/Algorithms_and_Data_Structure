# ____ singlyLinkedList ______ Node, LinkedList
#
# ___ swapNodes linkedList dataOne dataTwo
#     # 4->3->5->2->7->1 || 4->7->5->2->3->1
#     # 4 -> previousFirst
#     # 3 -> FirstNode
#     # 2 -> previousSecond
#     # 7 -> secondNode
#     currentNode _ ?.h..
#     previousFirst _ N..
#     previousSecond _ N..
#     w__ T..
#         __ c__.d.. __ dO..
#             firstNode _ c__
#             b..
#         pF__ _ c__
#         c__ _ c__.n..
#     c__ _ ?.h..
#     w__ T..
#         __ c__.d.. __ dT..
#             sN.. _ c__
#             b...
#         pS.. _ c__
#         c__ _ c__.n..
#     # Changing pointers
#     pF__.n.. _ sN..
#     nS.. _ sN__.n..
#     sN__.next _ fN__.n..
#     pS__.n.. _ fN..
#     fN__.n.. _ nS..
#
# nodeOne = Node(4)
# nodeTwo = Node(3)
# nodeThree = Node(5)
# nodeFour = Node(2)
# nodeFive = Node(7)
# nodeSix = Node(1)
# linkedList = LinkedList()
# #4->7->5->2->3->1
# linkedList.insertEnd(nodeOne)
# linkedList.insertEnd(nodeTwo)
# linkedList.insertEnd(nodeThree)
# linkedList.insertEnd(nodeFour)
# linkedList.insertEnd(nodeFive)
# linkedList.insertEnd(nodeSix)
# swapNodes(linkedList, 3, 7)
# linkedList.printList()
