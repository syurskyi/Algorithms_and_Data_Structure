class Deposit():
    def __init__(self):
        self.__principal = 0
        self.__rate = 0
        self.__term = 0

    def assign(self, p, r, t):
        self.__principal = p
        self.__rate = r
        self.__term = t

    def receive(self):
        return self.__principal, self.__rate, self.__term

    def amount(self):
        interest = int(self.__principal) * ( 1 + float(self.__rate) / 12 ) ** int(self.__term) 
        print("本利和:",interest)


p = input("請輸入本金(ex:100):")
r = input("請輸入年利率(ex:0.01):")
t = input("請輸入存款月份數(ex:12):")
account = Deposit()
account.assign(p, r, t)

print(account.receive())
account.amount()
