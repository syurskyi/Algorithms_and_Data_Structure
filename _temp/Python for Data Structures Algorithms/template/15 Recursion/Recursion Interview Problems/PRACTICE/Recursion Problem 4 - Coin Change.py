# Coin Change Problem
# Note: This problem has multiple solutions and is a classic problem in showing issues with basic 001_recursion.
# If you are having trouble with this problem (or it seems to be taking a long time to run in some cases) check out
# the Solution Notebook and fully read the conclusion link for a detailed description of the various ways to solve
# this problem!
# This problem is common enough that is actually has its own Wikipedia Entry!
# Problem Statement
# Given a target amount n and a list (array) of distinct coin values, what's the fewest coins needed to make
# the change amount.
#
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
#
# Implement your solution below:

___ rec_coin(target,coins
    min_coins _ target

    __ target __ coins:
        r_ 1
    ____
        ___ value __ [ c ___ c __ coins __ c<_ target]:
            num_coins _ rec_coin(target-value, coins) + 1
            min_coins _ min(num_coins, min_coins)
    r_ min_coins
    p..

rec_coin(10,[1,5]) #2
# 2
#
rec_coin(63,[1,5,10,25])
# 6
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
#       GO CHECK THE SOLUTION NOTEBOOK INSTEAD OF RUNNING THIS!
# """

____ n___.t.. ______ assert_equal

c_ TestCoins o..

    ___ checksolution
        coins _ [1,5,10,25]
        ? solution(45,coins),3)
        ? solution(23,coins),5)
        ? solution(74,coins),8)
        print ('Passed all tests.')
# # Run Test
#
test _ TestCoins()
test.check(rec_coin)
#
# EXTRA
#
# Good luck and remember to read the solution notebook for this once you've think you have a solution!