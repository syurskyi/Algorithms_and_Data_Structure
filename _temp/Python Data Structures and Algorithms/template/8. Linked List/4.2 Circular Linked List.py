#
# ____ e.. _______ E..
#
# c_ Circularlinkedlist
#
#     c_ _Node
#
#          - s _ '_element' '_next'
#
#         ___ -  element, next
#             _? _ ?
#             _? _ ?
#
#     ___ -
#         _head _ N..
#         _tail _ N..
#         _size _ 0
#
#     ___ -l
#         r_ ?
#
#     ___ is_empty
#         r_ ?
#
#     ___ add_first e
#         newest _  ? ? N..
#         __ ?
#             ?._> _ ?
#             _head _ ?
#             _tail _ ?
#         ____
#             _t__._n.. _ ?
#             ?._> _ _h..
#             ? _ ?
#             ? +_ 1
#
#     ___ add_last e
#         newest _  ? ? N..
#         __ ?
#             _h.. _ ?
#             ?._> _ ?
#         ____
#             ?._> _  t__._n..
#             ?._n.. _ ?
#         _t.. _ ?
#         ? +_ 1
#
#     ___ add_any e,pos
#         newest _  ? ? N..
#         thead _ ?
#         i _ 1
#         _____ ? < ?
#             t.. _ ?._n..
#             ? +_ 1
#         ?._> _ t__._n..
#         t__._n.. _ ?
#         ? +_ 1
#
#     ___ remove_first
#         __ ?
#             r_ ? 'Linked List Empty')
#         oldhead _ _t__._n..
#         _t__._n.. _ ?._n..
#         _h.. _ ?._n..
#         ? -_ 1
#         __ ?
#             _t.. _ N..
#         r_ ?._e..
#
#     ___ remove_last
#         __ ?
#             r_ ? 'Linked List Empty')
#         thead _ ?
#         i _ 0
#         _____ i < l..(_) - 2
#             t.. _ ?._n..
#             ? +_ 1
#         _t.. _ ?
#         t.. _ ?._n..
#         _t__._n.. _ ?
#         value _ ?._e..
#         ? -_ 1
#         r_ ?
#
#     ___ remove_any  pos
#         __ ?
#             r_ ? 'Linked List Empty')
#         thead _ ?
#         ? _ 1
#         _____ ? < ? - 1
#             t.. _ ?._n..
#             ? +_ 1
#         value _ ?._n..._e..
#         ?._n.. _ ?._n..._n..
#         ? -_ 1
#         r_ ?
#
#     ___ display
#
#         thead _ ?
#         ? _ 0
#         _____ ? < l..
#             print ?._e.. e.._'-->'
#             thead _ ?._n..
#             ? +_ 1
#         print()
#
#
# CL_ Circularlinkedlist()
# CL.add_last( 10)
# CL.add_last( 20)
# CL.add_last(30)
# CL.add_last(40)
# CL.display()
# print('Deteted: ', CL.remove_first())
# CL.display()
# CL.add_first(70)
# CL.display()
# print('Deteted: ', CL.remove_last())
# CL.display()
# CL.add_last(80)
# CL.display()
