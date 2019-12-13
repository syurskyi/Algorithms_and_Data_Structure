# Sentence Reversal
# Problem
# Given a string of words, reverse all the words. For example:
# Given
# 'This is the best'
# Return:
# 'best the is This'
# As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:
# '  space here'  and 'space here      '
# both become:
# 'here space'
# Solution
# We could take advantage of Python's abilities and solve the problem with the use of split() and some slicing or use
# of reversed:

def rev_word1(s):
    return " ".join(reversed(s.split()))

#Or

def rev_word2(s):
    return " ".join(s.split()[::-1])

rev_word1('Hi John,   are you ready to go?')
# 'go? to ready you are John, Hi'

rev_word2('Hi John,   are you ready to go?')
# 'go? to ready you are John, Hi'

# While these are valid solutions, in an interview setting you'll have to work out the basic algorithm that is used.
# In this case what we want to do is loop over the text and extract words form the string ourselves.
# Then we can push the words to a "stack" and in the end opo them all to reverse. Let's see what this actually looks
# like:

def rev_word3(s):
    """
    Manually doing the splits on the spaces.
    """

    words = []
    length = len(s)
    spaces = [' ']

    # Index Tracker
    i = 0

    # While index is less than length of string
    while i < length:

        # If element isn't a space
        if s[i] not in spaces:

            # The word starts at this index
            word_start = i

            while i < length and s[i] not in spaces:
                # Get index where word ends
                i += 1
            # Append that word to the list
            words.append(s[word_start:i])
        # Add to index
        i += 1

    # Join the reversed words
    return " ".join(reversed(words))

rev_word3('   Hello John    how are you   ')
# 'you are how John Hello'

rev_word3('    space before')
# 'before space'

# If you want you can further develop this solution so its all manual, you can create your own reversal function.
# Test Your Solution

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

from nose.tools import assert_equal


class ReversalTest(object):

    def test(self, sol):
        assert_equal(sol('    space before'), 'before space')
        assert_equal(sol('space after     '), 'after space')
        assert_equal(sol('   Hello John    how are you   '), 'you are how John Hello')
        assert_equal(sol('1'), '1')
        print("ALL TEST CASES PASSED")


# Run and test
t = ReversalTest()
t.test(rev_word3)