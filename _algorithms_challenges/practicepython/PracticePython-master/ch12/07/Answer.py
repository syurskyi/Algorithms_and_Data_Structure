import math

class Shape():

    def __init__(self, shape):
        self.shape = shape

    def length(self):
        pass

class Tri(Shape):

    def __init__(self, shape, a, b, c):
        self.perimeter = int(a) + int(b) + int(c)
        super().__init__(shape)

    def length(self):
        return self.perimeter

class Rec(Shape):

    def __init__(self, shape, a, b):
        self.perimeter = 2 * (int(a) + int(b))
        super().__init__(shape)

    def length(self):
        return self.perimeter

class Cir(Shape):

    def __init__(self, shape, a):
        self.perimeter = 2 * math.pi * int(a)
        super().__init__(shape)

    def length(self):
        return self.perimeter

input_shape = input("請輸入形狀名稱:\n")
shape = Shape(input_shape)
print(shape.shape)

input_shape = input("請輸入形狀名稱:\n")
input_a = input("請輸入第一個邊的邊長:\n")
input_b = input("請輸入第二個邊的邊長:\n")
input_c = input("請輸入第三個邊的邊長:\n")
tri = Tri(input_shape, input_a, input_b, input_c)
print(tri.shape)
print(tri.length())

input_shape = input("請輸入形狀名稱:\n")
input_a = input("請輸入第一個邊的邊長:\n")
input_b = input("請輸入第二個邊的邊長:\n")
rec = Rec(input_shape, input_a, input_b)
print(rec.shape)
print(rec.length())

input_shape = input("請輸入形狀名稱:\n")
input_a = input("請輸入第一個邊的邊長:\n")
cir = Cir(input_shape, input_a)
print(cir.shape)
print(cir.length())

