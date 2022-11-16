# String Permutation
# Problem Statement
# Given a string, write a function that uses 001_recursion to output a list of all the possible permutations of that string.
# For example, given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
# Note: If a character is repeated, treat each occurence as distinct, for example an input of 'xxx' would return
# a list with 6 "versions" of 'xxx'
# Fill Out Your Solution Below
#
# Let's think about what the steps we need to take here are:

___ permute(s
    output _ []

    __ len(s) <_ 1:
        output_[s]
    ____
        ___ i, let __ enumerate(s
            ___ perm __ permute(s[:i]+s[i+1:]
                output+_[let+perm]
    r_ output

permute('abc')
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
#
# Test Your Solution
#
# """
# RUN THIS CELL TO TEST YOUR SOLUTION.
# """

from nose.tools import assert_equal

c_ TestPerm o..

    ___ testsolution

        assert_equal(sorted(solution('abc')),sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        assert_equal(sorted(solution('dog')),sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']) )

        print ('All test cases passed.')



# # Run Tests
t _ TestPerm()
t.test(permute)
#
# All test cases passed.
#
# Good Luck!