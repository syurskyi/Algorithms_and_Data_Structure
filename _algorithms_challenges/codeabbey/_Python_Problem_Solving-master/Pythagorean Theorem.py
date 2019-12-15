import math
for i in range(int(input())):
    triangle= list(map(int,input().split()))
    a,b,c = triangle
    cal = math.sqrt(a**2 + b**2)
    print(cal)
    if c == cal:
        print('R',end=' ')
    #acute triangle which is less than 90 degree
    elif c < cal:
        print('A',end=' ')
    #obtuse triangle which is greater than 90 degree
    else:
        print('O',end=' ')