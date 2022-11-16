
___ func(numArray, val, l_0, h_-1
    __ n.. numArray: r_ -1
    __(h __ -1 h _ l..(numArray) - 1
    __ l __ h:
        __ numArray[l] __ val: r_ l
        ____ r_ -1
    m _ l + (h - l) // 2
    __ numArray[m] > val: r_ func(numArray, val, l, m - 1)
    elif numArray[m] < val: r_ func(numArray, val, m + 1, h)
    ____ r_ m
	    
numArray _ [1,2,3,4,5,6,7]
print(func(numArray, 7))    
