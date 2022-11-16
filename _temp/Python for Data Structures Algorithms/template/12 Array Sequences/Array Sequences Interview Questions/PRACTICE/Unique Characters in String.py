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
___ uni_char(s
    u _ set()
    ___ c __ s:
        __ c __ u:
            r_ False
        ____
            u.add(c)
    r_ True
    pass

# %%
'''
## Learn This One Line Solution
'''

# %%
# another 1-line solution
___ uni_char2(s
    r_ l..(set(s)) __ l..(s)
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


c_ TestUnique o..

    ___ test sol
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')
        
# Run Tests
t _ TestUnique()
t.test(uni_char)

# %%
'''
## Good Job!
'''