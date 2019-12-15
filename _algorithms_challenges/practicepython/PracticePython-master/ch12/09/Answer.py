import math

class Shape():

    def __init__(self, shape):
        self.shape = shape

    def length(self):
        pass

class Tri(Shape):

    def __init__(self, shape, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        super().__init__(shape)

    def length(self):
        self.perimeter = self.a + self.b + self.c
        return self.perimeter

    def area(self):
        self.area_s = (self.a + self.b + self.c) / 2
        self.area = (self.area_s * (self.area_s - self.a) * (self.area_s - self.b) * (self.area_s - self.c) )** 0.5
        return self.area

    def __eq__(self, Shape):
        return True if self.area == Shape.area else False

class Rec(Shape):

    def __init__(self, shape, a, b):
        self.a = int(a)
        self.b = int(b)
        super().__init__(shape)

    def length(self):
        self.perimeter = 2 * (self.a + self.b)
        return self.perimeter

    def area(self):
        self.area = self.a * self.b
        return self.area

    def __eq__(self, Shape):
        return True if self.area == Shape.area else False

class Cir(Shape):

    def __init__(self, shape, a):
        self.a = int(a)
        super().__init__(shape)

    def length(self):
        self.perimeter = 2 * math.pi * self.a
        return self.perimeter

    def area(self):
        self.area = self.a * self.a * self.a
        return self.area
    
    def __eq__(self, Shape):
        return True if self.area == Shape.area else False


input_shape = input("請輸入形狀名稱:\n")
input_a = input("請輸入第一個邊的邊長:\n")
input_b = input("請輸入第二個邊的邊長:\n")
input_c = input("請輸入第三個邊的邊長:\n")
tri1 = Tri(input_shape, input_a, input_b, input_c)
print(tri1.shape, " 面積為:", tri1.area())


input_shape = input("請輸入形狀名稱:\n")
input_a = input("請輸入第一個邊的邊長:\n")
input_b = input("請輸入第二個邊的邊長:\n")
input_c = input("請輸入第三個邊的邊長:\n")
tri2 = Tri(input_shape, input_a, input_b, input_c)
print(tri2.shape, " 面積為:", tri2.area())

print(tri2.__eq__(tri1))
