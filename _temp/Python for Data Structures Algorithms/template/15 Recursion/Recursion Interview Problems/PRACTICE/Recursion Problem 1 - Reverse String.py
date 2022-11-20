# Reverse a String
#
# This interview question requires you to reverse a string using 001_recursion. Make sure to think of the base case here.
# Again, make sure you use 001_recursion to accomplish this. Do not slice (e.g. string[::-1]) or use iteration,
# there must be a recursive call for the function.
# Fill out your solution below

___ reverse(s
    __(l..(s)<_1
        r_ s
    ____
        m _ i..(l..(s)/2)
        r_ reverse(s[m:]) + (reverse((s[:m])))
    p..

reverse('hello world')
# 'dlrow olleh'
#
# Test Your Solution
#
# Run the cell below to test your solution against the following cases:
#
string _ 'hello'
string _ 'hello world'
string _ '123456789'
#
# '''
# RUN THIS CELL TO TEST YOUR FUNCTION AGAINST SOME TEST CASES
# '''

____ n___.t.. ______ assert_equal

c_ TestReverse o..

    ___ test_revsolution
        ? solution('hello'),'olleh')
        ? solution('hello world'),'dlrow olleh')
        ? solution('123456789'),'987654321')

        print ('PASSED ALL TEST CASES!')

# Run Tests
test _ TestReverse()
test.test_rev(reverse)

# PASSED ALL TEST CASES!
#
# Good Luck!