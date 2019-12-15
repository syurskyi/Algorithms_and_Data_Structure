class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
                i = 0
                non_count = 0
                equals = False
                while i!= len(nums)-1:
                    try:
                        if nums[i] > nums[i+1]:
                            if i+1 == len(nums)-1:
                                nums[i+1] += (nums[i] - nums[i+1]) + 1
                               
                                non_count +=1
                                i = 0
                            else:    
                                if nums[i+1] < nums[i+2]:
                                    if equals == True:
                                        nums[i+1] = nums[i]
                                    else:
                                        if nums[i] < nums[i+2]:
                                            nums[i+1] = nums[i+2]
                                        else:
                                            nums[i] = nums[i+1]
                                else:
                                    nums[i] = (nums[i] - nums[i+1])
                                non_count += 1
                                i = 0
                        elif nums[i] == nums[i+1]:
                            equals = True
                            i += 1
                        else:
                            i += 1
                    except:
                        pass
                    if non_count >= 2:
                        break
                if non_count <= 1:
                    return True
                else:
                    return False