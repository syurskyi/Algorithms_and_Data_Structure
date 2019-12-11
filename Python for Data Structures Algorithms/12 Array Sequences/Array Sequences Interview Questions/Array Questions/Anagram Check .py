# %%
'''
# Anagram Check
## Problem
Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using
the exact same letters (so you can just rearrange the letters to get a different phrase or word).
For example:
    "public relations" is an anagram of "crap built on lies."
    "clint eastwood" is an anagram of "old west action"
**Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".**
## Solution
Fill out your solution below:
'''

# %%
def anagram(s1,s2):
    pass

# %%
anagram('dog','god')

# %%
anagram('clint eastwood','old west action')

# %%
anagram('aa','bb')

# %%
'''
# Test Your Solution
Run the cell below to test your solution
'''

# %%
"""
RUN THIS CELL TO TEST YOUR SOLUTION
# """
from nose.tools import assert_equal

class AnagramTest(object):

    def test(self, sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print("ALL TEST CASES PASSED")

# Run Tests
t = AnagramTest()
t.test(anagram)
#
# # %%
# t.test(anagram2)
#
# # %%
# '''
# # Good Job!
# '''