
# print the Fibonacci sequence up to n
def fibonacci_iteration(n):

    a, b = 0, 1

    while a < n:
        print(a)
        a, b = b, a + b


fibonacci_iteration(100)
