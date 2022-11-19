# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution
    ___ oddEvenList head: ListNode) __ ListNode:
        __(n.. head
            r_ head

        odd _ head
        even _ odd.n..
        evenList _ even

        _____(even ___ even.n..
            odd.n.. _ even.n..
            odd _ odd.n..

            even.n.. _ odd.n..
            even _ even.n..

        odd.n.. _ evenList
        r_ head