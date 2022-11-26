# c_ Node
#     ___ -  data
#         ?  ?
#         next _ N..
#         previous _ N..
# 
# c_ LinkedList
#     ___ - 
#         head _ N..
# 
#     ___ insertHead  newNode
#         __ head __ N..
#             head _ ?
#             ?.pr.. _ h..
#             r_
#         lastNode _ h__.pr..
#         ?.pr.. _ lN..
#         ?.ne.. _ h..
#         h__.pr.. _ ?
#         h.. _ ?
#         lN__.ne.. _ h..
# 
#     ___ insertEnd  newNode
#         __ head __ N..
#             head _ ?
#             ?.ne.. _ ?
#             ?.pr.. _ ?
#             r_
#         currentNode _ ?
#         w__ ?.ne.. __ no. h..
#             ? _ ?.ne..
#         ?.ne.. _ nN..
#         nN__.pr.. _ ?
#         nN__.ne.. _ head
#         h__.pr.. _ nN..
# 
#     ___ deleteHead
#         __ head __ N..
#             print("Empty list")
#             r_
#         previousHead _ h..
#         h__ _ h__.ne..
#         h__.pr.. _ ?.pr..
#         ?.pr...ne.. _ h..
#         ?.pr.. _ N..
#         ?.ne.. _ N..
# 
#     ___ deleteEnd
#         __ head __ N..
#             print("Empty List")
#             r_
#         currentNode _ h..
#         w__ T..
#             __ ?.ne...ne.. __ h..
#                 b...
#             ? _ ?.ne..
#         h__.pr.. _ ?
#         ?.ne...pr.. _ N..
#         ?.ne...ne.. _ N..
#         ?.ne.. _ h..
# 
#     ___ printList
#         __ head __ no. N..
#             currentNode _ h..
#             w__ T..
#                 print(?.data)
#                 ? _ ?.ne..
#                 __ ? __ head
#                     b..
#             # Print pr.. of head node to verify the connection to last node
#             print(?.pr...data)
# 
# nodeOne _ ? 10
# nodeTwo _ ? 20
# linkedList _ ?
# ?.iE.. nO..
# ?.iH.. nT..
# ?.dE..
# ?.pL..
