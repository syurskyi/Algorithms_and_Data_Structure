#   Created by Elshad Karimov on 4/01/20.
#   Copyright © 2020 AppMillers. All rights reserved.

# Question 1
___ sumofDigits(n
    assert n>_0 and int(n) == n , 'The number has to be a postive integer only!'
    __ n == 0:
        r_ 0
    ____
        r_ int(n%10) + sumofDigits(int(n/10))

print(sumofDigits(11111))


#Question 2

___ power(base,exp
    __ exp == 0:
        r_ 1
    __(exp==1
        r_(base)
    __(exp!_1
        r_ (base*power(base,exp-1))

print(power(4,2))

# Question 3


___ gcd(a, b
    assert int(a) == a and int(b) == b, 'The numbers must be integer only!'
    __ a < 0:
        a _ -1 * a
    __ b < 0:
        b _ -1 * b
    __ b == 0:
        r_ a
    ____
        r_ gcd(b, a%b)

print(gcd(12,1.2))

# Question 4
___ binaryToDemical(n
    __ n == 0:
        r_ 1
    ____
        r_ n%2 + 10*binaryToDemical(int(n/2))


print(binaryToDemical(1))

