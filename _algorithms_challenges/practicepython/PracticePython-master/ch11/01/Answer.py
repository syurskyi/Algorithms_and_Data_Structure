def multip_table(N):
    for i in range(N+1):
        for j in range(N+1):
            if(j != N): ## 排版用 扣除一行中最後一個,
                print(i,"x",j,"=",i*j,", ", end='')
            else:
                print(i,"x",j,"=",i*j," ", end='')
        print()



N = int(input("請輸入一個數字，將印出乘法表:\n"))
multip_table(N)
