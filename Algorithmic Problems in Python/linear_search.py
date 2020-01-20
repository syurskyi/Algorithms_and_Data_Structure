

def linear_search(array,item):

	#simple linear search in O(N) running time complexity
	for i in range(len(array)):
		
		#we have found the given item so return with the index
		if array[i] == item:
			return i

	#search miss: item not found
	return -1 
        
if __name__ == "__main__":

	array = [1,4,7,3,6,8,10,11,20,22]
	print(linear_search(array,111))