# Definition for singly-linked list.
c_ ListNode:
    ___ -  val_0, next_None
        ? _ ?
        next _ next


c_ Solution
    ___ reverseList head
        pre _ N..
        cur _ head
        suc _ N..

        _____ cur:
            suc _ ?.n..
            ?.n.. _ pre
            pre _ cur
            cur _ suc

        r_ pre