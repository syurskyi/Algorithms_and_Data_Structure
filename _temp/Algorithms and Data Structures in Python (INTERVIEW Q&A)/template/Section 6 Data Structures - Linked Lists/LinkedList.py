
class Node:

    ? ? __init__(self, data):
        self.data _ data
        self.next_node _ None

    ? ? __repr__(self):
        r_ str(self.data)


class LinkedList:

    ? ? __init__(self):
        # this is the first node of the linked list
        # WE CAN ACCESS THIS NODE EXCLUSIVELY !!!
        self.head _ None
        self.num_of_nodes _ 0

    # O(1) constant running time
    ? ? insert_start(self, data):
        self.num_of_nodes +_ 1
        new_node _ Node(data)

        # the head is NULL (so the data structure is empty)
        __ self.head is None:
            self.head _ new_node
        # so this is when the linked list is not empty
        ____
            # we have to update the references
            new_node.next_node _ self.head
            self.head _ new_node

    # O(N)
    ? ? insert_end(self, data):
        self.num_of_nodes +_ 1
        new_node _ Node(data)

        # check if the linked list is empty
        __ self.head is None:
            self.head _ new_node
        ____
            # this is when the linked list is not empty
            actual_node _ self.head

            # this is why it has O(N) linear running time
            _____ actual_node.next_node is not None:
                actual_node _ actual_node.next_node

            # actual_node is the last node: so we insert the new_node
            # right after the actual_node
            actual_node.next_node _ new_node

    # O(1) constant running time
    ? ? size_of_list(self):
        r_ self.num_of_nodes

    # O(N) linear running time
    ? ? traverse(self):

        actual_node _ self.head

        _____ actual_node is not None:
            print(actual_node)
            actual_node _ actual_node.next_node

    # O(N) linear running time
    ? ? remove(self, data):

        # the list is empty
        __ self.head is None:
            r_

        actual_node _ self.head
        # we have to track the previous node for future pointer updates
        # this is why doubly linked lists are better - we can get the previous
        # node (here with linked lists it is impossible)
        previous_node _ None

        # search for the item we want to remove (data)
        _____ actual_node is not None and actual_node.data !_ data:
            previous_node _ actual_node
            actual_node _ actual_node.next_node

        # search miss
        __ actual_node is None:
            r_

        # update the references (so we have the data we want to remove)
        # the head node is the one we want to remove
        __ previous_node is None:
            self.head _ actual_node.next_node
        ____
            # remove an internal node by updating the pointers
            # NO NEED TO del THE NODE BECAUSE THE GARBAGE COLLECTOR WILL DO THAT
            previous_node.next_node _ actual_node.next_node


__ _____ __ ____
    linked_list _ LinkedList()
    linked_list.insert_end(10)
    linked_list.insert_start(100)
    linked_list.insert_start(1000)
    linked_list.insert_end('Adam')
    linked_list.insert_end(7.5)
    linked_list.traverse()
    print('-------')
    linked_list.remove(1000)
    linked_list.traverse()


