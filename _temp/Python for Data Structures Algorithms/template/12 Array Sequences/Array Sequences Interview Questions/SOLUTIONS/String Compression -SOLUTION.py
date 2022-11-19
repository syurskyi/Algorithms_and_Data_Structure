# String Compression
# Problem
#
# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can
# falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even
# though this technically takes more space.
# The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
# Solution
# Since Python strings are immutable, we'll need to work off of a list of characters, and at the end convert that list
# back into a string with a join statement.
# The solution below should yield us with a Time and Space complexity of O(n). Let's take a look with careful attention
# to the explanatory comments:

___ compress(s
    """
    This solution compresses without checking. Known as the RunLength Compression algorithm.
    """

    # Begin Run as empty string
    r _ ""
    l _ l..(s)

    # Check for length 0
    __ l __ 0:
        r_ ""

    # Check for length 1
    __ l __ 1:
        r_ s + "1"

    # Intialize Values
    last _ s[0]
    cnt _ 1
    i _ 1

    _____ i < l:

        # Check to see if it is the same letter
        __ s[i] __ s[i - 1]:
            # Add a count if same as previous
            cnt +_ 1
        ____
            # Otherwise store the previous data
            r _ r + s[i - 1] + s..(cnt)
            cnt _ 1

        # Add to index count to terminate while loop
        i +_ 1

    # Put everything back into run
    r _ r + s[i - 1] + s..(cnt)

    r_ r

compress('AAAAABBBBCCCC')
# 'A5B4C4'

# Test Your Solution
"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

c_ TestCompress o..

    ___ test sol
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')

# Run Tests
t _ TestCompress()
t.test(compress)