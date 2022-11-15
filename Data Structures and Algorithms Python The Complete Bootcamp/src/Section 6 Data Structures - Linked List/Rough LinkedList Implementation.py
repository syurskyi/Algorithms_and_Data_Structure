class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self):
        pass

    def delete(self):
        pass

    # Traverse Method To Print All Elements #
    def traverse(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next


n1 = Node(3)
n2 = Node(7)
n3 = Node(2)
n4 = Node(9)

LL = LinkedList()
LL.head = n1
n1.next = n2
n2.next = n3
n3.next = n4

# Traverse Method To Print All Elements #
LL.traverse()