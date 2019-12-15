a =  [int(i) for i in input().split()]
a.remove(a[-1])
swap_count = 0
seed = 0

for i in range(len(a)):
    if i == len(a)-1:
        break
    if a[i] > a[i+1]:
        swap_count += 1
        temp = a[i]
        a[i] = a[i+1]
        a[i+1] = temp
    else:
        continue

#seed = seed - 4513010
for j in range(len(a)):
    #print('index',j,'value is',a[j])
    seed = (seed + a[j]) * 113
    
    if seed > 10000007:
        seed = seed % 10000007
        
print(swap_count, seed)