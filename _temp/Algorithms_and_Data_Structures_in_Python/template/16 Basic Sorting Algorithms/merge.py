
___ merge_sort(nums
    
	__ l..(nums) __ 1:
		r_
		
	middle_index _ l..(nums) // 2
		
	left_half _ nums[:middle_index]
	right_half _ nums[middle_index:]
	
	merge_sort(left_half)
	merge_sort(right_half)
	
	i _ 0
	j _ 0
	k _ 0
	
	_____ i<l..(left_half) and j<l..(right_half
		__ left_half[i] < right_half[j]:
			nums[k] _ left_half[i]
			i _ i + 1
		____
			nums[k] _ right_half[j]
			j _ j + 1
			
		k _ k + 1
		
	_____ i<l..(left_half
		nums[k] _ left_half[i]
		k _ k + 1
		i _ i + 1		
	
__ __name__ __ "__main__":
   
   nums _ [-3,-2,-1,1,2,1,0,-1,-2,-3]
   merge_sort(nums)
   print(nums)
  