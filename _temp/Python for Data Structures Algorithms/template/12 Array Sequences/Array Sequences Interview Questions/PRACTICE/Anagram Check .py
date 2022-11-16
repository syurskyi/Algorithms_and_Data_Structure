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
# 242. Valid Anagram(https://leetcode.com/problems/valid-anagram/description/)
___ anagram(s, t
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s_s.replace(' ','').lower()
    t_t.replace(' ','').lower()
    
    __(l..(s)!_len(t
        r_ F..
    counter _     # dict
    ___ letter __ s:
        __ letter __ counter:
            counter[letter] +_ 1
        ____
            counter[letter] _ 1

    ___ letter __ t:
        __ letter __ counter:
            counter[letter] -_ 1
        ____
            r_ F..

    ___ k __ counter:
        __ counter[k]!_0:
          r_ F..
    
    r_ T..
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
"""
from nose.tools import assert_equal

c_ AnagramTest o..
    
    ___ testsol
        assert_equal(sol('go go go','gggooo'),T..)
        assert_equal(sol('abc','cba'),T..)
        assert_equal(sol('hi man','hi     man'),T..)
        assert_equal(sol('aabbcc','aabbc'),F..)
        assert_equal(sol('123','1 2'),F..)
        print('ALL TEST CASES PASSED')

# Run Tests
t _ AnagramTest()
t.test(anagram)

# %%
# t.test(anagram2)

# %%
'''
# Good Job!
'''