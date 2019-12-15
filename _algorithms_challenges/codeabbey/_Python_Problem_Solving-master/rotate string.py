for i in range(int(input())):
    a,b = input().split()
    #
    b = b[int(a):] + b[:int(a)]
    print(b,end = ' ')