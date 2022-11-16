
___ selection_sort(nums
    
	___ i __ range(len(nums)-1
		
		index _ i
		
		___ j __ range(i+1,len(nums),1
			__ nums[j] < nums[index]:
				index _ j
			
		__ index !_ i:
			swap(nums,index,i)
			
	
	r_ nums
	
___ swap(nums, i, j
	temp _ nums[i]
	nums[i] _ nums[j]
	nums[j] _ temp
 
__ __name__ == "__main__":
   
   nums _ [-1,4,5,2,-2,0,1,2,3,2,1,0,1,2,3]
   print(selection_sort(nums))
  