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
#         h.. _ N..
#
#     ___ isListEmpty
#         __ ? __ N..
#             r_ T..
#         ____
#             r_ F..
#
#     ___ insertHead newNode
#         # data = > Matthew, next => None
#         temporaryNode _ ? # John
#         h.. _ ? # Matthew
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
#     ___ insertAt newNode, position
#         # head =>10->20->None || newNode => 15 -> None || position=>1
#         __ ? < 0 __ ? > l..
#             print("Invalid position")
#             r_
#         __ ? __ 0
#             i.. ?
#             r_
#         currentNode _ ? # 10, 20
#         currentPosition _ 0 # 0, 1
#         w__ T..
#             __ ? __ p..
#                 p__.n.. _ ?
#                 n__.n.. _ ?
#                 ______
#             p.. _ c..
#             ? _ ?.n..
#             ? +_ 1
#
#
#     ___ insertEnd newNode
#         __ ? __ N..
#             ? _ ?
#         ____
#             lastNode _ ?
#             w__ T..
#                 __ ?n.. __ N..
#                     ______
#                 l.. _ ?n..
#             ?n.. _ ?
#
#     ___ deleteHead
#         __ i.. __ F..
#             # head => 10 -> 15 -> 20 || 15->20->10-> None
#             previousHead _ ?
#             ? _ ?.n..
#             ?.n.. _ N..
#         ____
#             print("Linked List is empty. Delete failed")
#
#     ___ deleteAt position
#         __ ? < 0 __ ? > l..
#             print("Invalid position")
#             r_
#         __ i.. __ F..
#             __ ? __ 0
#                 d..
#                 r_
#             currentNode _ h..
#             currentPosition _ 0
#             w__ T..
#                 __ c.. __ p..
#                     p__.n.. _ c__.n..
#                     ?.n.. _ N..
#                     ______
#                 p.. _ c..
#                 ? _ ?.n..
#                 ? +_ 1
#
#
#     ___ deleteEnd
#         # head => John -> Ben -> Mattew -> None
#         __ i.. __ F..
#             __ ?.n.. __ N..
#                 d..
#                 r_
#             lastNode _ ?
#             w__ ?n.. __ n.. N..
#                 p.. _ ?
#                 l.. _ ?n..
#             p__.n.. _ N..
#         ____
#             print("Linked List is empty. Delete failed")
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
#             print(?.d..
#             ? _ ?.n..
#
# # Node => data, next
# # firstNode.data => John, firstNode.next => None
# firstNode _ ? "John"
# linkedList _ ?
# ?.i.. ?
# secondNode _ ? "Ben"
# linkedList _ ?
# ?.i.. ?
# thirdNode _ ? "Matthew")
# ?.i.. ?
# ?.p..
#
#
#
