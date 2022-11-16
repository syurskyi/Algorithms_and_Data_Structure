___ func(numArray, value
    l _ 0
    h _ l..(numArray) - 1
    _____ l <_ h:
        m _ (l + h) // 2
        __ numArray[m] > value: h _ m - 1
        elif numArray[m] < value: l _ m + 1
        ____ r_ m
    r_ -1
	
numArray _ [1,2,3,4,5,6,7,8]
print(func(numArray, 8))
