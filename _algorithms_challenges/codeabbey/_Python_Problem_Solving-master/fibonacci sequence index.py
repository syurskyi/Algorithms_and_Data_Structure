fib_store = [0,1]

#generating the fibonacci Sequence
for i in range(2,1000):
    fib_store.append(fib_store[-2] + fib_store[-1])

#searching for the index of the given element from Fibonacci Sequence
for i in range(int(input())):
    fib_num = int(input())
    #using index to find the index of the element from fibonacci sequence
    fib_index = fib_store.index(fib_num)
    print(fib_index,end=' ')