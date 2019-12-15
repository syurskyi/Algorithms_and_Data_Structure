num_ele, ele_type = [int(i) for i in input().split()]


ele = []
unique = []

while len(ele) < ele_type:
    num_count = [int(x) for x in input().split()]
    num_count.sort()
    #finding out unique elements in the list
    for x in num_count:
        if x not in unique:
            unique.append(x)
            
    #counting the occurence of the element in the list
    for i in range(len(unique)):
        count_store = num_count.count(unique[i])
        ele.append(count_store)
        
        
for k in ele:
    print(k,end=(' '))