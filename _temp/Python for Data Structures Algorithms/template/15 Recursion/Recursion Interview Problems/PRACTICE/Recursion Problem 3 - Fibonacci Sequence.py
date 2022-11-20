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
# Solve the problem using simple 001_recursion.

___ fib_rec(n
    __ n <_2:
        r_ i..((n+1)/2)
    ____
        r_ fib_rec(n-1) + fib_rec(n-2)
    p..

fib_rec(10)
# 55
#
# Dynamically
#
# Implement the function using dynamic programming by using a cache to store results (memoization).
#
# # Instantiate Cache information
n _ 10
cache _ [N..] * (n + 1)
print(cache)

___ fib_dyn(n
    __ cache[n] __ n.. N..
         r_ cache[n]
    __ n <_2:
        cache[n] _ i..((n+1)/2)
    ____
        cache[n] _ fib_dyn(n-1) + fib_dyn(n-2)
    r_ cache[n]
    p..

# [None, None, None, None, None, None, None, None, None, None, None]
#
fib_dyn(10)
# 55
#
# Iteratively
# Implement the solution with simple iteration.
#
___ fib_iter(n

    # Set starting point
    a _ 0
    b _ 1

    # Follow algorithm
    ___ i __ r..(n
        a, b _ b, a + b
    r_ a

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

____ n___.t.. ______ assert_equal

c_ TestFib o..

    ___ testsolution
        ? solution(10),55)
        ? solution(1),1)
        ? solution(23),28657)
        print ('Passed all tests.')
# UNCOMMENT FOR CORRESPONDING FUNCTION
t _ TestFib()

t.test(fib_rec)
#t.test(fib_dyn) # Note, will need to reset cache size for each test!
#t.test(fib_iter)

# Passed all tests.
#
# Conclusion
#
# Hopefully this interview question served as a good excercise in exploring 001_recursion, dynamic programming, and iterative solutions for a single problem! Its good to work through all three because in an interview a common question may just begin with requesting a recursive solution and then checking to se if you can implement the other forms!