## Fibonacci number
## 0 1 1 2 3 5 8 13 21 34 55 89 144...

F_len = int(input("請輸入要印出的費氏數列個數:\n"))


a = 0
b = 1
temp = 0

for i in range(F_len):
    print(a)
    
    temp = a
    a = a + b
    b = temp
