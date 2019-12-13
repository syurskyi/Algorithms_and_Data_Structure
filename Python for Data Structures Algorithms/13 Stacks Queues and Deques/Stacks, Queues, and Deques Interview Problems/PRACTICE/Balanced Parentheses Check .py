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

def balance_check(s):
    chars = []
    matches = {')':'(',']':'[','}':'{'}
    for c in s:
        if c in matches:
            if chars.pop() != matches[c]:
                return False
        else:
            chars.append(c)
    return chars == []
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

class TestBalanceCheck(object):

    def test(self, sol):
        assert_equal(sol('[](){([[[]]])}('), False)
        assert_equal(sol('[{{{(())}}}]((()))'), True)
        assert_equal(sol('[[[]])]'), False)
        print ('ALL TEST CASES PASSED')


# Run Tests

t = TestBalanceCheck()
t.test(balance_check)