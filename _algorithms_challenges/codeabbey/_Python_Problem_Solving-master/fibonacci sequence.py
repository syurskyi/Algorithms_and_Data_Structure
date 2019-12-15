fib_store = [0,1]
#generating the fibonacci Sequence
for i in range(2,1000):
    fib_store.append(fib_store[-2] + fib_store[-1])
    
#searching for the index of the given element from Fibonacci Sequence
for i in range(int(input())):
    fib_num = int(input())
    for j in range(len(fib_store)):
        if fib_num == fib_store[j]:
            break
    print(j,end=' ')