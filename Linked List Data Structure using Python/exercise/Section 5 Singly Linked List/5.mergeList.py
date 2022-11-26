# ____ singlyLinkedList ______ Node, LinkedList
#
# ___ mergeLists firstList secondList mergedList
#     # 1->3->4 || 2->7->9 || 1->2->3->4->7->9->None
#     currentFirst _ fL__.h..
#     currentSecond _ sL__.h..
#     w___ T..
#         __ cF__ __ N..
#             mL__.iE.. cS..
#             b..
#         __ cS__ __ N..
#             mL__.iE.. cF__
#             b..
#         __ cF__.da.. < cS__.da..
#             currentFirstNext _ cF__.ne..
#             cF__.ne.. _ N..
#             mL__.iE.. cF__
#             cF__ _ cFN..
#         ____
#             currentSeconNext _ cS__.ne..
#             cS__.ne.. _ N..
#             mL__.iE.. cS__
#             cS__ _ cSN..
#
#
# # First List
# nodeOne = Node(1)
# nodeTwo = Node(3)
# nodeThree = Node(4)
# firstList = LinkedList()
# firstList.insertEnd(nodeOne)
# firstList.insertEnd(nodeTwo)
# firstList.insertEnd(nodeThree)
#
# # Second List
# nodeFour = Node(2)
# nodeFive = Node(7)
# nodeSix = Node(9)
# secondList = LinkedList()
# secondList.insertEnd(nodeFour)
# secondList.insertEnd(nodeFive)
# secondList.insertEnd(nodeSix)
#
# print("Printing first list")
# firstList.printList()
# print("Printing second list")
# secondList.printList()
#
# mergedList = LinkedList()
#
# mergeLists(firstList, secondList, mergedList)
# del firstList
# del secondList
#
# print("Printing Merged List")
# mergedList.printList()
