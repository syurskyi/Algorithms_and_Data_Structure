c_ Solution:
    ___ solution candidates,ans,cur,target,index,sum
        __(sum__target
            ans.a..(cur[:])
        elif(sum<target
            n _ l..(candidates)
            ___ i __ range(index,n
                cur.a..(candidates[i])
                solution(candidates,ans,cur,target,i,sum+candidates[i])
                cur.pop()
        r_
    ___ combinationSum candidates: List[int], target: int) -> List[List[int]]:
        ans _    # list
        cur _    # list
        solution(candidates,ans,cur,target,0,0)
        r_ ans