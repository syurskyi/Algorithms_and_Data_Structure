
___ insertion_sort(nums
    
	___ i __ r..(l..(nums
		
		j _ i
		
		_____ j>0 ___ nums[j-1] > nums[j]:
			swap(nums,j,j-1)
			j _ j - 1
	
	r_ nums
	
___ swap(nums, i, j
	temp _ nums[i]
	nums[i] _ nums[j]
	nums[j] _ temp
 
__ __name__ __ "__main__":
   
   nums _ [5,4,3,2,1]
   print(insertion_sort(nums))
  