
#we can achieve O(logN) but the array must be sorted
def binary_search(array,item,left,right):

	#base case for recursive function calls
	#this is the search miss (array does not contain the item)
	if right < left:
		return -1

	#let's generate the middle item's index	
	middle = left + (right-left)//2
	print("Middle index: ",middle)
	
	#the middle item is the item we are looking for
	if array[middle] == item:
		return middle

	#the item we are looking for is smaller than the middle item
	#so we have to consider the left subarray
	elif array[middle] > item:
		print("Checking items on the left...")
		return binary_search(array,item,left,middle-1)
	
	#the item we are looking for is greater than the middle item
	#so we have to consider the right subarray	
	elif array[middle] < item:
		print("Checking items on the right...")
		return binary_search(array,item,middle+1,right)
        
if __name__ == "__main__":

	array = [1,4,7,8,9,10,11,20,22,25]
	
	print(binary_search(array,111,0,len(array)-1))