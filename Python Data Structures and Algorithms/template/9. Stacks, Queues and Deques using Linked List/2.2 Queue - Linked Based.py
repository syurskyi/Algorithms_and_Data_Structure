# ____ e.. _______ E..
#
#
# c_ LinkedQueue
#     c_ _Node:
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
#     ___ enqueue e
#         newNode _  ? ? N..
#         __ ?
#             _h.. _ ?
#         ____
#             _t..._n.. _ ?
#          t.. _ ?
#         _? _ ? + 1
#
#     ___ dequeue
#         __ ?
#             r_ ? 'Queue is Empty'
#         value _ ?._e..
#         _h.. _ ?._n..
#         ? _ ? - 1
#         __ ?
#             _t.. _ N..
#         r_ ?
#
#     ___ first
#         __ ?
#             r_ ? 'Queue is Empty'
#         r_ ?._e..
#
#     ___ display
#         temp _ ?
#         _____ ?
#             print ?._e.. e.._'-->'
#             t.. _ ?._n..
#         print()
#
#
# q _ LinkedQueue()
# q.enqueue(10)
# q.enqueue(20)
# q.display()
# print('Length: ', l..(q))
# print('Dequeue: ', q.dequeue())
# q.display()
# q.enqueue(30)
# q.enqueue(40)
# q.display()
# print('First Element: ', q.first())
# q.display()
# print('Dequeue: ', q.dequeue())
# q.display()
