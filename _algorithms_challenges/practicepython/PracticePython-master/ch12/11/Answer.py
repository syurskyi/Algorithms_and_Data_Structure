class CRect():

    def __init__(self, l=0, w=0, h=0):
        self.l = int(l)
        self.w = int(w)
        self.h = int(h)
        self.volume = None
        self.area = None
        
    def getAera(self):
        self.area = self.l * self.w
        return self.area
    
    def getVolume(self):
        self.volume = self.l * self.w * self.h
        return self.volume

    def show(self):
        if(self.volume == None):
            self.getVolume()
        print(self.volume)
        return self.volume

l = input("請輸入長方形的長:\n")
w = input("請輸入長方形的寬:\n")
h = input("請輸入長方形的高:\n")

rect = CRect(l, w, h)
rect.show()
