
def func(numArray, val, l=0, h=-1):
    if not numArray: return -1
    if(h == -1): h = len(numArray) - 1
    if l == h:
        if numArray[l] == val: return l
        else: return -1
    m = l + (h - l) // 2
    if numArray[m] > val: return func(numArray, val, l, m - 1)
    elif numArray[m] < val: return func(numArray, val, m + 1, h)
    else: return m
	    
numArray = [1,2,3,4,5,6,7]
print(func(numArray, 7))    
