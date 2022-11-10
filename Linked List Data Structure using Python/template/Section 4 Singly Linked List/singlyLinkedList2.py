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
#         h..  ? # Matthew
#         ?.n.. _ ?
#         d.. ?
#
#     ___ insertEnd newNode
#         __ h.. __ N..
#             h.. _ ?
#         ____
#             lastNode  h..
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
#             print(?.d..
#             c.. _ ?.n..
#
#
# # Node => data, next
# # firstNode.data => John, firstNode.next => None
# firstNode ? "John"
# linkedList  ?
# ?.i.. ?
# secondNode  ? "Ben"
# linkedList  ?
# ?.i.. ?
# thirdNode  ? "Matthew"
# ?.i.. ?
# ?.p..
#
