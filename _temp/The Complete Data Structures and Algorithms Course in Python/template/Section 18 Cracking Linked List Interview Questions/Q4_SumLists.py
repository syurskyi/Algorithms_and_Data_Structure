#   Created by Elshad Karimov on 18/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Question 4 - Sum Lists

____ LinkedList ______ LinkedList

___ sumList(llA, llB
    n1 _ llA.head
    n2 _ llB.head
    carry _ 0
    ll _ LinkedList()

    _____ n1 __ n2:
        result _ carry
        __ n1:
            result +_ n1.value
            n1 _ n1.n..
        __ n2:
            result +_ n2.value
            n2 _ n2.n..
        ll.add(i..(result % 10))
        carry _ result / 10
    
    r_ ll

llA _ LinkedList()
llA.add(7)
llA.add(1)
llA.add(6)


llB _ LinkedList()
llB.add(5)
llB.add(9)
llB.add(2)
print(llA)
print(llB)
print(sumList(llA, llB))
