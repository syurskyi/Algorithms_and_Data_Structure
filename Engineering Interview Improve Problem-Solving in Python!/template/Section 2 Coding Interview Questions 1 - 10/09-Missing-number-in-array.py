# [1,2,3,5,6] => 4
def missing_number(l):
    for i in range(1, len(l) + 1): #n
        if i != l[i - 1]:
            return i
    return -1

def missing_number_r(l, start, end): #l, 3, 5
    if start == end:
        return start + 1
    index_middle = int((start + end) / 2) # 3 + 5 / 2 = 4 
    if l[index_middle] == index_middle + 1:
        missing_number_r(l,index_middle + 1,end)
    else:
        missing_number_r(l,start,index_middle - 1)

print(missing_number_r([1,2,3,5,6],0,5))