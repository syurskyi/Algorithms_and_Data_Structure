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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

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
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

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
    def get(self, index):
        # __ ? < 0 __ ? >_ ?
        #     r_ N..
        temp = self.head
        # __ ? < ?/2
        #     ___ _ __ r_ ?
        #         ? _ ?.n..
        # ____
        #     t.. _ t..
        #     ___ _ __ r_ ? -1 ? -1
        #         ? _ ?.p..
        return temp

#     ___ set_value  ? value
#         t.. _ g.. ?
#         __ ?
#             ?.? _ ?
#             r_ T..
#         r_ F..
#
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if self.length == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        __ ? __ 0
            r_ p..
        __ ? __ ? - 1
            r_ p..

        t.. _ get ?

        ?.n__.p.. _ ?.p..
        ?.p...n.. _ ?.n..
        t__.n.. _ N..
        ?.p.. _ N..

        ? -_ 1
        r_ ?



my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

print('DLL before remove():')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() in middle:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(0).value)
print('DLL after remove() of first node:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() of last node:')
my_doubly_linked_list.print_list()

#
# """
#     EXPECTED OUTPUT:
#     ----------------
#     DLL before remove():
#     1
#     2
#     3
#     4
#     5
#
#     Removed node:
#     3
#     DLL after remove() in middle:
#     1
#     2
#     4
#     5
#
#     Removed node:
#     1
#     DLL after remove() of first node:
#     2
#     4
#     5
#
#     Removed node:
#     5
#     DLL after remove() of last node:
#     2
#     4
#
# """
#
