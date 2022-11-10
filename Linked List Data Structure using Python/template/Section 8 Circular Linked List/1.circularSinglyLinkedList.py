# c_ Node
#     ___  data
#         ? ?
#         ne.. _ N..
#
# c_ LinkedList
#     ___
#         head _ N..
#
#     ___ insertEnd  newNode
#         __ head __ N..
#             h.. _ ?
#             ?.ne.. _ h..
#             r_
#         currentNode _ h..
#         w___(?.ne.. __ no. h..
#             ? _ ?.ne..
#         ?.ne.. _ n..
#         ?.ne.. _ head
#
#     ___ insertHead  newNode
#         lastNode _ head
#         w___ ?.ne.. __ no. h..
#             ? _ ?.ne..
#         previousHead _ h..
#         head _ ?
#         ?.ne.. _ pH..
#         lN__.ne.. _ h..
#
#     ___ deleteEnd
#         lastNode _ h..
#         w___ ?.ne.. __ no. h..
#             previousNode _ ?
#             lN.. _ ?.ne..
#         ?.ne.. _ N..
#         pN_.ne.. _ h..
#
#     ___ deleteHead
#         lastNode _ h..
#         w___ ?.ne.. __ no. h..
#             ? _ ?.ne..
#         previousHead _ h..
#         h.. _ h__.ne..
#         ?.ne.. _ h..
#         pH__.ne.. _ N..
#
#     ___ printList
#         currentNode _ h..
#         w___ T..
#             print(?.data)
#             ? _ ?.ne..
#             __ ? __ h..
#                 break
#         print(?.data)
#
# nodeOne _ Node(10)
# nodeTwo _ Node(20)
# nodeThree _ Node(30)
# linkedList _ ?
# ?.iE.. nO..
# ?.iE.. nT..
# ?.iE.. nT..
# ?.dH..
# ?.pL..
