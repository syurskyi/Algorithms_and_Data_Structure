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
___ anagram(s1,s2
    p..

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

c_ AnagramTest o..

    ___ test sol
        assert_equal(sol('go go go','gggooo'),T..)
        assert_equal(sol('abc','cba'),T..)
        assert_equal(sol('hi man','hi     man'),T..)
        assert_equal(sol('aabbcc','aabbc'),F..)
        assert_equal(sol('123','1 2'),F..)
        print("ALL TEST CASES PASSED")

# Run Tests
t _ AnagramTest()
t.test(anagram)
#
# # %%
# t.test(anagram2)
#
# # %%
# '''
# # Good Job!
# '''