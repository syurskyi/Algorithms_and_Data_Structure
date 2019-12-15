d = int(input())
a = list(map(int,input().split()))

while len(a)!= 1:
    max = 0
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
    ind = a.index(max)
    print(ind,end=' ')
    a[ind],a[-1] = a[-1],a[ind]
    a.pop(-1)