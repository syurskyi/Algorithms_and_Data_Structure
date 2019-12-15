class CreateBankAccount():

    def __init__(self, __id='', __name='', __balance=0):
        self.__id = __id
        self.__name = __name
        self.__balance = __balance
        
    def dep(self, dep):   #存款
        if int(dep) > 0:
            self.__balance = self.__balance + int(dep)
        else:
            print("存款金額不正確!!")
            return
    
    def wit(self, wit):   #提款
        if int(wit) > 0:
            if self.__balance - int(wit) >= 0:
                self.__balance = self.__balance - int(wit)
            else:
                print("餘額不足!!")
                return
        else:
            print("提款金額不正確!!")
            return

    def tra(self, account, money=0):    #匯款
        if int(money) > 0:
            self.wit(int(money))
            account.dep(int(money))
            print("=== id:", self.__id, "使用者:", self.__name, "匯款", money, "元 給 id:", account.__id, "使用者:", account.__name, "===")
        else:
            print("轉帳金額不正確!!")
            return

    def display(self):
        print("id:", self.__id, "使用者:", self.__name, " 餘額:", self.__balance)



a = CreateBankAccount('00001', 'User_A', 1000)
b = CreateBankAccount('00002', 'User_B', 20000)

a.display()
b.display()

#a.wit(input("使用者a，請輸入提款金額:"))
#a.display()

#b.dep(input("使用者b，請輸入存款金額:"))
#b.display()

trans_money = input("使用者a欲匯款給使用者b，請輸入匯款金額:\n")
a.tra(b, trans_money)
print()

a.display()
b.display()
