# %%
'''
# String Compression
## Problem
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely
"compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though
this technically takes more space.
The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
'''

# %%
'''
## Solution
Fill out your solution below:
'''

# %%
def compress(s):
    pass

# %%
compress('AAAAABBBBCCCC')

# %%
'''
# Test Your Solution
'''

# %%
"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compress)

# %%
'''
## Good Job!
'''