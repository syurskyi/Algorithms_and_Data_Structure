class CBox():

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def GetArea(self):
        self.area = self.length * self.width

    def Display(self):
        print(self.area)
        

a = CBox(10, 5)
a.GetArea()
a.Display()


b = CBox(10, 500)
b.GetArea()
b.Display()


c = CBox(2, 42)
c.GetArea()
c.Display()
