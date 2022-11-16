c_ Solution:
    ___ hasCycle head: ListNode) -> bool:
        hare _ head
        turtle _ head

        _____ turtle and hare and hare.next:
            hare _ hare.next.next
            turtle _ turtle.next
            __(turtle == hare
                r_ True
        r_ False
