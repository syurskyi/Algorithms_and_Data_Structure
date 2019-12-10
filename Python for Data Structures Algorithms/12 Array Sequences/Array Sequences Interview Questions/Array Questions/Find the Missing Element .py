# %%
'''
# Find the Missing Element
## Problem
Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and
deleting a random element. Given these two arrays, find which element is missing in the second array.
Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
Input:
    finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
Output:
    5 is the missing number
## Solution
Fill out your solution below:
'''

# %%
def finder(arr1,arr2):
    
    pass

# %%
arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
finder(arr1,arr2)

# %%
arr1 = [5,5,7,7]
arr2 = [5,7,7]

finder(arr1,arr2)

# %%
'''
_____
'''

# %%
'''
# Test Your Solution
'''

# %%
"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestFinder(object):
    
    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print 'ALL TEST CASES PASSED'

# Run test
t = TestFinder()
t.test(finder)

# %%
'''
## Good Job!
'''