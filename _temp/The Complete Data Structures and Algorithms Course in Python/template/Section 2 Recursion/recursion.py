#### Russian Doll recursive function ###

___ openRussianDoll(doll
    __ doll __ 1:
        print("All dolls are opened")
    ____
        openRussianDoll(doll-1)


openRussianDoll(4)


# def recursionMethod(parameters):
#     if  exit from condition satisfied:
#         return some value
#     else:
#         recursionMethod(modified parameters)


___ firstMethod(
    secondMethod()
    print("I am the first Method")

___ secondMethod(
    thirdMethod()
    print("I am the second Method")

___ thirdMethod(
    fourthMethod()
    print("I am the third Method")

___ fourthMethod(
    print("I am the fourth Method")


firstMethod()


___ recursiveMethod(n
    __ n<1:
        print("n is less than 1")
    ____
        recursiveMethod(n-1)
        print(n)

recursiveMethod(4)
 ## Recursion vs Iterarion###

___ powerOfTwo(n
    __ n __ 0:
         r_ 1
    ____
        power _ powerOfTwo(n-1)
        r_ power * 2

print(powerOfTwo(3))

___ powerOfTwoIt(n
    i _ 0
    power _ 1
    _____ i < n:
        power _ power * 2
        i _ i + 1
    r_ power


print(powerOfTwoIt(4))

 ## Factorial###


___ factorial(n
    assert n >_ 0 and int(n) __ n, 'The number must be positive integer only!'
    __ n __ [0,1]:
        r_ 1
    ____
        r_ n * factorial(n-1)


 ## Fibonacci###

___ fibonacci(n
    assert n >_0 and int(n) __ n , 'Fibonacci number cannot be negative number or non integer.'
    __ n __ [0,1]:
        r_ n
    ____
        r_ fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))
