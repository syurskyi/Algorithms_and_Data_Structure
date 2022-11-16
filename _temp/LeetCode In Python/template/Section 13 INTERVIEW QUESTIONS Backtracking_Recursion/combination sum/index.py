c_ Solution:
    ___ solution candidates,ans,cur,target,index,sum
        __(sum==target
            ans.append(cur[:])
        elif(sum<target
            n _ len(candidates)
            ___ i __ range(index,n
                cur.append(candidates[i])
                solution(candidates,ans,cur,target,i,sum+candidates[i])
                cur.pop()
        r_
    ___ combinationSum candidates: List[int], target: int) -> List[List[int]]:
        ans _ []
        cur _ []
        solution(candidates,ans,cur,target,0,0)
        r_ ans