#  Created by Elshad Karimov on 3/17/20.
#  Copyright © 2020 Elshad Karimov. All rights reserved.


array _ [1, 2, 3, 4, 5]

######  Constant time complexity  #######
print('######  Constant time complexity  #######')
print(array[0])


######  Linear time complexity  #######
print('######  Linear time complexity  #######')
___ element __ array:
     print(element)


######  Logarithmic time complexity  #######
print('######  Logarithmic time complexity  #######')
___ index __ range(0,l..(array),3
     print(array[index])


######  Quadratic time complexity  #######
print('######  Quadratic time complexity  #######')
___ x __ array:
    ___ y __ array:
         print(x,y)


######  Exponential time complexity  #######
print('######  Exponential time complexity  #######')
___ fibonacci(n
    __ n <_ 1:
        r_ n
    r_ fibonacci(n-1) + fibonacci(n-2)


######  Add vs Multiply ####### 
arrayA _ [1,2,3,4,5,6,7,8,9]
arrayB _ [11,12,13,14,15,16,17,18,19] 

___ a __ arrayA:
    print(a)

___ b __ arrayB:
    print(b)

___ a __ arrayA:
    ___ b __ arrayB:
        print(a,b)

######  Iterative algorithm - finding the biggest number in the array ####### 

sample1Array _ [1,10,45,33,23,45,67,2,3,33,55,11,65,76,34,35,27,99]

___ findBiggestNumber(sampleArray
    biggestNumber _ sampleArray[0]
    ___ index __ range(1,l..(sampleArray)):
        __ sampleArray[index] > biggestNumber:
            biggestNumber _ sampleArray[index]
    print(biggestNumber)

findBiggestNumber(sample1Array)

######  Recursive algorithm - finding the biggest number in the array ####### 

___ findMaxNumRec(sampleArray, n
    __ n __ 1:
       r_ sampleArray[0]
    r_ max(sampleArray[n-1],findMaxNumRec(sampleArray,n-1))

print(findMaxNumRec(sample1Array,l..(sample1Array)))


######  Recursive algorithm multiple calls ####### 

___ f(n
    __ n <_ 1:
        r_ 1
    r_ f(n-1) + f(n-1)

print(f(3))







######  Quiz Questions ####### 


___ f1(n
    __ n <_ 0:
        r_ 1
    ____
        r_ 1 + f1(n-1)


___ f2(n
    __ n <_ 0:
        r_ 1
    ____
        r_ 1 + f2(n-5)


___ f3(n
    __ n <_ 0:
        r_ 1
    ____
        r_ 1 + f3(n/5)


___ f4(n,m,o
    __ n<_0:
        print(n,m,o)
    ____
        f4(n-1,m+1,o)
        f4(n-1,m,o+1)

___ f5(n
    ___ i __ range(0,n,2
        print(i)  
    __ n<_0:
        r_ 1
    ____
        r_ 1 + f5(n-5)

