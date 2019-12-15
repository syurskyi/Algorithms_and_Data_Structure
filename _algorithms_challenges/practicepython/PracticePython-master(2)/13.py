# Fibonacci - unfinished

# Ask how many numbers
num = int(input("Give me a number: "))

# Generates


def fibonacci():
    i = 1
    if num == 0:
        fib = []
    if num == 1:
        fib = [1]
    if num == 2:
        fib = [1, 1]
    if num > 2:
        fib[1, 1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1

    return fib


print (fibonacci())
