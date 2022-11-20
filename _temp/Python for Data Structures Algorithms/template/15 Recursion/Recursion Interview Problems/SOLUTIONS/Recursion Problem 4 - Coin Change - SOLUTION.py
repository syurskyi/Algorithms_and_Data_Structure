# Coin Change Problem
# Note: This problem has multiple solutions and is a classic problem in showing issues with basic 001_recursion.
# There are better solutions involving memoization and simple iterative solutions.If you are having trouble with this
# problem (or it seems to be taking a long time to run in some cases) check out the Solution Notebook and fully read
# the conclusion link for a detailed description of the various ways to solve this problem!
# This problem is common enough that is actually has its own Wikipedia Entry! Let's check the problem statement again:
#
# This is a classic 001_recursion problem: Given a target amount n and a list (array) of distinct coin values, what's the
# fewest coins needed to make the change amount.

# For example:
#
# If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to make change:
#
#     1+1+1+1+1+1+1+1+1+1
#
#     5 + 1+1+1+1+1
#
#     5+5
#
#     10
#
# With 1 coin being the minimum amount.
# Solution
# This is a classic problem to show the value of dynamic programming. We'll show a basic recursive example and show
# why it's actually not the best way to solve this problem.
# Make sure to read the comments in the code below to fully understand the basic logic!

___ rec_coin(target,coins
    '''
    INPUT: Target change amount and list of coin values
    OUTPUT: Minimum coins needed to make change

    Note, this solution is not optimized.
    '''

    # Default to target value
    min_coins _ target

    # Check to see if we have a single coin match (BASE CASE)
    __ target __ coins:
        r_ 1

    ____

        # for every coin value that is <= than target
        ___ i __ [c ___ c __ coins __ c <_ target]:

            # Recursive Call (add a count coin and subtract from the target)
            num_coins _ 1 + rec_coin(target-i,coins)

            # Reset Minimum if we have a new minimum
            __ num_coins < min_coins:

                min_coins _ num_coins

    r_ min_coins

# Let's see it in action.
#
rec_coin(63,[1,5,10,25])
# 6
#
# The problem with this approach is that it is very inefficient! It can take many, many recursive calls to finish this
# problem and its also inaccurate for non standard coin values (coin values that are not 1,5,10, etc.)
# We can see the problem with this approach in the figure below:
# from IPython.display import Image
# Image(url='http://interactivepython.org/runestone/static/pythonds/_images/callTree.png')
# Each node here corresponds to a call to the rec_coin function. The label on the node indicated the amount of change
# for which we are now computng the number of coins for. Note how we are recalculating values we've already solved!
# For instance 15 is called 3 times. It would be much better if we could keep track of function calls we've already
# made.
# Dynamic Programming Solution
# This is the key to reducing the work time for the function. The better solution is to remember past results,
# that way before computing a new minimum we can check to see if we already know a result.
#
# Let's implement this:

___ rec_coin_dynam(target,coins,known_results
    '''
    INPUT: This funciton takes in a target amount and a list of possible coins to use.
    It also takes a third parameter, known_results, indicating previously calculated results.
    The known_results parameter shoud be started with [0] * (target+1)

    OUTPUT: Minimum number of coins needed to make the target.
    '''

    # Default output to target
    min_coins _ target

    # Base Case
    __ target __ coins:
        known_results[target] _ 1
        r_ 1

    # Return a known result if it happens to be greater than 1
    ____ known_results[target] > 0:
        r_ known_results[target]

    ____
        # for every coin value that is <= than target
        ___ i __ [c ___ c __ coins __ c <_ target]:

            # Recursive call, note how we include the known results!
            num_coins _ 1 + rec_coin_dynam(target-i,coins,known_results)

            # Reset Minimum if we have a new minimum
            __ num_coins < min_coins:
                min_coins _ num_coins

                # Reset the known result
                known_results[target] _ min_coins

    r_ min_coins

# Let's test it!
#
target _ 74
coins _ [1,5,10,25]
known_results _ [0]*(target+1)
#
rec_coin_dynam(target,coins,known_results)#
# 8
#
# Test Your Solution
#
# Run the cell below to test your function against some test cases.
#
# Note that the TestCoins class only test functions with two parameter inputs, the list of coins and the target
#
# """
# RUN THIS CELL TO TEST YOUR FUNCTION.
# NOTE: NON-DYNAMIC FUNCTIONS WILL TAKE A LONG TIME TO TEST. IF YOU BELIEVE YOU HAVE A SOLUTION
# """

____ n___.t.. ______ assert_equal

c_ TestCoins o..

    ___ checksolution
        coins _ [1,5,10,25]
        ? solution(45,coins),3)
        ? solution(23,coins),5)
        ? solution(74,coins),8)

        print 'Passed all tests.'

# Run Test

test _ TestCoins()
test.check(rec_coin)

# Conclusion and Extra Resources
# For homework, read the link below and also implement the non-recursive solution described in the link!
# For another great resource on a variation of this problem, check out this link