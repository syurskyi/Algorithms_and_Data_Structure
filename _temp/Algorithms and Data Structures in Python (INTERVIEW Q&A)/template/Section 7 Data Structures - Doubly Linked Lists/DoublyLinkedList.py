#
# c_ Node
#
#     ? ? -  data
#         ? _ ?
#         next _ N..
#         previous _ N..
#
#
# c_ DoublyLinkedList
#
#     ? ? -
#         head _ N..
#         tail _ N..
#
#     # this operation inserts items at the end of the linked list
#     # so we have to manipulate the tail node in O(1) running time
#     ? ? insert data
#
#         new_node _ ? ?
#
#         # when the list is empty
#         __ h.. __ N..
#             ? _ ?
#             t.. _ ?
#         # there is at least 1 item in the data structure
#         # we keep inserting items at the end of the linked list
#         ____
#             ?.p.. _ ?
#             ?.n.. _ ?
#             t.. _ ?
#
#     # we can traverse a doubly linked list in both directions
#     ? ? traverse_forward
#
#         actual_node _ ?
#
#         _____ ? __ n.. N..
#             print("_d" _ ?.d..
#             a.. _ ?.n..
#
#     ? ? traverse_backward
#
#         a.. _ t..
#
#         _____ ? __ n.. N..
#             print("_d" _ ?.d..
#             a.. _ ?.p..
#
#
# __ _____ __ ____
#
#     linked_list _ DoublyLinkedList()
#     linked_list.insert(1)
#     linked_list.insert(2)
#     linked_list.insert(3)
#
#     # 1 2 3
#     linked_list.traverse_forward()
#
#     # 3 2 1
#     linked_list.traverse_backward()
#
#
