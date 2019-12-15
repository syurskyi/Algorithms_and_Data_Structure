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


input_shape = input("請輸入形狀名稱:\n")
input_a = input("請輸入第一個邊的邊長:\n")
input_b = input("請輸入第二個邊的邊長:\n")
input_c = input("請輸入第三個邊的邊長:\n")


tri = Tri(input_shape, input_a, input_b, input_c)
print(tri.shape)
print(tri.length())
