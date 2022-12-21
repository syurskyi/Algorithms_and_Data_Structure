# c_ ListNode
#     ___  -  val
#         ? _ ?
#         prev _ N..
#         next _ N..
#
#
# c_ MyLinkedList
#
#     ___  -
#         head _ N..
#         tail _ N..
#         size _ 0
#
#     ___ get  index
#         __ ? < 0 __ ? >_ s..
#             r_ -1
#
#         cur _ h..
#
#         ______ i.. !_ 0
#             cur _ ?.n..
#             i.. _ ? - 1
#
#         r_ ?.v..
#
#     ___ addAtHead  val
#         new_node = ? ?
#
#         __ h.. __ N..
#             h.. _ ?
#             ? _ ?
#         ____
#             ?.n.. _ h..
#             ?.p.. _ ?
#             ? _ ?
#
#         ? +_ 1
#
#     ___ addAtTail  val
#         new_node _ ? ?
#
#         __ h.. __ N..
#             ? _ ?
#             ? _ ?
#         ____
#             ?.p.. _ t..
#             ?.n.. _ ?
#             ? _ ?
#
#         ? +_ 1
#
#     ___ addAtIndex  index, val
#         __ ? < 0 __ ? > s..
#             r_
#         ____ ? __ 0
#             a.. ?
#         ____ ? __ s..
#             a.. ?
#         ____
#             cur _ h..
#             ______ ? - 1 !_ 0
#                 c.. _ ?.n..
#                 i.. -_ 1
#
#             new_node _ ? ?
#
#             ?.n.. _ c__.n..
#             ?.n__.p.. _ ?
#             c__.n.. _ ?
#             ?.p.. _ ?
#
#             ? +_ 1
#
#     ___ deleteAtIndex  index
#         __ ? < 0 __ ? >_ s..
#             r_
#         ____ ? __ 0
#             c.. _ h__.n..
#             __ c..
#                 ?.p.. _ N..
#
#             h.. _ ?.n..
#             ? -_ 1
#
#             __ s.. __ 0
#                 t.. _ N..
#         ____ ? __ s.. - 1
#             c.. _ t__.p..
#             __ ?
#                 ?.n.. _ N..
#             t.. _ ?.p..
#
#             ? -= 1
#
#             __ s.. __ 0
#                 h.. _ N..
#         ____
#             c.. _ h..
#             ______ i.. - 1 !_ 0
#                 c.. _ ?.n..
#                 ? -_ 1
#
#             c__.n.. _ c__.n__.n..
#             ?.n__.p.. _ ?
#
#             ? -_ 1
#
#
# ## Example Execution ##
# obj = MyLinkedList()
# obj.addAtHead(10)
# obj.addAtTail(15)
# obj.addAtTail(20)
# obj.deleteAtIndex(0)
# obj.addAtHead(40)
#
# print(obj.get(1))