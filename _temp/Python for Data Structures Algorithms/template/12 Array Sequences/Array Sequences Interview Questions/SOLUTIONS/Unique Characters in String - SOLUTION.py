# Unique Characters in String
# Problem
#
# Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all
# unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.
# Solution
#
# We'll show two possible solutions, one using a built-in data structure and a built in function, and another using
# a built-in data structure but using a look-up method to check if the characters are unique

___ uni_char(s
    r_ l..(set(s)) __ l..(s)

___ uni_char2(s
    chars _ set()
    ___ let __ s:
        # Check if in set
        __ let __ chars:
            r_ False
        ____
            #Add it to the set
            chars.add(let)
    r_ True

# Test Your Solution
"""
RUN THIS CELL TO TEST YOUR CODE>
"""
from nose.tools import assert_equal


c_ TestUnique o..

    ___ test sol
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')


# Run Tests
t _ TestUnique()
t.test(uni_char)

