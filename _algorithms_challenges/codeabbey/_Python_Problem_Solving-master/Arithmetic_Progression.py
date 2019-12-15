d = int(input())
count = 0
res = []
while count < d:
    a = input().split()
    a = list(map(int,a))
    val = a[0]
    step = a[1]
    for i in range(0,a[2]):
        if i==0:
            result = val
        else:
            result = result + (val + step * i)
            
    res.append(result)
    count = count + 1
    
res = ' '.join(str(j) for j in res)
print(res)