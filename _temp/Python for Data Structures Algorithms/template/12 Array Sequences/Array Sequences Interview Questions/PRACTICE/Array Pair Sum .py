# %%
'''
# Array Pair Sum
## Problem
Given an integer array, output all the ** *unique* ** pairs that sum up to a specific value **k**.
So the input:
    pair_sum([1,3,2,2],4)
would return **2** pairs:
     (1,3)
     (2,2)
**NOTE: FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS**
## Solution

Fll out your solution below:
'''

# %%
___ pair_sum(arr,k
    counter _ 0
    lookup _ s..
    ___ num __ arr:
        __ k-num __ lookup:
            counter+_1
        ____
            lookup.add(num)
    r_ counter
    pass

# %%
pair_sum([1,3,2,2],4)

# %%
'''
# Test Your Solution
'''

# %%
"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

c_ TestPair o..
    
    ___ testsol
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print('ALL TEST CASES PASSED')
        
#Run tests
t _ TestPair()
t.test(pair_sum)
    

# %%
'''
## Good Job!
'''