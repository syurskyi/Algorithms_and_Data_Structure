# Balanced Parentheses Check
# Problem Statement
#
# Given a string of opening and closing parentheses, check whether its balanced. We have 3 types of parentheses:
# round brackets: (), square brackets: [], and curly brackets: {}. Assume that the string doesnt contain any other
# character than these, no spaces words or numbers. As a reminder, balanced parentheses require every opening
# parenthesis to be closed in the reverse order opened. For example ([]) is balanced but ([)] is not.
#
# You can assume the input string has no spaces.
# Solution
#
# Fill out your solution below:

___ balance_check(s
    chars _    # list
    matches _ {')':'(',']':'[','}':'{'}
    ___ c __ s:
        __ c __ matches:
            __ chars.p..  !_ matches[c]:
                r_ F..
        ____
            chars.a..(c)
    r_ chars __    # list
    pass

balance_check('[]')
# True

balance_check('[](){([[[]]])}')
# True

balance_check('()(){]}')
# False

# Test Your Solution

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

c_ TestBalanceCheck o..

    ___ test sol
        assert_equal(sol('[](){([[[]]])}('), F..)
        assert_equal(sol('[{{{(())}}}]((()))'), T..)
        assert_equal(sol('[[[]])]'), F..)
        print ('ALL TEST CASES PASSED')


# Run Tests

t _ TestBalanceCheck()
t.test(balance_check)