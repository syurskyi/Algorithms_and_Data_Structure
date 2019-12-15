d = input().split()
d.sort()
res = []
d_dic = {}
for i in d:
    if i in d_dic:
        d_dic[i] += 1
    else:
        d_dic[i] = 1
for i in d_dic:
    if d_dic[i] > 1:
        if i not in res:
            res.append(i)
for i in res:
    print(i,end=' ')