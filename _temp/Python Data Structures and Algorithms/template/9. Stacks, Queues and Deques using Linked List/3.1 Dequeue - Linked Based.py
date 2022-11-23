# ____ e.. _______ E..
#
#
# c_ LinkedDeque
#
#     c_ _Node
#          - s _ ' -element' ' -next'
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
#         r_  ? __ 0
#
#     ___ add_first e
#         newest _  ? ? N..
#         __ ?
#             _head _ ?
#             _tail _ ?
#         ____
#             n.. ._n.. _ ?
#         ? _ ?
#         ? +_ 1
#
#     ___ add_last e
#         newest _  ? ? N..
#         __ ?
#             _h.. _ ?
#             _t.. _ ?
#         ____
#             _t__._n.. _ ?
#         _t.. _ ?
#         ? +_ 1
#
#     ___ remove_first
#         __ ?
#             r_ ? 'Linked List Empty')
#         value _ ?._e..
#         _h.. _ ?._n..
#         ? -_ 1
#
#         __ ?
#             _t.. _ N..
#         r_ ?
#
#     ___ remove_last
#         __ ?
#             r_ ? 'Linked List Empty')
#         thead _ ?
#         i _ 0
#         _____ ? < l..(_) - 2
#             t.. _ ?._n..
#             ? +_ 1
#         _t.. _ ?
#         t.. _ ?._n..
#         value _ ?._e..
#         _t__._n.. _ N..
#         ? -_ 1
#         r_ ?
#
#     ___ display
#         thead _ ?
#         _____ ?
#             print ?._e.. e.._ '-->' )
#             t.. _ ?._n..
#         print()
#
#
# L _ LinkedDeque()
# L.add_last(10)
# L.add_last(20)
# L.add_last(30)
# L.add_last(40)
# L.display()
# print('Deleted:', L.remove_first())
# L.display()
# L.add_first( 70)
# L.display()
# print('Deleted:', L.remove_last())
# L.display()
