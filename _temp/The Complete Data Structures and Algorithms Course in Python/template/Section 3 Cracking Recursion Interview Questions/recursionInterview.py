#   Created by Elshad Karimov on 4/01/20.
#   Copyright © 2020 AppMillers. All rights reserved.

# Question 1
___ sumofDigits(n
    assert n>_0 ___ i..(n) __ n , 'The number has to be a postive integer only!'
    __ n __ 0:
        r_ 0
    ____
        r_ i..(n_10) + sumofDigits(i..(n/10))

print(sumofDigits(11111))


#Question 2

___ power(base,exp
    __ exp __ 0:
        r_ 1
    __(exp__1
        r_(base)
    __(exp!_1
        r_ (base*power(base,exp-1))

print(power(4,2))

# Question 3


___ gcd(a, b
    assert i..(a) __ a ___ i..(b) __ b, 'The numbers must be integer only!'
    __ a < 0:
        a _ -1 * a
    __ b < 0:
        b _ -1 * b
    __ b __ 0:
        r_ a
    ____
        r_ gcd(b, a_b)

print(gcd(12,1.2))

# Question 4
___ binaryToDemical(n
    __ n __ 0:
        r_ 1
    ____
        r_ n_2 + 10*binaryToDemical(i..(n/2))


print(binaryToDemical(1))

