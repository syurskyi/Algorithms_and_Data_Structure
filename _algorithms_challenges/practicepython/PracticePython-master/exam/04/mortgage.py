class mortgage():
    def __init__(self):
        self.__loan = 0
        self.__rate = 0
        self.__year = 0

    def assign(self, l, r, y):
        self.__loan = l
        self.__rate = r
        self.__year = y

    def receive(self):
        return self.__loan, self.__rate, self.__year

    def term_fee(self):
        self.__fee = int(self.__loan) * ( 1 + float(self.__rate) / 12 ) ** (int(self.__year) *12)
        print("本利和:",self.__fee)


house = mortgage()
l = input("請輸入貸款金額(ex:100):")
r = input("請輸入貸款利率(ex:0.01):")
y = input("請輸入貸款年數(ex:2):")
house.assign(l, r, y)
print(house.receive())

house.term_fee()
