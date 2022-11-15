# %%
'''
# Unique Characters in String
## Problem
Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique
characters and should return True. The string 'aabcde' contains duplicate characters and should return false.
'''

# %%
'''
## Solution
Fill out your solution below:
'''

# %%
def uni_char(s):
    pass

# %%
'''
# Test Your Solution
'''

# %%
"""
RUN THIS CELL TO TEST YOUR CODE>
"""
from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')
        
# Run Tests
t = TestUnique()
t.test(uni_char)

# %%
'''
## Good Job!
'''