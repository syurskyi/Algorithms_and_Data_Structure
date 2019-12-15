class Cube():

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def GetArea(self):
        self.area = self.length * self.width

    def GetVolume(self):
        self.volume = self.length * self.width * self.height

    def DisplayArea(self):
        print(self.area)

    def Display(self):
        print(self.volume)


a = Cube(10, 5, 3)
a.GetVolume()
a.Display()

b = Cube(1000, 50, 30)
b.GetVolume()
b.Display()

c = Cube(95, 48, 302)
c.GetVolume()
c.Display()
