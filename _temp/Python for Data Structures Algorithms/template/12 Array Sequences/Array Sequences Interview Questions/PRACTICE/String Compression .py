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
___ compress(s
    r _ ""
    l _ len(s)
    
    __ l==0:
        r_ ''
    __ l==1:
        r_ s+'1'
    
    last _ s[0]
    cnt _ 1
    i_1
    
    _____ i<l:
        __ s[i]==s[i-1]:
            cnt +_ 1
        ____
            r_r+s[i-1]+str(cnt)
            cnt_1
        i+_1
    r _ r+s[i-1]+str(cnt)
    r_ r
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

c_ TestCompress o..

    ___ test sol
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print ('ALL TEST CASES PASSED')

# Run Tests
t _ TestCompress()
t.test(compress)

# %%
'''
## Good Job!
'''