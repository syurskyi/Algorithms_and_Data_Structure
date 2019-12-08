def func(numArray, value):
    l = 0
    h = len(numArray) - 1
    while l <= h: 
        m = (l + h) // 2
        if numArray[m] > value: h = m - 1
        elif numArray[m] < value: l = m + 1
        else: return m
    return -1
	
numArray = [1,2,3,4,5,6,7,8]
print(func(numArray, 8))
