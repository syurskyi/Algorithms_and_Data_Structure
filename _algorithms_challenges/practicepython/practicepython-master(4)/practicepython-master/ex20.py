#implement linear and binary search



def linear_search(inputlist,element):
	for i in range(0,len(inputlist)):
		if inputlist[i] == element:
			print "element found at position %d " % i
			return True
	return False



def binary_search(inputist,element):
	start = 0
	end = len(inputlist)
	while(start<end):
		mid = (start + end) / 2
		if(inputlist[mid] == element):
			print "found %d at postion %d" % (element, mid)
			return True
		elif element<inputlist[mid]:
			end = mid
		elif element > inputlist[mid]:
			start = mid+1
	return False


if __name__ == "__main__":
	inputlist = [1,2,3,4,5,6,7,8,9,10]
	print linear_search(inputlist,5)
	
	print linear_search(inputlist,0)

	print "binary search extra point"
	print binary_search(inputlist,5)
	print binary_search(inputlist,0)
	print binary_search(inputlist,8)
