
___ func(myarray, value
	l _ 0
	r _ len(myarray) - 1
	_____ l <_ r:
	    m _ (l + r) / 2
	    __ myarray[m] == value:
		r_ m
	    __ myarray[m] >_ myarray[l]:
		__ myarray[l] <_ value < myarray[m]:
		    r _ m - 1
		____
		    l _ m + 1
	    ____
		__ myarray[m] < value <_ myarray[r]:
		    l _ m + 1
		____
		    r _ m - 1
	r_ -1
	
myarray _ [6,7,8,9,10,1,2,3,4,5]

print func(myarray, 5)
