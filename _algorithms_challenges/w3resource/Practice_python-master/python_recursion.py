""" Python Data Structures and Algorithms :
Recursion - Exercises, Practice, Solution

Author: Yosef Fastow
Created: 6/16/2016
"""

import itertools


# 1
def sum_of_list(the_list):
    """ calculate the sum of a list of numbers """
    answer = 0
    for num in the_list:
        answer += num
    return answer


# print(sum_of_list([1,2,3,4]))

# 2


# 3
def recurssion_list_sum(many_list):
    """ adds the sum of numbers lists no matter list how there """
    lists = itertools.chain(many_list)
    answer = 0
    for num in lists:
        if type(num) == type([]):
            answer += recurssion_list_sum(num)
        else:
            answer += num
            
    return answer


# print(recurssion_list_sum([1, 2, [3,[4,5]], [5,6]]))


# 4
def factoral(number):
    """ returns the factoral or X! of a given number """
    answer = 1
    if number < 0:
        return False
    elif number == 1 or number == 0:
        return 1
    else:
        for num in range(1,number+1):
            answer *= num
    return answer


# print(factoral(20))


# 5
def fibonacci_sequence(num):
    """ determines the fibonacci_sequence of a given number"""
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    fibonacci_list = [0,1]
    for num in range(1,num):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    return fibonacci_list[-1]


# print(fibonacci_sequence(12))


# 6
def sum_digits(num):
    """ gets the sum of all digits in given number"""
    answer = 0
    for digit in str(num):
        answer += int(digit)
    return answer


# print(sum_digits(345))
# print(sum_digits(45))


# 7
def sum_series(number):
    """ alculate the sum of the positive integers of n+(n-2)+(n-4)...
    (until n-x =< 0)
    """
    if number % 2 == 0:
        range_list = [n for n in range(1, number) if n % 2 == 0]
    else:
       range_list = [n for n in range(1, number) if n % 2 != 0] 
    for num in range_list[::-1]:
        number += num
    return number

# print(sum_series(6))
# print(sum_series(13))


# 8
def hermonic_sum(amount_times):
    """ returns the hermonic sum (sum of reciprocals of the positive integers
    ex:1/2 + 1/4 + 1/8 + 1/16 + 1/32 + ...)
    """
    total = 0
    fraction = 1
    for num in range(amount_times):
        fraction = fraction * 2
        total += (1/(fraction))
    return round(total, 10)

# print(hermonic_sum(4))


# 9
def geometric_sum(times):
    """ calculates geometric series which is a series with a constant
    ratio between successive terms. ex 1/1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 ...

    """
    total = 0
    for num in range(1,times+1):
        total += (1/num)
    return round(total, 5)

# print(geometric_sum(5))
# print(geometric_sum(8))


# 10
def power(num, by_power):
    """calculates the value of 'num' by the power of 'by_power' """
    if by_power < 1:
        return 1
    total = 1
    for n in range(by_power):
        total = total * num
    return total

print(power(2, 7))
