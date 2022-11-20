#   Created by Elshad Karimov on 18/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

____ LinkedList ______ LinkedList

___ nthToLast(ll, n
    pointer1 _ ll.head
    pointer2 _ ll.head

    ___ i __ r..(n
        __ pointer2 __ N..
            r_ N..
        pointer2 _ pointer2.n..

    _____ pointer2:
        pointer1 _ pointer1.n..
        pointer2 _ pointer2.n..
    r_ pointer1

customLL _ LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(nthToLast(customLL, 3))