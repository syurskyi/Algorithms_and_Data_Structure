d = input().split()
result = []
for i in range(1,int(d[0])+1):
    val = int(d[i])
    cel =(val-32) * 5/9
    if (cel).int_integer():
        result.append(int(cel))
    elif cel < 0:
        cel = cel - 0.5
        result.append(int(cel))
    else:
        cel = cel + 0.5
        result.append(int(cel))
        
        
    
res = ' '.join(str(e) for e in result)
print(res)