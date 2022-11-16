# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution:
    ___ oddEvenList head: ListNode) -> ListNode:
        __(n.. head
            r_ head

        odd _ head
        even _ odd.next
        evenList _ even

        _____(even and even.next
            odd.next _ even.next
            odd _ odd.next

            even.next _ odd.next
            even _ even.next

        odd.next _ evenList
        r_ head