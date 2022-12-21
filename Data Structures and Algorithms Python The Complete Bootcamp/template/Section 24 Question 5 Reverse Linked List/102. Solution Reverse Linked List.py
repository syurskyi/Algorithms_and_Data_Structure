# Definition ___ singly-linked list.
c_ ListNode:
    ___  -  val=0, next=N..):
        val = val
        next = next


c_ Solution:
    ___ reverseList  head):
        pre = N..
        cur = head
        suc = N..

        ______ cur:
            suc = cur.next
            cur.next = pre
            pre = cur
            cur = suc

        r_ pre