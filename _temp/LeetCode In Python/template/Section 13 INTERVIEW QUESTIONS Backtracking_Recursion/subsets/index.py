c_ Solution:
    ___ solutionnums,ans,cur,index
        __(index>len(nums)):
            r_
        ans.append(cur[:])
        ___ i __ range(index,len(nums)):
            __(nums[i] n.. __ cur
                cur.append(nums[i])
                solution(nums,ans,cur,i)
                cur.pop()
        r_ 
    ___ subsets nums: List[int]) -> List[List[int]]:
        ans _ []
        cur _ []
        solution(nums,ans,cur,0)
        r_ ans