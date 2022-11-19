# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


c_ Solution

    ___ mergeTwoLists l1, l2
        cur _ ListNode(0)
        ans _ cur

        _____(l1 ___ l2
            __(l1.val > l2.val
                cur.n.. _ l2
                l2 _ l2.n..

            ____
                cur.n.. _ l1
                l1 _ l1.n..
            cur _ cur.n..

        _____(l1
            cur.n.. _ l1
            l1 _ l1.n..
            cur _ cur.n..
        _____(l2
            cur.n.. _ l2
            l2 _ l2.n..
            cur _ cur.n..
        r_ ans.n..

    ___ mergeKLists lists: List[ListNode]) __ ListNode:
        __(l..(lists) __ 0
            r_ N..

        i _ 0
        last _ l..(lists)-1
        j _ last

        _____(last !_ 0
            i _ 0
            j _ last

            _____(j > i
                lists[i] _ mergeTwoLists(lists[i], lists[j])
                i +_ 1
                j -_ 1
                last _ j

        r_ lists[0]
