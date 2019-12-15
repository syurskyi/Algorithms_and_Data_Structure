"""
   CodingBat List-2 Solutions

"""
"""
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1. 

count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
"""
def count_evens(nums):
    counter = 0
    for i in range (len(nums)):
        if nums[i] % 2 == 0:
            counter += 1
    return counter

"""
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values. 

big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8
"""
def big_diff(nums):
    maxnum = max(nums)
    minnum = min(nums)

    return maxnum - minnum

"""
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more. 

centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3
"""

def centered_average(nums):
    sum = 0
    total = len(nums)-2
    largest = nums.index(max(nums))     
    smallest = nums.index(min(nums))    
    if largest == smallest:             
        for i in range(len(nums)):      
            if nums[i] == nums[smallest]:
                largest = i             
    for i in range(len(nums)):
        if i != largest and i != smallest:      
            sum = sum + nums[i] 
    if total > 0:
        return sum / total         
    else:
        return sum      
        
"""
Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count. 

sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
"""
def sum13(nums):    
    sum = 0
    for i in range (len(nums)):
        if nums[i] != 13:
            sum += nums[i]
        elif nums[i] == 13 and i < len(nums)-1:
            nums[i]=0;
            nums[i+1] =0
            
    return sum   
            

"""
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers. 

sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
"""
def sum67(nums):            
        
    sum = 0
    i=0  
    while i < len(nums):
        if nums[i] == 6:
            while nums[i] != 7:
                i+=1
            i+=1
        if i<len(nums) and nums[i]!=6:  
                sum += nums[i]
                i+=1
    return sum   
     
"""
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere. 

has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
"""


def has22(nums):

    for i in range (len(nums)-1):
        if (nums[i] == 2) and (nums[i+1] == 2):
            return True
        
    return False
            
    

            
        
