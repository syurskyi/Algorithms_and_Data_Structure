win_dic = {'S':'P','P':'R','R':'S'}
for i in range(int(input())):
    count1 = 0
    count2 = 0
    a = list(map(str,input().split()))
    for j in a:
        if j[0] == j[1]:
            pass
        elif j[1] == win_dic[j[0]]:
            count1 += 1
        else:
            count2 += 1
    if count1 > count2:
        print('1',end=' ')
    else:
        print('2',end=' ')