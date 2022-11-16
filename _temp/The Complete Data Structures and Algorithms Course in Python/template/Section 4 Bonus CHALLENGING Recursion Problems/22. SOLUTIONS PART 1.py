# POWER SOLUTION

___ power(base, exponent
    __ exponent __ 0:
        r_ 1
    r_ base * power(base, exponent-1)

# FACTORIAL SOLUTION

___ factorial(num
    __ num <_ 1:
        r_ 1
    r_ num * factorial(num-1)

# PRODUCT OF ARRAY SOLUTION

___ productOfArray(arr
    __ l..(arr) __ 0:
        r_ 1
    r_ arr[0] * productOfArray(arr[1:])

# RECURSIVE RANGE SOLUTION

___ recursiveRange(num
    __ num <_ 0:
        r_ 0
    r_ num + recursiveRange(num - 1)

# FIBONACCI SOLUTION

___ fib(num
    __ (num < 2
        r_ num
    r_ fib(num - 1) + fib(num - 2)