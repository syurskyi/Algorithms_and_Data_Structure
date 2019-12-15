class math():
    
    def add(N):
        add_sum = 0
        for i in range(N+1):
            add_sum = add_sum + i
            if(i == 0):
                print(i, sep='', end='')
            else:
                print("+", i, sep='', end='')
        return add_sum
    
    def mul(N):
        mul_sum = 1
        for i in range(1,N+1):
            mul_sum = mul_sum * i
            if(i == 1):
                print("  ",i, sep='', end='')
            else:
                print("*", i, sep='', end='')
        return mul_sum


N = int(input("請輸入數字N，將做連加、連乘到數字N:\n"))
print(" =",math.add(N))
print(" =",math.mul(N))

