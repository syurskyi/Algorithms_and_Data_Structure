# ____ e.. _______ E..
#
#
# c_ Linkedlist
#
#     c_ _Node
#          - s _ '_element', '_next'
#
#         ___ -  element, next):
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
#         r_ ? __ 0
#
#     ___ add_first e
#         newest _ ? ? N..
#         __ ?
#             _head _ ?
#             _tail _ ?
#         ____
#             ?._> _ ?
#         ? _ ?
#         ? +_ 1
#
#     ___ add_last e
#         newest _ ? ? N..
#         __ ?
#             _h.. _ ?
#             _t.. _ ?
#         ____
#             _t__._? _ ?
#         _t.. _ ?
#         ? +_ 1
#
#     ___ add_any e, pos
#         newest _ ? ? N..
#         thead _  head
#         i _ 1
#         _____ ? < ?
#             t.. _ ?._n..
#             ? +_ 1
#         ?._> _ ?._n..
#         ?._n.. _ ?
#         ? +_ 1
#
#     ___ remove_first
#         __ ?
#             r_ ? 'Linked List Empty'
#         value _ ?._e..
#         _h.. _ ?._n..
#         ? -_ 1
#         __ ?
#             _t.. _ N..
#         r_ ?
#
#     ___ remove_last
#         __ ?
#             r_ ? 'Linked List Empty'
#         thead _  ?
#         i _ 0
#         _____ ? < l..(_) - 2
#             t.. _ ? ._n..
#             ? +_ 1
#         _t.. _ t..
#         t.. _ ?._n..
#         value _ ?._e..
#         _t__._n.. _ N..
#         ? -_ 1
#         r_ ?
#
#     ___ remove_any  pos
#         __ ?
#             r_ ? 'Linked List Empty'
#         t.. _  ?
#
#         i _ 1
#         _____ ? < ?-1
#             t.. _ ?._n..
#             ? +_ 1
#         value_ ?._..._e..
#         t__._n.. _ ?._n__._n..
#         ? -_ 1
#         r_ ?
#
#     ___ display
#         thead _ ?
#         _____ ?
#             print ?._e.. e.._'-->')
#             t.. _ ?._n..
#         print()
#
# L _ Linkedlist()
# L.add_last(10)
# L.add_last(20)
# L.add_last(30)
# L.add_last(40)
# L. display()
# print('Deteted: ', L.remove_first())
# L. display()
# L.add_first( 70)
# L. display()
# print('Deteted: ', L.remove_last())
# L.display()
# L.add_any(100, 2)
# L.display()
# L.remove_any(2)
# L.display()
