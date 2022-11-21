c_ ListNode:
    ___ -  val
        val _ val
        p.. _ N..
        n.. _ N..


c_ MyLinkedList:

    ___ -
        head _ N..
        tail _ N..
        size _ 0

    ___ get index
        __ index < 0 __ index >_ size:
            r_ -1

        cur _ head

        _____ index !_ 0:
            cur _ ?.n..
            index _ index - 1

        r_ ?.v..

    ___ addAtHead val
        new_node _ ListNode(val)

        __ head __ N..
            h.. _ ?
            tail _ new_node
        ____
            new_node.n.. _ head
            head.p.. _ new_node
            h.. _ ?

        size +_ 1

    ___ addAtTail val
        new_node _ ListNode(val)

        __ head __ N..
            h.. _ ?
            tail _ new_node
        ____
            new_node.p.. _ tail
            tail.n.. _ new_node
            tail _ new_node

        size +_ 1

    ___ addAtIndex index, val
        __ index < 0 __ index > size:
            r_
        ____ index __ 0:
            addAtHead(val)
        ____ index __ size:
            addAtTail(val)
        ____
            cur _ head
            _____ index - 1 !_ 0:
                cur _ ?.n..
                index -_ 1

            new_node _ ListNode(val)

            new_node.n.. _ ?.n..
            ?.n...prev _ new_node
            ?.n.. _ new_node
            new_node.p.. _ cur

            size +_ 1

    ___ deleteAtIndex index
        __ index < 0 __ index >_ size:
            r_
        ____ index __ 0:
            cur _ head.n..
            __ cur:
                ?.p.. _ N..

            head _ head.n..
            size -_ 1

            __ size __ 0:
                tail _ N..
        ____ index __ size - 1:
            cur _ tail.p..
            __ cur:
                ?.n.. _ N..
            tail _ tail.p..

            size -_ 1

            __ size __ 0:
                head _ N..
        ____
            cur _ head
            _____ index - 1 !_ 0:
                cur _ ?.n..
                index -_ 1

            ?.n.. _ ?.n...next
            ?.n...prev _ cur

            size -_ 1


## Example Execution ##
obj _ MyLinkedList()
obj.addAtHead(10)
obj.addAtTail(15)
obj.addAtTail(20)
obj.deleteAtIndex(0)
obj.addAtHead(40)

print(obj.get(1))