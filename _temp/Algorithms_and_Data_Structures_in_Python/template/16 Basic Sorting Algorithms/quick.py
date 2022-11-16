
___ quick_sort(nums,low,high
    
	__ low >_ high:
		r_
		
	pivot_index _ partition(nums,low,high)
	quick_sort(nums,low, pivot_index-1)
	quick_sort(nums, pivot_index+1,high)
	
	
___ partition(nums,low,high

	pivot_index _ (low+high)//2
	swap(nums,pivot_index,high)
	
	i _ low
	
	___ j __ range(low,high,1
		__ nums[j] <_ nums[high]:
			swap(nums,i,j)
			i _ i + 1
			
	swap(nums,i,high)
	
	r_ i
	
___ swap(nums,i,j
	temp _ nums[i]
	nums[i] _ nums[j]
	nums[j] _ temp
	
	
__ __name__ == "__main__":
   
   nums _ [-2,-1,0,1,0,-1,-2]
   quick_sort(nums,0,len(nums)-1)
   print(nums)
  