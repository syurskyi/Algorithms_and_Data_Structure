# POWER SOLUTION

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)

# FACTORIAL SOLUTION

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)

# PRODUCT OF ARRAY SOLUTION

def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])

# RECURSIVE RANGE SOLUTION

def recursiveRange(num):
    if num <= 0:
        return 0
    return num + recursiveRange(num - 1)

# FIBONACCI SOLUTION

def fib(num):
    if (num < 2):
        return num
    return fib(num - 1) + fib(num - 2)