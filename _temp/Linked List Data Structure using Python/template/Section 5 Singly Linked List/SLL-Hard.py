# # Delete nodes that have a greater value on the right side
#
# c_ Node
#     ___ - data
#         ?  ?
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
#         w__ ?.n.. __ no. N..
#             ? _ ?.n..
#         ?.n.. _ nN..
#
#     ___ deleteRight
#         currentNode _ h..
#         w__ ?.n.. __ no. N..
#             # Check if node on the right has a greater value
#             __ ?.n__.d.. > ?.d..
#                 # If currentNode is the head node, delete it and make the new node as the head node
#                 __ cN__ __ h..
#                     h.. _ cN__.n..
#                     cN__.n.. _ N..
#                     cN__ _ h..
#                     c____
#                 # If currentNode is not head node, make the previous node point to next node and remove this node
#                 pN__.n.. _ cN__.n..
#                 cN__.n.. _ N..
#                 cN__ _ h..
#             ____
#                 # Advance to next node if the data on the right side is not greater than currentNode
#                 pN.. _ cN__
#                 cN__ _ cN__.n..
#
#     ___ printList
#         __ h.. __ N..
#             print("Empty List")
#             r_
#         cN__ _ h..
#         w__ cN__ __ no. N..
#             print(cN__.data)
#             cN__ _ cN__.n..
#
# nodeOne = Node(10)
# nodeTwo = Node(5)
# nodeThree = Node(6)
# nodeFour = Node(2)
# nodeFive = Node(3)
# linkedList = LinkedList()
# linkedList.insertEnd(nodeOne)
# linkedList.insertEnd(nodeTwo)
# linkedList.insertEnd(nodeThree)
# linkedList.insertEnd(nodeFour)
# linkedList.insertEnd(nodeFive)
# linkedList.deleteRight()
# linkedList.printList()
