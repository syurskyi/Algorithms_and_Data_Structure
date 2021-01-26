
def factorial_head(n):

    # this is the base case - 0!=1
    if n == 0:
        return 1

    # use recursion
    result1 = factorial_head(n-1)

    # we do some operations
    result2 = n * result1
    return result2


def factorial_tail(n, accumulator=1):

    if n == 1:
        return accumulator

    return factorial_tail(n-1, n * accumulator)


print(factorial_tail(4))
