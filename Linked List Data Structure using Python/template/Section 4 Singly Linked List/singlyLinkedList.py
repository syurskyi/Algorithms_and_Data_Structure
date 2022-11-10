# # Create nodes
# # Create linked list
# # Add nodes to linked list
# # Print linked list
#
# c_ Node
#     ___ -  data
#         ? ?
#         n.. _ N..
#
# c_ LinkedList
#     ___ -
#         head  N..
#
#     ___ insert newNode
#         # head=>John->None
#         __ ? __ N..
#             ? _ ?
#         ____
#             # head=>John->Ben->None || John -> Matthew
#             lastNode _ ?
#             w__ T..
#                 __ ?n.. __ N..
#                     ______
#                 l.. _ ?n..
#             ?n.. _ ?
#
#     ___ printList
#         # head => John -> Ben -> Matthew -> None
#         __ ? __ N..
#             print("List is empty")
#             r_
#         currentNode _ ?
#         w__ T..
#             __ ? __ N..
#                 ______
#             print ?.d..
#             ? _ ?.n..
#
#
# # Node => data, next
# # firstNode.data => John, firstNode.next => None
# firstNode = ? "John"
# linkedList _ ?
# ?.i.. ?
# secondNode = ? "Ben"
# linkedList _ ?
# ?.i.. ?
# thirdNode = ? "Matthew"
# ?.i.. ?
# ?.p..
#
