#
# c_ Node
#
#     ? ? -  data
#         ? _ ?
#         next_node _ N..
#
#     ? ? -r
#         r_ s.. ?
#
#
# c_ LinkedList
#
#     ? ? -
#         # this is the first node of the linked list
#         # WE CAN ACCESS THIS NODE EXCLUSIVELY !!!
#         head _ N..
#         num_of_nodes _ 0
#
#     # O(1) constant running time
#     ? ? insert_start data
#         ? +_ 1
#         new_node _ ?
#
#         # the head is NULL (so the data structure is empty)
#         __ head __ N..
#             ? _ ?
#         # so this is when the linked list is not empty
#         ____
#             # we have to update the references
#             ?.n.. _ ?
#             ? _ ?
#
#     # O(N)
#     ? ? insert_end data
#         ? +_ 1
#         new_node _ ? ?
#
#         # check if the linked list is empty
#         __ head __ N..
#             ? _ ?
#         ____
#             # this is when the linked list is not empty
#             actual_node _ ?
#
#             # this is why it has O(N) linear running time
#             _____ ?.n.. __ n.. N..
#                 a.. _ ?.n..
#
#             # actual_node is the last node: so we insert the new_node
#             # right after the actual_node
#             ?.n.. _ ?
#
#     # O(1) constant running time
#     ? ? size_of_list
#         r_ n..
#
#     # O(N) linear running time
#     ? ? traverse
#
#         actual_node _ ?
#
#         _____ ? __ n.. N..
#             print ?
#             a.. _ ?.n..
#
#     # O(N) linear running time
#     ? ? remove data
#
#         # the list is empty
#         __ head __ N..
#             r_
#
#         actual_node _ ?
#         # we have to track the previous node for future pointer updates
#         # this is why doubly linked lists are better - we can get the previous
#         # node (here with linked lists it is impossible)
#         previous_node _ N..
#
#         # search for the item we want to remove (data)
#         _____ ? __ n.. N.. a.. ?.d.. !_ ?
#             p.. _ ?
#             a.. _ ?.n..
#
#         # search miss
#         __ a.. __ N..
#             r_
#
#         # update the references (so we have the data we want to remove)
#         # the head node is the one we want to remove
#         __ p.. __ N..
#             h.. _ ?.n..
#         ____
#             # remove an internal node by updating the pointers
#             # NO NEED TO del THE NODE BECAUSE THE GARBAGE COLLECTOR WILL DO THAT
#             ?.n.. _ ?.n..
#
#
# __ _____ __ ____
#     linked_list _ LinkedList()
#     linked_list.insert_end(10)
#     linked_list.insert_start(100)
#     linked_list.insert_start(1000)
#     linked_list.insert_end('Adam')
#     linked_list.insert_end(7.5)
#     linked_list.traverse()
#     print('-------')
#     linked_list.remove(1000)
#     linked_list.traverse()
#
#
