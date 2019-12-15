import math
data = int(input())
for i in range(data):
    cal = 0
    deno = 0
    res = ''
    a,b,c = nums = list(map(int,input().split()))
    cal = b**2 - (4*a*c)
    deno = 2*a
    if cal >= 0:
        x1 = (-b + math.sqrt(cal)) / deno
        x2 = (-b - math.sqrt(cal)) / deno
        res = str(int(x1))+' '+str(int(x2))
    else:
        cal = cal * -1
        x_cal = str(int(math.sqrt(cal) / deno)) + 'i'
        b_cal = -b /deno
        x1 = str(int(b_cal)) +'+'+ x_cal
        x2 = str(int(b_cal)) +'-'+ x_cal
        res = x1 + ' '+ x2
    if i == data-1:
        print(res,end = '')
    else:
        print(res,end = '; ')