
___ bubble_sort(nums
    
	___ i __ range(l..(nums)-1
		___ j __ range(0,l..(nums)-1-i,1
			__ nums[j] > nums[j+1]:
				swap(nums, j, j+1)
	
	r_ nums
	
___ swap(nums, i, j
	temp _ nums[i]
	nums[i] _ nums[j]
	nums[j] _ temp
 
__ __name__ __ "__main__":
   
   a _ [0,0,0,-1,-0,1,2,3,2,1]
   print(bubble_sort(a))
  