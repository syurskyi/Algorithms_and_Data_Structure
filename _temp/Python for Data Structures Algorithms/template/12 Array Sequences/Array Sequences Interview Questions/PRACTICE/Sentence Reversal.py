# %%
'''
# Sentence Reversal
## Problem
Given a string of words, reverse all the words. For example:
Given:
    'This is the best'
Return:
    'best the is This'
As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:
    '  space here'  and 'space here      '
both become:
    'here space'
## Solution
Fill out your solution below:
'''

# %%
___ rev_word(s
    r_ " ".j..(reversed(s.split()))
    pass

# %%
rev_word('Hi John,   are you ready to go?')

# %%
rev_word('    space before')

# %%
rev_word('space after     ')

# %%
'''
## Learn
- " ".join()
- reversed()
- s.split()
'''

# %%
# reversed()
'''
Init signature: reversed(self, /, *args, **kwargs)
Docstring:     
reversed(sequence) -> reverse iterator over values of the sequence

Return a reverse iterator
Type:           type
'''

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

c_ ReversalTest o..
    
    ___ testsol
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print ("ALL TEST CASES PASSED")
        
# Run and test
t _ ReversalTest()
t.test(rev_word)

# %%
'''
## Good Job!
'''