data = int(input())
result = []

for i in range(data):
    sum_numbs = 0
    avg = 0
    avg_numbs = input().split()
    
    for j in range(len(avg_numbs)-1):
        #print('value of avg ',j,' is ',avg_numbs[j])
        sum_numbs = sum_numbs + int(avg_numbs[j])
        #a = [int(x) for x in input().split()]
        #avg = sum(a) / (len(a) - 1)
        
    avg = sum_numbs / (len(avg_numbs)-1)
    if avg.is_integer():
        result.append(int(avg))
    else:
        avg = avg + 0.5
        result.append(int(avg))
        
for k in result:
    print(k,end=(' '))