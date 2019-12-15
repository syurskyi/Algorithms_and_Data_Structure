from module import Calculator

print("運算1:")
a = input("請輸入a的值:\n")
op = input("請輸入要做的運算(+ - * /):\n")
b = input("請輸入b的值:\n")

operation = Calculator(a, b, op)

print(operation.result)
print()

print("運算2:")
a2 = input("請輸入a的值:\n")
op2 = input("請輸入要做的運算(+ - * /):\n")
b2 = input("請輸入b的值:\n")

operation2 = Calculator(a2, b2, op2)

print(operation2.result)
