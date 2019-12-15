'''
I realized after some time after implementing a recursive solution (not shown),
it's not as easy to generate the actual fibonacci sequence as a list without
implementing some form of memoization to prevent duplicates from appearing.
While it would bring the solution to O(n) time, I felt it was beyond the intended
difficulty of the problem. Looking at other solutions, I thought this to be one
of the better ones, with an iterative form and cleaner code too!
'''

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
       fib_sequence += [fib_sequence[-1] + fib_sequence[-2]]
    return fib_sequence[0:n]

number = int(input("How many fibonacci numbers? "))

print(fibonacci(number))
