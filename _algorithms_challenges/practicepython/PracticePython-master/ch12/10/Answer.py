import math

class Calculator():

    def __init__(self, a, b, op):
        self.a = float(a)
        self.b = float(b)
        self.op = op
        if self.op == '+':
            self.add()
        if self.op == '-':
            self.sub()
        if self.op == '*':
            self.mul()
        if self.op == '/':
            self.div()
            
    def add(self):
        self.result = self.a + self.b

    def sub(self):
        self.result = self.a - self.b

    def mul(self):
        self.result = self.a * self.b

    def div(self):
        self.result = self.a / self.b

    def result(self):
        return self.result


a = input("請輸入a的值:\n")
b = input("請輸入b的值:\n")
op = input("請輸入要做的運算(+ - * /):\n")

operation = Calculator(a, b, op)

print(operation.result)
