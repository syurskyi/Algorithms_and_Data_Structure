#  Created by Elshad Karimov on 3/26/20.
#  Copyright © 2020 Elshad Karimov. All rights reserved.

################ Interview Questions #############
#Question1
___ foo(array
    sum _ 0
    product _ 1
    ___ i __ array:
        sum +_ i
    ___ i __ array:
        product *_ i
    print("Sum = "+s..(sum)+", Product = "+s..(product))

ar1 _ [1,2,3,4]
foo(ar1)

#Question2

___ printPairs(array
    ___ i __ array:
        ___ j __ array:
            print(s..(i)+","+s..(j))


#Question3
___ printUnorderedPairs(array
    ___ i __ r..(0,l..(array
        ___ j __ r..(i+1,l..(array
            print(array[i] + "," + array[j])





#Question4
___ printUnorderedPairs(arrayA, arrayB
    ___ i __ r..(l..(arrayA
        ___ j __ r..(l..(arrayB
            __ arrayA[i] < arrayB[j]:
                print(s..(arrayA[i]) + "," + s..(arrayB[j]))

arrayA _ [1,2,3,4,5]
arrayB _ [2,6,7,8]



#Question5
___ printUnorderedPairs(arrayA, arrayB
    ___ i __ r..(l..(arrayA
        ___ j __ r..(l..(arrayB
            ___ k __ r..(0,100000
                print(s..(arrayA[i]) + "," + s..(arrayB[j]))

# printUnorderedPairss(arrayA,arrayB)


#Question6
___ reverse(array
    ___ i __ r..(0,i..(l..(array)/2
        other _ l..(array)-i-1
        temp _ array[i]
        array[i] _ array[other]
        array[other] _ temp
    print(array)

reverse(arrayA)

#Question8

___ factorial(n
    __ n < 0:
        r_ -1
    ____ n __ 0:
        r_ 1
    ____
        r_ n * factorial(n-1)

print(factorial(3))

#Question9
___ allFib(n
    ___ i __ r..(n
        print(s..(i)+":, " + s..(fib(i)))

___ fib(n
    __ n <_ 0:
        r_ 0
    ____ n __ 1:
        r_ 1
    r_ fib(n-1) + fib(n-2)


allFib(4)

#Question10
___ powersOf2(n
    # print("n:"+str(n))
    __ n < 1:
        r_ 0
    ____ n __ 1:
        print(1)
        r_ 1
    ____
        prev _ powersOf2(i..(n/2))
        # print("prev:"+str(prev))
        print(prev)
        curr _ prev*2
        print(curr)
        r_ curr

powersOf2(50)