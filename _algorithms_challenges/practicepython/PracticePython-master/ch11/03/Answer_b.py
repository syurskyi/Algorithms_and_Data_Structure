## Fibonacci number
## 0 1 1 2 3 5 8 13 21 34 55 89 144...

F_len = int(input("請輸入要印出的費氏數列個數:\n"))


def Fibonacci(F_len):
    if(F_len == 0):
        return 0
    if(F_len == 1):
        return 1

    return Fibonacci(F_len-1) + Fibonacci(F_len-2)
    


print(Fibonacci(F_len))
