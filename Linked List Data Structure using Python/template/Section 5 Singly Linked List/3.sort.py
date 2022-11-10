# ____ singlyLinkedList ______ Node, LinkedList
#
# ___ swapNext linkedList previousNode largestNode nextNode
#     # 4->3->5->1 || 3->4->5->1 || 4->|1->5->None
#     lN__.n.. _ nN__.n..
#     nN__.n.. _ lN__
#     __ lN__ __ lL__.h..
#         lL__.head _ nN__
#         r_
#     pN__.n.. _  nN__
#
# ____ sort lL__
#     # number of iterations _ number of nodes - 1
#     numberOfIterations _ lL__.lL.. - 1 # 3
#     w___ nOI.. !_ 0 # 3, 2, 1
#         largestNode _ lL__.h..
#         pN__ _ N..
#         nOC.. _ nOI..
#         w__ nOC.. !_ 0
#             __ lN__.data > lN__.n...da..
#                 sN.. lL__ pN__ lN__ lN__.n..
#             ____
#                 pN__ _ lN__
#                 lN__ _ lN__.n..
#             nOC.. -_ 1
#
#         nOI.. -_ 1
#
# nodeOne = Node(4)
# nodeTwo = Node(3)
# nodeThree = Node(5)
# nodeFour = Node(1)
# linkedList = LinkedList()
# linkedList.insertEnd(nodeOne)
# linkedList.insertEnd(nodeTwo)
# linkedList.insertEnd(nodeThree)
# linkedList.insertEnd(nodeFour)
# sort(linkedList)
# linkedList.printList()
