
def func(myarray, value):
	l = 0
	r = len(myarray) - 1
	while l <= r:
	    m = (l + r) / 2
	    if myarray[m] == value:
		return m
	    if myarray[m] >= myarray[l]:
		if myarray[l] <= value < myarray[m]:
		    r = m - 1
		else:
		    l = m + 1
	    else:
		if myarray[m] < value <= myarray[r]:
		    l = m + 1
		else:
		    r = m - 1
	return -1
	
myarray = [6,7,8,9,10,1,2,3,4,5]		

print func(myarray, 5)
