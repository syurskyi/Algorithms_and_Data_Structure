# Reverse a String
#
# This interview question requires you to reverse a string using recursion. Make sure to think of the base case here.
# Again, make sure you use recursion to accomplish this. Do not slice (e.g. string[::-1]) or use iteration,
# there must be a recursive call for the function.
# Fill out your solution below

def reverse(s):
    if(len(s)<=1):
        return s
    else:
        m = int(len(s)/2)
        return reverse(s[m:]) + (reverse((s[:m])))
    pass

reverse('hello world')
# 'dlrow olleh'
#
# Test Your Solution
#
# Run the cell below to test your solution against the following cases:
#
string = 'hello'
string = 'hello world'
string = '123456789'
#
# '''
# RUN THIS CELL TO TEST YOUR FUNCTION AGAINST SOME TEST CASES
# '''

from nose.tools import assert_equal

class TestReverse(object):

    def test_rev(self,solution):
        assert_equal(solution('hello'),'olleh')
        assert_equal(solution('hello world'),'dlrow olleh')
        assert_equal(solution('123456789'),'987654321')

        print ('PASSED ALL TEST CASES!')

# Run Tests
test = TestReverse()
test.test_rev(reverse)

# PASSED ALL TEST CASES!
#
# Good Luck!