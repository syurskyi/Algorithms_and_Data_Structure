# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution
    ___ addTwoNumbers l1: ListNode, l2: ListNode) __ ListNode:
        ans _ ListNode(N..)
        pointer _ ans

        carry _ 0
        sum _ 0

        _____(l1!_None __ l2!_None
            sum _ carry
            __(l1!_None
                sum+_l1.val
                l1 _ l1.n..
            __(l2!_None
                sum+_l2.val
                l2 _ l2.val
            
            carry _ i..(sum/10)
            pointer.n..  _ ListNode(sum%10)

            pointer _ pointer.n..
        
        __(carry>0
            pointer.n.. _ ListNode(carry)
        
        r_ ans.n..