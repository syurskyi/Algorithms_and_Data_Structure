c_ ListNode:
    ___ -  val
        val _ val
        prev _ N..
        next _ N..


c_ MyLinkedList:

    ___ -
        head _ N..
        tail _ N..
        size _ 0

    ___ get index
        __ index < 0 or index >_ size:
            r_ -1

        cur _ head

        _____ index !_ 0:
            cur _ cur.next
            index _ index - 1

        r_ cur.val

    ___ addAtHead val
        new_node _ ListNode(val)

        __ head __ N..:
            head _ new_node
            tail _ new_node
        ____
            new_node.next _ head
            head.prev _ new_node
            head _ new_node

        size +_ 1

    ___ addAtTail val
        new_node _ ListNode(val)

        __ head __ N..:
            head _ new_node
            tail _ new_node
        ____
            new_node.prev _ tail
            tail.next _ new_node
            tail _ new_node

        size +_ 1

    ___ addAtIndex index, val
        __ index < 0 or index > size:
            r_
        elif index __ 0:
            addAtHead(val)
        elif index __ size:
            addAtTail(val)
        ____
            cur _ head
            _____ index - 1 !_ 0:
                cur _ cur.next
                index -_ 1

            new_node _ ListNode(val)

            new_node.next _ cur.next
            cur.next.prev _ new_node
            cur.next _ new_node
            new_node.prev _ cur

            size +_ 1

    ___ deleteAtIndex index
        __ index < 0 or index >_ size:
            r_
        elif index __ 0:
            cur _ head.next
            __ cur:
                cur.prev _ N..

            head _ head.next
            size -_ 1

            __ size __ 0:
                tail _ N..
        elif index __ size - 1:
            cur _ tail.prev
            __ cur:
                cur.next _ N..
            tail _ tail.prev

            size -_ 1

            __ size __ 0:
                head _ N..
        ____
            cur _ head
            _____ index - 1 !_ 0:
                cur _ cur.next
                index -_ 1

            cur.next _ cur.next.next
            cur.next.prev _ cur

            size -_ 1


## Example Execution ##
obj _ MyLinkedList()
obj.addAtHead(10)
obj.addAtTail(15)
obj.addAtTail(20)
obj.deleteAtIndex(0)
obj.addAtHead(40)

print(obj.get(1))