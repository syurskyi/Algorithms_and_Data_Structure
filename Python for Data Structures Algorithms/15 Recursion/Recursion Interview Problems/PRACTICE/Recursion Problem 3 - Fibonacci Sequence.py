# Fibonnaci Sequence
# In this interview excercise we will begin to get a feel of having to solve a single problem multiple ways!
# Problem Statement
# Implement a Fibonnaci Sequence in three different ways:
#     Recursively
#     Dynamically (Using Memoization to store results)
#     Iteratively
# Function Output
# Your function will accept a number n and return the nth number of the fibonacci sequence
# Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21,... starts off with a base case checking to see if n = 0 or 1, then it returns 1.
#
# Else it returns fib(n-1)+fib(n+2).
# Fill Out Your Solutions Below
# Recursively
#
# Solve the problem using simple recursion.

def fib_rec(n):
    if n <=2:
        return int((n+1)/2)
    else:
        return fib_rec(n-1) + fib_rec(n-2)
    pass

fib_rec(10)
# 55
#
# Dynamically
#
# Implement the function using dynamic programming by using a cache to store results (memoization).
#
# # Instantiate Cache information
n = 10
cache = [None] * (n + 1)
print(cache)

def fib_dyn(n):
    if cache[n] is not None:
         return cache[n]
    if n <=2:
        cache[n] = int((n+1)/2)
    else:
        cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    return cache[n]
    pass

# [None, None, None, None, None, None, None, None, None, None, None]
#
fib_dyn(10)
# 55
#
# Iteratively
# Implement the solution with simple iteration.
#
def fib_iter(n):

    # Set starting point
    a = 0
    b = 1

    # Follow algorithm
    for i in range(n):
        a, b = b, a + b
    return a

fib_iter(23)
# 28657
#
# Test Your Solution
#
# Run the cell below to test your solutions, simply uncomment the solution functions you wish to test!
#
# """
# UNCOMMENT THE CODE AT THE BOTTOM OF THIS CELL TO SELECT WHICH SOLUTIONS TO TEST.
# THEN RUN THE CELL.
# """

from nose.tools import assert_equal

class TestFib(object):

    def test(self,solution):
        assert_equal(solution(10),55)
        assert_equal(solution(1),1)
        assert_equal(solution(23),28657)
        print ('Passed all tests.')
# UNCOMMENT FOR CORRESPONDING FUNCTION
t = TestFib()

t.test(fib_rec)
#t.test(fib_dyn) # Note, will need to reset cache size for each test!
#t.test(fib_iter)

# Passed all tests.
#
# Conclusion
#
# Hopefully this interview question served as a good excercise in exploring recursion, dynamic programming, and iterative solutions for a single problem! Its good to work through all three because in an interview a common question may just begin with requesting a recursive solution and then checking to se if you can implement the other forms!