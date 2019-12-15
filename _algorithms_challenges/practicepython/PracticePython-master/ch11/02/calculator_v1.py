def calculator(a, b, operation):
    if(operation == '+'):
        return a + b
    if(operation == '-'):
        return a - b
    if(operation == '*'):
        return a * b
    if(operation == '/'):
        return a / b


print("這是一台簡易四則運算計算機，")

a = int(input("請輸入第一個數字:\n"))

operation = input("請輸入一個運算符號( + - * / ):\n")

b = int(input("請輸入第二個數字:\n"))

print(a ,operation, b, " = ", calculator(a, b, operation))
