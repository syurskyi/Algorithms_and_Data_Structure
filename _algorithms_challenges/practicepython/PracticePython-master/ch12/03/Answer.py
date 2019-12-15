import math

class Circle():

    def __init__(self, r):
        self.r = r

    def GetArea(self):
        self.area = self.r* self.r* math.pi
        return self.area     #math.pi = 3.141592653589793

    def GetPerimeter(self):
        self.perimeter = 2 * math.pi * self.r
        return self.perimeter

    def GetVolume(self):
        self.volume = (4/3) * math.pi * (self.r ** 2)
        return self.volume


a = Circle(10)

print(a.GetArea())
print(a.GetPerimeter())
print(a.GetVolume())
