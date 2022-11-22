c_ ListNode:
    ___ -  val
        val _ val
        p.. _ N..
        n.. _ N..


c_ MyLinkedList:

    ___ -
        h.. _ N..
        t.. _ N..
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

        __ h.. __ N..
            h.. _ ?
            tail _ new_node
        ____
            ?.n.. _ head
            ?.p.. _ new_node
            h.. _ ?

        size +_ 1

    ___ addAtTail val
        new_node _ ListNode(val)

        __ h.. __ N..
            h.. _ ?
            tail _ new_node
        ____
            ?.p.. _ tail
            ?.n.. _ new_node
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

            ?.n.. _ ?.n..
            ?.n...prev _ new_node
            ?.n.. _ new_node
            ?.p.. _ cur

            size +_ 1

    ___ deleteAtIndex index
        __ index < 0 __ index >_ size:
            r_
        ____ index __ 0:
            cur _ ?.n..
            __ cur:
                ?.p.. _ N..

            h.. _ ?.n..
            size -_ 1

            __ size __ 0:
                t.. _ N..
        ____ index __ size - 1:
            cur _ ?.p..
            __ cur:
                ?.n.. _ N..
            t.. _ ?.p..

            size -_ 1

            __ size __ 0:
                h.. _ N..
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