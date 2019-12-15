data = int(input())

res= ''
for i in range(0,data):
    para = input().split()
    
    para = list(map(int,para))
    
    a = para[0]
    b = para[1]
    c = para[2]
    
    if a + b > c and a + c > b  and b + c > a:
        res +='1'
        res += ' '
    else:
        res += '0'
        res += ' '
    
print(res)