# ____ singlyLinkedList ______ Node, LinkedList
#
# c_ NewNode N..
#     ___ - data
#         s__. - ?
#         isVisited _ F..
#
# ___ detectCycle l..
#     # John(True)->Ben(True)->Matthew(True)->Ben(True)
#     currentNode _ ?.h..
#     ?.isVisited _ T..
#     w___ T..
#         __ ?.n__.iV.. __ T..
#             ?.n.. _ N..
#             b_
#         ? _ ?.n..
#         ?.iV.. _ T..
#
#
# # John->Ben->Matthew->Ben->(Matthew->Ben...)
# nodeOne = NewNode('John')
# nodeTwo = NewNode('Ben')
# nodeThree = NewNode('Matthew')
# linkedList = LinkedList()
# linkedList.insertEnd(nodeOne)
# linkedList.insertEnd(nodeTwo)
# linkedList.insertEnd(nodeThree)
# nodeThree.next = nodeTwo
# detectCycle(linkedList)
# linkedList.printList()
