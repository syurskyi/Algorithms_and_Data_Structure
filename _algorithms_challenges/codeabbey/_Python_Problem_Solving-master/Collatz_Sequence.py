data = int(input())

a = [int(x) for x in input().split()]
#print(len(a))
res = []
for i in range(len(a)):
    #print('starting')
    count = 0
    xnext = a[i]
    while xnext != 1:
        if xnext % 2 == 0:
            xnext = xnext / 2
            #print('even:',xnext)
            if xnext == 1:
                count += 1
                #print('counting and appending')
                res.append(count)
                
                #print('even res:',res)
                continue
            else:
                count += 1
        else:
            #print('odd')
            xnext = (3*xnext) + 1
            #print('odd: ',xnext)
            
            if xnext == 1:
                count += 1
                res.append(count)
                #print(res)
                continue
            else:
                count += 1
for i in res:
    print(i,end=(' '))