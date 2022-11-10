# ____ doublyLinkedList ______ N.. L..
#
# ___ findGreater l..
#     # 5->3->10->2->15->None
#     length _ ?.lL.. # 5
#     __ ? > 3:
#         middlePosition _ ? // 2 # 5 / 2 => 2
#         currentNode _ ?.h..
#         currentPosition _ 0
#         w___ T..
#             __ c.. __ m..
#                 __ c___.p__.d.. > c___.n__.d..
#                     print("Previous node has a greater value than next node")
#                 ____
#                     print("Next node has a greater value than the previous node")
#                 b..
#             cN.. _ c___.n..
#             c.. +_ 1
#     ____
#         print("Not enough nodes")
#
# nodeOne _ ? 5
# nodeTwo _ ? 3
# nodeThree _ ? 10
# nodeFour _ ? 2
# nodeFive _ ? 15
# linkedList _ ?
# ?.insertEnd(nodeOne)
# ?.insertEnd(nodeTwo)
# #linkedList.insertEnd(nodeThree)
# #linkedList.insertEnd(nodeFour)
# #linkedList.insertEnd(nodeFive)
# ?.printList()
# findGreater(linkedList)
