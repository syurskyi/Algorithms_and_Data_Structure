# String Permutation
# Problem Statement
# Given a string, write a function that uses recursion to output a list of all the possible permutations of that string.
# For example, given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
# Note: If a character is repeated, treat each occurence as distinct, for example an input of 'xxx' would return
# a list with 6 "versions" of 'xxx'
# Fill Out Your Solution Below
#
# Let's think about what the steps we need to take here are:

def permute(s):
    output = []

    if len(s) <= 1:
        output=[s]
    else:
        for i, let in enumerate(s):
            for perm in permute(s[:i]+s[i+1:]):
                output+=[let+perm]
    return output

permute('abc')
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
#
# Test Your Solution
#
# """
# RUN THIS CELL TO TEST YOUR SOLUTION.
# """

from nose.tools import assert_equal

class TestPerm(object):

    def test(self,solution):

        assert_equal(sorted(solution('abc')),sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        assert_equal(sorted(solution('dog')),sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']) )

        print ('All test cases passed.')



# # Run Tests
t = TestPerm()
t.test(permute)
#
# All test cases passed.
#
# Good Luck!