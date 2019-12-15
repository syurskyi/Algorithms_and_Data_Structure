data = int(input())
a = list(map(int,input().split()))
for i in a:
    store = []
    count = 0
    while i not in store:
        store.append(i)
        i = int(i)
        i = i**2
        i = int(i/100)
        i = i%10000
        count += 1
print(count,end=' ')