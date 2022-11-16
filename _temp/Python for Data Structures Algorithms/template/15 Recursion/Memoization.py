# Memoization
#
# In this lecture we will discuss memoization and dynamic programming. For your homework assignment, read
# the Wikipedia article on Memoization, before continuing on with this lecture!
# Memoization effectively refers to remembering ("memoization" -> "memorandum" -> to be remembered) results of method
# calls based on the method inputs and then returning the remembered result rather than computing the result again.
# You can think of it as a cache for method results. We'll use this in some of the interview problems as improved
# versions of a purely recursive solution.
#
# A simple example for computing factorials using memoization in Python would be something like this:
#
# # Create cache for known results
factorial_memo _     # dict

___ factorial(k

    __ k < 2:
        r_ 1

    __ n.. k __ factorial_memo:
        factorial_memo[k] _ k * factorial(k-1)

    r_ factorial_memo[k]

factorial(4)
# 24
#
# Note how we are now using a dictionary to store previous results of the factorial function! We are now able
# to increase the efficiency of this function by remembering old results!
# Keep this in mind when working on the Coin Change Problem and the Fibonacci Sequence Problem.
# We can also encapsulate the memoization process into a class:

c_ Memoize:
    ___ -  f
        f _ f
        memo _     # dict
    ___ __call__ *args
        __ n.. args __ memo:
            memo[args] _ f(*args)
        r_ memo[args]

# Then all we would have to do is:

___ factorial(k

    __ k < 2:
        r_ 1

    r_ k * factorial(k - 1)

factorial _ Memoize(factorial)

# Try comparing the run times of the memoization versions of functions versus the normal recursive solutions!