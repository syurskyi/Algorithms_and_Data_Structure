# %%
'''
# Largest Continuous Sum
## Problem
Given an array of integers (positive and negative) find the largest continuous sum.
## Solution
Fill out your solution below:
'''

# %%
___ large_cont_sum(arr
    __ len(arr) == 0:
        r_ 0
    
    max_num _ sum _ arr[0]# max=sum=arr[0] bug: TypeError: 'int' object is not callable. (Do not use the keyword!)
    
    ___ n __ arr[1:]:
        sum _ max(sum+n, n)
        max_num _ max(sum, max_num)
    r_ max_num
    pass

# %%
large_cont_sum([1,2,-1,3,4,10,10,-10,-1])

# %%
'''
____
Many times in an interview setting the question also requires you to report back the start and end points of the sum.
Keep this in mind and see if you can solve that problem, we'll see it in the mock interview section of the course!
'''

# %%
'''
# Test Your Solution
'''

# %%
from nose.tools import assert_equal

c_ LargeContTest o..
    ___ testsol
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print ('ALL TEST CASES PASSED')
        
#Run Test
t _ LargeContTest()
t.test(large_cont_sum)

# %%
'''
## Good Job!
'''