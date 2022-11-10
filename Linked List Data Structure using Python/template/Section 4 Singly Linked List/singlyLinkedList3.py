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
#         head = N..
#
#     ___ insertHead newNode
#         # data = > Matthew, next => None
#         temporaryNode _ ? # John
#         head _ ? # Matthew
#         ?.n.. _ ?
#         d.. ?
#
#     ___ listLength
#         currentNode _ ?
#         length _ 0
#         w__ ? __ n.. N..
#             ? +_ 1
#             ? _ ?.n..
#         r_ ?
#
#     ___ insertAt newNode position
#         # head =>10->20->None || newNode => 15 -> None || position=>1
#         __ ? < 0 __ ? > l..
#             print("Invalid position")
#             r_
#         __ p.. __ 0
#             i.. ?
#             r_
#         currentNode _ ? # 10, 20
#         currentPosition _ 0 # 0, 1
#         w__ T..
#             __ ? __ p..
#                 p__.n.. _ n..
#                 ?.n.. _ c..
#                 ______
#             p.. _ c..
#             ? _ ?.n..
#             ? +_ 1
#
#
#     ___ insertEnd newNode
#         __ ? __ N..
#             h.. _ ?
#         ____
#             lastNode _ h..
#             w__ T..
#                 __ ?n.. __ N..
#                     ______
#                 lastNode _ ?n..
#             ?n.. _ ?
#
#     ___ printList
#         # head => John -> Ben -> Matthew -> None
#         __ head __ N..
#             print("List is empty")
#             r_
#         c.. _ h..
#         w__ T..
#             __ c.. __ N..
#                 ______
#             print(c__.d..
#             ? _ ?.n..
#
#
# # Node => data, next
# # firstNode.data => John, firstNode.next => None
# firstNode = ? 10
# linkedList _ ?
# ?.i.. ?
# secondNode = ? 20
# linkedList _ ?
# ?.i.. ?
# thirdNode = ? 15
# ?.i.. ? 10
# ?.p..
#
