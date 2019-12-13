# Reverse a String
# This interview question requires you to reverse a string using recursion. Make sure to think of the base case here.
# Again, make sure you use recursion to accomplish this. Do not slice (e.g. string[::-1]) or use iteration,
# there muse be a recursive call for the function.
# Solution
# In order to reverse a string using recursion we need to consider what a base and recursive case would look like.
# Here we've set a base case to be when the length of the string we are passing through the function is length
# less than or equal to 1.
# During the recursive case we grab the first letter and add it on to the recursive call.
#
def reverse(s):

    # Base Case
    if len(s) <= 1:
        return s

    # Recursion
    return reverse(s[1:]) + s[0]

reverse('hello world')
# 'dlrow olleh'
#
# Test Your Solution
#
# Run the cell below to test your solution against the following cases:

string = 'hello'
string = 'hello world'
string = '123456789'

# '''
# RUN THIS CELL TO TEST YOUR FUNCTION AGAINST SOME TEST CASES
# '''

from nose.tools import assert_equal

class TestReverse(object):

    def test_rev(self,solution):
        assert_equal(solution('hello'),'olleh')
        assert_equal(solution('hello world'),'dlrow olleh')
        assert_equal(solution('123456789'),'987654321')

        print 'PASSED ALL TEST CASES!'

# Run Tests
test = TestReverse()
test.test_rev(reverse)

# PASSED ALL TEST CASES!
#
# Extra Notes
#
# The "trick" to this question was thinking about what a base case would look like when reversing a string recursively. It takes a lot of practice to be able to begin thinking like this, so don't worry if you're struggling! However it is important to fully understand the solution!
#
# Good Job!