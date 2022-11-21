
class Node:

    ? ? __init__(self, data):
        self.data _ data
        self.next _ None
        self.previous _ None


class DoublyLinkedList:

    ? ? __init__(self):
        self.head _ None
        self.tail _ None

    # this operation inserts items at the end of the linked list
    # so we have to manipulate the tail node in O(1) running time
    ? ? insert(self, data):

        new_node _ Node(data)

        # when the list is empty
        __ self.head is None:
            self.head _ new_node
            self.tail _ new_node
        # there is at least 1 item in the data structure
        # we keep inserting items at the end of the linked list
        ____
            new_node.previous _ self.tail
            self.tail.next _ new_node
            self.tail _ new_node

    # we can traverse a doubly linked list in both directions
    ? ? traverse_forward(self):

        actual_node _ self.head

        _____ actual_node is not None:
            print("%d" % actual_node.data)
            actual_node _ actual_node.next

    ? ? traverse_backward(self):

        actual_node _ self.tail

        _____ actual_node is not None:
            print("%d" % actual_node.data)
            actual_node _ actual_node.previous


__ _____ __ ____

    linked_list _ DoublyLinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)

    # 1 2 3
    linked_list.traverse_forward()

    # 3 2 1
    linked_list.traverse_backward()


