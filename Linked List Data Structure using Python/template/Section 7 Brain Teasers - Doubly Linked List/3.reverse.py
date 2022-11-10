# ____ d.. ______ N.. L...
#
# ___ reverse ?
#     # (2->13->10->20->None | None<-2<-13<-10<-20) || (20->10->13->2->None | None<-20<-10<-13<-2)
#     currentNode _ ?.h..
#     w__ ? __ not N..
#         nextNode _ ?.n.. # 13, 10, 20, None
#         ?.n.. _ ?.p..
#         ?.p.. _ nN..
#         __ ?.p.. __ N..
#             lL__.h.. _ ?
#         ? _ nN..
#
# nodeOne _ ? 2
# nodeTwo _ ? 13
# nodeThree _ ? 10
# nodeFour _ ? 20
# linkedList _ ?
# ?.insertEnd(nodeOne)
# ?.insertEnd(nodeTwo)
# ?.insertEnd(nodeThree)
# ?.insertEnd(nodeFour)
# reverse(?)
# ?.printList()
