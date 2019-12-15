
for i in range(int(input())):
    res = 0    
    a = [int(i)* int(i) for i in input().split()]
    for j in a:
        res += j
    print(res,end=' ')
    