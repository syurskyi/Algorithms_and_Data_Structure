#
# ____ e.. _______ E..
#
# c_ Doublylinkedlist
#     c_ _Node
#          - s _ '_etement' '_prev' '_next'
#
#         ___ -  element prev next
#             _? _ ?
#             _? _ ?
#             _? _ ?
#
#     ___ -
#         _head _ ? N.. N.. N..
#         _tail _ ? N.. N.. N..
#         _h__._n.. _ _t..
#         _t__._p.. _ _h..
#         ? _ 0
#
#     ___ -l
#         r_ ?
#
#     ___ is_empty
#         r_ ? __ 0
#
#     ___ add_first e
#         newest _  ? ? N.. N..
#         __ ?
#             _h.. _ ?
#             _t.. _ ?
#         ____
#             ?._> _ _h..
#             ?._p.. _ ?
#         _h.. _ ?
#         ? +_ 1
#
#     ___ add_last e
#         newest _  ? ? N.. N..
#         __ ?
#             _h.. _ ?
#             _t.. _ ?
#         ____
#             _t__._n.. _ ?
#             ?._p.. _ _t..
#         _t.. _ ?
#         ? +_ 1
#
#     ___ add_any e pos
#         newest _  ? ? N.. N..
#         thead _ ?
#         i _ 1
#         _____ ? < ?
#             t.. _ ?._n..
#             ? +_ 1
#         ?._> _ ?._n..
#         t__._n.. _ ?
#         t__._n..._p.. _ ?
#         ?._p.. _ ?
#         ? +_ 1
#
#     ___ remove_first
#         __ ?
#             r_ ? 'List is Empty')
#         value _ ?._e..
#         _h.. _ ?._n..
#         ?._p.. _ N..
#         ? -_ 1
#         __ ?
#             _t.. _ N..
#         r_ ?
#
#     ___ remove_last
#         __ ?
#             r_ ? 'List is Empty')
#         thead _ ?
#         ? _ 0
#         _____ 1 < l..(_)-2
#             t.. _ ?._n..
#             ? +_ 1
#         _t.. _ ?
#         t.. _ ?._n..
#         value _ ?._e..
#         _t__._n.. _ N..
#         ? -_ 1
#         r_ ?
#
#     ___ remove_any  pos
#         __ ?
#             r_ ? 'List is Empty')
#         thead _ ?
#         ? _ 1
#         _____ 1 < ? - 1
#             t.. _ ?._next
#             ? +_ 1
#         t__._n.. _ ?._n..._n..
#         ?._n..._n__._p.. _ t..
#         ? -_ 1
#
#     ___ display
#         thead _ ?
#         _____ ?
#             print ?._e.. e.._'-->'
#             t.. _ ?._n..
#         print()
#
#
# L _ Doublylinkedlist()
# L.add_last(10)
# L.add_last(20)
# L.add_last(30)
# L.add_last(40)
# L. display()
# print('Delete: ', L.remove_first())
# L.display()
# L.add_first(70)
# L.display()
# print('Delete: ', L.remove_last())
# L.display()
# L.add_any(100, 2)
# L.display()
# L.remove_any(2)
# L.display()
