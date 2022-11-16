c_ Solution:
    ___ solutionnums,ans,cur,index
        __(index>l..(nums)):
            r_
        ans.a..(cur[:])
        ___ i __ range(index,l..(nums)):
            __(nums[i] n.. __ cur
                cur.a..(nums[i])
                solution(nums,ans,cur,i)
                cur.pop()
        r_ 
    ___ subsets nums: List[int]) -> List[List[int]]:
        ans _    # list
        cur _    # list
        solution(nums,ans,cur,0)
        r_ ans