class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
#
#     ___ append  value
#         n.. _ ? ?
#         __ ? __ N..
#             h.. _ ?
#             t.. _ ?
#         ____
#             t__.n.. _ ?
#             ?.p.. _ t..
#             t.. _ ?
#         ? =_ 1
#         r_ T..
#
#     ___ pop
#         __ ? __ 0
#             r_ N..
#         t.. _ t..
#         __ ? __ 1
#             h.. _ N..
#             t.. _ N..
#         ____
#             t.. _ t__.p..
#             ?.n.. _ N.
#             ?.p.. _ N..
#         ? -_ 1
#         r_ ?
#
#     ___ prepend  value
#         n.. _ ? ?
#         __ ? __ 0
#             h.. _ ?
#             t.. _ ?
#         ____
#             ?.n.. _ h..
#             ?.p.. _ ?
#             h.. _ ?
#         ? =_ 1
#         r_ T..
#
#     ___ pop_first
#         __ ? __ 0
#             r_ N..
#         t.. _ h..
#         __ ? __ 1
#             h.. _ N..
#             t.. _ N..
#         ____
#             h.. _ ?.n..
#             ?.p.. _ N..
#             t__.n.. _ N..
#         ? -_ 1
#         r_ ?
#
#     ___ get  index
#         __ ? < 0 __ ? >_ ?
#             r_ N..
#         t.. _ h..
#         __ ? < ?/2
#             ___ _ __ r_ ?
#                 ? _ ?.n..
#         ____
#             t.. _ t..
#             ___ _ __ r_ ? -1 ? -1
#                 ? _ ?.p..
#         r_ ?
#
#     ___ set_value  ? value
#         temp = get ?
#         __ ?
#             ?.? _ ?
#             r_ T..
#         r_ F..
#
#     ___ insert  ? value
#         __ ? < 0 __ ? > ?
#             r_ F..
#         __ ? __ 0
#             r_ p.. ?
#         __ ? __ ?
#             r_ a.. ?
#
#         n.. _ ? ?
#         b.. _ g.. ? - 1
#         a.. _ b__.n..
#
#         ?.p.. _ b..
#         ?.n.. _ a..
#         b__.n.. _ ?
#         a__.p.. _ n..
#
#         ? =_ 1
#         r_ T..
#
#


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(3)

print('DLL before insert():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.insert(1, 2)

print('\nDLL after insert(2) in middle:')
my_doubly_linked_list.print_list()

my_doubly_linked_list.insert(0, 0)

print('\nDLL after insert(0) at beginning:')
my_doubly_linked_list.print_list()

my_doubly_linked_list.insert(4, 4)

print('\nDLL after insert(4) at end:')
my_doubly_linked_list.print_list()

#
# """
#     EXPECTED OUTPUT:
#     ----------------
#     DLL before insert():
#     1
#     3
#
#     DLL after insert(2) in middle:
#     1
#     2
#     3
#
#     DLL after insert(0) at beginning:
#     0
#     1
#     2
#     3
#
#     DLL after insert(4) at end:
#     0
#     1
#     2
#     3
#     4
#
# """